"""critic: planes with BOTH sites of type R: det on the 3x3 grid {-1,0,1}^2 (bilinear det argument needs a grid);
and check that the (5,5) R families are among the (6,6) ones."""
import sys, json
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from multiprocessing import Pool
from collections import Counter, defaultdict
def tw(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def job(vu):
    import alex
    V = [a for a in vu[0].split('.') if a]; U = [a for a in vu[1].split('.') if a]; out = {}
    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            W = V + tw(m, n) + U; hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
            x = alex.alex_eval(hw, -1); out['%d,%d' % (m, n)] = abs(x) if x is not None else None
    return vu, out
if __name__ == '__main__':
    fam = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/rfamilies.json'))
    sites = defaultdict(set)
    for r in fam['6']:
        if r['type'] == 'PLANE-with-R': sites[(r['V'], r['U'])].add(r['site'])
    both = [vu for vu, s in sites.items() if len(s) == 2]
    with Pool(3) as P: res = P.map(job, both)
    ok = sum(1 for _, o in res if all(v == 1 for v in o.values()))
    print('double-R planes', len(both), 'det = 1 on the whole 3x3 grid:', ok)
    k6 = set((r['type'], r['V'], r['U'], tuple(r['d']), r.get('m0', 0), r.get('n0', 0)) for r in fam['6'])
    k5 = set((r['type'], r['V'], r['U'], tuple(r['d']), r.get('m0', 0), r.get('n0', 0)) for r in fam['5'])
    print('(5,5) R families', len(k5), 'contained in (6,6):', len(k5 & k6))
