# Check: U(mirror(w))(t) = J U(flip(w))(1/t) J, flip: s_i -> s_{n-i}; and flip(w) = Delta w Delta^-1.
from fractions import Fraction as Fr
def inv(w): return [-x for x in w[::-1]]
def cm(x, y): return x + y + inv(x) + inv(y)
def eye(n): return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
def mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def gen(n, a, t):
    i = abs(a) - 1; M = eye(n)
    if a > 0: M[i][i], M[i][i+1], M[i+1][i], M[i+1][i+1] = 1 - t, t, Fr(1), Fr(0)
    else:     M[i][i], M[i][i+1], M[i+1][i], M[i+1][i+1] = Fr(0), Fr(1), 1 / t, 1 - 1 / t
    return M
def U(w, n, t):
    M = eye(n)
    for a in w: M = mul(M, gen(n, a, t))
    return M
n = 4
X = [1, 2] * 6; A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
Phi0 = cm(X, cm(cm(A14, A24), A34))
mirror = [-a for a in Phi0]
flip = [(n - abs(a)) * (1 if a > 0 else -1) for a in Phi0]
J = [[Fr(int(i + j == n - 1)) for j in range(n)] for i in range(n)]
for t in (Fr(2), Fr(3), Fr(-1), Fr(5, 7)):
    print("t =", t, ": U(mirror Phi0)(t) == J U(flip Phi0)(1/t) J :", U(mirror, n, t) == mul(mul(J, U(flip, n, 1 / t)), J))
D4 = [1, 2, 3, 1, 2, 1]
print("flip(Phi0) is conjugate to Phi0 by Delta (checked in Burau at t=2,3/5 only, as a sanity check):",
      all(U(flip, n, t) == mul(mul(U(D4, n, t), U(Phi0, n, t)), U(inv(D4), n, t)) for t in (Fr(2), Fr(3, 5))))
