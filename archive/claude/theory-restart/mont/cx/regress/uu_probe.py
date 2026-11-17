"""Diagnostic for the residual ('u','u') sites: is the site curve null-homotopic in pi_1(S^3 - theta) = F_3/<<psi_V(c_U)>>?
(also = pi_1(B' - T') since the H-tree complement adds nothing).  Not a proof of anything by itself (interior curve)."""
import sys, pickle
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import geo, whitehead, fgroup
from classify import twist
import classify2 as C2
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
D1, D2 = int(sys.argv[1]), int(sys.argv[2])
dat = pickle.load(open(OUT + 'classify2_%d_%d.pkl' % (D1, D2), 'rb')); lines = dat['lines']
c3 = pickle.load(open(OUT + 'classify3_%d_%d.pkl' % (D1, D2), 'rb'))
tab = Counter(); ex = []
for i, r in c3.items():
    for site, v in r.items():
        if not v.startswith('NONE'): continue
        kind, wt, wb, d, m0, n0 = lines[i][:6]
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        W = V + twist(m0, n0) + U; j0 = len(V)
        curve = (2, 3) if site == 'X1' else (4, 5)
        res = []
        for k in C2.cuts(W, j0, site):
            Vt, Ub = W[:k], W[k:]
            w = geo.subst(geo.psi_top(Vt), curve)
            cupc = (3, 4)
            for L in reversed(Ub): cupc = fgroup.act(geo.INV[L], cupc)
            rr = geo.subst(geo.psi_top(Vt), cupc)
            res.append(whitehead.trivial_in_quotient(w, rr))
        key = (kind, site, 'nullhomotopic' if any(x is True for x in res) else 'r-not-primitive' if all(x is None for x in res) else 'NOT nullhomotopic')
        tab[key] += 1
        if len(ex) < 6 and key[2] != 'nullhomotopic': ex.append((wt, wb, m0, n0, site, res))
print(dict(tab))
for e in ex: print(e)
