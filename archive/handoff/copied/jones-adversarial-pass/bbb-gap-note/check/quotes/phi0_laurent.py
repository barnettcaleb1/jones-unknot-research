# Independent exact check of Phi0 = [(s1 s2)^6, [[A14,A24],A34]] under the unreduced Burau rep,
# with Laurent polynomials as dicts {exponent: int}. Also (t+1)-adic depth of rho(Phi0) - I.
from fractions import Fraction as F

def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0: del r[e]
    return r
def pmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1+e2] = r.get(e1+e2, 0) + c1*c2
    return {e: c for e, c in r.items() if c != 0}
def eye(n): return [[({0:1} if i == j else {}) for j in range(n)] for i in range(n)]
def mmul(A, B):
    n = len(A)
    return [[ (lambda i, j: __import__('functools').reduce(padd, (pmul(A[i][k], B[k][j]) for k in range(n)), {}))(i, j)
              for j in range(n)] for i in range(n)]
def gen(n, i, inv=False):
    M = eye(n)
    if not inv: blk = [[{0:1, 1:-1}, {1:1}], [{0:1}, {}]]          # [[1-t, t],[1, 0]]
    else:       blk = [[{}, {0:1}], [{-1:1}, {0:1, -1:-1}]]         # inverse: [[0,1],[t^-1, 1-t^-1]]
    for r in range(2):
        for c in range(2): M[i-1+r][i-1+c] = blk[r][c]
    return M
def word(n, w):
    M = eye(n)
    for g in w: M = mmul(M, gen(n, abs(g), g < 0))
    return M
def winv(w): return [-g for g in reversed(w)]
def comm(a, b): return a + b + winv(a) + winv(b)
def A(i, j):
    up = list(range(j-1, i, -1)); return up + [i, i] + winv(up)
def ev(p, t): return sum(F(c) * F(t) ** e for e, c in p.items())
def order_at_minus1(p):
    # vanishing order at t=-1 of a Laurent polynomial (inf for 0)
    if not p: return float('inf')
    lo = min(p); hi = max(p)
    coeffs = [p.get(e, 0) for e in range(lo, hi+1)]   # polynomial t^-lo * p, ascending
    k = 0
    while True:
        # evaluate at -1
        if sum(c * (-1) ** i for i, c in enumerate(coeffs)) != 0: return k
        # divide by (t+1): synthetic division, descending order
        # straightforward long division
        q = [0] * (len(coeffs) - 1); r = coeffs[:]
        for d in range(len(coeffs) - 1, 0, -1):
            q[d-1] = r[d]; r[d-1] -= r[d]; r[d] = 0
        assert r[0] == 0
        coeffs = q; k += 1

# sanity: braid relations as Laurent matrices
assert word(4, [1,2,1]) == word(4, [2,1,2]) and word(4, [1,3]) == word(4, [3,1]) and word(4, [2,-2]) == eye(4)
A14, A24, A34 = A(1,4), A(2,4), A(3,4)
a = [1, 2] * 6
b = comm(comm(A14, A24), A34)
phi0 = comm(a, b)
print("A14, A24, A34 =", A14, A24, A34, "; word length of Phi0 =", len(phi0))
for n in (4, 5):
    R = word(n, phi0)
    D = [[padd(R[i][j], {0:-1} if i == j else {}) for j in range(n)] for i in range(n)]
    print(f"n={n}: rho(Phi0) == I as Laurent matrix? {R == eye(n)}")
    for tv in (-1, 2, 3):
        print(f"      at t={tv:>2}: == I ? {all(ev(R[i][j], tv) == (1 if i == j else 0) for i in range(n) for j in range(n))}")
    print(f"      (t+1)-adic order of rho(Phi0)-I (min over entries) = {min(order_at_minus1(D[i][j]) for i in range(n) for j in range(n))}")
# Delta_3^4 = (s1 s2)^6 at t=-1
R = word(4, a)
print("(s1 s2)^6 at t=-1 == I ?", all(ev(R[i][j], -1) == (1 if i == j else 0) for i in range(4) for j in range(4)))
