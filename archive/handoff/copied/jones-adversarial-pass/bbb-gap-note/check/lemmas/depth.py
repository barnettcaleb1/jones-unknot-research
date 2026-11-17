# (t+1)-adic depth of Phi0 and of iterated commutators, plus the Lemma 2 matrix model.
# Unreduced Burau, sigma_i -> I + block [[1-t, t],[1, 0]] on rows/cols i,i+1 (Fox Jacobian of
# x_i -> x_i x_{i+1} x_i^{-1}, x_{i+1} -> x_i; word read left to right = right action).
# Exact arithmetic only.  Run: python3 -I depth.py
from fractions import Fraction as F
import sys
sys.setrecursionlimit(10000)

# ---------------- Laurent polynomials as {exp: int} ----------------
def padd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + s * v
        if r[k] == 0:
            del r[k]
    return r
def pshift(a, d): return {k + d: v for k, v in a.items()}
def pscale(a, c): return {k: c * v for k, v in a.items()} if c else {}
def pmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            r[k1 + k2] = r.get(k1 + k2, 0) + v1 * v2
    return {k: v for k, v in r.items() if v}
def peval(a, x): return sum(F(v) * F(x) ** k for k, v in a.items())
def val_tplus1(a, cap=60):
    """largest d with (t+1)^d | a in Z[t,t^-1]; inf for a == 0."""
    if not a:
        return float('inf')
    lo = min(a); c = [a.get(lo + i, 0) for i in range(max(a) - lo + 1)]  # poly in t, low->high
    d = 0
    while d < cap:
        # synthetic division by (t+1): root -1
        n = len(c) - 1
        q = [0] * n
        acc = 0
        # divide c(t) by (t+1) using high-to-low Horner
        hi = c[::-1]
        out = []
        acc = 0
        for coef in hi:
            acc = acc * (-1) + coef
            out.append(acc)
        rem = out[-1]
        if rem != 0:
            return d
        quo_hi = out[:-1]
        c = quo_hi[::-1]
        d += 1
    return d

ONE = {0: 1}; T = {1: 1}; TI = {-1: 1}; ONEMT = {0: 1, 1: -1}; ONEMTI = {0: 1, -1: -1}

def eye(n): return [[dict(ONE) if i == j else {} for j in range(n)] for i in range(n)]

def rmul_gen(M, g, transpose=False):
    """M <- M * rho(sigma_|g|^{sign g}) (columns i,i+1 change).  transpose=True uses rho^T gens."""
    i = abs(g) - 1
    if not transpose:
        blk = [[ONEMT, T], [ONE, {}]] if g > 0 else [[{}, ONE], [TI, ONEMTI]]
    else:
        blk = [[ONEMT, ONE], [T, {}]] if g > 0 else [[{}, TI], [ONE, ONEMTI]]
    for r in range(len(M)):
        a, b = M[r][i], M[r][i + 1]
        M[r][i] = padd(pmul(a, blk[0][0]), pmul(b, blk[1][0]))
        M[r][i + 1] = padd(pmul(a, blk[0][1]), pmul(b, blk[1][1]))
    return M

def rho(n, w, transpose=False):
    M = eye(n)
    for g in w:
        rmul_gen(M, g, transpose)
    return M

def depth(M):
    n = len(M)
    return min(val_tplus1(padd(M[i][j], ONE if i == j else {}, -1)) for i in range(n) for j in range(n))

def is_identity_at(M, x):
    n = len(M)
    return all(peval(M[i][j], x) == (1 if i == j else 0) for i in range(n) for j in range(n))

def invert_t(M):  # t -> 1/t entrywise
    return [[{-k: v for k, v in e.items()} for e in row] for row in M]

# ---------------- words ----------------
def winv(w): return [-x for x in reversed(w)]
def comm(a, b): return a + b + winv(a) + winv(b)
def A(i, j):
    up = list(range(j - 1, i, -1))
    return up + [i, i] + winv(up)
def freered(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out

a = [1, 2] * 6
b = comm(comm(A(1, 4), A(2, 4)), A(3, 4))
phi0 = comm(a, b)
print("Phi0 word length", len(phi0))

# sanity: braid relations for both generator conventions
for tr in (False, True):
    assert rho(4, [1, 2, 1], tr) == rho(4, [2, 1, 2], tr)
    assert rho(4, [1, 3], tr) == rho(4, [3, 1], tr)
    assert rho(4, [2, -2], tr) == eye(4)

R = rho(4, phi0)
print("unreduced rho_4(Phi0): identity as Laurent matrix?", R == eye(4))
print("  identity at t=-1?", is_identity_at(R, -1), "  at t=2?", is_identity_at(R, 2), "  at t=3?", is_identity_at(R, 3))
print("  (t+1)-adic depth of rho_4(Phi0)-I:", depth(R))
print("  depth, transposed generators:", depth(rho(4, phi0, True)))
print("  depth, t -> 1/t:", depth(invert_t(R)))
print("  depth of inverse braid:", depth(rho(4, winv(phi0))))
R5 = rho(5, phi0)
print("  stabilised rho_5(f(Phi0)): depth", depth(R5), " block form rho4(+)1:",
      all(R5[i][j] == (R[i][j] if i < 4 and j < 4 else (ONE if i == j else {})) for i in range(5) for j in range(5)))
# depth of the two factors
print("  depth of (s1 s2)^6:", depth(rho(4, a)), "  depth of b:", depth(rho(4, b)))

# ---------------- reduced Burau (3x3) depth, for comparison ----------------
def red_gen(n, i, t_inv=False):
    pass
# reduced Burau via the invariant subspace: unreduced rho fixes the row vector? use explicit formulas
def reduced(n, w):
    d = n - 1
    M = eye(d)
    for g in w:
        i = abs(g) - 1
        G = eye(d)
        # standard reduced Burau (Birman's book form): sigma_i -> I_{i-2} + [[1,t,0],[0,-t,0],[0,1,1]] + ...
        if g > 0:
            G[i][i] = {1: -1}
            if i - 1 >= 0: G[i - 1][i] = dict(T)
            if i + 1 < d: G[i + 1][i] = dict(ONE)
        else:
            G[i][i] = {-1: -1}
            if i - 1 >= 0: G[i - 1][i] = dict(ONE)
            if i + 1 < d: G[i + 1][i] = dict(TI)
        N = [[{} for _ in range(d)] for _ in range(d)]
        for r in range(d):
            for c in range(d):
                acc = {}
                for k in range(d):
                    if M[r][k] and G[k][c]:
                        acc = padd(acc, pmul(M[r][k], G[k][c]))
                N[r][c] = acc
        M = N
    return M
# sanity of the reduced form
assert reduced(4, [1, 2, 1]) == reduced(4, [2, 1, 2]) and reduced(4, [1, 3]) == reduced(4, [3, 1])
assert reduced(4, [2, -2]) == eye(3) and reduced(4, [1, -1]) == eye(3) and reduced(4, [3, -3]) == eye(3)
Rr = reduced(4, phi0)
print("reduced Burau of Phi0: identity at t=-1?", is_identity_at(Rr, -1), " depth", depth(Rr))

# ---------------- iterated commutators: depth >= k, still nontrivial ----------------
# Phi_{k+1} = [Phi0, Phi_k], Phi_1 = [Phi0, g Phi0 g^-1].  Brun_4 is normal, so all are Brunnian.
def trunc_rho_series(n, w, N):
    """rho(w) with t = h - 1, entries in Z[h]/(h^N) as length-N int lists."""
    tser = [-1, 1] + [0] * (N - 2)
    tinv = [-1] * N                                   # 1/(h-1) = -(1+h+h^2+...)
    one = [1] + [0] * (N - 1)
    zero = [0] * N
    def add(x, y): return [p + q for p, q in zip(x, y)]
    def sub(x, y): return [p - q for p, q in zip(x, y)]
    def mul(x, y):
        r = [0] * N
        for i, xi in enumerate(x):
            if xi:
                for j in range(N - i):
                    r[i + j] += xi * y[j]
        return r
    onemt = sub(one, tser); onemti = sub(one, tinv)
    M = [[list(one) if i == j else list(zero) for j in range(n)] for i in range(n)]
    for g in w:
        i = abs(g) - 1
        blk = [[onemt, tser], [one, zero]] if g > 0 else [[zero, one], [tinv, onemti]]
        for r in range(n):
            x, y = M[r][i], M[r][i + 1]
            M[r][i] = add(mul(x, blk[0][0]), mul(y, blk[1][0]))
            M[r][i + 1] = add(mul(x, blk[0][1]), mul(y, blk[1][1]))
    return M
def series_depth(M, N):
    n = len(M); d = N
    for i in range(n):
        for j in range(n):
            e = list(M[i][j])
            if i == j: e[0] -= 1
            for k in range(N):
                if e[k] != 0:
                    d = min(d, k); break
    return d  # == N means ">= N"
def rho_mod_p(n, w, tv, p=(1 << 61) - 1):
    tv %= p; ti = pow(tv, p - 2, p)
    M = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for g in w:
        i = abs(g) - 1
        blk = [[(1 - tv) % p, tv], [1, 0]] if g > 0 else [[0, 1], [ti, (1 - ti) % p]]
        for r in range(n):
            x, y = M[r][i], M[r][i + 1]
            M[r][i] = (x * blk[0][0] + y * blk[1][0]) % p
            M[r][i + 1] = (x * blk[0][1] + y * blk[1][1]) % p
    return M
def is_id_mod_p(M): return all(M[i][j] == (1 if i == j else 0) for i in range(len(M)) for j in range(len(M)))

N = 9
assert series_depth(trunc_rho_series(4, phi0, N), N) == depth(R)
for gname, g in (("s3", [3]), ("s1", [1]), ("A14", A(1, 4))):
    cur = comm(phi0, g + phi0 + winv(g))
    print(f"\nconjugator g={gname}:")
    for k in range(1, 5):
        w = freered(cur)
        d = series_depth(trunc_rho_series(4, w, N), N)
        nt2 = not is_id_mod_p(rho_mod_p(4, w, 2)); nt3 = not is_id_mod_p(rho_mod_p(4, w, 3))
        print(f"  Phi_{k}: reduced length {len(w):6d}, depth {d if d < N else '>=%d' % N}, "
              f"rho != I at t=2: {nt2}, at t=3: {nt3}")
        cur = comm(phi0, w)

# ---------------- Lemma 2 matrix model ----------------
# Class of the noose of (beta_3)X = row 3 of rho(X) (right action).  Pairing with alpha~ uses
# only x1, x2 (the loops around the endpoints of alpha), with monomials u1, u2 of opposite sign.
# Check: entries (3,1), (3,2) of rho(X) are divisible by (1-t) for pure X, and for
# X = s2^(2k) the quotient is a k-term same-sign geometric series (iota = k).
def divide_by(a, d):
    """exact division of Laurent poly a by Laurent poly d; returns None if inexact."""
    if not a: return {}
    a = dict(a); q = {}
    dl, dh = min(d), max(d)
    while a:
        lead = max(a)
        if a[lead] % d[dh]: return None
        c = a[lead] // d[dh]; e = lead - dh
        q[e] = c
        a = padd(a, pshift(pscale(d, c), e), -1)
        if a and max(a) < dh + min(q) - (dh - dl) - 50: return None
        if len(q) > 5000: return None
    return q
for k in range(1, 6):
    Rk = rho(4, [2] * (2 * k))
    q1, q2 = divide_by(Rk[2][0], ONEMT), divide_by(Rk[2][1], ONEMT)
    print(f"s2^{2*k}: rho[3][1]/(1-t) = {q1}, rho[3][2]/(1-t) = {dict(sorted(q2.items()))}")
import random
random.seed(7)
gens = [A(i, j) for i in range(1, 4) for j in range(i + 1, 5)]
ok = 0
for trial in range(40):
    X = []
    for _ in range(random.randint(1, 6)):
        gw = random.choice(gens)
        X += gw if random.random() < 0.5 else winv(gw)
    RX = rho(4, X); RY = rho(4, phi0 + X); RZ = rho(4, X + phi0)
    vals = []
    for MM in (RX, RY, RZ):
        q1 = divide_by(MM[2][0], ONEMT); q2 = divide_by(MM[2][1], ONEMT)
        assert q1 is not None and q2 is not None, "not divisible by 1-t"
        # |M_X(-1)| = |u1 q1(-1) + u2 q2(-1)| with u1 = -u2 up to t^(+-1); at t=-1 u2 = +-u1
        vals.append((peval(q1, -1), peval(q2, -1)))
    assert vals[0] == vals[1] == vals[2]
    ok += 1
print(f"\nLemma 2 model: {ok} random pure X: (3,1),(3,2) entries divisible by (1-t); "
      f"quotients at t=-1 equal for X, Phi0*X and X*Phi0")
