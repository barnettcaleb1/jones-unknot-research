# Independent re-derivation (does not import or exec phi0_check.py).
# Depth = (t+1)-adic valuation of rho(w) - I.  Substitute t = -1 + s and work in Z[[s]] / (s^K):
# t = -1 + s and t^-1 = -(1 + s + s^2 + ...) are units there, and Z[t, 1/t] -> Z[[s]] is injective,
# so the s-adic valuation of an entry equals its (t+1)-adic valuation (capped at K).
import sys
K = 14

def sadd(a, b): return [x + y for x, y in zip(a, b)]
def smul(a, b):
    r = [0] * K
    for i, x in enumerate(a):
        if x:
            for j in range(K - i):
                r[i + j] += x * b[j]
    return r
def const(c): return [c] + [0] * (K - 1)
ZERO, ONE = const(0), const(1)
T = [-1, 1] + [0] * (K - 2)                 # t = -1 + s
TI = [-1] * K                               # 1/t = -1/(1 - s)
assert smul(T, TI) == ONE
def neg(a): return [-x for x in a]
def ident(m): return [[ONE if i == j else ZERO for j in range(m)] for i in range(m)]
def mmul(A, B):
    m = len(A)
    out = []
    for i in range(m):
        row = []
        for j in range(m):
            acc = ZERO
            for k in range(m):
                acc = sadd(acc, smul(A[i][k], B[k][j]))
            row.append(acc)
        out.append(row)
    return out
def transpose(A): return [list(r) for r in zip(*A)]

# --- generator matrices -------------------------------------------------------------
def U(n, a):                                 # BB05 4.2: s_i -> I_{i-1} + [[1-t, t], [1, 0]] + I_{n-i-1}
    i = abs(a); M = ident(n)
    if a > 0: blk = [[sadd(ONE, neg(T)), T], [ONE, ZERO]]
    else:     blk = [[ZERO, ONE], [TI, sadd(ONE, neg(TI))]]
    for r in range(2):
        for c in range(2):
            M[i - 1 + r][i - 1 + c] = blk[r][c]
    return M
def R(n, a):                                 # note: row i of I_{n-1} -> (t, -t, 1) in cols i-1, i, i+1
    i = abs(a); M = ident(n - 1); r = i - 1
    vals = (T, neg(T), ONE) if a > 0 else (ONE, neg(TI), TI)
    for c, v in zip((r - 1, r, r + 1), vals):
        if 0 <= c < n - 1: M[r][c] = v
    return M
def BB(n, a):                                # BB05 4.2 reduced: I_{i-2} + [[1,-t,0],[0,-t,0],[0,-1,1]] + I_{n-i-2}
    i = abs(a); m = n - 1
    if a > 0:
        M = ident(m)
        blk = [[ONE, neg(T), ZERO], [ZERO, neg(T), ZERO], [ZERO, neg(ONE), ONE]]
        for x in range(3):
            for y in range(3):
                r, c = i - 2 + x, i - 2 + y          # 0-based rows/cols i-2, i-1, i (so -t at (i, i) 1-based)
                if 0 <= r < m and 0 <= c < m: M[r][c] = blk[x][y]
        return M
    # inverse: solve by Gauss over Z[[s]] -- the matrix is I off one column block; invert generically
    return inverse(BB(n, -a))
def inverse(M):                              # Gauss-Jordan over Z[[s]]; pivots must be units (constant term +-1)
    m = len(M); A = [row[:] + [ONE if i == j else ZERO for j in range(m)] for i, row in enumerate(M)]
    for col in range(m):
        piv = next(r for r in range(col, m) if A[r][col][0] in (1, -1))
        A[col], A[piv] = A[piv], A[col]
        p = A[col][col]
        # inverse of a unit power series p with p[0] = +-1
        q = [0] * K; q[0] = p[0]
        for k in range(1, K):
            q[k] = -p[0] * sum(p[j] * q[k - j] for j in range(1, k + 1))
        assert smul(p, q) == ONE
        A[col] = [smul(q, x) for x in A[col]]
        for r in range(m):
            if r != col and any(A[r][col]):
                f = A[r][col]
                A[r] = [sadd(x, neg(smul(f, y))) for x, y in zip(A[r], A[col])]
    return [row[m:] for row in A]

CONVS = {
    'U':   (lambda n, a: U(n, a),             lambda n: n),
    'UT':  (lambda n, a: transpose(U(n, a)),  lambda n: n),
    'R':   (lambda n, a: R(n, a),             lambda n: n - 1),
    'RT':  (lambda n, a: transpose(R(n, a)),  lambda n: n - 1),
    'BB05red': (lambda n, a: BB(n, a),        lambda n: n - 1),
}
def rep(w, n, conv):
    g, dim = CONVS[conv]
    M = ident(dim(n))
    for a in w:                                # left to right, as in the note
        M = mmul(M, g(n, a))
    return M
def depth(M):
    v = K
    for i, row in enumerate(M):
        for j, p in enumerate(row):
            q = sadd(p, neg(ONE)) if i == j else p
            for k, x in enumerate(q):
                if x:
                    v = min(v, k); break
    return v

# sanity: generators invert, braid relations hold (mod s^K) in every convention, n = 4
for conv in CONVS:
    for i in (1, 2, 3):
        assert rep([i, -i], 4, conv) == ident(CONVS[conv][1](4)), (conv, i)
    assert rep([1, 2, 1], 4, conv) == rep([2, 1, 2], 4, conv), conv
    assert rep([2, 3, 2], 4, conv) == rep([3, 2, 3], 4, conv), conv
    assert rep([1, 3], 4, conv) == rep([3, 1], 4, conv), conv

# --- the braids, built from scratch ----------------------------------------------------
def inv(w): return [-a for a in reversed(w)]
def comm(x, y): return x + y + inv(x) + inv(y)
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
X = [1, 2] * 6
b = comm(comm(A14, A24), A34)
Phi0 = comm(X, b)
assert len(Phi0) == 112
s3c = [3] + Phi0 + [-3]
C = [comm(Phi0, s3c)]
for _ in range(3):
    C.append(comm(Phi0, C[-1]))
mirror = lambda w: [-a for a in w]

print('K =', K, '(depths >= K would print as', K, ')')
print('%-8s %6s %6s %6s %6s %6s   %s' % ('conv', 'Phi0', 'C1', 'C2', 'C3', 'C4', 'mirror: Phi0 C1'))
for conv in CONVS:
    ds = [depth(rep(Phi0, 4, conv))] + [depth(rep(c, 4, conv)) for c in C]
    md = [depth(rep(mirror(Phi0), 4, conv)), depth(rep(mirror(C[0]), 4, conv))]
    print('%-8s %6d %6d %6d %6d %6d   %s' % ((conv,) + tuple(ds) + (md,)))
    sys.stdout.flush()
# B_5, f = s_i -> s_i
print('B5 (f): ', {conv: (depth(rep(Phi0, 5, conv)), depth(rep(C[0], 5, conv))) for conv in CONVS})
