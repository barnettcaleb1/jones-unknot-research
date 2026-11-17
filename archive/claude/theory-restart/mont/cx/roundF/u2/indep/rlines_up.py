"""u2/indep/rlines_up.py -- (information / negative control) the upstairs global-disc test on regress's type-R lines (764 at (6,6))
and on the R sites of the 572 PLANE-with-R planes.  regress: site circle null-homotopic in pi_1(S^3 - theta) but NOT cup-avoiding.
Expected: 'not-cup-avoiding' upstairs too (the lift of a non-cup-avoiding curve is not cup-avoiding)."""
import sys, json, pickle
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/indep')
from collections import Counter
import up, fam, run
REG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
d2 = pickle.load(open(REG + 'classify2_6_6.pkl', 'rb')); r3 = pickle.load(open(REG + 'classify3_6_6.pkl', 'rb'))
c = Counter()
for (i, cc, ex, nc, pt, Wb, cert) in d2['res']:
    t = fam.typ(cc, r3.get(i)); kind, wt, wb, d, m0, n0 = d2['lines'][i][:6]
    V, U = fam.sp(wt), fam.sp(wb)
    if t == 'R-residual':
        W = V + run.tw(m0, n0) + U
        ok, det = up.site_test(W[:len(V)], W[len(V):], 'X3')
        c[('R line', tuple(det))] += 1
    elif t == 'PLANE-with-R':
        for site, v in r3[i].items():
            if v.startswith('NONE'):
                ok, det = up.site_test(V, U, site)
                c[('R plane site', site, tuple(det))] += 1
for k in sorted(c, key=str): print('   ', k, c[k])
