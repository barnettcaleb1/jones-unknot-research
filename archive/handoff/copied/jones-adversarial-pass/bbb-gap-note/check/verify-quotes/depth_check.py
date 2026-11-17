# Independent check of the (t+1)-adic depth of rho(Phi0), claimed exactly 1 in the note (lines 91, 109).
# Laurent polynomials as dicts {exponent: int}. Unreduced and reduced Burau, words read left to right.
# Phi0 = [(s1 s2)^6, [[A14, A24], A34]], [x, y] = x y x^-1 y^-1.
from fractions import Fraction as F

def padd(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
        if c[k] == 0: del c[k]
    return c
def pmul(a, b):
    c = {}
    for i, x in a.items():
        for j, y in b.items():
            c[i + j] = c.get(i + j, 0) + x * y
    return {k: v for k, v in c.items() if v != 0}
def mmul(A, B):
    n = len(A)
    C = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]: continue
            for j in range(n):
                if B[k][j]: C[i][j] = padd(C[i][j], pmul(A[i][k], B[k][j]))
    return C
def eye(n): return [[({0: 1} if i == j else {}) for j in range(n)] for i in range(n)]
ONE, T, TI = {0: 1}, {1: 1}, {-1: 1}
def unred(n, i, inv):
    M = eye(n); k = i - 1
    blk = [[{0: 1, 1: -1}, T], [ONE, {}]] if not inv else [[{}, ONE], [TI, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2): M[k + r][k + c] = blk[r][c]
    return M
def red(n, i, inv):
    # reduced Burau (row convention): s_i -> I except row k: M[k][k-1]=t, M[k][k]=-t, M[k][k+1]=1
    d = n - 1; k = i - 1
    M = eye(d); M[k][k] = {1: -1}
    if k - 1 >= 0: M[k][k - 1] = T
    if k + 1 < d: M[k][k + 1] = ONE
    if not inv: return M
    # inverse: row k: M[k][k-1]=1, M[k][k]=-t^-1, M[k][k+1]=t^-1
    N = eye(d); N[k][k] = {-1: -1}
    if k - 1 >= 0: N[k][k - 1] = ONE
    if k + 1 < d: N[k][k + 1] = TI
    return N
def word(gen, n, d, w):
    M = eye(d)
    for g in w: M = mmul(M, gen(n, abs(g), g < 0))
    return M
def winv(w): return [-x for x in reversed(w)]
def comm(a, b): return a + b + winv(a) + winv(b)
def A(i, j):
    up = list(range(j - 1, i, -1)); return up + [i, i] + winv(up)
a = [1, 2] * 6
b = comm(comm(A(1, 4), A(2, 4)), A(3, 4))
phi0 = comm(a, b)

def to_poly(p):
    # Laurent dict -> (shift, list of coefficients of an honest polynomial)
    if not p: return 0, []
    lo, hi = min(p), max(p)
    return lo, [p.get(k, 0) for k in range(lo, hi + 1)]
def div_tplus1(coeffs):
    # divide polynomial (coeffs low->high) by (t+1); return quotient or None if not divisible
    c = coeffs[:]; q = [0] * (len(c) - 1)
    for k in range(len(c) - 1, 0, -1):
        q[k - 1] = c[k]; c[k - 1] -= c[k]; c[k] = 0
    return q if c[0] == 0 else None
def depth(M):
    n = len(M)
    E = [[padd(M[i][j], {0: -1} if i == j else {}) for j in range(n)] for i in range(n)]
    entries = [to_poly(E[i][j])[1] for i in range(n) for j in range(n) if E[i][j]]
    if not entries: return float('inf')
    d = 0
    while True:
        nxt = []
        for c in entries:
            q = div_tplus1(c)
            if q is None: return d
            nxt.append(q)
        entries = nxt; d += 1

# sanity: braid relations and inverses
for gen, n, d in ((unred, 4, 4), (red, 4, 3)):
    assert word(gen, n, d, [1, -1]) == eye(d) and word(gen, n, d, [-2, 2]) == eye(d)
    assert word(gen, n, d, [1, 2, 1]) == word(gen, n, d, [2, 1, 2])
    assert word(gen, n, d, [2, 3, 2]) == word(gen, n, d, [3, 2, 3])
    assert word(gen, n, d, [1, 3]) == word(gen, n, d, [3, 1])
print("word length", len(phi0))
for name, gen, n, d in (("unreduced B4", unred, 4, 4), ("reduced B4", red, 4, 3), ("unreduced B5 f(Phi0)", unred, 5, 5)):
    M = word(gen, n, d, phi0)
    print(f"{name}: rho(Phi0) == I as Laurent matrix? {M == eye(d)}; (t+1)-adic depth of rho(Phi0)-I = {depth(M)}")
    D = word(gen, n, d, a)
    print(f"{name}: depth of rho((s1s2)^6)-I = {depth(D)}")
