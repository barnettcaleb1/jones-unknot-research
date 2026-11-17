import sys, cmath, math, random
sys.path.insert(0, '.')
import numpy as np
from sig import mats, vc, basis, idx, qint
mstar = idx[tuple(sorted(((0,5),(1,4),(2,3))))]
def N_of(word, A):
    d,E,S,G = mats(A); v = vc(A); w = v.copy()
    Sinv = [np.linalg.inv(s) for s in S]
    for g in reversed(word):
        w = (S[abs(g)-1] if g>0 else Sinv[abs(g)-1]) @ w
    return w[mstar], v[mstar]
random.seed(7)
words = [[random.choice([1,2,3,4,5,-1,-2,-3,-4,-5]) for _ in range(random.randint(4,24))] for _ in range(300)]
worst_rcs = 1e9; worst_cs = -1e9; unit_dev = 0; minN = 1e9
for w in words:
    for th_deg in np.linspace(60.5, 67.0, 9):          # (4,1) arc
        A = cmath.exp(1j*math.radians(th_deg)); n, n0 = N_of(w, A)
        q3 = abs(qint(3, A)); minN = min(minN, abs(n)); worst_rcs = min(worst_rcs, abs(n) - q3)
    for th_deg in np.linspace(68.0, 112.0, 9):         # definite arc
        A = cmath.exp(1j*math.radians(th_deg)); n, n0 = N_of(w, A)
        worst_cs = max(worst_cs, abs(n) - abs(qint(3, A)))
    A = cmath.exp(1j*3*math.pi/8); n, _ = N_of(w, A); unit_dev = max(unit_dev, abs(abs(n) - 1))
print('min over (4,1)-arc of |N|-|[3]| (expect >= 0):', worst_rcs)
print('min |N| on (4,1)-arc (expect > 0):', minN)
print('max over definite arc of |N|-|[3]| (expect <= 0):', worst_cs)
print('max | |N(A=e^{3pi i/8})| - 1 | (expect 0):', unit_dev)
