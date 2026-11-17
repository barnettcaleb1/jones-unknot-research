"""Pass 3: apply the GLOBAL disc criterion (disc_test.site_disc) at every reachable cut to all lines/planes that classify2
left unexplained (NONE, PLANE-PARTIAL).  usage: classify3.py D1 D2 NPROC"""
import sys, pickle, time
from collections import Counter, defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
from classify import twist
import classify2 as C2
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
GOOD = ('T-disc', 'H-vertex', 'S-trivial')
def global_expl(W, j0, site):
    import disc_test
    curve = (2, 3) if site == 'X1' else (4, 5)
    seen = Counter()
    for i in C2.cuts(W, j0, site):
        r = disc_test.site_disc(W[:i], W[i:], curve)
        seen[r] += 1
        if r in GOOD: return r + ('' if i == j0 else '-recut'), seen
    return None, seen
def work(items):
    out = []
    for i, x, c in items:
        kind, wt, wb, d, m0, n0 = x[:6]
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        W = V + twist(m0, n0) + U; j0 = len(V)
        res = {}
        if kind == 'plane':
            for site in ('X1', 'X3'):
                e = C2.site_expl(W, j0, site)
                if e: res[site] = 'half:' + e
                else:
                    g, seen = global_expl(W, j0, site); res[site] = ('global:' + g) if g else ('NONE ' + str(dict(seen)))
        else:
            site = 'X1' if d == (1, 0) else 'X3'
            g, seen = global_expl(W, j0, site); res[site] = ('global:' + g) if g else ('NONE ' + str(dict(seen)))
        out.append((i, res))
    return out
if __name__ == '__main__':
    import multiprocessing as mp
    D1, D2, nproc = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    dat = pickle.load(open(OUT + 'classify2_%d_%d.pkl' % (D1, D2), 'rb'))
    lines, res = dat['lines'], dat['res']
    todo = [(i, lines[i], c) for (i, c, ex, nc, pt, Wb, cert) in res if c[3] in ('NONE', 'PLANE-PARTIAL')]
    print('unexplained after pass 2:', len(todo), flush=True)
    chunks = [todo[k::nproc * 4] for k in range(nproc * 4)]
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool:
        rr = pool.map(work, chunks)
    allr = dict(y for r in rr for y in r)
    print('time', round(time.time() - t0, 1), flush=True)
    tab = Counter(); ex = defaultdict(list)
    cmap = {i: c for (i, c, *_r) in res}
    for i, r in allr.items():
        c = cmap[i]
        key = (c[0], c[1], c[4] if c[0] != 'plane' else '', tuple(sorted((k, v.split(' ')[0] if v.startswith('NONE') else v) for k, v in r.items())))
        tab[key] += 1
        if len(ex[key]) < 4: ex[key].append((lines[i][1], lines[i][2], lines[i][4], lines[i][5], r))
    for k in sorted(tab, key=str): print('   ', k, tab[k])
    print('EXAMPLES of anything still NONE:')
    for k in sorted(ex, key=str):
        if any(v.startswith('NONE') for _, v in k[3]):
            print('  ', k)
            for e in ex[k]: print('      ', e)
    pickle.dump(allr, open(OUT + 'classify3_%d_%d.pkl' % (D1, D2), 'wb'))
