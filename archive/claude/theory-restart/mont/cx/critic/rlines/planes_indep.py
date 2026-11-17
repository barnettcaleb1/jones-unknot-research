"""critic: independent proof status of every unit PLANE ((6,6) census + census-missed): per site, Lemma K stabiliser
(lines_family.line_ok at offset (0,0)) and axis-freeness of the 1-parameter family through (0,0) (det = 1 at 5 points was
CHECKED for all of those in alldet.py); 2-parameter axis-freeness.  A plane is one knot type if both sites are Lemma-K
stabilisers; if one site is Lemma K and the other direction is axis-free, every member is the unknot (swap-sum);
if neither site is Lemma K but the plane is 2-parameter axis-free, a 3x3 det grid is needed (done for the 104 double-R)."""
import sys, json, pickle
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines'); sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/code')
from collections import Counter
from axisfree2 import typ, reduce
import lines_family as LF
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
def af(w): return not any(a in ('x0', 'y0') for a in reduce(w))
d2 = pickle.load(open(OUT + 'classify2_6_6.pkl', 'rb')); r3 = pickle.load(open(OUT + 'classify3_6_6.pkl', 'rb'))
planes = []
for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
    kind, wt, wb = d2['lines'][i][:3]
    if kind == 'plane': planes.append((typ(c, r3.get(i)), wt, wb))
for r in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/missed66_classified.json')):
    if r['kind'] == 'plane': planes.append(('MISSED-plane', r['V'], r['U_missed']))
tab = Counter(); need_grid = []
for t, wt, wb in planes:
    V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
    k1 = bool(LF.line_ok(V, U, (1, 0), (0, 0))); k3 = bool(LF.line_ok(V, U, (0, 1), (0, 0)))
    a1 = af(V + ['B1'] + U); a3 = af(V + ['B3'] + U); a13 = af(V + ['B1', 'B3'] + U)
    if k1 and k3: st = 'both Lemma K'
    elif (k1 and a3) or (k3 and a1): st = 'Lemma K + swap-sum'
    elif a13: st = '2-param axis-free (grid)'; need_grid.append((t, wt, wb))
    else: st = 'regress only'
    tab[(t, st)] += 1
for k in sorted(tab, key=str): print('   ', k, tab[k])
json.dump(need_grid, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/planes_need_grid.json', 'w'))
print('planes needing a 3x3 det grid:', len(need_grid))
