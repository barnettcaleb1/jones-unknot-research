"""critic: AXIS-FREENESS of every unit-line FAMILY of regress's census (5,5)/(6,6) and of the 14,790 census-missed lines.
Family word: V . offset twists . B . U, B = token for the varying block ((x3x3)^k: B3, (x1x1)^k: B1, (x1x1 y3y3)^k: BJ).
Moves (each an isotopy of EVERY member): cancellation x.y (x = INV y) across letters that commute with x
(right-angled relations {x0,x2},{x0,x3},{x1,x3}; B3 commutes with x0,x1,x3; B1 and BJ with x1,x3);
deleting an axis letter that commutes to the BOTTOM end (R1 at the bottom vertex).
Axis-free family => SWAP-SUM LEMMA: K_k = K'_k # rK'_k, K'_k a 4-plat (2-bridge) => K_k unknot iff det K_k = 1, and
det K'_k = |p(k)| with deg p <= 1 (one site) or <= 2 (joint site); so det K_k = 1 at 3 (resp. 5) points => all k.
(typ() copied from regress/certify_summary.py; that module is NOT imported because it rewrites files at import.)"""
import sys, pickle, json
from collections import Counter
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
def typ(c, r3):
    kind, d, rep, geo_t, sub = c
    if geo_t == 'SITE-STAB': return 'S1-cap' if sub.startswith('top') else 'S2-cup'
    if geo_t == 'JOINT-STAB': return 'J2-band-clasp' if sub.startswith('band-clasp') else 'J1-axis-split' if sub.startswith('axis-split') else 'J-both-caps'
    if geo_t == 'PLANE-GEO': return 'PLANE-geo'
    if r3 is None: return 'UNKNOWN'
    vals = list(r3.values())
    if kind == 'plane': return 'PLANE-geo' if all(not v.startswith('NONE') for v in vals) else 'PLANE-with-R'
    return 'E-end-segment' if not vals[0].startswith('NONE') else 'R-residual'
GEN = lambda L: L[1] if L[0] in 'xy' else L      # generator index or token
COMM = {('0', '2'), ('0', '3'), ('1', '3'), ('0', 'B3'), ('1', 'B3'), ('3', 'B3'), ('1', 'B1'), ('3', 'B1'), ('1', 'BJ'), ('3', 'BJ')}
def commute(a, b):
    ga, gb = GEN(a), GEN(b)
    return ga == gb or (ga, gb) in COMM or (gb, ga) in COMM
def reduce(W):
    W = list(W)
    while True:
        done = False
        for i in range(len(W)):
            a = W[i]
            if a not in INV: continue
            j = i + 1
            while j < len(W):
                if W[j] == INV[a]:
                    W = W[:i] + W[i + 1:j] + W[j + 1:]; done = True; break
                if not commute(a, W[j]): break
                j += 1
            if done: break
            if j == len(W) and a in ('x0', 'y0'):
                W = W[:i] + W[i + 1:]; done = True; break
        if not done: return W
def twist(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def family(V, U, d, m0, n0):
    if d == (0, 1): return V + (['x1', 'x1'] * m0 if m0 > 0 else ['y1', 'y1'] * (-m0)) + ['B3'] + (['x3', 'x3'] * n0 if n0 > 0 else ['y3', 'y3'] * (-n0)) + U
    if d == (1, 0): return V + (['x1', 'x1'] * m0 if m0 > 0 else ['y1', 'y1'] * (-m0)) + ['B1'] + (['x3', 'x3'] * n0 if n0 > 0 else ['y3', 'y3'] * (-n0)) + U
    return V + twist(m0, n0) + ['BJ'] + U
def axis_free(fam): return not any(a in ('x0', 'y0') for a in reduce(fam))
if __name__ == '__main__':
    out = {}
    for D in (5, 6):
        d2 = pickle.load(open(OUT + 'classify2_%d_%d.pkl' % (D, D), 'rb')); r3 = pickle.load(open(OUT + 'classify3_%d_%d.pkl' % (D, D), 'rb'))
        lines = d2['lines']; tab = Counter(); rl = []
        for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
            t = typ(c, r3.get(i)); kind, wt, wb, d, m0, n0 = lines[i][:6]
            V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
            if kind == 'plane':
                for site in ('X1', 'X3'):
                    f = V + (['B3'] if site == 'X3' else ['B1']) + U
                    af = axis_free(f); tab[(t, 'plane-' + site, af)] += 1
                    if t == 'PLANE-with-R' and r3.get(i, {}).get(site, '').startswith('NONE'):
                        rl.append({'type': t, 'site': site, 'V': wt, 'U': wb, 'd': [1, 0] if site == 'X1' else [0, 1], 'm0': 0, 'n0': 0, 'axis_free': af})
            else:
                af = axis_free(family(V, U, d, m0, n0)); tab[(t, d, af)] += 1
                if t == 'R-residual': rl.append({'type': t, 'V': wt, 'U': wb, 'd': list(d), 'm0': m0, 'n0': n0, 'axis_free': af})
        out[D] = rl
        print('ENUM', D)
        for k in sorted(tab, key=str): print('   ', k, tab[k])
        nf = [r for r in rl if not r['axis_free']]
        print('   R families NOT axis-free:', len(nf), 'of', len(rl))
        for r in nf[:6]: print('      ', r['V'], '|', r['U'], r['d'], r.get('m0'), r.get('n0'), '->', '.'.join(reduce(family([a for a in r['V'].split('.') if a], [a for a in r['U'].split('.') if a], tuple(r['d']), r['m0'], r['n0']))))
    # census-missed lines (critic/missed)
    ms = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/missed66_classified.json'))
    tab = Counter()
    for r in ms:
        V = [a for a in r['V'].split('.') if a]; U = [a for a in r['U_missed'].split('.') if a]
        if r['kind'] == 'plane':
            for site in ('X1', 'X3'): tab[('missed-plane', site, axis_free(V + (['B3'] if site == 'X3' else ['B1']) + U))] += 1
        else: tab[('missed', tuple(r['d']), r['type'][3], axis_free(family(V, U, tuple(r['d']), r['m0'], r['n0'])))] += 1
    print('MISSED LINES (6,6):')
    for k in sorted(tab, key=str): print('   ', k, tab[k])
    json.dump(out, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/rfamilies.json', 'w'))
