# Referee check (independent code). W(6,0), sigma_i -> A + A^-1 e_i.
# (1) first lemma data; (2) N-degeneracy e1*rho(s3 s5^-1) = e1; (3) structure of the smallest (length-2) case.
import sympy as sp
A = sp.symbols('A')
d = -A**2 - A**-2

def ncm(p):
    if not p: return [()]
    a = p[0]; out = []
    for k in range(1, len(p), 2):
        for x in ncm(p[1:k]):
            for y in ncm(p[k+1:]): out.append(((a, p[k]),) + x + y)
    return out
B = [tuple(sorted(m)) for m in ncm(list(range(6)))]
B.sort(key=lambda m: [x for pr in m for x in pr])
IDX = {m: i for i, m in enumerate(B)}
print('basis:', B)

def partner(m):
    P = {}
    for a, b in m: P[a] = b; P[b] = a
    return P

def E(i):  # cap/cup at points i,i+1 (0-based)
    M = sp.zeros(5, 5)
    for j, m in enumerate(B):
        P = partner(m)
        if P[i] == i + 1: M[j, j] += d
        else:
            a, b = P[i], P[i + 1]
            n = [q for q in m if i not in q and i + 1 not in q] + [(i, i + 1), tuple(sorted((a, b)))]
            M[IDX[tuple(sorted(n))], j] += 1
    return M
Es = [E(i) for i in range(5)]
I5 = sp.eye(5)
S = [A * I5 + Es[i] / A for i in range(5)]
Si = [I5 / A + A * Es[i] for i in range(5)]
ok = all(sp.simplify(S[i] * Si[i] - I5) == sp.zeros(5, 5) for i in range(5))
ok &= all(sp.simplify(S[i] * S[i+1] * S[i] - S[i+1] * S[i] * S[i+1]) == sp.zeros(5, 5) for i in range(4))
ok &= all(sp.simplify(S[i] * S[j] - S[j] * S[i]) == sp.zeros(5, 5) for i in range(5) for j in range(i + 2, 5))
print('braid relations:', ok)

def word(w):
    M = I5
    for x in w:
        M = M * (S[x - 1] if x > 0 else Si[-x - 1])
    return sp.expand(M)

# Gram form and Hermitian form
def loops(m, n):
    P, Q = partner(m), partner(n); seen = set(); c = 0
    for s in range(6):
        if s in seen: continue
        c += 1; x = s; side = 0
        while True:
            seen.add(x)
            y = P[x] if side == 0 else Q[x]
            seen.add(y); x = y; side ^= 1
            if x == s and side == 0: break
    return c
G = sp.Matrix(5, 5, lambda i, j: d ** loops(B[i], B[j]))
bar = lambda M: M.subs(A, 1 / A)
H = lambda x, y: sp.simplify((bar(x).T * G * y)[0, 0])

# v_c0: ker e1 ∩ ker e2
v0 = Es[0].col_join(Es[1]).nullspace(); assert len(v0) == 1
v0 = sp.simplify(v0[0] / v0[0][0])
print('v_c0 (normalised):', [sp.factor(x) for x in v0])
Nn = sp.factor(H(v0, v0)); print('H(v0,v0) =', Nn)

# (2) N-degeneracy
h = word([3, -5])
print('e1*rho(s3 s5^-1) == e1 :', sp.simplify(Es[0] * h - Es[0]) == sp.zeros(5, 5))
print('rho(s3 s5^-1) == identity on all of W? ', sp.simplify(h - I5) == sp.zeros(5, 5))

# (1) first lemma: U = ker e1 ∩ ker e5
Ub = sp.Matrix.hstack(*Es[0].col_join(Es[4]).nullspace()); print('dim U =', Ub.shape[1])
def restr(M):
    R = sp.simplify((Ub.T * Ub).inv() * Ub.T * (M * Ub))
    assert sp.simplify(Ub * R - M * Ub) == sp.zeros(5, 2); return R
X = restr(word([1, 2] * 3)); Y = restr(word([3, 3]))
def deg(f):
    f = sp.together(sp.simplify(f)); n, dn = sp.fraction(f)
    return sp.degree(sp.expand(n * A ** 80), A) - sp.degree(sp.expand(dn * A ** 80), A)
def ldeg(f):  # valuation at A=0 (lowest degree)
    f = sp.together(sp.simplify(f)); n, dn = sp.fraction(f)
    pn = sp.Poly(sp.expand(n * A ** 80), A); pd = sp.Poly(sp.expand(dn * A ** 80), A)
    lo = lambda p: min(m[0] for m in p.monoms())
    return lo(pn) - lo(pd)
tau = lambda g: 2 * deg(g.trace()) - deg(g.det())       # tree at A = infinity
tau0 = lambda g: -2 * ldeg(g.trace()) + ldeg(g.det())   # tree at A = 0
print('eig X:', X.eigenvals(), ' eig Y:', Y.eigenvals())
for nm, g in [('X', X), ('Y', Y), ('XY', X * Y), ('XY^-1', X * Y.inv()), ('X^2Y^-1', X**2 * Y.inv()), ('X^3Y^-2', X**3 * Y.inv()**2)]:
    print(nm, 'tau_inf =', tau(g), ' tau_0 =', tau0(g))
