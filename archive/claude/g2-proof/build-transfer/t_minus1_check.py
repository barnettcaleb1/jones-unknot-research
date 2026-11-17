# Sanity check (single identity, exact arithmetic): unreduced Burau of B_4,
# sigma_i -> I_{i-1} + [[1-t, t],[1, 0]] + I_{n-i-1}.
# Claim: T = (s1 s2)^6 (square of the twist about c = {p1,p2,p3}) is the identity at t = -1,
# so Phi0 = [T, Psi] with Psi = [[y1,y2],y3] Brunnian lies in Brun_4 and in ker(Burau_4 at t=-1),
# while Phi0 is a nontrivial braid (Burau at t = 2 is not the identity).
from fractions import Fraction as F
n = 4
def eye(): return [[F(int(i == j)) for j in range(n)] for i in range(n)]
def mul(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def inv(X):
    M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(X)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [v/pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f*b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]
def gen(i, t):
    X = eye(); a = i - 1
    X[a][a], X[a][a+1], X[a+1][a], X[a+1][a+1] = 1 - t, t, F(1), F(0)
    return X
def word(w, t):
    X = eye()
    for g in w:
        G = gen(abs(g), t); X = mul(X, G if g > 0 else inv(G))
    return X
def winv(w): return [-g for g in reversed(w)]
def comm(a, b): return a + b + winv(a) + winv(b)
def A(i):  # pure braid generator A_{i4}: strand 4 around strand i
    up = list(range(3, i, -1))          # s3 ... s_{i+1}
    return up + [i, i] + winv(up)
y1, y2, y3 = A(1), A(2), A(3)
Psi = comm(comm(y1, y2), y3)
T = [1, 2] * 6
Phi0 = comm(T, Psi)
for name, w in [("T=(s1 s2)^6", T), ("Psi=[[y1,y2],y3]", Psi), ("Phi0=[T,Psi]", Phi0)]:
    for t in (F(-1), F(2), F(3, 2)):
        print(f"{name:18s} t={str(t):4s} identity? {word(w, t) == eye()}")
print("length of Phi0 word:", len(Phi0))
