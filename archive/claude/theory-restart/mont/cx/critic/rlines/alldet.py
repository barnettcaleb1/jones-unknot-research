"""critic: SWAP-SUM second proof for EVERY axis-free unit line/plane-direction of regress's (6,6) census and of the
14,790 census-missed families: exact det(K_k) at k = -2..2 (single site: 3 points needed; joint (1,-1): 5 points).
Independent of regress's isotopy classifier."""
import sys, json, pickle
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines')
from multiprocessing import Pool
from collections import Counter
from axisfree2 import typ, family, axis_free
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
def tw(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def job(x):
    import alex
    lab, wt, wb, d, m0, n0 = x
    V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]; dets = []
    for k in range(-2, 3):
        W = V + tw(m0 + k * d[0], n0 + k * d[1]) + U
        hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
        v = alex.alex_eval(hw, -1); dets.append(abs(v) if v is not None else None)
    return lab, all(v == 1 for v in dets)
if __name__ == '__main__':
    d2 = pickle.load(open(OUT + 'classify2_6_6.pkl', 'rb')); r3 = pickle.load(open(OUT + 'classify3_6_6.pkl', 'rb'))
    lines = d2['lines']; items = []; tot = Counter()
    for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
        t = typ(c, r3.get(i)); kind, wt, wb, d, m0, n0 = lines[i][:6]
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        if kind == 'plane':
            for site, dd in (('X1', (1, 0)), ('X3', (0, 1))):
                tot[(t, 'plane-' + site)] += 1
                if axis_free(V + (['B1'] if site == 'X1' else ['B3']) + U): items.append(((t, 'plane-' + site), wt, wb, dd, 0, 0))
        else:
            tot[(t, d)] += 1
            if axis_free(family(V, U, d, m0, n0)): items.append(((t, d), wt, wb, d, m0, n0))
    for r in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/missed66_classified.json')):
        V = [a for a in r['V'].split('.') if a]; U = [a for a in r['U_missed'].split('.') if a]
        if r['kind'] == 'plane':
            for site, dd in (('X1', (1, 0)), ('X3', (0, 1))):
                tot[('MISSED-plane', site)] += 1
                if axis_free(V + (['B1'] if site == 'X1' else ['B3']) + U): items.append((('MISSED-plane', site), r['V'], r['U_missed'], dd, 0, 0))
        else:
            d = tuple(r['d']); tot[('MISSED', d)] += 1
            if axis_free(family(V, U, d, r['m0'], r['n0'])): items.append((('MISSED', d), r['V'], r['U_missed'], d, r['m0'], r['n0']))
    print('axis-free families to test', len(items), flush=True)
    with Pool(3) as P: res = P.map(job, items, chunksize=64)
    af = Counter(); ok = Counter()
    for lab, good in res:
        af[lab] += 1; ok[lab] += good
    for k in sorted(tot, key=str): print('   ', k, 'total', tot[k], 'axis-free', af[k], 'det=1 at 5 pts', ok[k])
    print('ALL axis-free det = 1:', sum(ok.values()), 'of', sum(af.values()))
    json.dump({str(k): [tot[k], af[k], ok[k]] for k in tot}, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/alldet66.json', 'w'), indent=0)
