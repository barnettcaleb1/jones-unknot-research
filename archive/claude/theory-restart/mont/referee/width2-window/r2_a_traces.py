"""exact ranks of the joint projectors E_ab = E_a(X1)E_b(X3) as traces (commuting idempotents => rank = trace)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/width2-window')
from r2lib import *
I9 = sp.eye(9)
X1, X3 = Smat(M['x1']), Smat(M['x3'])
lam = [sp.Integer(1), -t, t**3]
def P(X, a):
    R = I9
    for b in range(3):
        if b != a: R = R * (X - lam[b] * I9) / (lam[a] - lam[b])
    return R.applyfunc(sp.cancel)
P1 = [P(X1, a) for a in range(3)]; P3 = [P(X3, a) for a in range(3)]
tr = [[sp.cancel((P1[a] * P3[b]).trace()) for b in range(3)] for a in range(3)]
print('exact traces (= ranks) of E_ab, rows a=0,2,4 (X1 colour), cols b=0,2,4 (X3 colour):', tr)
print('E04, E40 zero matrices:', (P1[0] * P3[2]).applyfunc(sp.cancel) == sp.zeros(9), (P1[2] * P3[0]).applyfunc(sp.cancel) == sp.zeros(9))
