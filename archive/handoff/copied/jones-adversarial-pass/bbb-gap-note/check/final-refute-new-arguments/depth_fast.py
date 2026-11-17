# Remark 5 check, fast version.
# Unreduced Burau (same matrices as phi0_check.py, convention U) computed with t = -1 + u,
# entries as power series in u truncated at degree N (exact integers).  depth >= d  <=>  rho - I = 0 mod u^d.
# Nontriviality: exact Burau at t = 2 (rationals) != I.  Brunnian: delete each strand, B3 Burau (faithful) exact.
import sys, time
sys.path.insert(0, sys.argv[1])
from lib import inv, comm, red, pure, delete, Phi0
from fractions import Fraction
N = 9
def s_add(a, b): return [x + y for x, y in zip(a, b)]
def s_mul(a, b):
    r = [0] * N
    for i, x in enumerate(a):
        if x:
            for j in range(N - i):
                r[i + j] += x * b[j]
    return r
ZERO = [0] * N
ONE = [1] + [0] * (N - 1)
T = [-1, 1] + [0] * (N - 2)            # t = -1 + u
TINV = [-1] * N                        # 1/t = -1/(1-u) = -(1 + u + u^2 + ...)
ONEMT = s_add(ONE, [-x for x in T])     # 1 - t
ONEMTI = s_add(ONE, [-x for x in TINV]) # 1 - 1/t
def gen_series(n, a):
    i = abs(a)
    M = [[ONE if r == c else ZERO for c in range(n)] for r in range(n)]
    blk = [[ONEMT, T], [ONE, ZERO]] if a > 0 else [[ZERO, ONE], [TINV, ONEMTI]]
    for r in range(2):
        for c in range(2): M[i - 1 + r][i - 1 + c] = blk[r][c]
    return M
def right_mul_gen(M, n, a):            # M * gen(a), only columns i-1, i change
    i = abs(a) - 1
    G = gen_series(n, a)
    for row in M:
        x, y = row[i], row[i + 1]
        row[i] = s_add(s_mul(x, G[i][i]), s_mul(y, G[i + 1][i]))
        row[i + 1] = s_add(s_mul(x, G[i][i + 1]), s_mul(y, G[i + 1][i + 1]))
    return M
def burau_series(w, n):
    M = [[list(ONE) if r == c else list(ZERO) for c in range(n)] for r in range(n)]
    for a in w: right_mul_gen(M, n, a)
    return M
def depth_series(M):
    n = len(M); best = N
    for r in range(n):
        for c in range(n):
            e = list(M[r][c])
            if r == c: e[0] -= 1
            v = next((k for k, x in enumerate(e) if x), N)
            best = min(best, v)
    return best  # == N means ">= N"
def burau_at(w, n, t):
    t = Fraction(t)
    M = [[Fraction(int(r == c)) for c in range(n)] for r in range(n)]
    for a in w:
        i = abs(a) - 1
        g = [[1 - t, t], [1, 0]] if a > 0 else [[0, 1], [1 / t, 1 - 1 / t]]
        for row in M:
            x, y = row[i], row[i + 1]
            row[i], row[i + 1] = x * g[0][0] + y * g[1][0], x * g[0][1] + y * g[1][1]
    return M
def is_I(M): return all(M[r][c] == (r == c) for r in range(len(M)) for c in range(len(M)))
def brunnian(w):
    return all(is_I(burau_at(delete(w, 4, d), 3, 2)) and is_I(burau_at(delete(w, 4, d), 3, 3)) for d in (1, 2, 3, 4))
P = red(Phi0)
print("Phi0: len", len(P), "depth", depth_series(burau_series(P, 4)), "nontrivial(t=2)", not is_I(burau_at(P, 4, 2)))
c = red([3] + P + [-3])
print("c0 = s3 Phi0 s3^-1: len", len(c), "pure", pure(c, 4), "depth", depth_series(burau_series(c, 4)),
      "Brunnian", brunnian(c))
A, B = burau_at(P, 4, 2), burau_at(c, 4, 2)
AB = [[sum(A[r][k] * B[k][s] for k in range(4)) for s in range(4)] for r in range(4)]
BA = [[sum(B[r][k] * A[k][s] for k in range(4)) for s in range(4)] for r in range(4)]
print("Burau(Phi0), Burau(c0) commute at t=2?", AB == BA)
for k in (1, 2, 3, 4):
    t0 = time.time()
    c = red(comm(P, c))
    d = depth_series(burau_series(c, 4))
    print(f"c{k} = [Phi0, c{k-1}]: len {len(c)}, nontrivial(t=2) {not is_I(burau_at(c, 4, 2))}, "
          f"Brunnian {brunnian(c)}, depth {d if d < N else '>=%d' % N} (claim >= {k+1})  [{time.time()-t0:.1f}s]", flush=True)
