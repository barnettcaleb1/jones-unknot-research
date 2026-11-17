"""Sanity checks of the lead's claims (4) and (5) on W(6,0), numerically at a generic A.
TL action on the 5 crossingless matchings of 6 points (0-indexed), sigma_i = A*1 + A^-1*e_i,
bilinear form <m,m'> = delta^(loops of m u m'), delta = -A^2 - A^-2."""
import itertools, numpy as np

N = 6
def matchings(pts):
    if not pts: return [()]
    a = pts[0]; out = []
    for k in range(1, len(pts), 2):            # partner must leave an even block inside
        b = pts[k]
        for L in matchings(pts[1:k]):
            for R in matchings(pts[k+1:]):
                out.append(((a, b),) + L + R)
    return out
M = [tuple(sorted(m)) for m in matchings(list(range(N)))]
def partner(m):
    p = [None]*N
    for a, b in m: p[a] = b; p[b] = a
    return p
idx = {m: i for i, m in enumerate(M)}
def to_m(p):
    return tuple(sorted({(min(i, p[i]), max(i, p[i])) for i in range(N)}))

A = 0.83 * np.exp(0.61j)          # generic point
d = -A**2 - A**-2
D = len(M)
def E(i):
    X = np.zeros((D, D), complex)
    for m in M:
        p = partner(m)
        if p[i] == i+1:
            X[idx[m], idx[m]] += d
        else:
            a, b = p[i], p[i+1]
            q = p[:]; q[i] = i+1; q[i+1] = i; q[a] = b; q[b] = a
            X[idx[to_m(q)], idx[m]] += 1
    return X
Es = [E(i) for i in range(N-1)]
S = [A*np.eye(D) + A**-1*Es[i] for i in range(N-1)]
Sinv = [np.linalg.inv(s) for s in S]
def rho(word):                     # word: list of +-(i+1), 0-indexed generator i
    X = np.eye(D, dtype=complex)
    for g in word:
        X = X @ (S[g-1] if g > 0 else Sinv[-g-1])
    return X
def loops(m1, m2):
    p1, p2 = partner(m1), partner(m2); seen = set(); c = 0
    for s in range(N):
        if s in seen: continue
        c += 1; x = s; side = 0
        while True:
            seen.add(x); y = p1[x] if side == 0 else p2[x]; seen.add(y); x = y; side ^= 1
            if x == s and side == 0: break
    return c
G = np.array([[d**loops(a, b) for b in M] for a in M])

print("dim W(6,0) =", D)
print("e_i self-adjoint for form:", all(np.allclose(Es[i].T @ G, G @ Es[i]) for i in range(N-1)))
# claim (4): full twist on strands 2..6 (generators 2..5 in 1-indexed) is a scalar
FT = rho([2, 3, 4, 5]*5)
print("claim 4: (s2 s3 s4 s5)^5 scalar on W(6,0):", np.allclose(FT, FT[0, 0]*np.eye(D)))
# claim (5): twist about c = {1,2,3} = (s1 s2)^3 has eigenvalue multiplicities (4,1)
Tc = rho([1, 2]*3)
ev = np.linalg.eigvals(Tc)
print("claim 5: eigenvalues of (s1 s2)^3:", np.round(ev, 6))
lam = sorted(set(np.round(ev, 6)), key=lambda z: -list(np.round(ev, 6)).count(z))
mu4, mu1 = lam[0], lam[1]
print("   multiplicities:", [list(np.round(ev, 6)).count(z) for z in lam],
      " ratio-1 (kappa) =", np.round(mu1/mu4 - 1, 6))
R = (Tc - mu4*np.eye(D)) / (mu1 - mu4)                       # candidate rank-one projector
print("   Tc = mu4*(1 + kappa P), P rank one idempotent:",
      np.linalg.matrix_rank(R, tol=1e-8) == 1 and np.allclose(R @ R, R))
w, V = np.linalg.eig(Tc)
vc = V[:, np.argmin(abs(w - mu1))]
B = lambda x, y: x @ G @ y
print("   B(v_c, v_c) =", np.round(B(vc, vc), 6))
for word, name in [([3], "s3 (c' = {1,2,4})"), ([3, 2, 4, 3], "s3 s2 s4 s3"),
                   ([3, 3], "s3^2"), ([3, 4, 5, 2, 1], "s3 s4 s5 s2 s1"), ([4, 3, -2, 5], "s4 s3 s2^-1 s5")]:
    g = rho(word)
    print("   B(v_c, rho(g) v_c), g =", name, ":", np.round(B(vc, g @ vc), 6))
