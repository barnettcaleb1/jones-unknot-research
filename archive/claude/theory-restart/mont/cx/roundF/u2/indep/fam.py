"""u2/indep/fam.py -- extract the U2 families (read-only data; no regress code imported: the pickles hold builtins only).
typ() and the critic's axis-free reduction are re-typed here (logic copied, not imported)."""
import sys, os, json, pickle
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/code')     # audited copy: Lemma K (lines_family)
from collections import Counter
REG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
MISSED = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/missed66_classified.json'
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/families.json'
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
GEN = lambda L: L[1] if L[0] in 'xy' else L
COMMP = {('0', '2'), ('0', '3'), ('1', '3'), ('0', 'B3'), ('1', 'B3'), ('3', 'B3'), ('1', 'B1'), ('3', 'B1'), ('1', 'BJ'), ('3', 'BJ')}
def commute(a, b):
    ga, gb = GEN(a), GEN(b)
    return ga == gb or (ga, gb) in COMMP or (gb, ga) in COMMP
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
def tw1(L, k): return [L, L] * k if k > 0 else [INV[L], INV[L]] * (-k)
def family(V, U, d, m0, n0):
    if d == (0, 1): return V + tw1('x1', m0) + ['B3'] + tw1('x3', n0) + U
    if d == (1, 0): return V + tw1('x1', m0) + ['B1'] + tw1('x3', n0) + U
    return V + tw1('x1', m0) + tw1('x3', n0) + ['BJ'] + U
def axis_free(f): return not any(a in ('x0', 'y0') for a in reduce(f))
def sp(s): return [a for a in s.split('.') if a]
if __name__ == '__main__':
    import lines_family as LF
    fams = []; tab = Counter()
    for D in (6, 5):
        d2 = pickle.load(open(REG + 'classify2_%d_%d.pkl' % (D, D), 'rb')); r3 = pickle.load(open(REG + 'classify3_%d_%d.pkl' % (D, D), 'rb'))
        for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
            t = typ(c, r3.get(i)); kind, wt, wb, d, m0, n0 = d2['lines'][i][:6]
            g = r3.get(i, {})
            if kind != 'plane' and t == 'E-end-segment':
                af = axis_free(family(sp(wt), sp(wb), d, m0, n0))
                fams.append({'fid': '%d%d-L%d' % (D, D, i), 'src': '%d%d' % (D, D), 'kind': 'line', 'V': wt, 'U': wb, 'd': list(d), 'm0': m0, 'n0': n0,
                             'reg_type': t, 'reg_global': g, 'axis_free': af, 'base_cross': nc, 'base_pt': list(pt), 'base_word': list(Wb),
                             'u2_target': (D == 6 and not af) or D == 5})
                tab[(D, 'E line', tuple(d), 'axis-free' if af else 'NOT axis-free')] += 1
            elif kind == 'plane' and t == 'PLANE-geo' and any(v.startswith('global') for v in g.values()):
                V, U = sp(wt), sp(wb)
                k1 = bool(LF.line_ok(V, U, (1, 0), (0, 0))); k3 = bool(LF.line_ok(V, U, (0, 1), (0, 0)))
                a1 = axis_free(V + ['B1'] + U); a3 = axis_free(V + ['B3'] + U)
                crit = 'both Lemma K' if (k1 and k3) else 'Lemma K + swap-sum' if ((k1 and a3) or (k3 and a1)) else 'regress only'
                fams.append({'fid': '%d%d-P%d' % (D, D, i), 'src': '%d%d' % (D, D), 'kind': 'plane', 'V': wt, 'U': wb, 'd': [1, 0], 'm0': 0, 'n0': 0,
                             'reg_type': t, 'reg_global': g, 'critic_indep': crit, 'lemmaK': [k1, k3], 'axis_free_dirs': [a1, a3],
                             'base_cross': nc, 'base_pt': list(pt), 'base_word': list(Wb), 'u2_target': crit == 'regress only'})
                tab[(D, 'geo plane with T-disc site', crit)] += 1
    for r in json.load(open(MISSED)):
        if r['kind'] != 'plane' or r['type'][3] != 'PLANE-PARTIAL': continue
        V, U = sp(r['V']), sp(r['U_missed'])
        k1 = bool(LF.line_ok(V, U, (1, 0), (0, 0))); k3 = bool(LF.line_ok(V, U, (0, 1), (0, 0)))
        a1 = axis_free(V + ['B1'] + U); a3 = axis_free(V + ['B3'] + U)
        crit = 'both Lemma K' if (k1 and k3) else 'Lemma K + swap-sum' if ((k1 and a3) or (k3 and a1)) else 'regress only'
        fams.append({'fid': 'M66-P%d' % len(fams), 'src': 'missed66', 'kind': 'plane', 'V': r['V'], 'U': r['U_missed'], 'd': [1, 0], 'm0': 0, 'n0': 0,
                     'reg_type': 'PLANE-PARTIAL', 'reg_global': r['global'], 'critic_indep': crit, 'lemmaK': [k1, k3], 'axis_free_dirs': [a1, a3],
                     'base_cross': r['base_cross'], 'base_pt': r['base_pt'], 'base_word': sp(r['base_hw'][8:-6]) if r['base_hw'] != 's.l1.l1.u2.u2' else [],
                     'base_hw': r['base_hw'], 'u2_target': crit == 'regress only'})
        tab[('missed66', 'plane PARTIAL', crit)] += 1
    for k in sorted(tab, key=str): print('   ', k, tab[k])
    print('families', len(fams), 'u2 targets', sum(f['u2_target'] for f in fams))
    json.dump(fams, open(OUT, 'w'))
