"""Type-R lines (no isotopy found): certify individual points k in [-K,K] around the representative point.
<= 24 crossings: exact V_K (Tuzun-Sikora);  > 24: kcert screen (a V_K != 1 or Delta != 1 point would be a HIT candidate)
and a bounded Tietze attempt.  usage: r_sweep.py D NPROC K"""
import sys, pickle, json, time
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
class TO(Exception): pass
def job(args):
    items, K = args
    import signal, tietze, kcert
    from classify import twist, freered, ncross, VK1
    def h(s, f): raise TO()
    signal.signal(signal.SIGALRM, h)
    st = Counter(); bad = []
    for (wt, wb, d, m0, n0) in items:
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        for k in range(-K, K + 1):
            W = freered(V + twist(m0 + k * d[0], n0 + k * d[1]) + U)
            hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
            if ncross(W) <= 24:
                st['<=24 V_K=1 (CERTIFIED)' if VK1(W) else '<=24 V_K!=1'] += 1
                if not VK1(W): bad.append(hw)
                continue
            s, why = kcert.certify(hw)
            if s != 'V=1,Delta=1': st['>24 kcert NONTRIVIAL'] += 1; bad.append(hw); continue
            try:
                signal.alarm(10)
                n, rels = tietze.wirtinger(hw); steps = []
                gens, rr = tietze.simplify(n, rels, steps)
                signal.alarm(0)
                ok = len(gens) <= 1 and not rr and tietze.replay(hw, steps)
            except TO:
                ok = False
            st['>24 Tietze <a|> (CERTIFIED)' if ok else '>24 V=1,Delta=1 UNRESOLVED'] += 1
    return st, bad
if __name__ == '__main__':
    import multiprocessing as mp
    D, nproc, K = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    d2 = pickle.load(open(OUT + 'classify2_%d_%d.pkl' % (D, D), 'rb')); c3 = pickle.load(open(OUT + 'classify3_%d_%d.pkl' % (D, D), 'rb'))
    lines = d2['lines']
    items = []
    for i, r in c3.items():
        kind, wt, wb, d, m0, n0 = lines[i][:6]
        if kind == 'offset' and list(r.values())[0].startswith('NONE'): items.append((wt, wb, d, m0, n0))
    print('type-R lines', len(items), flush=True)
    chunks = [(items[j::nproc * 2], K) for j in range(nproc * 2)]
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool: rr = pool.map(job, chunks)
    tot = Counter(); bad = []
    for s, b in rr: tot.update(s); bad.extend(b)
    print('points k in [-%d,%d]:' % (K, K), dict(tot), 'bad', bad[:5], 'time', round(time.time() - t0, 1), flush=True)
    json.dump({'K': K, 'stats': dict(tot), 'bad': bad}, open(OUT + 'r_sweep_%d.json' % D, 'w'))
