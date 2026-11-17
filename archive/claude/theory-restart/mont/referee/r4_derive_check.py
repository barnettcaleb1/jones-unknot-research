"""Referee: independent redo of the Theorem V unit derivation (Vandermonde in lambda = (1,-t,t^3), admissibility zeros)."""
import sympy as sp
t, up, um, A, B = sp.symbols('t u_p u_m A B')
Phi3 = 1 + t + t**2; Phi5 = 1 + t + t**2 + t**3 + t**4
# closure values as linear forms in (A,B): e1^T X^-1 v and e1^T X v with v1 = A, v2 = (B - A)/(1 - t^3)
X = sp.Matrix([[1, 1 - t**4], [0, -t]])
v = sp.Matrix([A, (B - A) / (1 - t**3)])
J1 = sp.simplify((X.inv() * v)[0]); Jm1 = sp.simplify((X * v)[0])
J0 = A + (t + 1/t) * B                      # partial trace tr_{V2}(A P1 + B P3) = A + [4]/[2] B
lam = [1, -t, t**3]
K = sp.symbols('K0A K0B K2A K2B K4A K4B')
Kc = [K[0]*A + K[1]*B, K[2]*A + K[3]*B, K[4]*A + K[5]*B]
eqs = []
for a, val in [(1, up*J1), (0, J0), (-1, um*Jm1)]:
    expr = sp.expand(sp.together(sum(lam[c]**a * Kc[c] for c in range(3)) - val))
    num = sp.numer(sp.together(expr))
    P = sp.Poly(num, A, B)
    eqs += [P.coeff_monomial(A), P.coeff_monomial(B)]
sol = sp.solve(eqs, K, dict=True)[0]
cond = [sp.factor(sp.numer(sp.together(sol[K[1]]))), sp.factor(sp.numer(sp.together(sol[K[4]])))]
print('K0_B numerator:', cond[0]); print('K4_A numerator:', cond[1])
rel = sp.solve(cond[0], up)
print('from K0_B = 0: u_p =', [sp.expand(r) for r in rel])
print('K4_A = 0 then holds automatically:', [sp.simplify(cond[1].subs(up, r)) for r in rel])
for upv, umv in [(t**4, t**-4), (-t, -1/t)]:
    s2 = {k: sp.factor(sp.simplify(sol[k].subs({up: upv, um: umv}))) for k in K}
    print('units', (upv, umv), ' K0 =', s2[K[0]], '*A +', s2[K[1]], '*B ; K2 =', s2[K[2]], '*A +', s2[K[3]], '*B ; K4 =', s2[K[4]], '*A +', s2[K[5]], '*B')
    print('   identity-box ratios K0:K2:K4 =', [sp.factor(s2[K[0]] + s2[K[1]]), sp.factor(s2[K[2]] + s2[K[3]]), sp.factor(s2[K[4]] + s2[K[5]])])
