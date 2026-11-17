# Random bare words W in <M,J>; tensors C = f*G*W*E^eps (and E^eps on the left);
# exact evaluation in Q(zeta_8)=Q[A]/(A^4+1); gauge by D=diag(1,i), i=A^2.
# Checks: (a) D^-1 W(zeta) D = scalar * SL2(Z);  (b) D^-1 (W E)(zeta) D = scalar * integral det -1;
# (c) normal form C(zeta) = v [[i c, d],[a, -i b]];  (d) sign of det C / C_anchor^2 at all four anchors.
import sympy as sp, random
A = sp.symbols('A')
PHI = sp.Poly(A**4+1, A, domain='QQ')
d = -A**2 - A**-2
G = sp.Matrix([[d,1],[1,d]])
M = sp.Matrix([[A,0],[1/A,-A**-3]])
Mi = sp.Matrix([[1/A,0],[A,-A**3]])
J = sp.Matrix([[0,1],[1,0]])
E = sp.Matrix([[d,1],[-1,-d]])
assert (M*Mi).applyfunc(sp.simplify) == sp.eye(2)

def red(e):
    """reduce a Laurent polynomial in A to Q[A]/(A^4+1) (A^-1 = -A^3)."""
    e = sp.expand(e)
    e = sp.expand(e.subs(A**-1, -A**3)) if e.has(A) else e
    # generic: multiply out negative powers
    e = sp.together(e)
    num, den = sp.fraction(e)
    num = sp.Poly(num, A, domain='QQ'); den = sp.Poly(den, A, domain='QQ')
    if den.degree() > 0 or den.LC() != 1:
        den_inv = sp.invert(den, PHI)
        num = (num*den_inv)
    return num.rem(PHI)
def redM(X): return X.applyfunc(lambda e: red(e).as_expr())
def mul(a,b): return (sp.Poly(a,A,domain='QQ')*sp.Poly(b,A,domain='QQ')).rem(PHI).as_expr()
def inv(a): return sp.invert(sp.Poly(a,A,domain='QQ'), PHI).as_expr()
def is_rational(a):
    return sp.Poly(a, A, domain='QQ').degree() <= 0
I_ = A**2   # i = zeta^2
Dg = sp.diag(1, I_); Dgi = sp.diag(1, -I_)
def gauge(X): return redM(Dgi*X*Dg)
def normalize(X):
    """return (scalar s, rational matrix L) with X = s*L, dividing by first nonzero entry."""
    for e in X:
        if red(e).as_expr() != 0:
            s = e; break
    si = inv(s)
    L = X.applyfunc(lambda e: mul(e, si))
    assert all(is_rational(e) for e in L), L
    L = L.applyfunc(sp.Rational)
    return s, L
def primitive_integral(L):
    den = sp.ilcm(*[sp.Rational(e).q for e in L])
    L = L*den
    g = sp.igcd(*[int(e) for e in L])
    return L/g

random.seed(20261115)
gens = {'M':M,'m':Mi,'J':J}
bad = 0; n_tests = 0
stats = {('in','diag'):set(), ('in','off'):set(), ('out','diag'):set(), ('out','off'):set()}
for trial in range(60):
    L_ = random.randint(1,9)
    word = ''.join(random.choice('MmJ') for _ in range(L_))
    W = sp.eye(2)
    for ch in word: W = (W*gens[ch]).applyfunc(sp.expand)
    Wg = gauge(W)
    s, Lw = normalize(Wg); Lw = primitive_integral(Lw)
    assert all(e == int(e) for e in Lw) and Lw.det() == 1, (word, Lw)      # (a)
    for eps, side in [(0,'R'),(1,'R'),(1,'L')]:
        S = W if eps == 0 else (W*E if side == 'R' else E*W)
        S = S.applyfunc(sp.expand)
        Sg = gauge(S)
        s, L = normalize(Sg); L = primitive_integral(L)
        detL = L.det()
        assert all(e == int(e) for e in L) and detL == (1 if eps == 0 else -1), (word, eps, L)   # (b)
        # make s consistent with primitive L: Sg = s' * L
        k = [(i,j) for i in range(2) for j in range(2) if L[i,j] != 0][0]
        sp_ = mul(Sg[k], sp.Rational(1, L[k]))
        a,b,c,dd = L[0,0], L[0,1], L[1,0], L[1,1]
        C = redM((G*S).applyfunc(sp.expand))
        NF = sp.Matrix([[I_*c, dd],[a, -I_*b]]).applyfunc(lambda e: mul(e, sp_))
        assert (C - NF).applyfunc(lambda e: red(e).as_expr()) == sp.zeros(2,2), (word, eps)      # (c)
        detC = red(C.det()).as_expr()
        for (i,j) in [(0,0),(0,1),(1,0),(1,1)]:
            if C[i,j] == 0: continue
            r = mul(detC, inv(mul(C[i,j], C[i,j])))
            assert is_rational(r), r
            r = sp.Rational(r)
            n_tests += 1
            key = ('in' if eps == 0 else 'out', 'diag' if i == j else 'off')
            stats[key].add(sp.sign(r))
            # predicted values
            entryL = {(0,0):c,(1,1):b,(0,1):dd,(1,0):a}[(i,j)]
            pred = sp.Rational(detL,1) * (1 if i == j else -1) / entryL**2   # det C = -detL*v^2; C_ii^2 = -entry^2 v^2; C_ij^2 = entry^2 v^2
            assert r == pred, (word, eps, i, j, r, pred)
print('anchor tests:', n_tests)
for k,v in stats.items(): print(k, 'signs observed:', v)
print('ALL ASSERTIONS PASSED: (a) Gamma -> scalar*SL2(Z); (b) outer coset -> scalar*integral det -1;')
print(' (c) C(zeta)=v[[ic,d],[a,-ib]]; (d) det C/C_ij^2 = detL*(-1)^(i+j)/entry^2')
