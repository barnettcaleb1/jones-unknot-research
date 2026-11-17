# Which exact (t+1)-adic depths occur among nontrivial Brunnian 4-braids built from Phi0?
# depth(Phi) = largest d with rho_4(Phi) == I mod (t+1)^d (unreduced Burau).
# Work in Z[h]/(h^N), t = h - 1.  Run: python3 -I odd_depth.py
import random, itertools
N = 8
def add(x, y): return [p + q for p, q in zip(x, y)]
def sub(x, y): return [p - q for p, q in zip(x, y)]
def mul(x, y):
    r = [0] * N
    for i, xi in enumerate(x):
        if xi:
            for j in range(N - i):
                r[i + j] += xi * y[j]
    return r
tser = [-1, 1] + [0] * (N - 2); tinv = [-1] * N
one = [1] + [0] * (N - 1); zero = [0] * N
onemt = sub(one, tser); onemti = sub(one, tinv)
GEN = {}
def blk(g): return [[onemt, tser], [one, zero]] if g > 0 else [[zero, one], [tinv, onemti]]
def rho(w, n=4):
    M = [[list(one) if i == j else list(zero) for j in range(n)] for i in range(n)]
    for g in w:
        i = abs(g) - 1; B = blk(g)
        for r in range(n):
            x, y = M[r][i], M[r][i + 1]
            M[r][i] = add(mul(x, B[0][0]), mul(y, B[1][0]))
            M[r][i + 1] = add(mul(x, B[0][1]), mul(y, B[1][1]))
    return M
def depth(M):
    d = N
    for i in range(len(M)):
        for j in range(len(M)):
            e = list(M[i][j]); e[0] -= int(i == j)
            for k in range(N):
                if e[k]:
                    d = min(d, k); break
    return d
def lead(M, d):
    return [[M[i][j][d] - (int(i == j) if d == 0 else 0) for j in range(len(M))] for i in range(len(M))]
def winv(w): return [-x for x in reversed(w)]
def comm(a, b): return a + b + winv(a) + winv(b)
def conj(g, w): return g + w + winv(g)
def A(i, j):
    up = list(range(j - 1, i, -1)); return up + [i, i] + winv(up)
def fr(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out
def rho_mod_p(w, tv, n=4, p=(1 << 61) - 1):
    tv %= p; ti = pow(tv, p - 2, p)
    M = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for g in w:
        i = abs(g) - 1
        B = [[(1 - tv) % p, tv], [1, 0]] if g > 0 else [[0, 1], [ti, (1 - ti) % p]]
        for r in range(n):
            x, y = M[r][i], M[r][i + 1]
            M[r][i] = (x * B[0][0] + y * B[1][0]) % p
            M[r][i + 1] = (x * B[0][1] + y * B[1][1]) % p
    return M
def nontrivial(w):
    M = rho_mod_p(w, 2)
    return any(M[i][j] != int(i == j) for i in range(4) for j in range(4))

a = [1, 2] * 6
b = comm(comm(A(1, 4), A(2, 4)), A(3, 4))
phi0 = fr(comm(a, b))
X1 = lead(rho(phi0), 1)
print("leading coefficient of rho(Phi0) at order 1 (X1):")
for r in X1: print("   ", r)
# products of X1 with itself
def mm(P, Q): return [[sum(P[i][k] * Q[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
print("X1^2 =", mm(X1, X1))
rank_guess = sum(1 for r in X1 if any(r))
print("nonzero rows of X1:", rank_guess)

random.seed(11)
def randword(L):
    w = []
    for _ in range(L):
        g = random.choice([1, 2, 3]) * random.choice([1, -1])
        w.append(g)
    return fr(w)
# depth-1 Brunnian seeds: conjugates of Phi0 and of a second seed built from (s2 s3)^6
b2 = comm(comm(A(1, 2), A(1, 3)), A(1, 4))       # Brunnian-type commutator through strand 1
seed2 = fr(comm([2, 3] * 6, b2))
print("\nseed2 = [(s2 s3)^6, [[A12,A13],A14]]: nontrivial", nontrivial(seed2), " depth", depth(rho(seed2)))
seeds = [phi0, seed2]
found = {}
for trial in range(400):
    s1 = conj(randword(random.randint(0, 6)), random.choice(seeds))
    s2 = conj(randword(random.randint(0, 6)), random.choice(seeds))
    s3 = conj(randword(random.randint(0, 6)), random.choice(seeds))
    c2 = fr(comm(s1, s2))                    # depth >= 2
    c3 = fr(comm(c2, s3))                    # depth >= 3
    for name, w in (("[s,s]", c2), ("[[s,s],s]", c3)):
        if not w: continue
        d = depth(rho(w))
        key = (name, d)
        if key not in found and nontrivial(w):
            found[key] = len(w)
print("\nexact depths found (construction, depth): word length")
for k in sorted(found): print("   ", k, found[k])
# products: depth(PQ) = min if depths differ
