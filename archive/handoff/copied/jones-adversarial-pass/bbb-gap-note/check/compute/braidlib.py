"""Independent exact-arithmetic braid toolkit (written from scratch for the hostile-referee check).

Conventions
-----------
Braid words: lists of nonzero ints, k = sigma_k, -k = sigma_k^{-1}. Product uv = "u then v"
(word concatenation, left to right).

Free group words: lists of nonzero ints, j = x_j, -j = x_j^{-1}.

Artin action (RIGHT action, x.(uv) = (x.u).v):
    sigma_i :  x_i -> x_i x_{i+1} x_i^{-1},  x_{i+1} -> x_i,  x_j -> x_j otherwise.
    sigma_i^{-1}: x_i -> x_{i+1},  x_{i+1} -> x_{i+1}^{-1} x_i x_{i+1}.
With this convention the abelianised Fox Jacobian  J_ij = d(x_i . w)/d x_j |_{x_k = t}
is multiplicative, J(uv) = J(u) J(v), and J(sigma_i) = I + [[1-t, t],[1, 0]] block
on rows/cols i, i+1: the unreduced Burau matrix in convention "U" below.

Laurent polynomials: dict {exponent: int coefficient}, zero coefficients removed.
"""
from fractions import Fraction
import random

# ---------------------------------------------------------------- words
def parse(s):
    out = []
    for tok in s.split():
        if '^-1' in tok:
            out.append(-int(tok[1:tok.index('^')]))
        else:
            out.append(int(tok[1:]))
    return out

def inv(w):
    return [-a for a in reversed(w)]

def comm(x, y):
    return x + y + inv(x) + inv(y)

def power(w, k):
    if k >= 0:
        return w * k
    return inv(w) * (-k)

def reduce_word(w):
    st = []
    for a in w:
        if st and st[-1] == -a:
            st.pop()
        else:
            st.append(a)
    return st

def rev(w):
    return list(reversed(w))

def mirror(w):
    return [-a for a in w]

# ---------------------------------------------------------------- Artin action
def _subst_table(a):
    i = abs(a)
    if a > 0:
        return {i: [i, i + 1, -i], i + 1: [i]}
    return {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}

def _apply_subst(word, table):
    out = []
    for c in word:
        j = abs(c)
        img = table.get(j, [j])
        out.extend(img if c > 0 else inv(img))
    return reduce_word(out)

def artin_right(w, n):
    """images[j] = x_j . w (right action), j = 1..n, freely reduced."""
    imgs = {j: [j] for j in range(1, n + 1)}
    for a in w:
        assert 1 <= abs(a) <= n - 1, (a, n)
        tab = _subst_table(a)
        for j in imgs:
            imgs[j] = _apply_subst(imgs[j], tab)
    return imgs

def artin_left(w, n):
    """Left action phi_w = phi_{a1} o ... o phi_{ak} (anti-version), as a cross-check."""
    imgs = {j: [j] for j in range(1, n + 1)}
    for a in w:
        tab = _subst_table(a)
        new = {}
        for j in imgs:
            src = tab.get(j, [j])
            word = []
            for c in src:
                word.extend(imgs[abs(c)] if c > 0 else inv(imgs[abs(c)]))
            new[j] = reduce_word(word)
        imgs = new
    return imgs

def is_trivial(w, n):
    imgs = artin_right(w, n)
    return all(imgs[j] == [j] for j in imgs)

def same_braid(u, v, n):
    return is_trivial(u + inv(v), n)

# ---------------------------------------------------------------- permutation / deletion
def perm(w, n):
    """pos -> strand label after the braid (strands labelled by starting position)."""
    p = list(range(1, n + 1))
    for a in w:
        k = abs(a)
        p[k - 1], p[k] = p[k], p[k - 1]
    return p

def is_pure(w, n):
    return perm(w, n) == list(range(1, n + 1))

def delete_strand(w, n, d):
    """Remove the strand that STARTS at position d. Returns a word in B_{n-1}."""
    p = list(range(1, n + 1))   # p[pos-1] = strand at pos
    out = []
    for a in w:
        k = abs(a)
        s1, s2 = p[k - 1], p[k]
        if d not in (s1, s2):
            posd = p.index(d) + 1
            kk = k - 1 if posd < k else k
            out.append(kk if a > 0 else -kk)
        p[k - 1], p[k] = p[k], p[k - 1]
    return out

# ---------------------------------------------------------------- Laurent polynomials
def L(d):
    return {e: c for e, c in d.items() if c != 0}

ONE = {0: 1}
ZERO = {}

def ladd(a, b):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + c
    return L(r)

def lneg(a):
    return {e: -c for e, c in a.items()}

def lsub(a, b):
    return ladd(a, lneg(b))

def lmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return L(r)

def lsubs_inv(a):
    """t -> 1/t"""
    return {-e: c for e, c in a.items()}

def leval(a, t):
    t = Fraction(t)
    return sum((Fraction(c) * t ** e for e, c in a.items()), Fraction(0))

def mult_root_minus1(a):
    """multiplicity of t = -1 as a root of the Laurent polynomial a (inf for 0)."""
    if not a:
        return float('inf')
    lo = min(a)
    hi = max(a)
    coeffs = [a.get(e, 0) for e in range(lo, hi + 1)]  # coeffs[i] of t^i (after shift by t^-lo)
    k = 0
    while True:
        v = sum(c * (-1) ** i for i, c in enumerate(coeffs))   # value at t = -1
        if v != 0:
            return k
        # Horner / synthetic division by (t + 1), leading coefficient first
        out, acc = [], 0
        for c in reversed(coeffs):
            acc = acc * (-1) + c
            out.append(acc)
        remainder = out.pop()
        assert remainder == 0
        coeffs = list(reversed(out))
        k += 1

def lstr(a):
    if not a:
        return '0'
    terms = []
    for e in sorted(a):
        c = a[e]
        terms.append(f"{c:+d}*t^{e}")
    return ' '.join(terms)

# ---------------------------------------------------------------- matrices over Z[t^{+-1}]
def mid(n):
    return [[dict(ONE) if i == j else {} for j in range(n)] for i in range(n)]

def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[{} for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if not A[i][k]:
                continue
            for j in range(p):
                if B[k][j]:
                    C[i][j] = ladd(C[i][j], lmul(A[i][k], B[k][j]))
    return C

def mT(A):
    return [list(r) for r in zip(*A)]

def meq(A, B):
    return all(L(A[i][j]) == L(B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def mminusI(A):
    n = len(A)
    return [[lsub(A[i][j], ONE if i == j else {}) for j in range(n)] for i in range(n)]

def meval(A, t):
    return [[leval(x, t) for x in row] for row in A]

def is_identity_at(A, t):
    E = meval(A, t)
    return all(E[i][j] == (1 if i == j else 0) for i in range(len(E)) for j in range(len(E)))

def depth(A):
    """largest k with A == I mod (t+1)^k (inf if A == I)."""
    D = mminusI(A)
    return min(mult_root_minus1(x) for row in D for x in row)

# ---------------------------------------------------------------- Burau generators
def unreduced_gen(n, a):
    """Convention U: sigma_i -> I + [[1-t, t],[1, 0]] at rows/cols i,i+1 (1-based)."""
    i = abs(a) - 1
    M = mid(n)
    if a > 0:
        blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]]
    else:  # inverse: [[0, 1],[t^-1, 1 - t^-1]]
        blk = [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2):
            M[i + r][i + c] = blk[r][c]
    return M

def reduced_gen(n, a):
    """Reduced Burau ((n-1)x(n-1)), the common textbook form:
    s_1 -> [[-t,1],[0,1]] + I, s_i -> rows i-1..i+1 [[1,0,0],[t,-t,1],[0,0,1]], s_{n-1} -> [[1,0],[t,-t]]."""
    m = n - 1
    i = abs(a)
    M = mid(m)
    if a > 0:
        # row i (1-based) of the (n-1)x(n-1) matrix: entries at cols i-1, i, i+1
        r = i - 1
        if r - 1 >= 0:
            M[r][r - 1] = {1: 1}
        M[r][r] = {1: -1}
        if r + 1 < m:
            M[r][r + 1] = {0: 1}
    else:
        r = i - 1
        # inverse row: cols i-1 -> 1, i -> -t^-1, i+1 -> t^-1
        if r - 1 >= 0:
            M[r][r - 1] = {0: 1}
        M[r][r] = {-1: -1}
        if r + 1 < m:
            M[r][r + 1] = {-1: 1}
    return M

def burau(w, n, conv):
    """conv in {'U','UT','R','RT'}: unreduced, unreduced-transposed generators,
    reduced, reduced-transposed generators. Product taken left to right."""
    if conv in ('U', 'UT'):
        size, gen = n, unreduced_gen
    else:
        size, gen = n - 1, reduced_gen
    M = mid(size)
    for a in w:
        G = gen(n, a)
        if conv in ('UT', 'RT'):
            G = mT(G)
        M = mmul(M, G)
    return M

# ---------------------------------------------------------------- Fox calculus
def fox_row(word, n):
    """abelianised Fox derivatives (d word / d x_j)|_{x=t}, j=1..n, as Laurent polys."""
    row = [{} for _ in range(n)]
    e = 0
    for c in word:
        j = abs(c) - 1
        if c > 0:
            row[j] = ladd(row[j], {e: 1})
            e += 1
        else:
            e -= 1
            row[j] = ladd(row[j], {e: -1})
    return row

def fox_jacobian(w, n):
    imgs = artin_right(w, n)
    return [fox_row(imgs[j], n) for j in range(1, n + 1)]

def random_word(n, length, rng):
    return [rng.choice([1, -1]) * rng.randint(1, n - 1) for _ in range(length)]
