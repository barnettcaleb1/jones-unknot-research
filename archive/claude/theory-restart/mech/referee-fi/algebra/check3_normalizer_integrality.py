# (1) Projective centralizer of Gamma in PGL_2(K) is trivial  => N_{PGL_2(K)}(Gamma) embeds in Aut(PSL2(Z))=PGL2(Z),
#     so the full projective normalizer is Gamma or Gamma x| C2; E gives the latter.  (Independent of Theorem A.)
# (2) [E] not in Gamma: det E is not (Laurent unit) x (square in K).
# (3) Integrality step of Theorem B.
# (4) Determinant classes mod squares of bare words (alpha in hS=alpha S k is a Laurent unit).
import sympy as sp, random
A = sp.symbols('A')
d = -A**2 - A**-2
G = sp.Matrix([[d,1],[1,d]])
M = sp.Matrix([[A,0],[1/A,-A**-3]])
Mi = sp.Matrix([[1/A,0],[A,-A**3]])
J = sp.Matrix([[0,1],[1,0]])
E = sp.Matrix([[d,1],[-1,-d]])
x1,x2,x3,x4 = sp.symbols('x1:5')
X = sp.Matrix([[x1,x2],[x3,x4]])
print('(1) twisted centralizer: solve X J = s1 J X, X M = s2 M X')
for s1 in (1,-1):
    for s2 in (1,-1):
        eqs = list((X*J - s1*J*X)) + list(((X*M - s2*M*X)*A**3).applyfunc(sp.expand))
        sol = sp.solve(eqs, [x1,x2,x3,x4], dict=True)
        Xs = [X.subs(s) for s in sol]
        print('  s1=%+d s2=%+d ->' % (s1,s2), Xs, ' dets:', [sp.simplify(x.det()) for x in Xs])
# characters: X g X^-1 = lam(g) g ; lam(J)^2=1 from J^2=I ; lam(M)^2=1 from det. So the four cases above are exhaustive.
print('  tr M =', sp.simplify(M.trace()), '(nonzero => X M X^-1 = -M impossible)')

print('(2) det E =', sp.factor(E.det()), ';  squarefree part nontrivial => not unit*square in Q(A)')
p = sp.Poly(sp.expand(-A**4*E.det()), A)
print('    A^8+A^4+1 squarefree:', sp.gcd(p, p.diff(A)) == 1, ' factors:', sp.factor_list(p.as_expr()))

print('(3) integrality step')
random.seed(7)
gens = {'M':M,'m':Mi,'J':J}
def word(n):
    W = sp.eye(2)
    for ch in ''.join(random.choice('MmJ') for _ in range(n)): W = (W*gens[ch]).applyfunc(sp.expand)
    return W
for f in [-A**5, A**2+1, 1 - A + A**2]:
    W = word(6)
    C = (f*G*W).applyfunc(sp.expand)
    Winv = W.inv().applyfunc(lambda e: sp.expand(sp.simplify(e)))
    # W^-1 entries are Laurent polynomials (det W a Laurent unit)
    assert all(sp.fraction(sp.together(e))[1].is_number or sp.Poly(sp.fraction(sp.together(e))[1],A).is_monomial for e in Winv)
    f_rec = sp.expand(sp.simplify((C*Winv)[0,1]))
    # seeds: v = P e_i, w = Q e_j rational bracket vectors
    P = word(4); Q = word(5)
    vals = [sp.factor(sp.expand((P[:,i].T*C*Q[:,j])[0,0])) for i in range(2) for j in range(2)]
    print('   f =', f, '| recovered (C W^-1)_12 =', sp.factor(f_rec), '| det W =', sp.simplify(W.det()))
    print('      seed brackets divisible by f:', all(sp.simplify(sp.cancel(v/f)).as_numer_denom()[1].as_poly(A).is_monomial if not sp.simplify(sp.cancel(v/f)).as_numer_denom()[1].is_number else True for v in vals))
print('(4) det classes: det M =', sp.simplify(M.det()), ' det J =', J.det(),
      ' => det(bare word) = +-A^(2k)... so alpha^2 = det h/det k = +-A^(2k); -1 not a square in Q(A) => alpha = +-A^k')
