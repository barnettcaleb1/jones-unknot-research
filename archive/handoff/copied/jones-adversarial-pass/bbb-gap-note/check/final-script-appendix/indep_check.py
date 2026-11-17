#!/usr/bin/env python3
"""Independent re-derivation of the computational claims in bbb-gap-note.tex.

Written from scratch for the final script/appendix audit.  Does NOT import phi0_check.py.
Different algorithms from phi0_check.py on purpose:
  * free reduction by repeated adjacent-pair scans (not a stack);
  * Artin action as a LEFT action (word processed right to left, substitution);
  * Burau matrices evaluated numerically with Fractions at given t (no symbolic polys),
    inverses of generators obtained by Gauss-Jordan, not hard-coded;
  * reduced Burau obtained from the unreduced one by an explicit change of basis
    (quotient by the fixed column vector (1,..,1), and restriction to the kernel of the
    fixed row vector (1,t,..,t^{n-1})), not from the textbook reduced formula;
  * symbolic identity checked with a separate polynomial type (offset + coefficient list);
  * (t+1)-adic depth computed by expanding at t = -1 + s in truncated power series Z[s]/(s^K).
"""
from fractions import Fraction as Fr

# ------------------------------------------------------------------ words
def inverse(w):
    return [-x for x in w[::-1]]

def cm(x, y):                      # [x, y] = x y x^-1 y^-1
    return x + y + inverse(x) + inverse(y)

def freereduce(w):
    w = list(w)
    while True:
        out, i, changed = [], 0, False
        while i < len(w):
            if i + 1 < len(w) and w[i] == -w[i + 1]:
                i += 2
                changed = True
            else:
                out.append(w[i])
                i += 1
        w = out
        if not changed:
            return w

# ------------------------------------------------------------------ Artin action (left action)
def gen_aut(a):
    """Automorphism of F_n for the letter a, as a dict x_k -> word (letters are +-k)."""
    i = abs(a)
    if a > 0:
        return {i: [i, i + 1, -i], i + 1: [i]}
    # inverse automorphism, derived: sigma_i^-1 : x_i -> x_{i+1}, x_{i+1} -> x_{i+1}^-1 x_i x_{i+1}
    return {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}

def stackreduce(w):                # fast reduction used inside the Artin action
    st = []
    for c in w:
        if st and st[-1] == -c:
            st.pop()
        else:
            st.append(c)
    return st

def apply_aut(aut, word):
    out = []
    for c in word:
        img = aut.get(abs(c), [abs(c)])
        out += img if c > 0 else inverse(img)
    return stackreduce(out)

def act_left(w, n):
    """Psi_w = phi_{a1} o phi_{a2} o ... o phi_{am}, built by prefix composition:
    Psi_{i+1}(x_k) = Psi_i(phi_{a_{i+1}}(x_k)).  Returns dict k -> reduced word Psi_w(x_k)."""
    img = {k: [k] for k in range(1, n + 1)}
    for a in w:
        g = gen_aut(a)
        new = {}
        for k in range(1, n + 1):
            out = []
            for c in g.get(k, [k]):
                im = img[abs(c)]
                out += im if c > 0 else inverse(im)
            new[k] = stackreduce(out)
        img = new
    return img

def is_trivial(w, n):
    return all(v == [k] for k, v in act_left(w, n).items())

def same(u, v, n):
    return act_left(u, n) == act_left(v, n)

def perm(w, n):
    p = list(range(1, n + 1))
    for a in w:
        k = abs(a)
        p[k - 1], p[k] = p[k], p[k - 1]
    return p

def is_pure(w, n):
    return perm(w, n) == list(range(1, n + 1))

def delete_strand(w, n, d):
    """Delete the strand that starts at position d (labels = starting positions)."""
    pos = list(range(1, n + 1))       # pos[j] = label of strand currently at position j+1
    out = []
    for a in w:
        k = abs(a)
        left, right = pos[k - 1], pos[k]
        if d != left and d != right:
            where = pos.index(d) + 1      # 1-based current position of strand d
            newk = k - 1 if where < k else k
            out.append(newk if a > 0 else -newk)
        pos[k - 1], pos[k] = right, left
    return out

# ------------------------------------------------------------------ numeric matrices over Q
def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]

def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), Fr(0)) for j in range(p)] for i in range(n)]

def mat_inv(A):
    n = len(A)
    M = [row[:] + eye(n)[i] for i, row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]

def transpose(A):
    return [list(r) for r in zip(*A)]

def U_gen(n, a, t):
    """Unreduced Burau: sigma_i -> I_{i-1} + [[1-t, t], [1, 0]] + I_{n-i-1}."""
    i = abs(a) - 1
    M = eye(n)
    M[i][i], M[i][i + 1], M[i + 1][i], M[i + 1][i + 1] = 1 - t, t, Fr(1), Fr(0)
    return M if a > 0 else mat_inv(M)

def U_word(w, n, t, order="lr"):
    M = eye(n)
    letters = w if order == "lr" else list(reversed(w))
    for a in letters:
        M = mat_mul(M, U_gen(n, a, t))
    return M

def quotient_reduced(M):
    """M fixes the column vector (1,...,1).  In the basis e_1..e_{n-1}, (1..1) the matrix is
    block lower triangular; return the top-left (n-1)x(n-1) block (action on the quotient)."""
    n = len(M)
    C = eye(n)
    for i in range(n):
        C[i][n - 1] = Fr(1)
    N = mat_mul(mat_mul(mat_inv(C), M), C)
    assert all(N[i][n - 1] == (i == n - 1) for i in range(n)), "fixed vector not fixed"
    return [row[: n - 1] for row in N[: n - 1]]

def sub_reduced(M, t):
    """M fixes the row vector (1, t, ..., t^{n-1}); its kernel W (column vectors) is invariant.
    Basis f_i = e_{i+1} - t e_i (i=1..n-1), completed by e_1; return the action on W."""
    n = len(M)
    C = [[Fr(0)] * n for _ in range(n)]
    for i in range(n - 1):
        C[i + 1][i] = Fr(1)
        C[i][i] = -t
    C[0][n - 1] = Fr(1)
    N = mat_mul(mat_mul(mat_inv(C), M), C)
    assert all(N[n - 1][j] == 0 for j in range(n - 1)), "W not invariant"
    return [row[: n - 1] for row in N[: n - 1]]

def isI(M):
    return M == eye(len(M))

# ------------------------------------------------------------------ polynomials (offset, coeffs)
class LP:
    """Laurent polynomial  t^lo * (c0 + c1 t + ...), integer coefficients."""
    def __init__(self, lo, cs):
        cs = list(cs)
        while cs and cs[-1] == 0:
            cs.pop()
        k = 0
        while k < len(cs) and cs[k] == 0:
            k += 1
        self.lo, self.cs = (lo + k, cs[k:]) if cs else (0, [])
    def __add__(s, o):
        if not s.cs: return o
        if not o.cs: return s
        lo = min(s.lo, o.lo)
        hi = max(s.lo + len(s.cs), o.lo + len(o.cs))
        cs = [0] * (hi - lo)
        for p in (s, o):
            for k, c in enumerate(p.cs):
                cs[p.lo - lo + k] += c
        return LP(lo, cs)
    def __neg__(s):
        return LP(s.lo, [-c for c in s.cs])
    def __sub__(s, o):
        return s + (-o)
    def __mul__(s, o):
        if not s.cs or not o.cs: return LP(0, [])
        cs = [0] * (len(s.cs) + len(o.cs) - 1)
        for i, a in enumerate(s.cs):
            for j, b in enumerate(o.cs):
                cs[i + j] += a * b
        return LP(s.lo + o.lo, cs)
    def __eq__(s, o):
        return (s.lo, s.cs) == (o.lo, o.cs)
    def ev(s, t):
        return sum((Fr(c) * Fr(t) ** (s.lo + k) for k, c in enumerate(s.cs)), Fr(0))

ZERO, ONE = LP(0, []), LP(0, [1])
T = LP(1, [1])
TINV = LP(-1, [1])

def lp_eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]

def lp_mul(A, B):
    n = len(A)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            acc = ZERO
            for k in range(n):
                acc = acc + A[i][k] * B[k][j]
            row.append(acc)
        out.append(row)
    return out

def lp_U_gen(n, a, invert_t=False):
    t, ti = (TINV, T) if invert_t else (T, TINV)
    i = abs(a) - 1
    M = lp_eye(n)
    if a > 0:
        blk = [[ONE - t, t], [ONE, ZERO]]
    else:
        blk = [[ZERO, ONE], [ti, ONE - ti]]
    for r in range(2):
        for c in range(2):
            M[i + r][i + c] = blk[r][c]
    return M

def lp_U_word(w, n, invert_t=False):
    M = lp_eye(n)
    for a in w:
        M = lp_mul(M, lp_U_gen(n, a, invert_t))
    return M

def lp_minus_I(M):
    return [[M[i][j] - (ONE if i == j else ZERO) for j in range(len(M))] for i in range(len(M))]

def lp_scale(p, M):
    return [[p * x for x in row] for row in M]

# ------------------------------------------------------------------ truncated power series at t = -1 + s
K = 6
def ps(cs):
    cs = list(cs)[:K]
    return cs + [0] * (K - len(cs))
PS_T = ps([-1, 1])                       # t = -1 + s
PS_TINV = ps([-1] * K)                   # 1/t = -1/(1 - s) = -(1 + s + s^2 + ...)
PS_ONE, PS_ZERO = ps([1]), ps([])
def ps_add(a, b): return [x + y for x, y in zip(a, b)]
def ps_neg(a): return [-x for x in a]
def ps_mul(a, b):
    r = [0] * K
    for i, x in enumerate(a):
        if x:
            for j in range(K - i):
                r[i + j] += x * b[j]
    return r
assert ps_mul(PS_T, PS_TINV) == PS_ONE

def ps_eye(n): return [[PS_ONE if i == j else PS_ZERO for j in range(n)] for i in range(n)]
def ps_mat_mul(A, B):
    n = len(A)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            acc = PS_ZERO
            for k in range(n):
                acc = ps_add(acc, ps_mul(A[i][k], B[k][j]))
            row.append(acc)
        out.append(row)
    return out
def ps_U_gen(n, a):
    i = abs(a) - 1
    M = ps_eye(n)
    if a > 0:
        blk = [[ps_add(PS_ONE, ps_neg(PS_T)), PS_T], [PS_ONE, PS_ZERO]]
    else:
        blk = [[PS_ZERO, PS_ONE], [PS_TINV, ps_add(PS_ONE, ps_neg(PS_TINV))]]
    for r in range(2):
        for c in range(2):
            M[i + r][i + c] = blk[r][c]
    return M
def ps_U_word(w, n):
    M = ps_eye(n)
    for a in w:
        M = ps_mat_mul(M, ps_U_gen(n, a))
    return M
def ps_depth(M):
    """s-adic valuation of M - I (K means 'at least K')."""
    n = len(M)
    v = K
    for i in range(n):
        for j in range(n):
            e = ps_add(M[i][j], ps_neg(PS_ONE if i == j else PS_ZERO))
            k = next((k for k, x in enumerate(e) if x), K)
            v = min(v, k)
    return v

# ================================================================== the braids
A14 = [3, 2, 1, 1, -2, -3]
A24 = [3, 2, 2, -3]
A34 = [3, 3]
X = [1, 2] * 6
b = cm(cm(A14, A24), A34)
Phi0 = cm(X, b)
D3sq = [1, 2, 1] * 2              # Delta_3^2 written as (s1 s2 s1)^2 (different word from (s1 s2)^3)
D4 = [1, 2, 3, 1, 2, 1]           # Delta_4 = s1 s2 s3 s1 s2 s1
D4sq = D4 * 2
delta = inverse(D3sq) + D4sq

results = []
def rec(name, ok, extra=""):
    results.append((name, ok))
    print(("ok    " if ok else "BAD   ") + name + (("  [" + extra + "]") if extra else ""))

# sanity of my Artin action
rec("Artin(left) satisfies braid relations in B4",
    same([1, 2, 1], [2, 1, 2], 4) and same([2, 3, 2], [3, 2, 3], 4) and same([1, 3], [3, 1], 4)
    and not is_trivial([1], 4) and is_trivial([2, -2], 4))

# word lengths
rec("word length of Phi0 as written = 112", len(Phi0) == 112, str(len(Phi0)))
red = freereduce(Phi0)
rec("freely reduced length = 76 (scan algorithm and stack algorithm agree)",
    len(red) == 76 and red == stackreduce(Phi0), str(len(red)))

# X, delta
rec("X = (s1 s2)^6 equals Delta_3^4 = (s1 s2 s1)^4", same(X, [1, 2, 1] * 4, 4))
rec("Delta_3^2 = (s1 s2)^3", same(D3sq, [1, 2] * 3, 4))
rec("delta = Delta_3^-2 Delta_4^2 equals A14 A24 A34", same(delta, A14 + A24 + A34, 4))
rec("Phi0 = [delta^-2, b]", same(Phi0, cm(inverse(delta) + inverse(delta), b), 4))
rec("Phi0 nontrivial (Artin action)", not is_trivial(Phi0, 4))
rec("Phi0 pure", is_pure(Phi0, 4))

# Brunnian: delete each strand
for d in (1, 2, 3, 4):
    v = delete_strand(Phi0, 4, d)
    rec(f"delete strand {d}: freely reduces to empty / trivial Artin action on F3",
        freereduce(v) == [] and is_trivial(v, 3), f"len {len(v)}")
# K4 membership
inK4 = lambda v: is_pure(v, 4) and is_trivial(delete_strand(v, 4, 4), 3)
rec("A14, A24, A34, b, delta, Phi0 all in K4", all(inK4(v) for v in (A14, A24, A34, b, delta, Phi0)))
# deleting strand 4 from A_i4 must give the trivial braid; deleting others not (A_i4 not Brunnian)
rec("A14 not killed by deleting strand 2 (sanity: deletion not vacuous)",
    not is_trivial(delete_strand(A14, 4, 2), 3))

# ---------------- numeric Burau, unreduced, several conventions
convs = {
    "U  (lr product)": lambda w, n, t: U_word(w, n, t, "lr"),
    "U  (reversed product)": lambda w, n, t: U_word(w, n, t, "rl"),
    "UT": lambda w, n, t: transpose(U_word(w, n, t, "rl")),
    "Rq (quotient-reduced)": lambda w, n, t: quotient_reduced(U_word(w, n, t, "lr")),
    "Rs (sub-reduced)": lambda w, n, t: sub_reduced(U_word(w, n, t, "lr"), t),
}
for n in (4, 5):
    for cname, F in convs.items():
        at_m1 = isI(F(Phi0, n, Fr(-1)))
        vals = {t: isI(F(Phi0, n, Fr(t))) for t in (Fr(2), Fr(1, 2), Fr(3), Fr(1, 3))}
        rec(f"B{n} {cname}: Phi0 = I at t=-1", at_m1)
        rec(f"B{n} {cname}: Phi0 != I at t = 2, 1/2, 3, 1/3", not any(vals.values()),
            ", ".join(f"t={t}: {'I' if v else 'not I'}" for t, v in vals.items()))

# mirror convention: s_i -> s_i^-1 in every letter
mirror = lambda w: [-a for a in w]
rec("mirror(Phi0) = I at t=-1 and != I at t=2, 1/2 (U)",
    isI(U_word(mirror(Phi0), 4, Fr(-1))) and not isI(U_word(mirror(Phi0), 4, Fr(2)))
    and not isI(U_word(mirror(Phi0), 4, Fr(1, 2))))

# ---------------- symbolic identity rho(X) - I = (1 + t^3)(rho(Delta_3^2) - I)
UX = lp_U_word(X, 4)
UD = lp_U_word(D3sq, 4)
lhs, rhs = lp_minus_I(UX), lp_scale(ONE + LP(3, [1]), lp_minus_I(UD))
rec("U: rho(X) - I == (1 + t^3)(rho(Delta_3^2) - I) exactly (symbolic)", lhs == rhs)
# entries of U(Delta_3^2) for the record
print("      U(Delta_3^2) - I, nonzero entries:",
      [(i + 1, j + 1, (p.lo, p.cs)) for i, row in enumerate(lp_minus_I(UD)) for j, p in enumerate(row) if p.cs])
# convention with t -> 1/t
UXi, UDi = lp_U_word(X, 4, True), lp_U_word(D3sq, 4, True)
rec("t->1/t convention: (1 + t^3) identity FAILS", lp_minus_I(UXi) != lp_scale(ONE + LP(3, [1]), lp_minus_I(UDi)))
rec("t->1/t convention: (1 + t^-3) identity holds", lp_minus_I(UXi) == lp_scale(ONE + LP(-3, [1]), lp_minus_I(UDi)))
# mirror convention numerically: rho(mirror X) - I vs (1 + t^3) and (1 + t^-3)
ok_m3, ok_mm3 = True, True
for tv in (Fr(2), Fr(3), Fr(5, 7)):
    MX = U_word(mirror(X), 4, tv); MD = U_word(mirror(D3sq), 4, tv)
    L = [[MX[i][j] - (i == j) for j in range(4)] for i in range(4)]
    for f, flag in ((1 + tv ** 3, "p"), (1 + tv ** -3, "m")):
        R = [[f * (MD[i][j] - (i == j)) for j in range(4)] for i in range(4)]
        if flag == "p": ok_m3 &= (L == R)
        else: ok_mm3 &= (L == R)
rec("mirror convention: (1 + t^3) identity FAILS, (1 + t^-3) holds (numeric at 3 points)",
    (not ok_m3) and ok_mm3)
# identity in the reduced (quotient / sub) conventions, numeric at 20 points (polynomial degree <= 15)
ok_q = ok_s = True
for k in range(1, 21):
    tv = Fr(k, 7) + Fr(1, 3)
    for kind in ("q", "s"):
        if kind == "q":
            RX = quotient_reduced(U_word(X, 4, tv)); RD = quotient_reduced(U_word(D3sq, 4, tv))
        else:
            RX = sub_reduced(U_word(X, 4, tv), tv); RD = sub_reduced(U_word(D3sq, 4, tv), tv)
        L = [[RX[i][j] - (i == j) for j in range(3)] for i in range(3)]
        R = [[(1 + tv ** 3) * (RD[i][j] - (i == j)) for j in range(3)] for i in range(3)]
        if kind == "q": ok_q &= (L == R)
        else: ok_s &= (L == R)
rec("reduced (quotient and sub): identity holds at 20 rational points", ok_q and ok_s)

# ---------------- depth via expansion at t = -1 + s
dPhi = ps_depth(ps_U_word(Phi0, 4))
rec("depth of Phi0 (U, B4) is exactly 1", dPhi == 1, str(dPhi))
rec("depth of f(Phi0) (U, B5) is exactly 1", ps_depth(ps_U_word(Phi0, 5)) == 1)
Psi = [3] + Phi0 + [-3]
c1 = cm(Phi0, Psi)
c2 = cm(Phi0, c1)
d1, d2 = ps_depth(ps_U_word(c1, 4)), ps_depth(ps_U_word(c2, 4))
rec("depth of [Phi0, s3 Phi0 s3^-1] >= 2 and of [Phi0,[Phi0, s3 Phi0 s3^-1]] >= 3", d1 >= 2 and d2 >= 3,
    f"found {d1}, {d2}")
rec("depth X >= 1 (X = I at t=-1), sanity", ps_depth(ps_U_word(X, 4)) >= 1)

# ---------------- non-commutation of Phi0 and s3 Phi0 s3^-1
P2, Q2 = U_word(Phi0, 4, Fr(2)), U_word(Psi, 4, Fr(2))
rec("U(Phi0) and U(s3 Phi0 s3^-1) do not commute (at t=2)", mat_mul(P2, Q2) != mat_mul(Q2, P2))
# (non-commuting Burau images already imply the braids do not commute)
rec("s3 Phi0 s3^-1 is Brunnian too", all(freereduce(delete_strand(Psi, 4, d)) == [] or
                                           is_trivial(delete_strand(Psi, 4, d), 3) for d in (1, 2, 3, 4))
    and is_pure(Psi, 4))

# ---------------- Section 7 of the paper (pp. 26-27), polynomials as printed (sign, exponent) in order
MPhi = [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (1, -3), (1, -1), (1, 1)]
MPhiGamma = [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (1, -4), (1, -2), (1, 0)]
MGamma = [(-1, 0), (-1, 2), (1, 1), (1, -1), (-1, 0), (-1, 2), (1, 3), (1, 1), (1, -1), (-1, -2),
          (-1, 0), (1, -1), (1, -3), (-1, -2), (-1, 0), (1, 1), (1, -1), (1, -3), (-1, -2), (-1, 0)]
val = lambda P: sum(e * (-1) ** k for e, k in P)
def simplified(P):
    d = {}
    for e, k in P:
        d[k] = d.get(k, 0) + e
    return {k: c for k, c in d.items() if c}
rec("Sec 7: M_Phi has 8 terms, value 2 at t=-1", (len(MPhi), val(MPhi)) == (8, 2), f"{len(MPhi)}, {val(MPhi)}")
rec("Sec 7: M_PhiGamma has 8 terms, value 8", (len(MPhiGamma), val(MPhiGamma)) == (8, 8),
    f"{len(MPhiGamma)}, {val(MPhiGamma)}")
rec("Sec 7: M_Gamma has 20 terms, value -20", (len(MGamma), val(MGamma)) == (20, -20),
    f"{len(MGamma)}, {val(MGamma)}")
rec("Sec 7: simplified forms match the paper's second lines",
    simplified(MPhi) == {0: 1, 2: 1, 4: 1, 3: -1, -3: 1, -1: 1}
    and simplified(MPhiGamma) == {0: 2, 2: 1, 4: 1, 3: -1, 1: -1, -4: 1, -2: 1}
    and simplified(MGamma) == {-3: 2, -2: -3, -1: 4, 0: -5, 1: 3, 2: -2, 3: 1})
rec("Sec 7: eps_i (-1)^k_i constant for the two parity polynomials, not for M_Phi",
    len({e * (-1) ** k for e, k in MPhiGamma}) == 1 and len({e * (-1) ** k for e, k in MGamma}) == 1
    and len({e * (-1) ** k for e, k in MPhi}) == 2)
rec("Sec 7: sum |simplified coeffs| = 8, 20 for parity polys; 6 for M_Phi",
    [sum(abs(c) for c in simplified(P).values()) for P in (MPhiGamma, MGamma, MPhi)] == [8, 20, 6])

print()
print("reduced word of Phi0 (76 letters):", " ".join(map(str, red)))
bad = [n for n, ok in results if not ok]
print("ALL OK" if not bad else f"{len(bad)} BAD: {bad}")
