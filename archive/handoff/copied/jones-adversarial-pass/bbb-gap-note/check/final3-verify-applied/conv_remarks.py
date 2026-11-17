# Independent check of the two convention remarks in the first paragraph of Appendix A
# (not checked by phi0_check.py):
#  (i)  D R(s_i^{+-1})^T D == BB05 reduced(s_i^{+-1}),  D = diag(1, -1, 1, ...), n = 3..6, at several t;
#  (ii) "replacing every s_i by the opposite half twist ... changes all of these by t -> 1/t up to conjugation":
#       for M in U, UT, R, RT and n = 4, 5, at several rational t0, the space of C with
#       C M(s_i)(1/t0) = M(s_i^-1)(t0) C for all i is 1-dimensional and its nonzero element is invertible.
from fractions import Fraction as F

def eye(m): return [[F(int(i == j)) for j in range(m)] for i in range(m)]
def T(A): return [list(r) for r in zip(*A)]
def U(n, a, t):
    i = abs(a); M = eye(n)
    blk = [[1 - t, t], [F(1), F(0)]] if a > 0 else [[F(0), F(1)], [1 / t, 1 - 1 / t]]
    for r in range(2):
        for c in range(2): M[i - 1 + r][i - 1 + c] = F(blk[r][c])
    return M
def R(n, a, t):
    i = abs(a); M = eye(n - 1); r = i - 1
    vals = (t, -t, F(1)) if a > 0 else (F(1), -1 / t, 1 / t)
    for c, v in zip((r - 1, r, r + 1), vals):
        if 0 <= c < n - 1: M[r][c] = F(v)
    return M
def BB(n, a, t):                                  # BB05 p. 46; inverse computed from the formula G = I + u e_i^T
    i = abs(a); m = n - 1; M = eye(m)
    col = {i - 2: -t, i - 1: -t, i: F(-1)}        # 0-based rows of column i-1 (1-based column i)
    if a < 0:
        col = {i - 2: F(-1), i - 1: -1 / t, i: -1 / t}
    for r, v in col.items():
        if 0 <= r < m: M[r][i - 1] = F(v)
    return M
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

ok_i = True
for n in range(3, 7):
    D = [[F((-1) ** r) if r == c else F(0) for c in range(n - 1)] for r in range(n - 1)]
    for i in range(1, n):
        for a in (i, -i):
            for t in (F(2), F(-3, 7), F(5, 3), F(11, 2)):
                if mm(mm(D, T(R(n, a, t))), D) != BB(n, a, t): ok_i = False; print('MISMATCH', n, a, t)
            if mm(BB(n, a, F(5, 3)), BB(n, -a, F(5, 3))) != eye(n - 1): ok_i = False; print('BB inverse wrong', n, a)
print('(i) D R^T D == BB05 reduced for s_i and s_i^-1, n = 3..6:', ok_i)

def nullspace(rows, N):
    A = [r[:] for r in rows]; piv = []; k = 0
    for col in range(N):
        p = next((i for i in range(k, len(A)) if A[i][col] != 0), None)
        if p is None: continue
        A[k], A[p] = A[p], A[k]; pv = A[k][col]; A[k] = [x / pv for x in A[k]]
        for i in range(len(A)):
            if i != k and A[i][col] != 0:
                f = A[i][col]; A[i] = [x - f * y for x, y in zip(A[i], A[k])]
        piv.append(col); k += 1
    free = [c for c in range(N) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * N; v[fc] = F(1)
        for r, pc in enumerate(piv): v[pc] = -A[r][fc]
        basis.append(v)
    return basis
def det(M):
    M = [r[:] for r in M]; m = len(M); d = F(1)
    for c in range(m):
        p = next((i for i in range(c, m) if M[i][c] != 0), None)
        if p is None: return F(0)
        if p != c: M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]
        for i in range(c + 1, m):
            f = M[i][c] / M[c][c]; M[i] = [x - f * y for x, y in zip(M[i], M[c])]
    return d
CONV = {'U': lambda n, a, t: U(n, a, t), 'UT': lambda n, a, t: T(U(n, a, t)),
        'R': lambda n, a, t: R(n, a, t), 'RT': lambda n, a, t: T(R(n, a, t))}
for name, g in CONV.items():
    for n in (4, 5):
        for t0 in (F(5, 3), F(-7, 2)):
            m = len(g(n, 1, t0)); rows = []
            for i in range(1, n):
                A, B = g(n, i, 1 / t0), g(n, -i, t0)      # want C A = B C
                for r in range(m):
                    for c in range(m):
                        eq = [F(0)] * (m * m)
                        for k in range(m):
                            eq[r * m + k] += A[k][c]
                            eq[k * m + c] -= B[r][k]
                        rows.append(eq)
            basis = nullspace(rows, m * m)
            # the commutant is 1-dim for R, RT (irreducible) and 2-dim for U, UT (reduced + trivial summand at generic t0);
            # test whether some combination of the basis is invertible
            combos = [[F(1)] + [F(0)] * (len(basis) - 1)] + [[F(1)] + [F(k + 2)] * (len(basis) - 1) for k in range(3)]
            inv_ok = any(det([[sum(cf * v[r * m + c] for cf, v in zip(co, basis)) for c in range(m)] for r in range(m)]) != 0
                         for co in combos) if basis else False
            print(f'(ii) {name:2} n={n} t0={str(t0):5}: dim of conjugator space = {len(basis)}, an invertible conjugator exists: {inv_ok}')
