"""Extra checks: Moody polynomial of Phi0 and conjugates, Lemma 2 test, depth of iterated commutators."""
import sys, random
sys.path.insert(0, '$HOME/jones-adversarial-pass/bbb-gap-note/check/compute')
from braidlib import *

def Aij(i, j):
    left = list(range(j - 1, i, -1))
    return left + [i, i] + inv(left)

A14, A24, A34 = Aij(1, 4), Aij(2, 4), Aij(3, 4)
X = power([1, 2], 6)
b = reduce_word(comm(comm(A14, A24), A34))
Phi0 = reduce_word(comm(X, b))

def ldiv_exact(p, q):
    """exact division of Laurent polys p / q (q has a unit leading coeff); returns None if inexact."""
    if not p:
        return {}
    p = dict(p); out = {}
    qh = max(q); qc = q[qh]
    ql = min(q)
    guard = 0
    while p:
        ph = max(p)
        c = p[ph]
        if c % qc:
            return None
        e = ph - qh
        if e + ql < min(p) - 10**6:
            return None
        out[e] = c // qc
        p = lsub(p, lmul({e: c // qc}, q))
        guard += 1
        if guard > 100000 or (p and max(p) < min(q) + e - 10**6):
            return None
        if p and max(p) - qh < min(p) - ql - 1 and False:
            return None
        if p and (max(p) - qh) < (min(out) - 10**6):
            return None
        # stop if remainder degree span is smaller than q's span and nonzero
        if p and (max(p) - min(p)) < (qh - ql):
            return None
    return out

def moody(w, n):
    """M = (B31 - t B32)/(1 - t) from the unreduced Burau (convention U); valid for pure w."""
    B = burau(w, n, 'U')
    num = lsub(B[2][0], lmul({1: 1}, B[2][1]))
    M = ldiv_exact(num, {0: 1, 1: -1})
    assert M is not None, "not divisible by 1-t"
    return M

def summ(M):
    return (bool(M), leval(M, -1), sum(abs(v) for v in M.values()), (min(M), max(M)) if M else None)

print("=== (a) Moody polynomial M = W1 - t W2 for Phi0 and variants (convention U) ===")
for name, w in (("Phi0", Phi0), ("rev", rev(Phi0)), ("mirror", mirror(Phi0)), ("rev mirror", rev(mirror(Phi0)))):
    M = moody(w, 4)
    print(f"  {name:10s}: nonzero {summ(M)[0]}, M(-1) = {summ(M)[1]}, sum|coeff| = {summ(M)[2]}, exponent range {summ(M)[3]}")
# identity braid and b for comparison
print("  identity : M =", moody([], 4))
Mb = moody(b, 4)
print(f"  b        : nonzero {bool(Mb)}, M(-1) = {leval(Mb, -1)}, sum|coeff| = {sum(abs(v) for v in Mb.values())}")

print("\n=== (b) conjugates g Phi0 g^-1 ===")
rng = random.Random(7)
gens4 = [A14, A24, A34]
tests = [("A34^%d" % m, power(A34, m)) for m in (1, 2, 5, 31)]
for k in range(8):
    g = []
    for _ in range(rng.randint(3, 8)):
        g += power(rng.choice(gens4), rng.choice([1, -1]))
    tests.append(("rand K4 #%d" % k, g))
for k in range(4):
    tests.append(("rand B4 #%d" % k, random_word(4, rng.randint(4, 10), rng)))
for name, g in tests:
    w = reduce_word(g + Phi0 + inv(g))
    if not is_pure(w, 4):
        continue
    M = moody(w, 4)
    B = burau(w, 4, 'U')
    print(f"  {name:12s}: M nonzero {bool(M)}, M(-1) = {leval(M, -1)}, depth {depth(B)}, I at -1 {is_identity_at(B, -1)}")

print("\n=== (c) Lemma 2 test in B5: Y = f(Phi0); M_{Y G}(-1) == M_G(-1) and M_{G Y}(-1) == M_G(-1) ===")
gens5 = [Aij(i, j) for i in range(1, 6) for j in range(i + 1, 6)]
Y = Phi0
allok = True
for k in range(12):
    G = []
    for _ in range(rng.randint(2, 6)):
        G += power(rng.choice(gens5), rng.choice([1, -1]))
    MG = moody(G, 5)
    MYG = moody(Y + G, 5)
    MGY = moody(G + Y, 5)
    ok = leval(MYG, -1) == leval(MG, -1) and leval(MGY, -1) == leval(MG, -1)
    allok &= ok
    print(f"  G#{k}: M_G(-1) = {leval(MG, -1)}, M_YG(-1) = {leval(MYG, -1)}, M_GY(-1) = {leval(MGY, -1)}, "
          f"M_YG == M_G as polys: {MYG == MG}  -> {'ok' if ok else 'MISMATCH'}")
print("  Lemma 2 consistent on all samples:", allok)

print("\n=== (d) leading coefficients and ad-nilpotency for iterated commutators ===")
def lead(B):
    """C(-1) where B = I + (t+1) C."""
    D = mminusI(B)
    out = []
    for row in D:
        r = []
        for p in row:
            if not p:
                r.append(Fraction(0)); continue
            q = ldiv_exact(p, {0: 1, 1: 1})
            assert q is not None
            r.append(leval(q, -1))
        out.append(r)
    return out
def fmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def fsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
CX = lead(burau(X, 4, 'U'))
print("  C_X(-1) =", [[str(x) for x in r] for r in CX])
P = CX
nil = None
for k in range(1, 6):
    if all(x == 0 for r in P for x in r):
        nil = k; break
    P = fmul(P, CX)
print("  C_X(-1) nilpotent of index:", nil)
N = lead(burau(Phi0, 4, 'U'))
ks = []
cur = N
for k in range(1, 12):
    nz = any(x != 0 for r in cur for x in r)
    ks.append((k, nz))
    cur = fsub(fmul(CX, cur), fmul(cur, CX))
print("  ad_{C_X}^{k-1}(N_1) nonzero for k =", [k for k, nz in ks if nz], " zero for k =", [k for k, nz in ks if not nz])
