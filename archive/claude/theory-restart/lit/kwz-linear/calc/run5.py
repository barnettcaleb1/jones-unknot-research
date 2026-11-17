import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/calc')
from hf import *
from collections import Counter
from fractions import Fraction

def klass(X):
    """(X_bullet, X_circ) as Counters q -> signed count, sign (-1)^h, with base generator at (q,h)=(0,0)"""
    out = [Counter(), Counter()]
    for g in range(len(X.idem)):
        h2 = X.q[g] - X.d2[g]
        assert h2 % 2 == 0
        out[X.idem[g]][X.q[g]] += 1 if (h2 // 2) % 2 == 0 else -1
    return out
def bar(c): return Counter({-k: v for k, v in c.items()})
def mul(a, b):
    o = Counter()
    for i, x in a.items():
        for j, y in b.items(): o[i + j] += x * y
    return Counter({k: v for k, v in o.items() if v})
def add(a, b):
    o = Counter(a)
    for k, v in b.items(): o[k] += v
    return Counter({k: v for k, v in o.items() if v})
def chi_hf(res):
    o = Counter()
    for (q, d2), dim in res.items():
        h2 = q - d2
        assert h2 % 2 == 0
        o[q] += dim * (1 if (h2 // 2) % 2 == 0 else -1)
    return Counter({k: v for k, v in o.items() if v})

def predicted_times_denominator(X, Y):
    Xb, Xc = map(bar, klass(X)); Yb, Yc = klass(Y)
    qq = Counter({1: 1, -1: 1})
    return add(mul(qq, add(mul(Xb, Yb), mul(Xc, Yc))), add(mul(Xb, Yc), mul(Xc, Yb)))

ok = True
cases = []
for m in (1, 2, 3):
    for Y in (s_curve(m), r_curve(m)):
        for X in [arc0(), arcinf()] + [arc_int(-n) for n in (1, 2, 3, 4)] + [arc_int(n) for n in (1, 2, 3)]:
            lhs = mul(chi_hf(hf(X, Y)), Counter({1: 1, -1: -1}))     # chi * (q - q^-1)
            rhs = predicted_times_denominator(X, Y)
            good = (lhs == rhs)
            ok &= good
            if not good: print("MISMATCH", X.name, Y.name, sorted(lhs.items()), sorted(rhs.items()))
print("K_0 pairing formula chi(Mor(X,Y)) (q-q^-1) = (q+q^-1)(Xb~ Yb + Xc~ Yc) + Xb~ Yc + Xc~ Yb verified:", ok)
