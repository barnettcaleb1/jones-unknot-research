"""critic: for every type-R family (regress (5,5),(6,6): lines and R directions of planes), exact det(K_k) = |Delta_K(-1)|
(tools/alex.alex_eval) at k = -3..3 on the ACTUAL member words, plus the 2-parameter axis-freeness of R planes.
SWAP-SUM LEMMA (critic, PROVED; CLAIMS.md sec. 4): axis-free family => K_k = K'_k # rK'_k, K'_k a 4-plat; det K'_k = |p(k)|,
deg p <= 1 => det K_k = 1 at 3 points forces det = 1, hence K'_k (2-bridge, det 1) = unknot, for ALL k."""
import sys, json
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines')
from multiprocessing import Pool
from collections import Counter
from axisfree2 import reduce, family
def tw(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def job(r):
    import alex
    V = [a for a in r['V'].split('.') if a]; U = [a for a in r['U'].split('.') if a]
    d = tuple(r['d']); m0, n0 = r.get('m0', 0), r.get('n0', 0)
    dets = {}
    for k in range(-3, 4):
        W = V + tw(m0 + k * d[0], n0 + k * d[1]) + U
        hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
        x = alex.alex_eval(hw, -1)
        dets[k] = abs(x) if x is not None else None
    both = None
    if r['type'] == 'PLANE-with-R':
        both = not any(a in ('x0', 'y0') for a in reduce(V + ['B1', 'B3'] + U))
    return (r['type'], r['V'], r['U'], tuple(d), m0, n0, dets, both)
if __name__ == '__main__':
    fam = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/rfamilies.json'))
    items = fam['6']
    with Pool(3) as P: res = P.map(job, items, chunksize=8)
    tab = Counter(); bad = []
    for t, V, U, d, m0, n0, dets, both in res:
        ok = all(v == 1 for v in dets.values())
        tab[(t, ok, both)] += 1
        if not ok: bad.append((t, V, U, d, m0, n0, dets))
    print('R families (6,6):', dict(tab)); print('families with some det != 1:', len(bad), bad[:5])
    json.dump([list(x[:6]) + [x[6], x[7]] for x in res], open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/rdet66.json', 'w'))
