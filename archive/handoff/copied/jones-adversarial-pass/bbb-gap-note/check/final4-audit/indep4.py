#!/usr/bin/env python3
"""Independent checks for the final4 audit (shares no code with phi0_check.py).

Laurent polynomials: tuple-free dict {exp: coeff}.  Power series in s = t+1 truncated mod s^N.
Conventions: U (unreduced, block [[1-t,t],[1,0]]), UT (transposes), R (reduced, row i -> (t,-t,1)
in cols i-1,i,i+1), RT (transposes), BB (Birman-Brendle reduced from survey p.46:
I_{i-2} + [[1,-t,0],[0,-t,0],[0,-1,1]] + I_{n-i-2}, -t at (i,i)).
Words: list of nonzero ints, product of matrices taken left to right (and also right to left).
"""
import sys
from fractions import Fraction

# ---------- Laurent polynomials ----------
def L(d): return {e: c for e, c in d.items() if c}
def ladd(a, b):
    r = dict(a)
    for e, c in b.items(): r[e] = r.get(e, 0) + c
    return L(r)
def lneg(a): return {e: -c for e, c in a.items()}
def lmul(a, b):
    r = {}
    for e, c in a.items():
        for f, d in b.items(): r[e+f] = r.get(e+f, 0) + c*d
    return L(r)
ONE = {0: 1}; ZERO = {}
def T(k=1, c=1): return {k: c}

def eye(m): return [[dict(ONE) if i == j else {} for j in range(m)] for i in range(m)]
def matmul(A, B):
    m = len(A)
    C = [[{} for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for k in range(m):
            if not A[i][k]: continue
            for j in range(m):
                if B[k][j]: C[i][j] = ladd(C[i][j], lmul(A[i][k], B[k][j]))
    return C
def transpose(A): return [list(r) for r in zip(*A)]

# 2x2 / 3x3 generator matrices and their inverses, computed by hand and re-verified below
def gen_U(n, i, sgn):
    M = eye(n)
    if sgn > 0: blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]]
    else:       blk = [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2): M[i-1+r][i-1+c] = blk[r][c]
    return M
def gen_R(n, i, sgn):
    # row i (1-based) of I_{n-1} replaced by (t,-t,1) in cols i-1,i,i+1; inverse computed generically below
    M = eye(n-1)
    r = i-1
    vals = [({1: 1}, r-1), ({1: -1}, r), ({0: 1}, r+1)]
    for v, c in vals:
        if 0 <= c < n-1: M[r][c] = v
    return M
def gen_BB(n, i, sgn):
    M = eye(n-1)
    # block rows/cols (i-1, i, i+1) in 1-based -> 0-based i-2, i-1, i
    blk = [[{0: 1}, {1: -1}, {}], [{}, {1: -1}, {}], [{}, {0: -1}, {0: 1}]]
    for a in range(3):
        for b in range(3):
            rr, cc = i-2+a, i-2+b
            if 0 <= rr < n-1 and 0 <= cc < n-1:
                M[rr][cc] = blk[a][b]
    return M

def inverse_laurent(M):
    """Inverse of a unimodular-ish Laurent matrix via Gauss-Jordan over Q(t) restricted: we instead
    verify candidate inverse by multiplication; candidate obtained by solving at symbolic level
    using the fact that each generator differs from I in one row (R) or one column (RT)."""
    raise NotImplementedError

def row_gen_inverse(M, r):
    """M = I except row r. For such M with M[r][r] = u a unit monomial, inverse is I except row r:
    inv[r][r] = 1/u, inv[r][c] = -M[r][c]/u for c != r."""
    m = len(M)
    u = M[r][r]
    assert len(u) == 1
    (e, c), = u.items(); assert c in (1, -1)
    uinv = {-e: c}
    N = eye(m)
    for cc in range(m):
        if cc == r: N[r][cc] = uinv
        elif M[r][cc]: N[r][cc] = lneg(lmul(M[r][cc], uinv))
    return N

def col_gen_inverse(M, cidx):
    return transpose(row_gen_inverse(transpose(M), cidx))

def gens(conv, n):
    G = {}
    for i in range(1, n):
        if conv in ('U', 'UT'):
            P, Q = gen_U(n, i, 1), gen_U(n, i, -1)
            if conv == 'UT': P, Q = transpose(P), transpose(Q)
        elif conv in ('R', 'RT'):
            P = gen_R(n, i, 1); Q = row_gen_inverse(P, i-1)
            if conv == 'RT': P, Q = transpose(P), transpose(Q)
        elif conv == 'BB':
            P = gen_BB(n, i, 1); Q = col_gen_inverse(P, i-1)
        G[i], G[-i] = P, Q
        m = len(P)
        assert matmul(P, Q) == eye(m) and matmul(Q, P) == eye(m), (conv, n, i)
    return G

def word_mat(w, G, m, order='LR'):
    M = eye(m)
    seq = w if order == 'LR' else list(reversed(w))
    for a in seq: M = matmul(M, G[a])
    return M

def is_eye(M): return M == eye(len(M))
def sub_eye(M): return [[ladd(p, {0: -1} if i == j else {}) for j, p in enumerate(r)] for i, r in enumerate(M)]
def scal(p, M): return [[lmul(p, x) for x in r] for r in M]

# ---------- power series in s = t + 1, mod s^N ----------
N = 14
def ps_from_laurent(p):
    # t = s - 1 ; t^{-1} = -(1 + s + s^2 + ...)
    tpos = [-1, 1] + [0]*(N-2)
    tneg = [-1]*N
    def psmul(a, b):
        r = [0]*N
        for i, x in enumerate(a):
            if x:
                for j in range(N-i):
                    if b[j]: r[i+j] += x*b[j]
        return r
    def pspow(base, k):
        r = [1] + [0]*(N-1)
        for _ in range(k): r = psmul(r, base)
        return r
    out = [0]*N
    for e, c in p.items():
        term = pspow(tpos, e) if e >= 0 else pspow(tneg, -e)
        for i in range(N): out[i] += c*term[i]
    return out
def psmul(a, b):
    r = [0]*N
    for i, x in enumerate(a):
        if x:
            for j in range(N-i):
                if b[j]: r[i+j] += x*b[j]
    return r
def psadd(a, b): return [x+y for x, y in zip(a, b)]
def ps_eye(m): return [[[1 if (i == j and k == 0) else 0 for k in range(N)] for j in range(m)] for i in range(m)]
def ps_matmul(A, B):
    m = len(A)
    C = [[[0]*N for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for k in range(m):
            a = A[i][k]
            if not any(a): continue
            for j in range(m):
                C[i][j] = psadd(C[i][j], psmul(a, B[k][j]))
    return C
def ps_mat(M): return [[ps_from_laurent(p) for p in r] for r in M]
def ps_word(w, PG, m, order='LR'):
    M = ps_eye(m)
    seq = w if order == 'LR' else list(reversed(w))
    for a in seq: M = ps_matmul(M, PG[a])
    return M
def ps_depth(M):
    m = len(M); best = N
    for i in range(m):
        for j in range(m):
            v = list(M[i][j])
            if i == j: v[0] -= 1
            for k in range(N):
                if v[k]:
                    best = min(best, k); break
    return best  # N means "at least N"

# ---------- free group / Artin action (own implementation) ----------
def finv(w): return [-a for a in reversed(w)]
def fred(w):
    s = []
    for a in w:
        if s and s[-1] == -a: s.pop()
        else: s.append(a)
    return s
def fcomm(x, y): return x + y + finv(x) + finv(y)
def artin_images(w, n):
    # right action: s_i: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i ; inverse: x_i -> x_{i+1}, x_{i+1} -> x_{i+1}^-1 x_i x_{i+1}
    im = {k: [k] for k in range(1, n+1)}
    for a in w:
        i = abs(a)
        if a > 0: rule = {i: [i, i+1, -i], i+1: [i]}
        else:     rule = {i: [i+1], i+1: [-(i+1), i, i+1]}
        for k in im:
            out = []
            for c in im[k]:
                r = rule.get(abs(c), [abs(c)])
                out += r if c > 0 else finv(r)
            im[k] = fred(out)
    return im
def same_braid(u, v, n): return artin_images(u, n) == artin_images(v, n)

# ---------- the braids ----------
A14 = [3, 2, 1, 1, -2, -3]; A24 = [3, 2, 2, -3]; A34 = [3, 3]
X = [1, 2]*6
b = fcomm(fcomm(A14, A24), A34)
Phi0 = fcomm(X, b)
s3c = [3] + Phi0 + [-3]
D3 = [1, 2, 1]; D3sq = D3 + D3; D4 = [1, 2, 3, 1, 2, 1]; D4sq = D4 + D4

res = []
def rec(name, ok):
    res.append((name, ok)); print(('OK   ' if ok else 'BAD  ') + name)

# Garside: Delta_3 = s1 s2 s1, Delta_3^2 = (s1 s2)^3, Delta_3^4 = X, Delta_4^2 = (s1 s2 s3)^4
rec("Delta_3^2 == (s1 s2)^3", same_braid(D3sq, [1, 2]*3, 3))
rec("Delta_3 == s2 s1 s2 (Garside positive half twist on 3 strands)", same_braid(D3, [2, 1, 2], 3))
rec("X == Delta_3^4", same_braid(X, D3sq*2, 4))
rec("Delta_4^2 == (s1 s2 s3)^4", same_braid(D4sq, [1, 2, 3]*4, 4))
rec("Delta_3^-2 Delta_4^2 == A14 A24 A34", same_braid(finv(D3sq) + D4sq, A14 + A24 + A34, 4))
# 28-letter word in a-basis: b = [[a1,a2],a3], delta = a1 a2 a3, Phi0 = [delta^-2, b]
delta_a = [1, 2, 3]; b_a = fcomm(fcomm([1], [2]), [3])
kw = fred(fcomm(finv(delta_a)*2, b_a))
rec(f"[delta^-2, b] in a-basis: {len(kw)} letters, exponent sums {[sum((c==i)-(c==-i) for c in kw) for i in (1,2,3)]}",
    len(kw) == 28 and all(sum((c == i) - (c == -i) for c in kw) == 0 for i in (1, 2, 3)))
delta_w = finv(D3sq) + D4sq
rec("Phi0 == [delta^-2, b] as braids", same_braid(Phi0, fcomm(finv(delta_w)*2, b), 4))

# BB05 = D RT D with alternating D, n = 3..6; and fails with non-alternating for n = 5
for n in range(3, 7):
    GRT = gens('RT', n); GBB = gens('BB', n)
    m = n-1
    Dalt = [[{0: (-1)**i} if i == j else {} for j in range(m)] for i in range(m)]
    ok = all(matmul(matmul(Dalt, GRT[a]), Dalt) == GBB[a] for a in GRT)
    Dnon = [[{0: (-1 if i == 1 else 1)} if i == j else {} for j in range(m)] for i in range(m)]
    ok2 = all(matmul(matmul(Dnon, GRT[a]), Dnon) == GBB[a] for a in GRT)
    rec(f"n={n}: diag(1,-1,1,-1,..) RT diag(..) == BB05 reduced: {ok}; with diag(1,-1,1,1,..): {ok2}", ok and (ok2 == (n <= 4)))

# braid relations for all conventions, n = 4, 5
for n in (4, 5):
    for conv in ('U', 'UT', 'R', 'RT', 'BB'):
        G = gens(conv, n); m = len(G[1])
        ok = True
        for i in range(1, n-1):
            ok &= word_mat([i, i+1, i], G, m) == word_mat([i+1, i, i+1], G, m)
        for i in range(1, n):
            for j in range(i+2, n):
                ok &= word_mat([i, j], G, m) == word_mat([j, i], G, m)
        rec(f"braid relations B_{n} {conv}", ok)

# Prop 4(b) identity, exact, in all conventions; mirror and t -> 1/t versions
def tinv(M): return [[{-e: c for e, c in p.items()} for p in r] for r in M]
for conv in ('U', 'UT', 'R', 'RT', 'BB'):
    G = gens(conv, 4); m = len(G[1])
    MX, MD = word_mat(X, G, m), word_mat(D3sq, G, m)
    ok1 = sub_eye(MX) == scal({0: 1, 3: 1}, sub_eye(MD))
    ok1b = sub_eye(MX) != scal({0: 1, -3: 1}, sub_eye(MD))
    mir = lambda w: [-a for a in w]
    MXm, MDm = word_mat(mir(X), G, m), word_mat(mir(D3sq), G, m)
    ok2 = sub_eye(MXm) == scal({0: 1, -3: 1}, sub_eye(MDm))
    ok3 = sub_eye(tinv(MX)) == scal({0: 1, -3: 1}, sub_eye(tinv(MD)))
    # also with the product taken right to left
    MXr, MDr = word_mat(X, G, m, 'RL'), word_mat(D3sq, G, m, 'RL')
    ok4 = sub_eye(MXr) == scal({0: 1, 3: 1}, sub_eye(MDr))
    rec(f"Prop4(b) {conv}: (1+t^3) identity {ok1}, not with 1+t^-3 {ok1b}, mirror 1+t^-3 {ok2}, t->1/t {ok3}, RL order {ok4}",
        ok1 and ok1b and ok2 and ok3 and ok4)
    # (t+1) | 1+t^3 so at t=-1 identity
    at_m1 = all(sum(c*(-1)**e for e, c in p.items()) == (1 if i == j else 0) for i, r in enumerate(MX) for j, p in enumerate(r))
    rec(f"rho(X) = I at t=-1 in {conv}", at_m1)

# depths via power series
def depths(conv, order='LR', n=4):
    G = gens(conv, n); m = len(G[1])
    PG = {a: ps_mat(M) for a, M in G.items()}
    P = ps_word(Phi0, PG, m, order); Pi = ps_word(finv(Phi0), PG, m, order)
    Q = ps_word(s3c, PG, m, order); Qi = ps_word(finv(s3c), PG, m, order)
    out = [ps_depth(P)]
    # C1 = [Phi0, s3c], C_{k+1} = [Phi0, C_k]
    C = ps_matmul(ps_matmul(ps_matmul(P, Q), Pi), Qi)
    Ci = ps_matmul(ps_matmul(ps_matmul(Q, P), Qi), Pi)    # (x y x^-1 y^-1)^-1 = y x y^-1 x^-1
    cd = [ps_depth(C)]
    for _ in range(3):
        C, Ci = ps_matmul(ps_matmul(ps_matmul(P, C), Pi), Ci), ps_matmul(ps_matmul(ps_matmul(C, P), Ci), Pi)
        cd.append(ps_depth(C))
    # noncommutation of images
    nc = ps_matmul(P, Q) != ps_matmul(Q, P)
    return out[0], cd, nc

for order in ('LR', 'RL'):
    for conv in ('U', 'UT', 'R', 'RT', 'BB'):
        d0, cd, nc = depths(conv, order)
        print(f"   {order} {conv:2}: depth(Phi0)={d0}  depths of C1..C4 = {cd}  images noncommute (mod s^{N}): {nc}")
        exp_cd = [2, 4, 6, 8] if conv in ('U', 'UT') else [3, 4, 6, 8]
        rec(f"{order} {conv}: depth Phi0 = 1, commutator depths {cd} == {exp_cd}", d0 == 1 and cd == exp_cd and nc)
for conv in ('U', 'UT', 'R', 'RT', 'BB'):
    d0, cd, nc = depths(conv, 'LR', n=5)
    print(f"   B5 {conv:2}: depth f(Phi0)={d0}  depths of f(C1..C4) = {cd}")

# exact check of the commutator depth claim in all four conventions (exact Laurent, product left to right)
def mult_root_m1(p):
    lo, hi = min(p), max(p)
    c = [p.get(e, 0) for e in range(lo, hi+1)]
    k = 0
    while sum(x*(-1)**i for i, x in enumerate(c)) == 0:
        # synthetic division by (t+1): c is low->high coefficients
        q = [0]*(len(c)-1)
        rem = 0
        hc = c[::-1]  # high -> low
        out = []
        acc = 0
        for x in hc:
            acc = x - acc
            out.append(acc)
        # out[-1] is remainder (should be 0)
        assert out[-1] == 0
        c = out[:-1][::-1]
        k += 1
    return k
for conv in ('U', 'UT', 'R', 'RT'):
    G = gens(conv, 4); m = len(G[1])
    C = word_mat(fcomm(Phi0, s3c), G, m)
    D = sub_eye(C)
    dd = min(mult_root_m1(p) for r in D for p in r if p)
    rec(f"exact depth of [Phi0, s3 Phi0 s3^-1] in {conv} = {dd}", dd == (2 if conv[0] == 'U' else 3))

print("\nSUMMARY:", sum(ok for _, ok in res), "OK,", sum(not ok for _, ok in res), "BAD")
sys.exit(0 if all(ok for _, ok in res) else 1)
