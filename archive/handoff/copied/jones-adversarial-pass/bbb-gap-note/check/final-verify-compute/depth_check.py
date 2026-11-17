# Depth ((t+1)-adic order of rho(Phi0) - I) in both orientations; my own root-multiplicity routine.
src = open('$HOME/jones-adversarial-pass/bbb-gap-note/check/final-verify-compute/conv_check.py').read()
exec(src.split("CONVS = {")[0])
from fractions import Fraction as Fr
def mult_m1(p):                       # multiplicity of t = -1 as a root of the Laurent polynomial p != 0
    lo, hi = min(p), max(p); c = [Fr(p.get(e, 0)) for e in range(lo, hi + 1)]   # coefficients of t^lo * q(t)
    k = 0
    while sum(x * (-1) ** i for i, x in enumerate(c)) == 0:
        # synthetic division of q(t) by (t + 1), coefficients in increasing degree
        hi_first = c[::-1]; out = [hi_first[0]]
        for x in hi_first[1:-1]: out.append(x - out[-1])
        c = out[::-1]; k += 1
    return k
def depth(M): return min(mult_m1(p) for p in (x for r in minusI(M) for x in r) if p)
assert mult_m1({0: 1, 1: 2, 2: 1}) == 2 and mult_m1({0: 1, 3: 1}) == 1 and mult_m1({-3: 1, 0: 1}) == 1 and mult_m1({0: 1, 1: -1}) == 0
for name, M in [("U", U(Phi0, 4)), ("U, t->1/t", mapM(tinv, U(Phi0, 4))), ("U of mirror word", U(mirror(Phi0), 4)),
                ("U contragredient", tr(U(inv(Phi0), 4))), ("R", R(Phi0, 4)), ("R of mirror word", R(mirror(Phi0), 4)),
                ("U in B5 of mirror word", U(mirror(Phi0), 5))]:
    print(f"{name:26} depth = {depth(M)}")
