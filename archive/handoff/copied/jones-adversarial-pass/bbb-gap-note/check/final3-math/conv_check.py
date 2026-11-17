#!/usr/bin/env python3
"""Independent exact checks (written from scratch, does not import phi0_check.py) of the
new/changed convention claims in note/bbb-gap-note.tex:

 (A) Prop 4(b): rho(X)-I = (1+t^3)(rho(D3^2)-I) in U, UT, R, RT; after reversing every half
     twist (mirror word) or t -> 1/t the factor is 1+t^-3.
 (B) Appendix: D * R^T(s_i^{+-1}) * D equals the BB05 reduced matrix
     I_{i-2} + [[1,-t,0],[0,-t,0],[0,-1,1]] + I_{n-i-2} (with -t at (i,i)), for n = 3..6,
     with D = diag(1,-1,1,-1,...) alternating; also test the non-alternating reading.
 (C) Appendix: mirror changes each of U, UT, R, RT by t -> 1/t up to conjugation by a
     matrix C(t) in GL(Z[t,1/t]):  M(s_i^-1)(t) = C(t) M(s_i)(1/t) C(t)^-1 for all i.
 (D) Appendix: U is the Fox Jacobian (x_k -> t) of x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i,
     and Fox Jacobians multiply in word order for a right action.
 (E) Section 4 new sentence: b = [[A14,A24],A34] is Brunnian (each strand deletion trivial).
"""
import random
from fractions import Fraction

# ---------- Laurent polynomials as dict {exp: coeff} ----------
def lp_add(a, b, s=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + s * c
    return {e: c for e, c in r.items() if c}
def lp_mul(a, b):
    r = {}
    for e, c in a.items():
        for f, d in b.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}
def lp_inv_t(a): return {-e: c for e, c in a.items()}          # t -> 1/t
ONE, ZERO = {0: 1}, {}
def T(k=1, c=1): return {k: c}

def mat_id(n): return [[dict(ONE) if i == j else {} for j in range(n)] for i in range(n)]
def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    R = [[{} for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if not A[i][k]: continue
            for j in range(p):
                if B[k][j]:
                    R[i][j] = lp_add(R[i][j], lp_mul(A[i][k], B[k][j]))
    return R
def mat_T(A): return [list(r) for r in zip(*A)]
def mat_map(A, f): return [[f(x) for x in r] for r in A]
def mat_eq(A, B): return all(x == y for ra, rb in zip(A, B) for x, y in zip(ra, rb))
def mat_sub_I(A): return [[lp_add(x, ONE if i == j else {}, -1) for j, x in enumerate(r)] for i, r in enumerate(A)]

# ---------- generators, built independently ----------
def U_gen(n, a):
    i = abs(a) - 1
    M = mat_id(n)
    if a > 0:
        blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]]
    else:   # inverse of [[1-t, t],[1, 0]] is [[0, 1],[1/t, 1 - 1/t]]
        blk = [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2):
            M[i + r][i + c] = blk[r][c]
    return M
def R_gen(n, a):
    """reduced: s_i replaces row i of I_{n-1} by (t, -t, 1) in cols i-1, i, i+1 (1-based)."""
    i = abs(a)
    M = mat_id(n - 1)
    row = [{} for _ in range(n - 1)]
    if a > 0:
        vals = {i - 1: {1: 1}, i: {1: -1}, i + 1: {0: 1}}
    else:
        # inverse computed by hand-free method: solve below instead of hard-coding
        return mat_inv_unitri_row(R_gen(n, i), i - 1)
    for c, v in vals.items():
        if 1 <= c <= n - 1:
            row[c - 1] = v
    M[i - 1] = row
    return M
def mat_inv_unitri_row(M, r):
    """inverse of a matrix equal to I except row r: row r' = -row/piv off diag, 1/piv on diag."""
    n = len(M)
    piv = M[r][r]
    assert len(piv) == 1, piv
    (e, c), = piv.items()
    assert c in (1, -1)
    pinv = {-e: c}            # 1/piv (c = +-1)
    N = mat_id(n)
    N[r] = [lp_mul(lp_mul(M[r][j], pinv), {0: -1}) if j != r else pinv for j in range(n)]
    return N
def BB05_red(n, a):
    """BB05 Section 4.2 reduced: s_i -> I_{i-2} + [[1,-t,0],[0,-t,0],[0,-1,1]] + I_{n-i-2},
    the -t in the middle at (i,i); truncated at the edges."""
    i = abs(a)
    M = mat_id(n - 1)
    blk = {(i - 1, i - 1): {0: 1}, (i - 1, i): {1: -1}, (i, i): {1: -1}, (i + 1, i): {0: -1}, (i + 1, i + 1): {0: 1}}
    for (r, c), v in blk.items():
        if 1 <= r <= n - 1 and 1 <= c <= n - 1:
            M[r - 1][c - 1] = v
    if a < 0:
        return mat_inv_unitri_col(M, i - 1)
    return M
def mat_inv_unitri_col(M, c):
    return mat_T(mat_inv_unitri_row(mat_T(M), c))

def gen(n, a, conv):
    if conv == 'U': return U_gen(n, a)
    if conv == 'UT': return mat_T(U_gen(n, a))
    if conv == 'R': return R_gen(n, a)
    if conv == 'RT': return mat_T(R_gen(n, a))
    if conv == 'BB05R': return BB05_red(n, a)
    raise ValueError(conv)
def rep(w, n, conv):
    size = n if conv in ('U', 'UT') else n - 1
    M = mat_id(size)
    for a in w:
        M = mat_mul(M, gen(n, a, conv))
    return M

CONVS = ('U', 'UT', 'R', 'RT')
out = []
def report(name, ok):
    out.append(('PASS  ' if ok else 'FAIL  ') + name)
    print(out[-1])

# sanity: each is a representation, inverses correct
for n in (3, 4, 5, 6):
    for conv in CONVS + ('BB05R',):
        size = n if conv in ('U', 'UT') else n - 1
        ok = all(mat_eq(mat_mul(gen(n, i, conv), gen(n, -i, conv)), mat_id(size)) for i in range(1, n))
        ok &= all(mat_eq(rep([i, i + 1, i], n, conv), rep([i + 1, i, i + 1], n, conv)) for i in range(1, n - 1))
        ok &= all(mat_eq(rep([i, j], n, conv), rep([j, i], n, conv)) for i in range(1, n) for j in range(i + 2, n))
        report(f"sanity n={n} {conv}: braid relations and inverses", ok)

# ---------- (A) Prop 4(b) identity in all conventions and orientations ----------
X = [1, 2] * 6
D3sq = [1, 2] * 3
mirror = lambda w: [-a for a in w]
for conv in CONVS:
    LX, LD = mat_sub_I(rep(X, 4, conv)), mat_sub_I(rep(D3sq, 4, conv))
    report(f"(A) {conv}: rho(X)-I == (1+t^3)(rho(D3^2)-I)", mat_eq(LX, mat_map(LD, lambda p: lp_mul({0: 1, 3: 1}, p))))
    report(f"(A) {conv}: rho(X)-I != (1+t^-3)(rho(D3^2)-I)", not mat_eq(LX, mat_map(LD, lambda p: lp_mul({0: 1, -3: 1}, p))))
    LXm, LDm = mat_sub_I(rep(mirror(X), 4, conv)), mat_sub_I(rep(mirror(D3sq), 4, conv))
    report(f"(A) {conv} mirrored word: factor is 1+t^-3", mat_eq(LXm, mat_map(LDm, lambda p: lp_mul({0: 1, -3: 1}, p))))
    LXi, LDi = mat_map(LX, lp_inv_t), mat_map(LD, lp_inv_t)
    report(f"(A) {conv} with t -> 1/t: factor is 1+t^-3", mat_eq(LXi, mat_map(LDi, lambda p: lp_mul({0: 1, -3: 1}, p))))
# 1+t^-3 = t^-3 (1+t^3), t+1 | 1+t^3
report("(A) 1+t^-3 == t^-3 (1+t^3)", lp_mul({-3: 1}, {0: 1, 3: 1}) == {0: 1, -3: 1})
report("(A) 1+t^3 == (1+t)(1-t+t^2)", lp_mul({0: 1, 1: 1}, {0: 1, 1: -1, 2: 1}) == {0: 1, 3: 1})

# ---------- (B) BB05 reduced vs D R^T D ----------
def diag_alt(m): return [[{0: (-1) ** i} if i == j else {} for j in range(m)] for i in range(m)]
def diag_naive(m): return [[{0: (-1 if i == 1 else 1)} if i == j else {} for j in range(m)] for i in range(m)]
for n in (3, 4, 5, 6):
    Dm = diag_alt(n - 1)
    ok = all(mat_eq(mat_mul(mat_mul(Dm, gen(n, a, 'RT')), Dm), BB05_red(n, a)) for i in range(1, n) for a in (i, -i))
    report(f"(B) n={n}: diag(1,-1,1,-1,..) RT(s_i^+-1) diag(..) == BB05 reduced, all i", ok)
    Dn = diag_naive(n - 1)
    okn = all(mat_eq(mat_mul(mat_mul(Dn, gen(n, a, 'RT')), Dn), BB05_red(n, a)) for i in range(1, n) for a in (i, -i))
    report(f"(B) n={n}: non-alternating diag(1,-1,1,1,..) also works? {okn} (expected True only for n<=4)", okn == (n <= 4))
# also: BB05 reduced orientation (identity factor 1+t^3)
LX, LD = mat_sub_I(rep(X, 4, 'BB05R')), mat_sub_I(rep(D3sq, 4, 'BB05R'))
report("(B) BB05 reduced: rho(X)-I == (1+t^3)(rho(D3^2)-I)", mat_eq(LX, mat_map(LD, lambda p: lp_mul({0: 1, 3: 1}, p))))
report("(B) BB05 reduced: D3^2 -> t^3 I_2 on B_3", mat_eq(rep(D3sq, 3, 'BB05R'), [[{3: 1}, {}], [{}, {3: 1}]]))

# ---------- (C) mirror == t -> 1/t up to conjugation by C(t) in GL(Z[t^+-1]) ----------
def J(m): return [[dict(ONE) if j == m - 1 - i else {} for j in range(m)] for i in range(m)]
def Delta(n):
    w = []
    for k in range(1, n):
        w += list(range(k, 0, -1))
    return w
def det(M):
    # Laurent determinant by cofactor expansion (small sizes only)
    n = len(M)
    if n == 1: return M[0][0]
    r = {}
    for j in range(n):
        if not M[0][j]: continue
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        r = lp_add(r, lp_mul(lp_mul(M[0][j], {0: (-1) ** j}), det(minor)))
    return r
for n in (4, 5):
    for conv in CONVS:
        size = n if conv in ('U', 'UT') else n - 1
        base = 'U' if conv in ('U', 'UT') else 'R'
        Cb = mat_mul(J(size), mat_map(rep(Delta(n), n, base), lp_inv_t))     # C = J M(Delta)(1/t)
        if conv.endswith('T'):
            # for transposes: M^T(s^-1)(t) = C^-T M^T(s)(1/t) C^T ; test via C^T M^T(s^-1)(t) == M^T(s)(1/t) C^T
            CT = mat_T(Cb)
            ok = all(mat_eq(mat_mul(CT, gen(n, -i, conv)), mat_mul(mat_map(gen(n, i, conv), lp_inv_t), CT)) for i in range(1, n))
        else:
            ok = all(mat_eq(mat_mul(gen(n, -i, conv), Cb), mat_mul(Cb, mat_map(gen(n, i, conv), lp_inv_t))) for i in range(1, n))
        d = det(Cb)
        unit = len(d) == 1 and list(d.values())[0] in (1, -1)
        report(f"(C) n={n} {conv}: M(s_i^-1)(t) = C M(s_i)(1/t) C^-1 for all i, C = J*{base}(Delta)(1/t), det C = {d} (unit: {unit})", ok and unit)

# depth / t=-1 invariance of the opposite orientation, directly on Phi0
def inv(w): return [-a for a in reversed(w)]
def comm(x, y): return x + y + inv(x) + inv(y)
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
b = comm(comm(A14, A24), A34)
Phi0 = comm(X, b)
def ev(p, x): return sum(c * Fraction(x) ** e for e, c in p.items())
def is_I_at(M, x): return all(ev(p, x) == (1 if i == j else 0) for i, r in enumerate(M) for j, p in enumerate(r))
def mult_root(p):
    k = 0
    q = dict(p)
    while q and ev(q, -1) == 0:
        # divide by (t+1): synthetic on shifted poly
        lo = min(q); hi = max(q)
        coeffs = [q.get(e, 0) for e in range(lo, hi + 1)]
        res, acc = [], 0
        for c in reversed(coeffs):
            acc = c - acc; res.append(acc)
        assert res[-1] == 0
        res = res[:-1][::-1]
        q = {lo + i: c for i, c in enumerate(res) if c}
        k += 1
    return k
def depth(M):
    D = mat_sub_I(M)
    vals = [mult_root(p) for r in D for p in r if p]
    return min(vals) if vals else float('inf')
for n in (4, 5):
    for conv in CONVS:
        Mm = rep(mirror(Phi0), n, conv)
        report(f"(C) n={n} {conv}: mirror(Phi0) = I at t=-1, != I at 2,1/2,3,1/3, depth 1",
               is_I_at(Mm, -1) and not any(is_I_at(Mm, x) for x in (2, Fraction(1, 2), 3, Fraction(1, 3))) and depth(Mm) == 1)

# ---------- (D) Fox calculus ----------
def artin_right(w, n):
    img = {j: [j] for j in range(1, n + 1)}
    def red(s):
        o = []
        for a in s:
            if o and o[-1] == -a: o.pop()
            else: o.append(a)
        return o
    for a in w:
        i = abs(a)
        if a > 0: sub = {i: [i, i + 1, -i], i + 1: [i]}
        else: sub = {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}
        for j in img:
            o = []
            for c in img[j]:
                s = sub.get(abs(c), [abs(c)])
                o += s if c > 0 else [-x for x in reversed(s)]
            img[j] = red(o)
    return img
def fox_row(word, n):
    row = [{} for _ in range(n)]
    prefix = 0   # exponent sum of the prefix (x_k -> t)
    for c in word:
        k = abs(c) - 1
        if c > 0:
            row[k] = lp_add(row[k], {prefix: 1}); prefix += 1
        else:
            prefix -= 1; row[k] = lp_add(row[k], {prefix: -1})
    return row
for n in (4, 5):
    ok = all(mat_eq([fox_row(artin_right([a], n)[k], n) for k in range(1, n + 1)], U_gen(n, a)) for i in range(1, n) for a in (i, -i))
    report(f"(D) n={n}: Fox Jacobian of each generator's Artin automorphism == U", ok)
random.seed(1)
ok = True
for _ in range(30):
    w = [random.choice([1, -1]) * random.randint(1, 3) for _ in range(random.randint(1, 9))]
    J1 = [fox_row(artin_right(w, 4)[k], 4) for k in range(1, 5)]
    ok &= mat_eq(J1, rep(w, 4, 'U'))
report("(D) 30 random words in B_4: Fox Jacobian of the right Artin action == U product in word order", ok)

# ---------- (E) b is Brunnian ----------
def delete(w, n, d):
    p, o = list(range(1, n + 1)), []
    for a in w:
        k = abs(a)
        if d not in (p[k - 1], p[k]):
            kk = k - 1 if p.index(d) < k - 1 else k
            o.append(kk if a > 0 else -kk)
        p[k - 1], p[k] = p[k], p[k - 1]
    return o
def pure(w, n):
    p = list(range(n))
    for a in w:
        k = abs(a); p[k - 1], p[k] = p[k], p[k - 1]
    return p == list(range(n))
def trivial(w, n): return all(v == [j] for j, v in artin_right(w, n).items())
report("(E) b is pure and nontrivial", pure(b, 4) and not trivial(b, 4))
report("(E) b is Brunnian: deleting each of strands 1..4 gives a trivial braid",
       all(trivial(delete(b, 4, d), 3) for d in (1, 2, 3, 4)))
report("(E) X is not Brunnian (deleting strand 4 leaves (s1 s2)^6 != 1)", not trivial(delete(X, 4, 4), 3))
report("(E) rho(X) = I at t = -1 (U)", is_I_at(rep(X, 4, 'U'), -1))
report("(E) Phi0 is Brunnian", all(trivial(delete(Phi0, 4, d), 3) for d in (1, 2, 3, 4)) and not trivial(Phi0, 4))

fails = [s for s in out if s.startswith('FAIL')]
print(f"\n{len(out) - len(fails)} PASS, {len(fails)} FAIL")
