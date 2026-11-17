import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/calc')
from hf import *
from fractions import Fraction

def absolute(res, shift_q, shift_h):
    """res computed with target base generator at (q,delta)=(0,0); shift so that target base generator sits at (shift_q, shift_h) in (q,h)."""
    out = []
    for (q, d2), dim in sorted(res.items()):
        h = Fraction(q - d2, 2)
        out += [(q + shift_q, h + shift_h)] * dim
    return sorted(out)

# 2602.23442 Def 3.12: C(r_n(0)): source bullet at q^{-n} h^{-n}; C(s_2n(0)): source circ (top-left) at q^{-2n-1} h^{-n-1}. a(0)=[bullet] at q^0 h^0.
print("absolute (q,h) with the gradings of arXiv:2602.23442 Def. 3.12; first argument a single generator at q^0h^0")
for n in (1, 2, 3, 4):
    R = r_curve(n)   # base generator 0 = source
    S = s_curve(n)   # base generator 0 = top-left circ = source
    print(f" HF([bullet], r_{n}(0)) =", [(q, str(h)) for q, h in absolute(hf(arc0(), R), -n, -n)])
    print(f" HF([circ],   r_{n}(0)) =", [(q, str(h)) for q, h in absolute(hf(arcinf(), R), -n, -n)])
    print(f" HF([circ],   s_{2*n}(0)) =", [(q, str(h)) for q, h in absolute(hf(arcinf(), S), -2*n-1, -n-1)])
# K_0 classes
print("K_0 classes (sum over generators of (-1)^h q^q), 2602.23442 gradings:")
for n in (1, 2, 3):
    for X, sq, sh in ((r_curve(n), -n, -n), (s_curve(n), -2*n-1, -n-1)):
        cls = {0: {}, 1: {}}
        for g in range(len(X.idem)):
            q = X.q[g] + sq; h = Fraction(X.q[g] - X.d2[g], 2) + sh
            assert h.denominator == 1
            cls[X.idem[g]][q] = cls[X.idem[g]].get(q, 0) + (1 if int(h) % 2 == 0 else -1)
        fmt = lambda d: ' '.join(f"{c:+d}q^{q}" for q, c in sorted(d.items()) if c) or '0'
        print(f"  [{X.name}] = bullet:( {fmt(cls[0])} )   circ:( {fmt(cls[1])} )")
