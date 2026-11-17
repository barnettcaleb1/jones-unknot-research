# Minimal exact algebra: Laurent polynomials over Z (dict exp->coeff), matrices,
# free groups, Artin action, Fox calculus.  Independent of the earlier scripts.

# ---------------- Laurent polynomials ----------------
def lp(d=None):
    return {k: v for k, v in (d or {}).items() if v != 0}
def lconst(c): return lp({0: c})
def ladd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + v
    return lp(r)
def lneg(a): return {k: -v for k, v in a.items()}
def lsub(a, b): return ladd(a, lneg(b))
def lmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            r[k1 + k2] = r.get(k1 + k2, 0) + v1 * v2
    return lp(r)
def lmono(c, e): return lp({e: c})
def leval(a, t):
    from fractions import Fraction
    t = Fraction(t)
    return sum(v * t ** k for k, v in a.items())
def ldiv_tplus1(a):
    """Divide a Laurent poly by (t+1) exactly; return (quotient, ok)."""
    if not a: return {}, True
    lo = min(a); hi = max(a)
    # shift to polynomial
    coeffs = [a.get(lo + i, 0) for i in range(hi - lo + 1)]  # c0 + c1 t + ...
    # synthetic division by (t+1): from top degree
    n = len(coeffs) - 1
    q = [0] * n
    rem = coeffs[:]
    for d in range(n, 0, -1):
        c = rem[d]
        q[d - 1] = c
        rem[d] -= c
        rem[d - 1] -= c
    ok = all(x == 0 for x in rem)
    return lp({lo + i: q[i] for i in range(n)}), ok
def tplus1_adic(a, cap=50):
    """largest m with (t+1)^m | a (a != 0)."""
    if not a: return None
    m = 0
    while m < cap:
        q, ok = ldiv_tplus1(a)
        if not ok: return m
        a = q; m += 1
    return m

# ---------------- matrices over Laurent polys ----------------
def meye(n): return [[lconst(1) if i == j else {} for j in range(n)] for i in range(n)]
def mmul(A, B):
    n = len(A); m = len(B[0]); k = len(B)
    R = [[{} for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for l in range(k):
            if not A[i][l]: continue
            for j in range(m):
                if B[l][j]:
                    R[i][j] = ladd(R[i][j], lmul(A[i][l], B[l][j]))
    return R
def msub(A, B): return [[lsub(a, b) for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def mis_eye(A): return A == meye(len(A))
def meval(A, t): return [[leval(x, t) for x in r] for r in A]

# ---------------- free group words: letters are +-j (j>=1) ----------------
def fred(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out
def finv(w): return [-x for x in reversed(w)]
def fcomm(a, b): return a + b + finv(a) + finv(b)   # [a,b] = a b a^-1 b^-1

# ---------------- Artin action (geometrically derived, see report) ----------------
# H_i = counterclockwise half twist of p_i,p_{i+1}; pushforward on loops based at p* (bottom):
#   x_i -> x_{i+1},  x_{i+1} -> x_{i+1} x_i x_{i+1}^-1, others fixed.
# Braid words are read left to right = applied first to last (right action).
def sig_img(i, s):
    if s > 0:
        return {i: [i + 1], i + 1: [i + 1, i, -(i + 1)]}
    else:  # inverse automorphism
        return {i: [-i, i + 1, i], i + 1: [i]}
def subst(w, m):
    out = []
    for x in w:
        a = abs(x); img = m.get(a, [a])
        out += img if x > 0 else finv(img)
    return fred(out)
def act_word(braid, w):
    """image of the free-group word w under the braid (applied left to right)"""
    for g in braid:
        w = subst(w, sig_img(abs(g), 1 if g > 0 else -1))
    return w
def act(n, braid):
    imgs = {j: [j] for j in range(1, n + 1)}
    for g in braid:
        m = sig_img(abs(g), 1 if g > 0 else -1)
        imgs = {j: subst(imgs[j], m) for j in imgs}
    return imgs
def is_trivial(n, braid):
    return all(v == [j] for j, v in act(n, braid).items())

# ---------------- Fox calculus / homological Burau ----------------
def fox_row(w, n):
    """abelianised Fox derivatives d w / d x_j (x_j -> t), j=1..n, as Laurent polys"""
    row = [{} for _ in range(n)]
    e = 0  # exponent of prefix
    for x in w:
        j = abs(x) - 1
        if x > 0:
            row[j] = ladd(row[j], lmono(1, e)); e += 1
        else:
            e -= 1; row[j] = ladd(row[j], lmono(-1, e))
    return row
def fox_gen(n, i, inv=False):
    """Fox Jacobian (x_j -> t) of the Artin automorphism of H_i (rows = images of x_j)."""
    M = meye(n)
    if not inv:
        blk = [[{}, lconst(1)], [lp({1: 1}), lp({0: 1, 1: -1})]]
    else:
        blk = [[lp({0: 1, -1: -1}), lp({-1: 1})], [lconst(1), {}]]
    for r in range(2):
        for c in range(2):
            M[i - 1 + r][i - 1 + c] = blk[r][c]
    return M
def fox_burau(n, braid):
    """homological Burau via the chain rule: J(XY) = J(X) J(Y) for the right action"""
    M = meye(n)
    for g in braid:
        M = mmul(M, fox_gen(n, abs(g), g < 0))
    return M
def fox_burau_direct(n, braid):
    imgs = act(n, braid)
    return [fox_row(imgs[j], n) for j in range(1, n + 1)]

# standard unreduced Burau matrices sigma_i -> I + block [[1-t,t],[1,0]]
def burau_gen(n, i, inv=False):
    M = meye(n)
    if not inv:
        blk = [[lp({0: 1, 1: -1}), lp({1: 1})], [lconst(1), {}]]
    else:
        blk = [[{}, lconst(1)], [lp({-1: 1}), lp({0: 1, -1: -1})]]
    for r in range(2):
        for c in range(2):
            M[i - 1 + r][i - 1 + c] = blk[r][c]
    return M
def burau(n, braid):
    M = meye(n)
    for g in braid:
        M = mmul(M, burau_gen(n, abs(g), g < 0))
    return M

# ---------------- strand deletion ----------------
def delete_strand(braid, k, n):
    """delete the strand that starts at position k (1-based) from a braid word on n strands"""
    pos = list(range(1, n + 1))  # pos[p-1] = strand label at position p
    out = []
    for g in braid:
        i = abs(g)
        a, b = pos[i - 1], pos[i]
        if a == k or b == k:
            pass
        else:
            kp = pos.index(k) + 1  # position of strand k
            ii = i if kp > i + 1 else i - 1
            out.append(ii if g > 0 else -ii)
        pos[i - 1], pos[i] = b, a
    return out, pos
def perm(braid, n):
    pos = list(range(1, n + 1))
    for g in braid:
        i = abs(g); pos[i - 1], pos[i] = pos[i], pos[i - 1]
    return pos
