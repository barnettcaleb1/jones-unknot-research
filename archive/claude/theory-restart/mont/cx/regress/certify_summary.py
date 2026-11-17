"""Combine classify2 + classify3: per (enumeration, type): lines, base <= 24 & V_K = 1 (whole line CERTIFIED_UNKNOT when the
isotopy is PROVED), base > 24 (one knot, UNRESOLVED), type R (line UNRESOLVED)."""
import pickle, sys
from collections import Counter, defaultdict
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
def typ(c, r3):
    kind, d, rep, geo_t, sub = c
    if geo_t == 'SITE-STAB': return 'S1-cap' if sub.startswith('top') else 'S2-cup'
    if geo_t == 'JOINT-STAB': return 'J2-band-clasp' if sub.startswith('band-clasp') else 'J1-axis-split' if sub.startswith('axis-split') else 'J-both-caps'
    if geo_t == 'PLANE-GEO': return 'PLANE-geo'
    if r3 is None: return 'UNKNOWN'
    vals = list(r3.values())
    if kind == 'plane': return 'PLANE-geo' if all(not v.startswith('NONE') for v in vals) else 'PLANE-with-R'
    return 'E-end-segment' if not vals[0].startswith('NONE') else 'R-residual'
lines_out = []
big = defaultdict(set)
for D in (5, 6):
    d2 = pickle.load(open(OUT + 'classify2_%d_%d.pkl' % (D, D), 'rb')); r3 = pickle.load(open(OUT + 'classify3_%d_%d.pkl' % (D, D), 'rb'))
    tab = defaultdict(Counter)
    for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
        t = typ(c, r3.get(i))
        key = (t, c[1] if c[0] != 'plane' else 'plane')
        tab[key]['lines'] += 1
        if nc <= 24 and cert is True: tab[key]['base<=24,V=1'] += 1
        elif nc <= 24: tab[key]['base<=24,V!=1 or not knot'] += 1
        else:
            tab[key]['base>24'] += 1; big[D].add(Wb)
    lines_out.append('ENUMERATION (%d,%d)' % (D, D))
    tot = Counter()
    for k in sorted(tab, key=str):
        lines_out.append('   %-16s %-8s %s' % (k[0], k[1], dict(tab[k]))); tot.update(tab[k])
    lines_out.append('   TOTAL %s' % dict(tot))
    lines_out.append('   distinct base words with > 24 crossings: %d' % len(big[D]))
open(OUT + 'certify_summary.txt', 'w').write('\n'.join(lines_out) + '\n')
print('\n'.join(lines_out))
pickle.dump({D: sorted(big[D]) for D in big}, open(OUT + 'big_bases.pkl', 'wb'))
