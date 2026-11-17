# Independent braid toolkit for the verify-compute pass (written from scratch).
# Braid words: lists of nonzero ints, +i = sigma_i, -i = sigma_i^{-1}.
# Free-group words: lists of nonzero ints, +j = x_j, -j = x_j^{-1}.
from fractions import Fraction as F


# ---------- free groups ----------
def fred(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def finv(w):
    return [-x for x in reversed(w)]


def comm(a, b):  # [a,b] = a b a^-1 b^-1 (the note's convention)
    return a + b + finv(a) + finv(b)


# ---------- Artin action B_n -> Aut(F_n) ----------
# sigma_i : x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i ; inverse accordingly.
def sig_map(i, s):
    if s > 0:
        return {i: [i, i + 1, -i], i + 1: [i]}
    return {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}


def subst(w, m):
    out = []
    for x in w:
        img = m.get(abs(x), [abs(x)])
        out += img if x > 0 else finv(img)
    return fred(out)


def artin(n, word):
    """Images of x_1..x_n under the automorphism of the braid word.
    Convention: process letters left to right, img <- phi_g(img)
    (an anti-homomorphism; injective, which is all we use)."""
    imgs = {j: [j] for j in range(1, n + 1)}
    for g in word:
        m = sig_map(abs(g), 1 if g > 0 else -1)
        imgs = {j: subst(imgs[j], m) for j in imgs}
    return imgs


def is_trivial(n, word):
    return all(v == [j] for j, v in artin(n, word).items())


def equal_in_Bn(n, w1, w2):
    return is_trivial(n, w1 + finv(w2))


def delete_strand(n, word, i):
    """For a PURE braid word: induced automorphism of F_n/<<x_i>> = F_{n-1},
    renumbered so the survivors are 1..n-1. Returns dict of images."""
    im = artin(n, word)
    ren = {}
    k = 0
    for j in range(1, n + 1):
        if j != i:
            k += 1
            ren[j] = k
    out = {}
    for j, v in im.items():
        if j == i:
            continue
        killed = fred([x for x in v if abs(x) != i])
        out[ren[j]] = [ren[abs(x)] * (1 if x > 0 else -1) for x in killed]
    return out


def is_pure(n, word):
    im = artin(n, word)
    for j, v in im.items():
        # x_j must map to a conjugate of x_j:  v = u x_j u^-1
        k = len(v) // 2
        if len(v) % 2 != 1 or v[k] != j or fred(v[:k] + v[k + 1:]) != []:
            return False
    return True


# ---------- pure braid generators ----------
def A(i, j):
    """Artin generator A_ij = s_{j-1}...s_{i+1} s_i^2 s_{i+1}^-1 ... s_{j-1}^-1."""
    up = list(range(j - 1, i, -1))
    return up + [i, i] + finv(up)


# ---------- Laurent polynomials (dict exp -> int) ----------
def padd(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0:
            del r[k]
    return r


def pmul(p, q):
    r = {}
    for a, x in p.items():
        for b, y in q.items():
            r[a + b] = r.get(a + b, 0) + x * y
    return {k: v for k, v in r.items() if v != 0}


def pev(p, t):
    t = F(t)
    return sum((F(c) * t ** k for k, c in p.items()), F(0))


def pder_at(p, t):
    t = F(t)
    return sum((F(c) * k * t ** (k - 1) for k, c in p.items() if k != 0), F(0))


def meye(n):
    return [[({0: 1} if i == j else {}) for j in range(n)] for i in range(n)]


def mmul(A_, B_):
    n = len(A_)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            acc = {}
            for k in range(n):
                if A_[i][k] and B_[k][j]:
                    acc = padd(acc, pmul(A_[i][k], B_[k][j]))
            row.append(acc)
        out.append(row)
    return out


def burau_gen(n, i, inv=False):
    """Unreduced Burau: s_i -> I + block [[1-t, t],[1, 0]] at rows/cols i,i+1."""
    M = meye(n)
    if not inv:
        blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]]
    else:
        blk = [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2):
            M[i - 1 + r][i - 1 + c] = blk[r][c]
    return M


def burau(n, word):
    M = meye(n)
    for g in word:
        M = mmul(M, burau_gen(n, abs(g), g < 0))
    return M


def delete_strand_diagram(n, word, d):
    """Diagrammatic strand deletion: drop every crossing that involves the strand
    that STARTS at position d, renumber the others. Returns an (n-1)-strand word."""
    pos_of = {k: k for k in range(1, n + 1)}      # strand label -> current position
    at = {k: k for k in range(1, n + 1)}          # position -> strand label
    out = []
    for g in word:
        i = abs(g)
        s1, s2 = at[i], at[i + 1]
        if d not in (s1, s2):
            pd = pos_of[d]
            out.append((i - 1 if pd < i else i) * (1 if g > 0 else -1))
        at[i], at[i + 1] = s2, s1
        pos_of[s1], pos_of[s2] = i + 1, i
    return out
