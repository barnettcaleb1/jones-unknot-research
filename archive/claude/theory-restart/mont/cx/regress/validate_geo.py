"""Validate the free-group half models against rho_2 over all tops/bottoms of the (D1,D2) enumeration:
geometric disc (curve dies in the half's complement group)  ==>  rho_2 scalar action (support in one colour class).
Rep-level: Sv = sectors (a,b) with E_ab V v != 0; X1 scalar on V v <=> all a equal; X3 scalar <=> all b equal;
X1 X3^-1 scalar <=> all a - b equal ... (1,-1) slope e_a - e_b constant.  Same for covectors w = phi U."""
import sys, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
from collections import Counter
import census_fixed as CF, geo
E = CF.E
def one_class(S, f): return len(set(f(s) for s in S)) <= 1
D1, D2 = int(sys.argv[1]), int(sys.argv[2])
t, u, bl, TG, BG, nt, nb = CF.setup(D1, D2, 1)
res = {}
for side, G, tests in (('top', TG, geo.top_tests), ('bot', BG, geo.bot_tests)):
    tab = Counter()
    for cls, lst in G.items():
        for w, co, S in lst:
            g = tests(list(w))
            r1 = one_class(S, lambda s: s[0]); r3 = one_class(S, lambda s: s[1]); rj = one_class(S, lambda s: E[s[0]] - E[s[1]])
            tab[('X1', g['c01'], r1)] += 1; tab[('X3', g['c23'], r3)] += 1; tab[('X1X3^-1', g['c0123'], rj)] += 1
            if side == 'top' and g['c0123'] and not all(s[0] == s[1] for s in S): tab['top split but a!=b sector'] += 1
    res[side] = tab
    print(side, 'words', sum(len(l) for l in G.values()))
    for k in sorted(tab, key=str): print('   (site, geometric disc, rep scalar) =', k, ':', tab[k])
