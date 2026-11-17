import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import census_fixed as CF, geo
E = CF.E
t, u, bl, TG, BG, nt, nb = CF.setup(5, 5, 1)
for cls, lst in TG.items():
    for w, co, S in lst:
        g = geo.top_tests(list(w))
        rj = len(set(E[s[0]] - E[s[1]] for s in S)) <= 1
        if rj and not g['c0123']:
            # also test the exact kernel stabiliser for X1 X3^-1 and X1^2 X3^-2
            st1 = geo.top_same(list(w), list(w) + ['x1', 'y3'])
            st2 = geo.top_same(list(w), list(w) + ['x1', 'x1', 'y3', 'y3'])
            print('.'.join(w), 'support', sorted(S), 'tests', g, 'kernel-stab X1X3^-1:', st1, ' X1^2X3^-2:', st2)
