# Independent re-check (verify-construction lens) of the facts about Phi0 that the
# note's headline (l. 9) and Section 4 Conclusion (l. 71) rely on.
#   Phi0 = [(s1 s2)^6, [[A14, A24], A34]],  [x, y] = x y x^-1 y^-1.
# Written from scratch (not copied from the earlier scripts):
#   * Artin action as a LEFT action on F_4 by automorphisms, braid word read right-to-left
#     (opposite bookkeeping to the earlier scripts), used for: nontriviality, purity,
#     Brunnian property, the identity Phi0 = [delta^-2, b], and delta in K_4.
#   * Unreduced Burau as exact Laurent-polynomial matrices (dict exponent -> int),
#     in the "transpose" form s_i -> I + block [[1-t, 1], [t, 0]], so that conventions
#     differ from the earlier checks; triviality at t = -1 and nontriviality, plus
#     the (t+1)-adic depth.
from fractions import Fraction

# ---------------- free group F_n, letters +-k ----------------
def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out

def winv(w):
    return [-x for x in reversed(w)]

def subst(w, img):
    out = []
    for x in w:
        a = abs(x)
        out += img[a] if x > 0 else winv(img[a])
    return red(out)

def gen_aut(n, g):
    """Automorphism of F_n for sigma_{|g|}^{sign g}: dict k -> word."""
    i = abs(g)
    img = {k: [k] for k in range(1, n + 1)}
    if g > 0:   # x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i
        img[i] = [i, i + 1, -i]
        img[i + 1] = [i]
    else:       # inverse: x_i -> x_{i+1}, x_{i+1} -> x_{i+1}^-1 x_i x_{i+1}
        img[i] = [i + 1]
        img[i + 1] = [-(i + 1), i, i + 1]
    return img

def compose(f, g, n):
    """(f o g)(x) = f(g(x))."""
    return {k: subst(g[k], f) for k in range(1, n + 1)}

def braid_aut(n, word):
    """Left action: the braid w1 w2 ... wr acts as A(w1) o A(w2) o ... o A(wr)."""
    tot = {k: [k] for k in range(1, n + 1)}
    for g in word:
        tot = compose(tot, gen_aut(n, g), n)
    return tot

def is_id(aut):
    return all(v == [k] for k, v in aut.items())

def comm(a, b):
    return a + b + winv(a) + winv(b)

def A(i, j):
    up = list(range(j - 1, i, -1))
    return up + [i, i] + winv(up)

n = 4
# sanity: braid relations hold for this action
assert braid_aut(4, [1, 2, 1]) == braid_aut(4, [2, 1, 2])
assert braid_aut(4, [1, 3]) == braid_aut(4, [3, 1])
assert is_id(braid_aut(4, [2, -2])) and is_id(braid_aut(4, [-3, 3]))

a = [1, 2] * 6
A14, A24, A34 = A(1, 4), A(2, 4), A(3, 4)
b = comm(comm(A14, A24), A34)
phi0 = comm(a, b)
aut = braid_aut(4, phi0)
print("Artin (left action): Phi0 trivial?", is_id(aut), "| image lengths", {k: len(v) for k, v in aut.items()})

# purity: each x_k maps to a conjugate of x_k
pure = True
for k, v in aut.items():
    h = len(v) // 2
    if not (len(v) % 2 == 1 and v[h] == k and red(v[:h] + v[h + 1:]) == []):
        pure = False
print("pure:", pure)

# Brunnian: deleting strand i = killing x_i; the induced automorphism of F_3 must be trivial
for i in range(1, 5):
    kill = lambda w: red([x for x in w if abs(x) != i])
    ok = all(kill(aut[k]) == [k] for k in aut if k != i)
    print("delete strand %d: trivial? %s" % (i, ok))

# delta = Delta_3^-2 Delta_4^2 lies in K_4 (deleting strand 4 kills it) and Phi0 = [delta^-2, b]
D3sq = [1, 2] * 3
D4sq = [1, 2, 3] * 4
delta = winv(D3sq) + D4sq
ad = braid_aut(4, delta)
kill4 = lambda w: red([x for x in w if abs(x) != 4])
print("delta pure & strand-4 deletion trivial (delta in K_4)?",
      all(kill4(ad[k]) == [k] for k in (1, 2, 3)))
print("Phi0 == [delta^-2, b] exactly (Artin, faithful)?",
      braid_aut(4, phi0) == braid_aut(4, comm(winv(delta) + winv(delta), b)))
print("Delta_4^2 central?", all(braid_aut(4, D4sq + [g]) == braid_aut(4, [g] + D4sq) for g in (1, 2, 3)))
# b in K_4 too
ab = braid_aut(4, b)
print("b in K_4 (strand-4 deletion trivial)?", all(kill4(ab[k]) == [k] for k in (1, 2, 3)), "| b trivial?", is_id(ab))

# ---------------- Laurent polynomials ----------------
def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0:
            del r[e]
    return r

def pmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = e1 + e2
            r[e] = r.get(e, 0) + c1 * c2
            if r[e] == 0:
                del r[e]
    return r

def peval(p, t):
    return sum(Fraction(c) * Fraction(t) ** e for e, c in p.items())

ONE = {0: 1}
def mat_id(n):
    return [[dict(ONE) if i == j else {} for j in range(n)] for i in range(n)]

def mat_mul(X, Y):
    n = len(X)
    Z = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not X[i][k]:
                continue
            for j in range(n):
                if Y[k][j]:
                    Z[i][j] = padd(Z[i][j], pmul(X[i][k], Y[k][j]))
    return Z

def burau_gen(n, g):
    """Transpose form of unreduced Burau: block [[1-t, 1], [t, 0]]; inverse block [[0, t^-1], [1, 1-t^-1]]."""
    M = mat_id(n)
    i = abs(g) - 1
    if g > 0:
        blk = [[{0: 1, 1: -1}, {0: 1}], [{1: 1}, {}]]
    else:
        blk = [[{}, {-1: 1}], [{0: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2):
            M[i + r][i + c] = blk[r][c]
    return M

def burau(n, word):
    M = mat_id(n)
    for g in word:
        M = mat_mul(M, burau_gen(n, g))
    return M

assert mat_mul(burau_gen(4, 2), burau_gen(4, -2)) == mat_id(4)
assert burau(4, [1, 2, 1]) == burau(4, [2, 1, 2])

for nn in (4, 5):
    M = burau(nn, phi0)
    Dm = [[padd(M[i][j], {0: -1}) if i == j else M[i][j] for j in range(nn)] for i in range(nn)]
    nz = any(Dm[i][j] for i in range(nn) for j in range(nn))
    at = lambda t: all(peval(Dm[i][j], t) == 0 for i in range(nn) for j in range(nn))
    print("B_%d: Burau(Phi0) == I as Laurent matrix? %s | == I at t=-1? %s | at t=2? %s | at t=3? %s"
          % (nn, not nz, at(-1), at(2), at(3)))

# (t+1)-adic depth of Burau(Phi0) - I in B_4: largest d with (t+1)^d dividing every entry
def divide_by_tp1(p):
    """Return p/(t+1) if exact, else None. p is a Laurent poly dict."""
    if not p:
        return {}
    lo = min(p)
    hi = max(p)
    coeffs = [p.get(e, 0) for e in range(lo, hi + 1)]  # ascending
    # synthetic division of polynomial (in t, shifted by t^lo) by (t+1), descending order
    desc = coeffs[::-1]
    q = []
    rem = 0
    for c in desc:
        rem = c - rem
        q.append(rem)
    # with divisor (t + 1): coefficients b_k = a_k - b_{k-1}; remainder is last
    remainder = q[-1]
    if remainder != 0:
        return None
    qd = q[:-1]  # descending coefficients of quotient
    qa = qd[::-1]
    return {lo + e: c for e, c in enumerate(qa) if c != 0}

# sanity check of the division routine
assert divide_by_tp1({0: 1, 1: 1}) == {0: 1}
assert divide_by_tp1({0: 1, 2: -1}) == {0: 1, 1: -1}   # 1 - t^2 = (1+t)(1-t)
assert divide_by_tp1({0: 1, 1: 2, 2: 1}) == {0: 1, 1: 1}
assert divide_by_tp1({0: 1}) is None

M = burau(4, phi0)
Dm = [[padd(M[i][j], {0: -1}) if i == j else M[i][j] for j in range(4)] for i in range(4)]
depth = 0
cur = Dm
while True:
    nxt = []
    ok = True
    for row in cur:
        nr = []
        for p in row:
            q = divide_by_tp1(p)
            if q is None:
                ok = False
                break
            nr.append(q)
        if not ok:
            break
        nxt.append(nr)
    if not ok:
        break
    depth += 1
    cur = nxt
    if depth > 50:
        break
print("(t+1)-adic depth of Burau_4(Phi0) - I:", depth)
