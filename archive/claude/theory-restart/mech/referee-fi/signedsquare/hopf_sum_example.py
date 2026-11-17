#!/usr/bin/env python3
"""Example showing the unit seed is needed for 'f is a unit' (not for the sign step): N(T1+T2) # Hopf.
C = <Hopf> G, full Gamma symmetry (S scalar), no unit seed, C(zeta_8) = -2 G(zeta_8) != 0."""
import sys
sys.dont_write_bytecode = True
from twobox import *
w = [(1, 'B1'), (1, 'B2'), (2, 1), (2, 1)]
C = pd_tensor(w, 3); C2 = tl_tensor(w, 3)
print("PD == TL:", C == C2)
for i in range(2):
    for j in range(2):
        print("C[%d][%d] = %s" % (i, j, pstr(C[i][j])))
hopf = {4: -1, -4: -1}
Gm = [[dict(DELTA), {0: 1}], [{0: 1}, dict(DELTA)]]
print("C == (-A^4 - A^-4) * G:", all(pclean(C[i][j]) == pclean(pmul(hopf, Gm[i][j])) for i in range(2) for j in range(2)))
res = analyse(C)
for (i, j), d in sorted(res["anchors"].items()):
    print("anchor", (i, j), "value", zstr(res["Z"][i][j]), "ratio", zstr(d["ratio"]), "law ok:", d["ok"])
