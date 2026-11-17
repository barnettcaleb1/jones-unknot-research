#!/usr/bin/env python3
"""final3 'script' lens: independent re-derivation of the NEW claims in phi0_check.py / the appendix.

Written from scratch.  Does NOT import or exec phi0_check.py (its source is only read as text,
and only the literal Section 7 lists are parsed with ast.literal_eval, to compare transcriptions).

Design choices that differ from phi0_check.py:
  * braid words are lists of (index, sign) pairs; free reduction by repeated scans;
  * one generic matrix builder over three different rings:
      LP  exact Laurent polynomials stored as (lowest exponent, coefficient list);
      PS  truncated power series Z[s]/(s^K) with t = s - 1 (depth = s-adic valuation of M - I);
      QQ  rationals, t a fixed Fraction;
  * generator inverses are NOT hard-coded: they are computed by an explicit adjugate formula
    for the 2x2 block (U) and checked by multiplication; for R the inverse row is derived and checked.
"""
from fractions import Fraction as Fr
import ast, re, random, sys, os

OUT = []
def report(tag, ok, detail=''):
    line = ('OK   ' if ok else 'BAD  ') + tag + (('  [' + detail + ']') if detail else '')
    print(line); OUT.append((tag, ok))

# ------------------------------------------------------------------ words
def letter(i, e=1): return [(i, e)]
def winv(w): return [(i, -e) for (i, e) in reversed(w)]
def wcomm(x, y): return x + y + winv(x) + winv(y)
def wred(w):
    w = list(w)
    changed = True
    while changed:
        changed = False
        for k in range(len(w) - 1):
            if w[k][0] == w[k + 1][0] and w[k][1] == -w[k + 1][1]:
                del w[k:k + 2]; changed = True; break
    return w
def W(*ints): return [(abs(a), 1 if a > 0 else -1) for a in ints]
def mirror(w): return [(i, -e) for (i, e) in w]

s1, s2, s3 = W(1), W(2), W(3)
A14 = s3 + s2 + s1 + s1 + winv(s2) + winv(s3)
A24 = s3 + s2 + s2 + winv(s3)
A34 = s3 + s3
X = (s1 + s2) * 6
D3sq = (s1 + s2) * 3
b = wcomm(wcomm(A14, A24), A34)
Phi0 = wcomm(X, b)
Phi0r = wred(Phi0)
conj3 = s3 + Phi0r + winv(s3)
C = wred(wcomm(Phi0r, conj3))                 # [Phi0, s3 Phi0 s3^-1]
report('word lengths 112 / 76 / commutator reduced length', len(Phi0) == 112 and len(Phi0r) == 76, f'{len(Phi0)}, {len(Phi0r)}, |C|={len(C)}')

# ------------------------------------------------------------------ rings
class LP:                                      # exact Laurent polynomial
    __slots__ = ('lo', 'c')
    def __init__(self, lo, c):
        while c and c[-1] == 0: c = c[:-1]
        k = 0
        while k < len(c) and c[k] == 0: k += 1
        self.c = list(c[k:]); self.lo = (lo + k) if self.c else 0
    @staticmethod
    def mono(coef, e): return LP(e, [coef])
    def __add__(self, o):
        if not self.c: return o
        if not o.c: return self
        lo = min(self.lo, o.lo); hi = max(self.lo + len(self.c), o.lo + len(o.c))
        r = [0] * (hi - lo)
        for k, x in enumerate(self.c): r[self.lo - lo + k] += x
        for k, x in enumerate(o.c): r[o.lo - lo + k] += x
        return LP(lo, r)
    def __neg__(self): return LP(self.lo, [-x for x in self.c])
    def __sub__(self, o): return self + (-o)
    def __mul__(self, o):
        if not self.c or not o.c: return LP(0, [])
        r = [0] * (len(self.c) + len(o.c) - 1)
        for i, x in enumerate(self.c):
            if x:
                for j, y in enumerate(o.c): r[i + j] += x * y
        return LP(self.lo + o.lo, r)
    def __eq__(self, o): return self.lo == o.lo and self.c == o.c
    def iszero(self): return not self.c
    def flip(self):                            # t -> 1/t
        return LP(-(self.lo + len(self.c) - 1), list(reversed(self.c)))
    def mult_minus1(self):                     # multiplicity of the root t = -1, via repeated division
        c, k = list(self.c), 0
        assert c
        while True:
            # Horner at -1
            v = 0
            for x in reversed(c): v = v * (-1) + x
            if v != 0: return k
            # divide by (t + 1): long division from the top
            q = [0] * (len(c) - 1); rem = list(c)
            for d in range(len(c) - 1, 0, -1):
                q[d - 1] = rem[d]; rem[d - 1] -= rem[d]; rem[d] = 0
            assert rem[0] == 0
            c, k = q, k + 1

class RingLP:
    def one(self): return LP(0, [1])
    def zero(self): return LP(0, [])
    def t(self): return LP(1, [1])
    def ti(self): return LP(-1, [1])
    def c(self, k): return LP(0, [k])
class RingPS:                                  # Z[s]/(s^K), t = s - 1
    def __init__(self, K): self.K = K
    def one(self): return tuple([1] + [0] * (self.K - 1))
    def zero(self): return tuple([0] * self.K)
    def t(self): return tuple([-1, 1] + [0] * (self.K - 2))
    def ti(self): return tuple([-1] * self.K)  # 1/(s-1) = -(1 + s + s^2 + ...)
    def c(self, k): return tuple([k] + [0] * (self.K - 1))
class RingQ:
    def __init__(self, t0): self.t0 = Fr(t0)
    def one(self): return Fr(1)
    def zero(self): return Fr(0)
    def t(self): return self.t0
    def ti(self): return 1 / self.t0
    def c(self, k): return Fr(k)

def radd(R, a, b):
    if isinstance(R, RingPS): return tuple(x + y for x, y in zip(a, b))
    return a + b
def rneg(R, a):
    if isinstance(R, RingPS): return tuple(-x for x in a)
    return -a
def rmul(R, a, b):
    if isinstance(R, RingPS):
        K = R.K; r = [0] * K
        for i, x in enumerate(a):
            if x:
                for j in range(K - i): r[i + j] += x * b[j]
        return tuple(r)
    return a * b
def rzero(R, a):
    if isinstance(R, RingPS): return not any(a)
    if isinstance(R, RingLP): return a.iszero()
    return a == 0

def mat_id(R, m): return [[R.one() if i == j else R.zero() for j in range(m)] for i in range(m)]
def mat_mul(R, A, B):
    m = len(A); out = []
    for i in range(m):
        row = []
        for j in range(m):
            acc = R.zero()
            for k in range(m):
                if not rzero(R, A[i][k]) and not rzero(R, B[k][j]):
                    acc = radd(R, acc, rmul(R, A[i][k], B[k][j]))
            row.append(acc)
        out.append(row)
    return out
def mat_T(M): return [list(r) for r in zip(*M)]
def mat_sub_I(R, M):
    return [[radd(R, x, rneg(R, R.one())) if i == j else x for j, x in enumerate(row)] for i, row in enumerate(M)]
def mat_isI(R, M): return all(rzero(R, x) for row in mat_sub_I(R, M) for x in row)
def mat_eq(R, A, B): return all(rzero(R, radd(R, x, rneg(R, y))) for ra, rb in zip(A, B) for x, y in zip(ra, rb))

# ------------------------------------------------------------------ generators
def gen_U(R, n, i, e):
    M = mat_id(R, n); a = i - 1
    one, t, ti = R.one(), R.t(), R.ti()
    if e > 0:
        blk = [[radd(R, one, rneg(R, t)), t], [one, R.zero()]]
    else:
        # inverse of [[1-t, t],[1, 0]] by the adjugate formula: det = -t, inverse = (1/det) [[0, -t], [-1, 1-t]]
        mdi = rneg(R, ti)                        # 1/det = -1/t
        blk = [[R.zero(), rmul(R, mdi, rneg(R, t))],
               [rmul(R, mdi, rneg(R, one)), rmul(R, mdi, radd(R, one, rneg(R, t)))]]
    for r in range(2):
        for c in range(2): M[a + r][a + c] = blk[r][c]
    return M
def gen_R(R, n, i, e):
    M = mat_id(R, n - 1); r = i - 1
    t, ti = R.t(), R.ti()
    vals = (t, rneg(R, t), R.one()) if e > 0 else (R.one(), rneg(R, ti), ti)
    for c, v in zip((r - 1, r, r + 1), vals):
        if 0 <= c <= n - 2: M[r][c] = v
    return M
def gen_BB05(R, n, i, e):                      # survey p. 46: I_{i-2} + [[1,-t,0],[0,-t,0],[0,-1,1]] + I_{n-i-2}, -t at (i,i)
    assert e > 0
    M = mat_id(R, n - 1); a = i - 1             # 0-based position of the (i,i) entry
    t = R.t()
    blk = [[R.one(), rneg(R, t), R.zero()], [R.zero(), rneg(R, t), R.zero()], [R.zero(), rneg(R, R.one()), R.one()]]
    for rr in range(3):
        for cc in range(3):
            r_, c_ = a - 1 + rr, a - 1 + cc
            if 0 <= r_ <= n - 2 and 0 <= c_ <= n - 2: M[r_][c_] = blk[rr][cc]
    return M
def gen(R, conv, n, i, e):
    if conv == 'U': return gen_U(R, n, i, e)
    if conv == 'UT': return mat_T(gen_U(R, n, i, e))
    if conv == 'R': return gen_R(R, n, i, e)
    if conv == 'RT': return mat_T(gen_R(R, n, i, e))
    raise ValueError(conv)
def rep(R, conv, n, w):
    M = mat_id(R, n - (conv[0] == 'R'))
    for (i, e) in w: M = mat_mul(R, M, gen(R, conv, n, i, e))
    return M
CONVS = ('U', 'UT', 'R', 'RT')
LPR = RingLP()

# sanity: generator inverses and braid relations, n = 3..6, all conventions, exact
ok = True
for n in (3, 4, 5, 6):
    for conv in CONVS:
        m = n - (conv[0] == 'R')
        for i in range(1, n):
            ok &= mat_isI(LPR, mat_mul(LPR, gen(LPR, conv, n, i, 1), gen(LPR, conv, n, i, -1)))
            ok &= mat_isI(LPR, mat_mul(LPR, gen(LPR, conv, n, i, -1), gen(LPR, conv, n, i, 1)))
        for i in range(1, n - 1):
            ok &= mat_eq(LPR, rep(LPR, conv, n, W(i, i + 1, i)), rep(LPR, conv, n, W(i + 1, i, i + 1)))
        for i in range(1, n):
            for j in range(i + 2, n):
                ok &= mat_eq(LPR, rep(LPR, conv, n, W(i, j)), rep(LPR, conv, n, W(j, i)))
report('own generators: inverses and all braid relations hold, n = 3..6, U UT R RT', ok)

# ------------------------------------------------------------------ claim: Fox Jacobian per letter (own Fox code, own Artin images)
def artin_letter(i, e):                        # images under the automorphism of one letter (as in the docstring)
    if e > 0: return {i: [(i, 1), (i + 1, 1), (i, -1)], i + 1: [(i, 1)]}
    return {i: [(i + 1, 1)], i + 1: [(i + 1, -1), (i, 1), (i + 1, 1)]}
def fox_row(word, n):                          # d word / d x_k, abelianised x_j -> t, as LP
    row = [LP(0, []) for _ in range(n)]
    pref = 0
    for (j, e) in word:
        if e > 0: row[j - 1] = row[j - 1] + LP.mono(1, pref); pref += 1
        else: pref -= 1; row[j - 1] = row[j - 1] + LP.mono(-1, pref)
    return row
ok = True
for n in (3, 4, 5, 6):
    for i in range(1, n):
        for e in (1, -1):
            img = {k: [(k, 1)] for k in range(1, n + 1)}; img.update(artin_letter(i, e))
            J = [fox_row(img[k], n) for k in range(1, n + 1)]
            ok &= mat_eq(LPR, J, gen(LPR, 'U', n, i, e))
report('per-letter Fox Jacobian of the Artin automorphism == U(s_i^{+-1}), n = 3..6', ok)

# ------------------------------------------------------------------ claim: Phi0 != I at t = 1/2, 1/3 (and 2, 3), = I at -1, B4 and B5
ok_m1, ok_ne = True, True
for n in (4, 5):
    for conv in CONVS:
        for t0 in (Fr(-1),):
            ok_m1 &= mat_isI(RingQ(t0), rep(RingQ(t0), conv, n, Phi0))
        for t0 in (Fr(2), Fr(1, 2), Fr(3), Fr(1, 3)):
            Rq = RingQ(t0)
            ok_ne &= not mat_isI(Rq, rep(Rq, conv, n, Phi0))
            ok_ne &= not mat_isI(Rq, rep(Rq, conv, n, Phi0r))
report('Burau(Phi0) = I at t = -1 (B4, B5; U UT R RT; rational evaluation)', ok_m1)
report('Burau(Phi0) != I at t = 2, 1/2, 3, 1/3 (B4, B5; U UT R RT; unreduced and reduced word)', ok_ne)
# opposite orientation directly: the mirror word at t = 2, 3 (equivalent to Phi0 at 1/2, 1/3)
ok = all(not mat_isI(RingQ(t0), rep(RingQ(t0), conv, n, mirror(Phi0)))
         for n in (4, 5) for conv in CONVS for t0 in (Fr(2), Fr(3), Fr(1, 2), Fr(1, 3)))
report('mirror(Phi0) != I at t = 2, 3, 1/2, 1/3 as well', ok)

# ------------------------------------------------------------------ depth via power series (t = s - 1), K = 7
PS = RingPS(7)
def depth_ps(M):
    D = mat_sub_I(PS, M)
    vals = [next((k for k, x in enumerate(e) if x), None) for row in D for e in row]
    vals = [v for v in vals if v is not None]
    return min(vals) if vals else '>=%d' % PS.K
def depth_lp(M):
    D = mat_sub_I(LPR, M)
    vals = [e.mult_minus1() for row in D for e in row if not e.iszero()]
    return min(vals) if vals else float('inf')
dep = {}
for n in (4, 5):
    for conv in CONVS:
        dep[(n, conv, 'Phi0')] = depth_ps(rep(PS, conv, n, Phi0))
        dep[(n, conv, 'C')] = depth_ps(rep(PS, conv, n, C))
        dep[(n, conv, 'mirrorC')] = depth_ps(rep(PS, conv, n, mirror(C)))
report('depth(Phi0) == 1 in B4/B5, all conventions (power series)', all(dep[(n, c, 'Phi0')] == 1 for n in (4, 5) for c in CONVS),
       ', '.join(f'{n}{c}:{dep[(n, c, "Phi0")]}' for n in (4, 5) for c in CONVS))
report('depth([Phi0, s3 Phi0 s3^-1]) == 2 in B4/B5, all conventions (power series)',
       all(dep[(n, c, 'C')] == 2 for n in (4, 5) for c in CONVS),
       ', '.join(f'{n}{c}:{dep[(n, c, "C")]}' for n in (4, 5) for c in CONVS))
report('depth of the mirror commutator == 2 as well', all(dep[(n, c, 'mirrorC')] == 2 for n in (4, 5) for c in CONVS))
UC = rep(LPR, 'U', 4, C)
dC_lp = depth_lp(UC)
report('depth([Phi0, s3 Phi0 s3^-1]) in U, exact Laurent + repeated division', dC_lp == 2, f'found {dC_lp}')
report('[Phi0, s3 Phi0 s3^-1] is nontrivial (U image != I exactly, and != I at t = 2)',
       not mat_isI(LPR, UC) and not mat_isI(RingQ(2), rep(RingQ(2), 'U', 4, C)))
# commutator of the matrices, computed from the matrices themselves (not from the word) -> same depth
P = rep(LPR, 'U', 4, Phi0r); Q = rep(LPR, 'U', 4, conj3)
Pi = rep(LPR, 'U', 4, winv(Phi0r)); Qi = rep(LPR, 'U', 4, winv(conj3))
report('U(Phi0) U(s3 Phi0 s3^-1) != U(s3 Phi0 s3^-1) U(Phi0)', not mat_eq(LPR, mat_mul(LPR, P, Q), mat_mul(LPR, Q, P)))
CM = mat_mul(LPR, mat_mul(LPR, mat_mul(LPR, P, Q), Pi), Qi)
report('matrix commutator equals U(word commutator) exactly', mat_eq(LPR, CM, UC))
# depth >= 2 is forced: P = I + (t+1)A, Q = I + (t+1)B  =>  [P,Q] = I + (t+1)^2 (...) ; exactly 2 means AB - BA != 0 mod (t+1)
# check: the leading term (AB - BA) at t = -1 is nonzero, computed in the power-series ring
P_ps, Q_ps = rep(PS, 'U', 4, Phi0r), rep(PS, 'U', 4, conj3)
A1 = [[x[1] for x in row] for row in mat_sub_I(PS, P_ps)]   # coefficient of s^1
B1 = [[x[1] for x in row] for row in mat_sub_I(PS, Q_ps)]
A0 = [[x[0] for x in row] for row in mat_sub_I(PS, P_ps)]
B0 = [[x[0] for x in row] for row in mat_sub_I(PS, Q_ps)]
mm = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
comm1 = [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(mm(A1, B1), mm(B1, A1))]
report('first-order terms: (P - I), (Q - I) vanish at t=-1 and their s^1 parts do not commute',
       all(x == 0 for r in A0 + B0 for x in r) and any(x for r in comm1 for x in r))

# ------------------------------------------------------------------ claim (11): identities, both orientations, exact
def scal(R, p, M): return [[rmul(R, p, x) for x in row] for row in M]
f_plus = LP(0, [1, 0, 0, 1])        # 1 + t^3
f_minus = LP(-3, [1, 0, 0, 1])      # t^-3 + 1
ok_p, ok_m, ok_cross = True, True, True
for conv in CONVS:
    UX, UD = rep(LPR, conv, 4, X), rep(LPR, conv, 4, D3sq)
    ok_p &= mat_eq(LPR, mat_sub_I(LPR, UX), scal(LPR, f_plus, mat_sub_I(LPR, UD)))
    mX, mD = rep(LPR, conv, 4, mirror(X)), rep(LPR, conv, 4, mirror(D3sq))
    ok_m &= mat_eq(LPR, mat_sub_I(LPR, mX), scal(LPR, f_minus, mat_sub_I(LPR, mD)))
    ok_cross &= not mat_eq(LPR, mat_sub_I(LPR, mX), scal(LPR, f_plus, mat_sub_I(LPR, mD)))
report('rho(X) - I == (1 + t^3)(rho(D3^2) - I), U UT R RT', ok_p)
report('mirror words: rho - I == (1 + t^-3)(...), U UT R RT', ok_m)
report('mirror words: the (1 + t^3) version is FALSE (so the mirror check has teeth)', ok_cross)
# also B5
ok5 = all(mat_eq(LPR, mat_sub_I(LPR, rep(LPR, c, 5, mirror(X))), scal(LPR, f_minus, mat_sub_I(LPR, rep(LPR, c, 5, mirror(D3sq))))) for c in CONVS)
report('mirror identity also holds in B5 (not claimed; extra)', ok5)

# ------------------------------------------------------------------ mirror == t -> 1/t up to conjugation by rep(Delta)^-1 J, exact, n = 4, 5
def flipM(M): return [[x.flip() for x in row] for row in M]
def Jm(m): return [[LP(0, [1]) if i + j == m - 1 else LP(0, []) for j in range(m)] for i in range(m)]
def Delta(n):
    w = []
    for k in range(n - 1, 0, -1): w += W(*range(1, k + 1))
    return w
random.seed(20261103)
ok = True
for n in (4, 5):
    for conv in CONVS:
        m = n - (conv[0] == 'R')
        Dl, Dli, J = rep(LPR, conv, n, Delta(n)), rep(LPR, conv, n, winv(Delta(n))), Jm(m)
        words = [Phi0r, X, D3sq, b] + [[(random.randint(1, n - 1), random.choice((1, -1))) for _ in range(12)] for _ in range(8)]
        for w in words:
            lhs = rep(LPR, conv, n, mirror(w))
            rhs = mat_mul(LPR, mat_mul(LPR, mat_mul(LPR, Dli, J), flipM(rep(LPR, conv, n, w))), mat_mul(LPR, J, Dl))
            ok &= mat_eq(LPR, lhs, rhs)
report('rep(mirror w)(t) == rep(Delta)^-1 J rep(w)(1/t) J rep(Delta), U UT R RT, n = 4, 5 (conjugator invertible over Z[t,1/t])', ok)

# ------------------------------------------------------------------ BB05 reduced form == diag(1,-1,1,..) R^T diag(1,-1,1,..)
def Dsign(m): return [[LP(0, [(-1) ** i]) if i == j else LP(0, []) for j in range(m)] for i in range(m)]
ok = True
for n in (3, 4, 5, 6):
    Ds = Dsign(n - 1)
    for i in range(1, n):
        lhs = gen_BB05(LPR, n, i, 1)
        rhs = mat_mul(LPR, mat_mul(LPR, Ds, mat_T(gen_R(LPR, n, i, 1))), Ds)
        ok &= mat_eq(LPR, lhs, rhs)
        # inverse letter: BB05(s_i) * (D R(s_i^-1)^T D) == I
        rinv = mat_mul(LPR, mat_mul(LPR, Ds, mat_T(gen_R(LPR, n, i, -1))), Ds)
        ok &= mat_isI(LPR, mat_mul(LPR, lhs, rinv))
    # BB05 matrices satisfy the braid relations
    def bb(w):
        M = mat_id(LPR, n - 1)
        for (i, e) in w:
            g = gen_BB05(LPR, n, i, 1) if e > 0 else mat_mul(LPR, mat_mul(LPR, Ds, mat_T(gen_R(LPR, n, i, -1))), Ds)
            M = mat_mul(LPR, M, g)
        return M
    for i in range(1, n - 1): ok &= mat_eq(LPR, bb(W(i, i + 1, i)), bb(W(i + 1, i, i + 1)))
    for i in range(1, n):
        for j in range(i + 2, n): ok &= mat_eq(LPR, bb(W(i, j)), bb(W(j, i)))
report('BB05 reduced matrices == diag(1,-1,..) R^T diag(1,-1,..) for s_i^{+-1}, n = 3..6; BB05 satisfies the relations', ok)
# RT is the restriction of U (right action on row vectors) to the sum-zero hyperplane, basis e_j - e_{j+1}
ok = True
for n in (3, 4, 5):
    Bm = [[LP(0, [1 if k == j else (-1 if k == j + 1 else 0)]) for k in range(n)] for j in range(n - 1)]   # rows e_j - e_{j+1}
    for i in range(1, n):
        for e in (1, -1):
            lhs = [[sum((Bm[j][k] * gen_U(LPR, n, i, e)[k][l] for k in range(n)), LP(0, [])) for l in range(n)] for j in range(n - 1)]
            RTm = mat_T(gen_R(LPR, n, i, e))
            rhs = [[sum((RTm[j][k] * Bm[k][l] for k in range(n - 1)), LP(0, [])) for l in range(n)] for j in range(n - 1)]
            ok &= all(x == y for r1, r2 in zip(lhs, rhs) for x, y in zip(r1, r2))
report('RT(s_i^{+-1}) is U(s_i^{+-1}) restricted to the sum-zero row vectors (so R, RT are genuine reduced Burau)', ok)

# ------------------------------------------------------------------ (10): 28-letter word in the free basis a_i = A_i4, own computation
fa = lambda *k: [(abs(x), 1 if x > 0 else -1) for x in k]
a1, a2, a3 = fa(1), fa(2), fa(3)
delta_a = a1 + a2 + a3
b_a = wcomm(wcomm(a1, a2), a3)
kw = wred(wcomm(winv(delta_a + delta_a), b_a))
es = [sum(e for (i, e) in kw if i == k) for k in (1, 2, 3)]
report('[delta^-2, b] in the free basis: reduced length 28, exponent sums 0', len(kw) == 28 and es == [0, 0, 0], f'len {len(kw)}, sums {es}')

# ------------------------------------------------------------------ (13): Section 7 polynomials, own transcription from the page images
MINE = {
    'M_Phi':      't^0 + t^2 + t^4 - t^3 - t + t^-3 + t^-1 + t',
    'M_PhiGamma': 't^0 + t^2 + t^4 - t^3 - t + t^-4 + t^-2 + t^0',
    'M_Gamma':    '-t^0 - t^2 + t + t^-1 - t^0 - t^2 + t^3 + t + t^-1 - t^-2 - t^0 + t^-1 + t^-3 - t^-2 - t^0 + t + t^-1 + t^-3 - t^-2 - t^0',
}
SIMPLIFIED = {   # printed second lines, as {exponent: coefficient}
    'M_Phi': {0: 1, 2: 1, 4: 1, 3: -1, -3: 1, -1: 1},
    'M_PhiGamma': {0: 2, 2: 1, 4: 1, 3: -1, 1: -1, -4: 1, -2: 1},
    'M_Gamma': {-3: 2, -2: -3, -1: 4, 0: -5, 1: 3, 2: -2, 3: 1},
}
def parse(sx):
    terms = re.findall(r'([+-]?)\s*t(?:\^(-?\d+))?', sx.replace(' ', ''))
    return [(-1 if sg == '-' else 1, int(ex) if ex else 1) for sg, ex in terms]
mine = {k: parse(v) for k, v in MINE.items()}
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'phi0_check.py')).read()
script_lists = {}
for name in ('M_Phi', 'M_PhiGamma', 'M_Gamma'):
    m = re.search(r'^' + name + r' = (\[.*?\])\n(?=\S)', src, re.S | re.M)
    script_lists[name] = ast.literal_eval(m.group(1).replace('\n', ' '))
for name in mine:
    report(f'(13) script list {name} == my transcription, term by term and in order', script_lists[name] == mine[name],
           f'{len(mine[name])} terms')
for name in mine:
    coll = {}
    for sg, ex in mine[name]: coll[ex] = coll.get(ex, 0) + sg
    coll = {e: c for e, c in coll.items() if c}
    report(f'(13) {name}: my unsimplified list collects to the printed simplified form', coll == SIMPLIFIED[name])
val = {k: sum(sg * (-1) ** (ex % 2) for sg, ex in v) for k, v in mine.items()}
cnt = {k: len(v) for k, v in mine.items()}
report('(13) counts 8, 20, 8 and values 8, -20, 2', (cnt['M_PhiGamma'], cnt['M_Gamma'], cnt['M_Phi'], val['M_PhiGamma'], val['M_Gamma'], val['M_Phi']) == (8, 20, 8, 8, -20, 2),
       f'{cnt} {val}')
sgn = {k: sorted({sg * (-1) ** (ex % 2) for sg, ex in v}) for k, v in mine.items()}
report('(13) eps(-1)^k constant on the two parity arcs, not on beta', sgn['M_PhiGamma'] == [1] and sgn['M_Gamma'] == [-1] and sgn['M_Phi'] == [-1, 1], str(sgn))
abs_sum = {k: sum(abs(c) for c in SIMPLIFIED[k].values()) for k in SIMPLIFIED}
report('(13) Lemma 1 cross-check: |coeff| sums of simplified forms are 8, 20 (parity arcs) and 6 < 8 for beta', abs_sum == {'M_Phi': 6, 'M_PhiGamma': 8, 'M_Gamma': 20}, str(abs_sum))

print('\nSUMMARY:', sum(ok for _, ok in OUT), 'OK,', sum(not ok for _, ok in OUT), 'BAD')
sys.exit(0 if all(ok for _, ok in OUT) else 1)
