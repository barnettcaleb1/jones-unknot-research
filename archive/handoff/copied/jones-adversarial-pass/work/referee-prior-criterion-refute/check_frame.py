"""Independent check of the double-frame lemma and of the foreign-line = collision identity.
Own TL code; nothing imported from the workspace or from sibling scratch dirs."""
import random
import sympy as sp

A = sp.symbols('A')
d = -A**2 - A**-2

def matchings(pts):
    if not pts:
        return [()]
    a, out = pts[0], []
    for k in range(1, len(pts), 2):
        for x in matchings(pts[1:k]):
            for y in matchings(pts[k + 1:]):
                out.append(((a, pts[k]),) + x + y)
    return out

B = [tuple(sorted(m)) for m in matchings(list(range(1, 7)))]
idx = {m: i for i, m in enumerate(B)}

def e(i):
    M = sp.zeros(5, 5)
    for j, m in enumerate(B):
        P = {}
        for a, b in m:
            P[a] = b; P[b] = a
        if P[i] == i + 1:
            M[j, j] += d
        else:
            a, b = P[i], P[i + 1]
            n = [q for q in m if i not in q and i + 1 not in q] + [(i, i + 1), tuple(sorted((a, b)))]
            M[idx[tuple(sorted(n))], j] += 1
    return M

E = {i: e(i) for i in range(1, 6)}
S = {i: A * sp.eye(5) + E[i] / A for i in range(1, 6)}
Si = {i: S[i].inv() for i in range(1, 6)}
simp = lambda M: M.applyfunc(lambda x: sp.factor(sp.cancel(x)))
assert simp(S[1] * S[2] * S[1] - S[2] * S[1] * S[2]) == sp.zeros(5, 5)
print('basis', B)

# Gram / Hermitian form
def loops(m, n):
    adj = {}
    for a, b in list(m) + list(n):
        adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
    seen, c = set(), 0
    for p in adj:
        if p in seen:
            continue
        c += 1; st = [p]
        while st:
            q = st.pop()
            if q in seen:
                continue
            seen.add(q); st.extend(adj[q])
    return c
G = sp.Matrix(5, 5, lambda i, j: d ** loops(B[i], B[j]))
bar = lambda M: M.applyfunc(lambda x: x.subs(A, 1 / A))
H = lambda x, y: sp.factor(sp.cancel((bar(x).T * G * y)[0, 0]))

Tc0 = simp((S[1] * S[2]) ** 3)
v0 = (Tc0 - A**6 * sp.eye(5)).nullspace()
assert len(v0) == 1
v0 = simp(v0[0] / v0[0][4] * (A**4 + 1 + A**-4))
print('v_c0 =', list(v0))
print('e1 v0 = 0:', simp(E[1] * v0) == sp.zeros(5, 1), ' e5 v0 = 0:', simp(E[5] * v0) == sp.zeros(5, 1))

# U = ker e1 cap ker e5
N = E[1].col_join(E[5]).nullspace()
print('dim U =', len(N))
Ub = sp.Matrix.hstack(*N)
def restr(M):
    R = simp((Ub.T * Ub).inv() * Ub.T * (M * Ub))
    assert simp(Ub * R - M * Ub) == sp.zeros(5, 2)
    return R
X = restr(Tc0); Y = restr(simp(S[3] ** 2))
print('eig X', sp.factor(X.charpoly().as_expr()), ' eig Y', sp.factor(Y.charpoly().as_expr()))

def degA(f):
    f = sp.cancel(sp.together(f))
    n, dn = sp.fraction(f)
    if n == 0:
        return -10**9
    return sp.Poly(sp.expand(n), A).degree() - sp.Poly(sp.expand(dn), A).degree()
def tau(g):
    return max(0, 2 * degA(g.trace()) - degA(g.det()))
Xi, Yi = simp(X.inv()), simp(Y.inv())
gens = {'x': X, 'X': Xi, 'y': Y, 'Y': Yi}
inv = {'x': 'X', 'X': 'x', 'y': 'Y', 'Y': 'y'}
print('tau X, Y, XY, XY^-1 =', tau(X), tau(Y), tau(simp(X * Y)), tau(simp(X * Yi)))
# overlap from the pair: tau(XY^-1) - tau(XY) = 2*overlap (coherent case)
# Schottky sanity: random cyclically reduced words all hyperbolic
random.seed(1)
bad = 0
for trial in range(40):
    L = random.randint(2, 8)
    w = []
    while len(w) < L:
        c = random.choice('xXyY')
        if w and inv[c] == w[-1]:
            continue
        w.append(c)
    if inv[w[0]] == w[-1]:
        continue
    M = sp.eye(2)
    for c in w:
        M = M * gens[c]
    M = simp(M)
    if tau(M) == 0:
        bad += 1; print('elliptic word', ''.join(w))
print('random cyclically reduced words with tau = 0:', bad)

# Foreign line = collision: rho(s1) v = mu v  <=>  e1 v = 0 or v in im e1. Check on a random psi
# that [rho(s1) rho(psi) v0] = [rho(psi) v0] holds iff e1 rho(psi) v0 = 0 (tautology check, numerically at A=3/7).
def word_mat(wd, val):
    M = sp.eye(5)
    for g in wd:
        M = M * (S[abs(g)] if g > 0 else Si[abs(g)]).subs(A, val)
    return M
val = sp.Rational(3, 7)
for trial in range(3):
    wd = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(8)]
    w = word_mat(wd, val) * v0.subs(A, val)
    w2 = S[1].subs(A, val) * w
    coll = sp.Matrix.hstack(w, w2).rank() == 1
    fl = (E[1].subs(A, val) * w) == sp.zeros(5, 1)
    print('word', wd, 'collision(c, s1 c):', coll, ' foreign line:', fl)
# positivity: on the unit circle near A = i the form is definite, so Q = H(v, e1 v) = |e1 v|^2/delta
th = sp.pi / 2 + sp.Rational(1, 20)
Gn = sp.N(G.subs(A, sp.exp(sp.I * th)), 30)
print('Gram eigenvalues near A=i (Hermitian):', [sp.N(sp.re(x), 6) for x in Gn.eigenvals().keys()])
