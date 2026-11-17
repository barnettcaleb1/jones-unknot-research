# Sanity check of one identity: in Kasahara's normalization (AGT 1 (2001) p.43-44) of Jones's genus-2 rep,
# rho(iota) for the hyperelliptic involution iota = z1 z2 z3 z4 z5 z5 z4 z3 z2 z1 is the identity,
# and the separating twist (z1 z2 z1)^4 is t^6 I + rank one.  Exact arithmetic at t = 3/2.
from fractions import Fraction as F
t = F(3, 2)
def mul(A, B): return [[sum(A[i][k]*B[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
def inv(A):
    n = 5; M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f*b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]
I = [[F(int(i == j)) for j in range(5)] for i in range(5)]
z1 = [[-1/t**2, 0, 0, 0, t**3],[0, -1/t**2, 1/t**2, 0, 0],[0, 0, t**3, 0, 0],[0, 0, 1/t**2, -1/t**2, 0],[0, 0, 0, 0, t**3]]
xi = [[0,0,1,0,0],[0,0,0,0,1],[1,0,0,0,0],[0,1,0,0,0],[0,0,0,1,0]]
xi = [[F(x) for x in r] for r in xi]; xinv = inv(xi)
z = [z1]
for i in range(4): z.append(mul(mul(xi, z[-1]), xinv))
iota = I
for M in z + z[::-1]: iota = mul(iota, M)
print("rho(iota) == I :", iota == I)
xi6 = I
for _ in range(6): xi6 = mul(xi6, xi)
print("rho(xi)^6 == I :", xi6 == I)
sep = I
w = mul(mul(z[0], z[1]), z[0])
for _ in range(4): sep = mul(sep, w)
D = [[sep[i][j] - (t**6 if i == j else 0) for j in range(5)] for i in range(5)]
nonzero_rows = [i for i in range(5) if any(D[i])]
print("sep twist - t^6 I: nonzero rows =", nonzero_rows)
