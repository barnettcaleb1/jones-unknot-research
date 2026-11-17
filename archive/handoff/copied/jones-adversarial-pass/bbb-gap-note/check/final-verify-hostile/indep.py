#!/usr/bin/env python3
"""Independent checks for the verifier of the 'hostile' lens findings.

Exact Laurent-polynomial arithmetic (dict exp -> int), unreduced Burau
sigma_i -> I + [[1-t, t],[1, 0]] block, words multiplied left to right.

Checks:
 (1) depth of Phi0 and of the iterated commutators used in Remark 5,
     and their nontriviality at t = 2 (Finding 5);
 (2) Moody polynomials M_{f(Phi0) G} and M_G for a few G in K_5, via the
     noose class c = e_3 rho(X) and the functional L(c) = c_1 - t^{-1} c_2
     (Fox-calculus model; L kills the class e_1 + t e_2 of x_1 x_2):
     values at t = -1 agree up to sign, polynomials differ (Finding 3);
 (3) a toy check of the 'parity representative is minimal' argument
     (Finding 4) on exponent/sign sequences.
"""
from fractions import Fraction
import itertools, random, sys

# ---------- Laurent polynomials ----------
def padd(a, b, s=1):
    r = dict(a)
    for e, c in b.items():
        v = r.get(e, 0) + s * c
        if v:
            r[e] = v
        else:
            r.pop(e, None)
    return r

def pmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1 + e2
            v = r.get(e, 0) + c1 * c2
            if v:
                r[e] = v
            else:
                r.pop(e, None)
    return r

def pshift(a, k):
    return {e + k: c for e, c in a.items()}

def peval(a, t):
    return sum(Fraction(c) * Fraction(t) ** e for e, c in a.items())

ONE = {0: 1}
ZERO = {}

def div_t_plus_1(a):
    """Return a/(t+1) if exact, else None."""
    if not a:
        return {}
    lo = min(a)
    hi = max(a)
    coeffs = [a.get(lo + i, 0) for i in range(hi - lo + 1)]  # ascending
    # divide polynomial sum coeffs[i] t^i by (1 + t): synthetic from top
    n = len(coeffs) - 1
    q = [0] * n
    rem = coeffs[:]
    for i in range(n, 0, -1):
        q[i - 1] = rem[i]
        rem[i] -= q[i - 1]
        rem[i - 1] -= q[i - 1]
    if any(rem):
        return None
    return {lo + i: c for i, c in enumerate(q) if c}

def div_one_minus_t(a):
    """Return a/(1-t) if exact, else None."""
    # 1 - t = -(t - 1); divide by (t-1) then negate
    if not a:
        return {}
    lo = min(a)
    hi = max(a)
    coeffs = [a.get(lo + i, 0) for i in range(hi - lo + 1)]
    n = len(coeffs) - 1
    q = [0] * n
    rem = coeffs[:]
    for i in range(n, 0, -1):
        q[i - 1] = rem[i]
        rem[i] -= q[i - 1]
        rem[i - 1] += q[i - 1]
    if any(rem):
        return None
    return {lo + i: -c for i, c in enumerate(q) if c}

# ---------- matrices ----------
def mid(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]

def mmul(A, B):
    n = len(A)
    R = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]:
                continue
            for j in range(n):
                if B[k][j]:
                    R[i][j] = padd(R[i][j], pmul(A[i][k], B[k][j]))
    return R

def gen(n, i, inv=False):
    M = mid(n)
    a = i - 1
    if not inv:
        M[a][a] = {0: 1, 1: -1}
        M[a][a + 1] = {1: 1}
        M[a + 1][a] = {0: 1}
        M[a + 1][a + 1] = {}
    else:
        # inverse of [[1-t, t],[1,0]] is [[0,1],[t^-1, 1 - t^-1]]
        M[a][a] = {}
        M[a][a + 1] = {0: 1}
        M[a + 1][a] = {-1: 1}
        M[a + 1][a + 1] = {0: 1, -1: -1}
    return M

def rho(n, word):
    M = mid(n)
    for g in word:
        M = mmul(M, gen(n, abs(g), g < 0))
    return M

def inv_word(w):
    return [-g for g in reversed(w)]

def comm(x, y):
    return x + y + inv_word(x) + inv_word(y)

def A(i, j):
    # sigma_{j-1} ... sigma_{i+1} sigma_i^2 sigma_{i+1}^{-1} ... sigma_{j-1}^{-1}
    up = list(range(j - 1, i, -1))
    return up + [i, i] + [-g for g in reversed(up)]

def is_identity(M):
    n = len(M)
    return all(M[i][j] == (ONE if i == j else ZERO) for i in range(n) for j in range(n))

def depth(M, cap=40):
    n = len(M)
    D = [[padd(M[i][j], ONE if i == j else ZERO, -1) for j in range(n)] for i in range(n)]
    if all(not D[i][j] for i in range(n) for j in range(n)):
        return float('inf')
    d = 0
    while d < cap:
        nxt = []
        ok = True
        for i in range(n):
            row = []
            for j in range(n):
                q = div_t_plus_1(D[i][j])
                if q is None:
                    ok = False
                    break
                row.append(q)
            if not ok:
                break
            nxt.append(row)
        if not ok:
            return d
        D = nxt
        d += 1
    return d

def at(M, t):
    return [[peval(e, t) for e in row] for row in M]

def is_id_num(M):
    n = len(M)
    return all(M[i][j] == (1 if i == j else 0) for i in range(n) for j in range(n))

# ---------- braids ----------
X = [1, 2] * 6
b = comm(comm(A(1, 4), A(2, 4)), A(3, 4))
Phi0 = comm(X, b)
print("len(Phi0 word) =", len(Phi0))

R0 = rho(4, Phi0)
print("(1) depth(Phi0) =", depth(R0), "; identity at t=2?", is_id_num(at(R0, 2)))

s3conj = [3] + Phi0 + [-3]
Rinv0 = rho(4, inv_word(Phi0))
Rc = rho(4, s3conj)
Rcinv = rho(4, inv_word(s3conj))
# C1 = [Phi0, s3 Phi0 s3^-1]; C_{k+1} = [Phi0, C_k]
C = mmul(mmul(mmul(R0, Rc), Rinv0), Rcinv)
Cinv = mmul(mmul(mmul(Rc, R0), Rcinv), Rinv0)  # inverse of [a,b] is [b,a]
for k in range(1, 4):
    print("    C_%d: depth = %s ; identity at t=2? %s" % (k, depth(C), is_id_num(at(C, 2))))
    newC = mmul(mmul(mmul(R0, C), Rinv0), Cinv)
    newCinv = mmul(mmul(mmul(C, R0), Cinv), Rinv0)
    C, Cinv = newC, newCinv

# (2) Moody polynomials in B_5
def moody(n, Mat):
    c1 = Mat[2][0]
    c2 = Mat[2][1]
    L = padd(c1, pshift(c2, -1), -1)
    q = div_one_minus_t(L)
    return L, q

def normal_form(p):
    if not p:
        return ()
    lo = min(p)
    items = sorted((e - lo, c) for e, c in p.items())
    # fix the overall sign so leading low coefficient is positive
    s = 1 if items[0][1] > 0 else -1
    return tuple((e, s * c) for e, c in items)

def equal_up_to_unit(p, q):
    return normal_form(p) == normal_form(q)

Y5 = rho(5, Phi0)  # f = standard inclusion sigma_i -> sigma_i
print("(2) rho_5(f(Phi0)) identity at t=-1?", is_id_num(at(Y5, -1)))
random.seed(7)
Agens = [A(1, 5), A(2, 5), A(3, 5), A(4, 5)]
trials = 0
differ = 0
for trial in range(8):
    w = []
    for _ in range(random.randint(2, 5)):
        g = random.randrange(4)
        e = random.choice([1, -1])
        w += Agens[g] if e == 1 else inv_word(Agens[g])
    G = rho(5, w)
    YG = mmul(Y5, G)
    LG, MG = moody(5, G)
    LYG, MYG = moody(5, YG)
    assert MG is not None and MYG is not None, "1-t divisibility failed"
    vG = peval(MG, -1)
    vYG = peval(MYG, -1)
    same_val = abs(vG) == abs(vYG)
    eq = equal_up_to_unit(MG, MYG)
    l1G = sum(abs(c) for c in MG.values())
    l1YG = sum(abs(c) for c in MYG.values())
    trials += 1
    differ += (not eq)
    print("    G#%d: |M_G(-1)|=%s |M_YG(-1)|=%s equal=%s ; M_YG == t^k M_G ? %s ; L1(M_G)=%d L1(M_YG)=%d"
          % (trial, abs(vG), abs(vYG), same_val, eq, l1G, l1YG))
print("    differing polynomials in %d of %d trials" % (differ, trials))

# sanity: L kills class of x1 x2 (e_1 + t e_2) and M_{sigma_2^2} is a monomial
Ls = padd({0: 1}, pshift({1: 1}, -1), -1)
print("    L(e1 + t e2) =", Ls)
_, Ms = moody(4, rho(4, [2, 2]))
print("    M_{sigma_2^2} =", Ms)

# (3) Finding 4 toy: for a sign/exponent sequence built from a disk sequence
# satisfying parity, |sum eps (-1)^k| = number of points; a finger move
# (empty bigon, |P|=0, sign-changing) breaks parity and drops |M(-1)| below m'.
def seq_from_disks(eps0, k0, disks):
    eps, k = [eps0], [k0]
    for (W, sc) in disks:
        k.append(k[-1] + W)
        eps.append(-eps[-1] if sc else eps[-1])
    return eps, k

ok = True
for _ in range(2000):
    m = random.randint(1, 12)
    disks = []
    for _ in range(m - 1):
        P = random.randint(1, 5)
        W = P * random.choice([1, -1])
        sc = (P % 2 == 1)  # parity condition
        disks.append((W, sc))
    eps, k = seq_from_disks(1, 0, disks)
    val = sum(e * (-1) ** kk for e, kk in zip(eps, k))
    if abs(val) != m:
        ok = False
print("(3) parity sequences: |M(-1)| == number of points in all trials:", ok)
# finger move inserts an empty sign-changing disk pair: W=0, sign flips twice
eps, k = seq_from_disks(1, 0, [(1, True), (0, True), (0, True), (2, False)])
val = sum(e * (-1) ** kk for e, kk in zip(eps, k))
print("    finger-move example: points =", len(eps), " |M(-1)| =", abs(val))
