# Independent check of the lane's Phi0 = [(s1 s2)^6, [[y1,y2],y3]], y_i = A_{i4}.
# Unreduced Burau, s_i -> I + block [[1-t, t],[1, 0]] on rows/cols i,i+1. Exact rationals.
from fractions import Fraction as F
def eye(n): return [[F(int(i == j)) for j in range(n)] for i in range(n)]
def mul(A, B):
    n = len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def gen(n, i, t, inv=False):
    M = eye(n); t = F(t)
    blk = [[1-t, t], [F(1), F(0)]] if not inv else [[F(0), F(1)], [1/t, 1-1/t]]
    for r in range(2):
        for c in range(2): M[i-1+r][i-1+c] = blk[r][c]
    return M
def word(n, w, t):
    M = eye(n)
    for g in w: M = mul(M, gen(n, abs(g), t, g < 0))
    return M
def inv(w): return [-g for g in reversed(w)]
def comm(a, b): return a + b + inv(a) + inv(b)
# sanity: generator times its inverse is I
assert mul(gen(4, 2, 3), gen(4, 2, 3, True)) == eye(4)
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
a = [1, 2]*6
b = comm(comm(A14, A24), A34)
phi0 = comm(a, b)
print("word length of Phi0:", len(phi0))
for n in (4, 5):          # n = 5 is the stabilization f(Phi0)
    for tv in (-1, 2, 3):
        print(f"B_{n}, t={tv:>2}: Burau(Phi0) == I ? {word(n, phi0, tv) == eye(n)}")
print("(s1 s2)^6 on B_5 at t=-1 == I ?", word(5, a, -1) == eye(5))
print("(s1 s2)^6 on B_5 at t= 2 == I ?", word(5, a, 2) == eye(5))
