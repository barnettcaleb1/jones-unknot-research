"""critic: independent (swap-sum) proof for the AXIS-FREE type-E lines of regress's (6,6) census:
exact det(K_k) at k = -2..2 (3 points suffice: one site, deg p <= 1)."""
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
    wt, wb, d, m0, n0 = x
    V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]; dets = []
    for k in range(-2, 3):
        W = V + tw(m0 + k * d[0], n0 + k * d[1]) + U
        hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
        v = alex.alex_eval(hw, -1); dets.append(abs(v) if v is not None else None)
    return x, dets
if __name__ == '__main__':
    d2 = pickle.load(open(OUT + 'classify2_6_6.pkl', 'rb')); r3 = pickle.load(open(OUT + 'classify3_6_6.pkl', 'rb'))
    lines = d2['lines']; items = []
    for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
        if typ(c, r3.get(i)) != 'E-end-segment': continue
        kind, wt, wb, d, m0, n0 = lines[i][:6]
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        if axis_free(family(V, U, d, m0, n0)): items.append((wt, wb, d, m0, n0))
    with Pool(3) as P: res = P.map(job, items, chunksize=16)
    ok = sum(1 for _, ds in res if all(v == 1 for v in ds))
    print('axis-free E lines', len(items), 'det = 1 at k = -2..2:', ok)
    json.dump([[list(x), ds] for x, ds in res], open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/edet66.json', 'w'))
