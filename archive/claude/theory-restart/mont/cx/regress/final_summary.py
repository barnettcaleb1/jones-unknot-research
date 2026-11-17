"""Final per-type status of every unit line / plane: CERTIFIED_UNKNOT (whole line) = isotopy PROVED (S1,S2,J1,J2,E, planes-geo)
and base certified ((a) <= 24 crossings & V_K = 1 exact, or (b) replayed Tietze certificate); else UNRESOLVED."""
import pickle, json, os
from collections import Counter, defaultdict
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
from certify_summary import typ
tz = {}
for f in ('certify_big.json', 'certify_big2.json'):
    if os.path.exists(OUT + f):
        for x in json.load(open(OUT + f)):
            tz[x[0]] = tz.get(x[0], False) or bool(x[1])
lines_out = []
unres = defaultdict(list)
for D in (5, 6):
    d2 = pickle.load(open(OUT + 'classify2_%d_%d.pkl' % (D, D), 'rb')); r3 = pickle.load(open(OUT + 'classify3_%d_%d.pkl' % (D, D), 'rb'))
    tab = defaultdict(Counter)
    for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
        t = typ(c, r3.get(i)); key = (t, c[1] if c[0] != 'plane' else 'plane')
        hw = 's.l1.l1.' + '.'.join(Wb) + '.u2.u2'
        base_ok = (nc <= 24 and cert is True) or (nc > 24 and tz.get(hw, False))
        proved = t not in ('R-residual', 'PLANE-with-R', 'UNKNOWN')
        if proved and base_ok: st = 'CERTIFIED_UNKNOT (line)'
        elif proved: st = 'ONE KNOT, UNRESOLVED (base >24, no certificate)'; unres[D].append(hw)
        else: st = 'UNRESOLVED (no isotopy; base %s)' % ('certified' if base_ok else 'uncertified')
        tab[key][st] += 1
    lines_out.append('ENUMERATION (%d,%d)' % (D, D))
    tot = Counter()
    for k in sorted(tab, key=str):
        lines_out.append('   %-16s %-8s %s' % (k[0], k[1], dict(tab[k]))); tot.update(tab[k])
    lines_out.append('   TOTAL %s' % dict(tot))
open(OUT + 'final_summary.txt', 'w').write('\n'.join(lines_out) + '\n')
json.dump({D: sorted(set(v)) for D, v in unres.items()}, open(OUT + 'unresolved_one_knot_bases.json', 'w'), indent=0)
print('\n'.join(lines_out))
