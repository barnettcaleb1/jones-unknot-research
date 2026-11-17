import random, sympy as S
from annulus_eval import E_minus, E_plus, mod_phi5, Q
rnd = random.Random(7); ok = integ = 0; N = 40
for _ in range(N):
    n = rnd.choice([2, 3, 4]); D = []
    for _ in range(rnd.randint(2, 6)):
        j = rnd.randrange(n-1); D.append(('e', j) if rnd.random() < 0.25 else ('s', j, rnd.choice([1, -1])))
    em, ep = E_minus(D, n), E_plus(D, n)
    ok += mod_phi5(em - ep) == 0
    integ += all(c.is_integer for c in S.Poly(S.expand(em*Q**60), Q).coeffs()) and all(c.is_integer for c in S.Poly(S.expand(ep*Q**60), Q).coeffs())
print(f'{ok}/{N} equal at zeta5; {integ}/{N} both integral Laurent polynomials in Q')
