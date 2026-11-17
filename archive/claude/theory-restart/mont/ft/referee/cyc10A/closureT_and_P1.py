import sympy as S
from annulus_eval import run, Q, A
Lm = lambda n: Q**(2*n) - (Q + 1/Q)*(-1/Q)**n
def to_Q(num, nF):
    val = S.cancel(S.together(sum(S.Integer(v)*A**e for e, v in num.items()) / (-A**2 - A**-2)**(nF+1)))
    return S.simplify(val.subs(A, (-1/Q)**S.Rational(1,4)))
# closure of T^n in the 2-strand picture: axis at 0, colour-2 cable at 1,2, T = s0 s1 s1 s0 (type x), f2 once, all closed
for n in range(1, 6):
    w = [('cap', 0), ('cap', 1), ('cap', 2)]          # axis pair (0, 5)... nested: 0-5, 1-4, 2-3
    w += [('F', 1)]
    for _ in range(n): w += [('x', 0), ('x', 1), ('x', 1), ('x', 0)]
    w += [('cup', 2), ('cup', 1), ('cup', 0)]
    p = run(w)
    val = S.cancel(sum(S.Integer(v)*A**e for e, v in p.items()) / (-A**2 - A**-2)**2)
    target = Lm(n).subs(Q, -A**-4)
    print(f'reduced closure(T^{n}) == L_{n}^- :', S.simplify(val - target) == 0)
# TL-level projector identity (7): on (C^2)^{x3}, colour 1 = factor 0, colour 2 = factors 1,2 with f2
def TLrep(var, n):
    e = S.zeros(4); e[1,1] = -var**2; e[1,2] = 1; e[2,1] = 1; e[2,2] = -var**-2
    return [S.kronecker_product(S.kronecker_product(S.eye(2**i), e), S.eye(2**(n-i-2))) for i in range(n-1)]
E = TLrep(A, 3); I8 = S.eye(8); d0 = -A**2 - A**-2
s = [A*I8 + A**-1*E[i] for i in range(2)]
F = I8 - E[1]/d0
T = F*s[0]*s[1]*s[1]*s[0]
Qo = -A**-4
P1 = (T + Qo**-1*F)/(Qo**2 + Qo**-1)
z = lambda M: all(S.simplify(x) == 0 for x in M)
print('(T - Q^2)(T + Q^-1) = 0 on V1xV2:', z((T - Qo**2*F)*(T + Qo**-1*F)))
print('P1 idempotent:', z(P1*P1 - P1), '| rank P1 = 2 (= dim V1):', P1.subs(A, S.Rational(3,2)).rank() == 2)
# P1 = i p: image is the attached channel = image of the colour-1 -> colour-1 x colour-2 vertex (f2 applied to cup on 0,1 ... )
# vertex i: V1 -> V1 x V2 realised as (cup on strands 1,2 inserted? ) -- check P1 kills V3: T acts by -Q^-1 there; done by min poly.
