# Independent recomputation (no shared code) of the (t+1)-adic depths of
# C1 = [Phi0, s3 Phi0 s3^-1], C_{k+1} = [Phi0, C_k], in unreduced (U, UT) and
# reduced (R, RT, BB05) Burau matrices, B4.  Power series in s = t + 1, truncated at degree N.
# [x, y] = x y x^-1 y^-1, words multiplied left to right.
N = 14

def sadd(a, b): return [x + y for x, y in zip(a, b)]
def ssub(a, b): return [x - y for x, y in zip(a, b)]
def smul(a, b):
    r = [0] * N
    for i, x in enumerate(a):
        if x:
            for j in range(N - i):
                if b[j]:
                    r[i + j] += x * b[j]
    return r
ZERO = [0] * N
ONE = [1] + [0] * (N - 1)
T = [-1, 1] + [0] * (N - 2)          # t = -1 + s
TI = [-1] * N                         # 1/t = -1/(1 - s)
assert smul(T, TI) == ONE
def neg(a): return [-x for x in a]

def eye(m): return [[list(ONE) if i == j else list(ZERO) for j in range(m)] for i in range(m)]
def mmul(A, B):
    m = len(A)
    out = []
    for i in range(m):
        row = []
        for j in range(m):
            acc = list(ZERO)
            for k in range(m):
                if any(A[i][k]) and any(B[k][j]):
                    acc = sadd(acc, smul(A[i][k], B[k][j]))
            row.append(acc)
        out.append(row)
    return out
def transpose(A): return [list(r) for r in zip(*A)]

def U_gen(n, a):
    i = abs(a) - 1
    M = eye(n)
    blk = [[ssub(ONE, T), T], [ONE, ZERO]] if a > 0 else [[ZERO, ONE], [TI, ssub(ONE, TI)]]
    for r in range(2):
        for c in range(2):
            M[i + r][i + c] = list(blk[r][c])
    return M

def R_gen(n, a):
    # reduced: sigma_i replaces row i of I_{n-1} by (t, -t, 1) in cols i-1, i, i+1 (1-based);
    # inverse: row i = (1, -1/t, 1/t)
    i = abs(a)
    m = n - 1
    M = eye(m)
    vals = (T, neg(T), ONE) if a > 0 else (ONE, neg(TI), TI)
    row = [list(ZERO) for _ in range(m)]
    for c, v in zip((i - 1, i, i + 1), vals):
        if 1 <= c <= m:
            row[c - 1] = list(v)
    M[i - 1] = row
    return M

def BB_gen(n, a):
    # Birman-Brendle survey reduced matrices: I_{i-2} + [[1,-t,0],[0,-t,0],[0,-1,1]] + I_{n-i-2},
    # -t at (i,i); i.e. column i = (-t, -t, -1) in rows i-1, i, i+1. Inverse computed by formula check below.
    i = abs(a)
    m = n - 1
    M = eye(m)
    if a > 0:
        col = {i - 1: neg(T), i: neg(T), i + 1: [-1] + [0] * (N - 1)}
    else:
        # inverse of I + (c - e_i) e_i^T is I - (c - e_i) e_i^T / c_i with c_i = -t
        c = {i - 1: neg(T), i: neg(T), i + 1: [-1] + [0] * (N - 1)}
        w = {k: (ssub(v, ONE) if k == i else v) for k, v in c.items()}
        inv_ci = neg(TI)                           # 1/(-t)
        col = {}
        for k, v in w.items():
            col[k] = sadd(ONE if k == i else ZERO, neg(smul(v, inv_ci)))
    for r, v in col.items():
        if 1 <= r <= m:
            M[r - 1][i - 1] = list(v)
    return M

def rep(word, n, conv):
    if conv in ('U', 'UT'):
        g = lambda a: U_gen(n, a)
    elif conv in ('R', 'RT'):
        g = lambda a: R_gen(n, a)
    else:
        g = lambda a: BB_gen(n, a)
    tr = conv in ('UT', 'RT')
    M = eye(n if conv in ('U', 'UT') else n - 1)
    for a in word:
        G = g(a)
        if tr:
            G = transpose(G)
        M = mmul(M, G)
    return M

def depth(M):
    best = N
    for i, row in enumerate(M):
        for j, e in enumerate(row):
            e = ssub(e, ONE) if i == j else e
            for k, x in enumerate(e):
                if x:
                    best = min(best, k)
                    break
    return best

def inv(w): return [-a for a in reversed(w)]
def comm(x, y): return x + y + inv(x) + inv(y)

A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
X = [1, 2] * 6
b = comm(comm(A14, A24), A34)
Phi0 = comm(X, b)
c0 = [3] + Phi0 + [-3]

# sanity: generators times inverses are identity, braid relations hold (n = 4)
for conv in ('U', 'UT', 'R', 'RT', 'BB'):
    for i in (1, 2, 3):
        assert rep([i, -i], 4, conv) == eye(4 if conv in ('U', 'UT') else 3), (conv, i)
    assert rep([1, 2, 1], 4, conv) == rep([2, 1, 2], 4, conv)
    assert rep([2, 3, 2], 4, conv) == rep([3, 2, 3], 4, conv)
    assert rep([1, 3], 4, conv) == rep([3, 1], 4, conv)

for conv in ('U', 'UT', 'R', 'RT', 'BB'):
    P, Pi = rep(Phi0, 4, conv), rep(inv(Phi0), 4, conv)
    Q, Qi = rep(c0, 4, conv), rep(inv(c0), 4, conv)
    C = mmul(mmul(mmul(P, Q), Pi), Qi)
    Ci = mmul(mmul(mmul(Q, P), Qi), Pi)
    ds = []
    for k in range(4):
        ds.append(depth(C))
        C, Ci = mmul(mmul(mmul(P, C), Pi), Ci), mmul(mmul(mmul(C, P), Ci), Pi)
    print(f"{conv:3}: depth Phi0 = {depth(P)}, depths C1..C4 = {ds}")
