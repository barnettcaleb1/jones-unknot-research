#!/usr/bin/env python3
# Independent re-derivation (no code shared with phi0_check.py or the reviewer's indep3.py) of the
# (t+1)-adic depth of C = [Phi0, s3 Phi0 s3^-1] in several Burau conventions, B_4 and B_5.
# Two independent depth algorithms:
#   (E) exact Laurent polynomials stored as (low exponent, coefficient list), valuation at t = -1 by
#       Taylor shift t = s - 1 (binomial expansion), not by synthetic division;
#   (P) truncated power series in s = t + 1 (mod s^K), with t^-1 = -(1 + s + s^2 + ...).
from math import comb
import sys, time

# ---------------- braid words (letters: k = sigma_k, -k = sigma_k^-1; products left to right) -----------
def winv(w): return [-a for a in w[::-1]]
def wcomm(x, y): return x + y + winv(x) + winv(y)          # [x, y] = x y x^-1 y^-1
def wred(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return out
def A(i, j):                                               # s_{j-1} .. s_{i+1} s_i^2 s_{i+1}^-1 .. s_{j-1}^-1
    up = list(range(j - 1, i, -1))
    return up + [i, i] + winv(up)
X = [1, 2] * 6
b = wcomm(wcomm(A(1, 4), A(2, 4)), A(3, 4))
Phi0 = wcomm(X, b)
S3P = [3] + Phi0 + [-3]
C = wcomm(Phi0, S3P)
mirror = lambda w: [-a for a in w]

# ---------------- exact Laurent polynomials: (low, [c_low, c_low+1, ...]) ---------------------------------
ZERO = (0, [])
def lnorm(p):
    lo, c = p
    i, j = 0, len(c)
    while i < j and c[i] == 0: i += 1
    while j > i and c[j - 1] == 0: j -= 1
    return (lo + i, c[i:j]) if i < j else ZERO
def ladd(p, q):
    if not p[1]: return q
    if not q[1]: return p
    lo = min(p[0], q[0]); hi = max(p[0] + len(p[1]), q[0] + len(q[1]))
    c = [0] * (hi - lo)
    for k, x in enumerate(p[1]): c[p[0] - lo + k] += x
    for k, x in enumerate(q[1]): c[q[0] - lo + k] += x
    return lnorm((lo, c))
def lmul(p, q):
    if not p[1] or not q[1]: return ZERO
    c = [0] * (len(p[1]) + len(q[1]) - 1)
    for i, x in enumerate(p[1]):
        if x:
            for j, y in enumerate(q[1]): c[i + j] += x * y
    return lnorm((p[0] + q[0], c))
def L(d): return lnorm((min(d), [d.get(e, 0) for e in range(min(d), max(d) + 1)])) if d else ZERO
ONE = L({0: 1})
def val_m1(p):                       # (t+1)-adic valuation by Taylor shift; inf for 0
    if not p[1]: return float('inf')
    c = p[1]                          # t^low is a unit; valuation of the polynomial part
    for m in range(len(c)):
        if sum(x * comb(j, m) * (-1) ** (j - m) for j, x in enumerate(c) if j >= m) != 0: return m
    raise AssertionError

# ---------------- truncated power series in s = t + 1 ---------------------------------------------------
K = 14
def pz(): return [0] * K
def pt(e):                           # t^e as a series in s
    if e >= 0:                       # (s - 1)^e
        return [comb(e, m) * (-1) ** (e - m) if m <= e else 0 for m in range(K)]
    # t^-1 = -1/(1 - s) = -sum s^m ; t^e = (t^-1)^(-e) = (-1)^(-e) sum C(m + |e| - 1, m) s^m
    f = -e
    return [(-1) ** f * comb(m + f - 1, m) for m in range(K)]
def padd(p, q): return [x + y for x, y in zip(p, q)]
def pmul(p, q):
    r = [0] * K
    for i, x in enumerate(p):
        if x:
            for j in range(K - i): r[i + j] += x * q[j]
    return r
def P_from(d):                       # Laurent dict -> series
    r = pz()
    for e, c in d.items(): r = padd(r, [c * x for x in pt(e)])
    return r
def pval(p): return next((k for k, x in enumerate(p) if x), None)

# ---------------- generator matrices as Laurent dicts ----------------------------------------------------
def I_d(m): return [[{0: 1} if i == j else {} for j in range(m)] for i in range(m)]
def U_gen(n, a):                     # BB05 Section 4.2 unreduced
    i = abs(a); M = I_d(n)
    blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]] if a > 0 else [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2): M[i - 1 + r][i - 1 + c] = blk[r][c]
    return M
def BB05red_gen(n, a):               # BB05 reduced: column i -> (-t, -t, -1) in rows i-1, i, i+1 (1-based)
    i = abs(a); M = I_d(n - 1)
    if a > 0: col = {i - 1: {1: -1}, i: {1: -1}, i + 1: {0: -1}}
    else:     col = {i - 1: {0: -1}, i: {-1: -1}, i + 1: {-1: -1}}   # derived by Sherman-Morrison, checked below
    for r, v in col.items():
        if 1 <= r <= n - 1: M[r - 1][i - 1] = v
    return M
def Rrow_gen(n, a):                  # row i -> (t, -t, 1) in cols i-1, i, i+1 (the note's description of R)
    i = abs(a); M = I_d(n - 1)
    if a > 0: row = {i - 1: {1: 1}, i: {1: -1}, i + 1: {0: 1}}
    else:     row = {i - 1: {0: 1}, i: {-1: -1}, i + 1: {-1: 1}}
    for c, v in row.items():
        if 1 <= c <= n - 1: M[i - 1][c - 1] = v
    return M
def transpose(M): return [list(r) for r in zip(*M)]

GENS = {
    'U':        lambda n, a: U_gen(n, a),
    'UT':       lambda n, a: transpose(U_gen(n, a)),
    'R':        lambda n, a: Rrow_gen(n, a),
    'RT':       lambda n, a: transpose(Rrow_gen(n, a)),
    'BB05red':  lambda n, a: BB05red_gen(n, a),
    'U_rtl':    None,   # right-to-left product of U generators (opposite composition order), handled below
}

# exact Laurent matrices
def Lmat(Md): return [[L(x) for x in row] for row in Md]
def lmm(A_, B_):
    m = len(A_)
    out = []
    for i in range(m):
        row = []
        for j in range(m):
            acc = ZERO
            for k in range(m):
                if A_[i][k][1] and B_[k][j][1]: acc = ladd(acc, lmul(A_[i][k], B_[k][j]))
            row.append(acc)
        out.append(row)
    return out
def rep_exact(conv, n, w):
    if conv == 'U_rtl':
        w = w[::-1]; conv = 'U'
    g = GENS[conv]
    m = n - 1 if conv in ('R', 'RT', 'BB05red') else n
    M = [[ONE if i == j else ZERO for j in range(m)] for i in range(m)]
    for a in w: M = lmm(M, Lmat(g(n, a)))
    return M
def depth_exact(M):
    v = [val_m1(ladd(x, L({0: -1}) if i == j else ZERO)) for i, row in enumerate(M) for j, x in enumerate(row)]
    return min(v)
def is_identity_exact(M):
    return all((x == ONE) if i == j else (not x[1]) for i, row in enumerate(M) for j, x in enumerate(row))

# power series matrices
def Pmat(Md): return [[P_from(x) for x in row] for row in Md]
def pmm(A_, B_):
    m = len(A_)
    return [[_dot(A_, B_, i, j, m) for j in range(m)] for i in range(m)]
def _dot(A_, B_, i, j, m):
    r = pz()
    for k in range(m):
        if any(A_[i][k]) and any(B_[k][j]): r = padd(r, pmul(A_[i][k], B_[k][j]))
    return r
_PC = {}
def pgen(conv, n, a):
    key = (conv, n, a)
    if key not in _PC: _PC[key] = Pmat(GENS[conv](n, a))
    return _PC[key]
def rep_ps(conv, n, w):
    if conv == 'U_rtl':
        w = w[::-1]; conv = 'U'
    m = n - 1 if conv in ('R', 'RT', 'BB05red') else n
    M = [[pt(0) if i == j else pz() for j in range(m)] for i in range(m)]
    for a in w: M = pmm(M, pgen(conv, n, a))
    return M
def depth_ps(M):
    v = [pval(padd(x, [-1] + [0] * (K - 1)) if i == j else x) for i, row in enumerate(M) for j, x in enumerate(row)]
    v = [x for x in v if x is not None]
    return min(v) if v else '>=%d' % K

def out(s): print(s); sys.stdout.flush()

# ---------------- sanity: generators are representations, inverses correct ------------------------------
for conv in ('U', 'UT', 'R', 'RT', 'BB05red'):
    for n in (4, 5):
        ok = True
        for i in range(1, n):
            ok &= is_identity_exact(rep_exact(conv, n, [i, -i])) and is_identity_exact(rep_exact(conv, n, [-i, i]))
        for i in range(1, n - 1):
            ok &= rep_exact(conv, n, [i, i + 1, i]) == rep_exact(conv, n, [i + 1, i, i + 1])
        for i in range(1, n):
            for j in range(i + 2, n):
                ok &= rep_exact(conv, n, [i, j]) == rep_exact(conv, n, [j, i])
        out(f'sanity {conv:8} n={n}: inverses and braid relations hold: {ok}')

# BB05 reduced == D * RT * D, D = diag(1,-1,1,...), for every generator
def conjD(M):
    return [[x if (i + j) % 2 == 0 else lmul(L({0: -1}), x) for j, x in enumerate(row)] for i, row in enumerate(M)]
okD = all(Lmat(BB05red_gen(n, a)) == conjD(Lmat(transpose(Rrow_gen(n, a))))
          for n in (3, 4, 5, 6) for i in range(1, n) for a in (i, -i))
out(f'BB05 reduced == diag(1,-1,..) RT diag(1,-1,..) for all s_i^(+-1), n = 3..6: {okD}')

# ---------------- word facts ----------------------------------------------------------------------------
out(f'|Phi0| = {len(Phi0)}, reduced {len(wred(Phi0))}; |C| = {len(C)}, reduced {len(wred(C))}')

# ---------------- exact depths of Phi0 and C in all conventions, B4 and B5 --------------------------------
t0 = time.time()
for n in (4, 5):
    for conv in ('U', 'UT', 'U_rtl', 'R', 'RT', 'BB05red'):
        dP = depth_exact(rep_exact(conv, n, Phi0))
        MC = rep_exact(conv, n, C)
        dC = depth_exact(MC)
        dCm = depth_exact(rep_exact(conv, n, mirror(C)))
        out(f'EXACT B{n} {conv:8}: depth Phi0 = {dP}, depth C = {dC}, depth mirror(C) = {dCm}, C != I: {not is_identity_exact(MC)}')
out(f'(exact part took {time.time() - t0:.1f} s)')

# ---------------- entrywise valuations of U(C) - I and BB05red(C) - I (B4) ---------------------------------
for conv in ('U', 'R', 'BB05red'):
    M = rep_exact(conv, 4, C)
    out(f'valuations of {conv}(C) - I, B4:')
    for i, row in enumerate(M):
        out('   ' + str([val_m1(ladd(x, L({0: -1}) if i == j else ZERO)) for j, x in enumerate(row)]))

# ---------------- structure: U in the basis f_k = e_k - e_{k+1} (k < n), e_n -------------------------------
# row vectors act on the right: v -> v U(g).  Sum-zero row vectors form an invariant submodule.
def change_basis_U(M, n):
    # rows of new matrix = coordinates of (basis vector) * M in the new basis
    basis = []
    for k in range(n - 1):
        v = [ZERO] * n; v[k] = ONE; v[k + 1] = L({0: -1}); basis.append(v)
    v = [ZERO] * n; v[n - 1] = ONE; basis.append(v)
    def coords(w):                   # w = sum_k c_k f_k + c_n e_n ; c_k = w_1 + .. + w_k for k < n, c_n = total sum
        cs, acc = [], ZERO
        for k in range(n - 1):
            acc = ladd(acc, w[k]); cs.append(acc)
        cs.append(ladd(acc, w[n - 1]))
        return cs
    rows = []
    for v in basis:
        w = [ZERO] * n
        for k in range(n):
            if v[k][1]:
                for j in range(n): w[j] = ladd(w[j], lmul(v[k], M[k][j]))
        rows.append(coords(w))
    return rows
MU = rep_exact('U', 4, C)
NB = change_basis_U(MU, 4)
out('U(C) in basis (e1-e2, e2-e3, e3-e4, e4): last column (should be 0,0,0,1 => block triangular):')
out('   ' + str([NB[i][3] for i in range(4)]))
sub = [row[:3] for row in NB[:3]]
cocyc = NB[3][:3]
out(f'   depth of the restriction to sum-zero row vectors = {depth_exact(sub)}; '
    f'valuations of the off-diagonal row c(C) = {[val_m1(x) for x in cocyc]}')
out(f'   restriction == RT(C) exactly: {sub == rep_exact("RT", 4, C)}')

# ---------------- B5 reduced restricted to B4 vs U4 (equivalence over Z[t^+-1]) ---------------------------
# depth check is enough for the claim; also check rank via a change of basis is not attempted here.

# ---------------- iterated commutators, power series ------------------------------------------------------
t0 = time.time()
Ck = C
for k in range(1, 5):
    ds = {conv: depth_ps(rep_ps(conv, 4, Ck)) for conv in ('U', 'UT', 'R', 'RT', 'BB05red')}
    out(f'PS iterated commutator #{k}: |word| = {len(Ck)}, depths B4: {ds}')
    Ck = wred(wcomm(Phi0, Ck))
out(f'(power-series part took {time.time() - t0:.1f} s)')
# power-series and exact agree on Phi0 and C
agree = all(depth_ps(rep_ps(conv, n, w)) == depth_exact(rep_exact(conv, n, w))
            for conv in ('U', 'UT', 'R', 'RT', 'BB05red') for n in (4, 5) for w in (Phi0, C))
out(f'power-series depth == exact depth for Phi0 and C in all conventions, B4 and B5: {agree}')
