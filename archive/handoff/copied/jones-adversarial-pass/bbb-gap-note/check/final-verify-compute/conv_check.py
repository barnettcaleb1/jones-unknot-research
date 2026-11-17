#!/usr/bin/env python3
"""Independent verifier (from scratch) for compute-lens findings 1-3 on bbb-gap-note.

Laurent polynomials are dicts {exponent: int}.  Braid words are lists of nonzero ints
(k = s_k, -k = s_k^-1).  Several Burau conventions are built, including ones derived
homologically via Fox calculus from both directions of the Artin action, and the
orientation-reversed ones (t -> 1/t, mirror word, contragredient).
"""
from fractions import Fraction as Fr
import random

# ---------------- Laurent polynomials ----------------
def P(d): return {e: c for e, c in d.items() if c}
def add(a, b):
    r = dict(a)
    for e, c in b.items(): r[e] = r.get(e, 0) + c
    return P(r)
def neg(a): return {e: -c for e, c in a.items()}
def mul(a, b):
    r = {}
    for e, c in a.items():
        for f, d in b.items(): r[e + f] = r.get(e + f, 0) + c * d
    return P(r)
def tinv(a): return {-e: c for e, c in a.items()}
ONE, ZERO, T, TI = {0: 1}, {}, {1: 1}, {-1: 1}

def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def mm(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            s = {}
            for l in range(k):
                if A[i][l] and B[l][j]: s = add(s, mul(A[i][l], B[l][j]))
            row.append(s)
        out.append(row)
    return out
def tr(A): return [list(r) for r in zip(*A)]
def mapM(f, A): return [[f(x) for x in r] for r in A]
def minusI(A): return [[add(x, neg(ONE)) if i == j else x for j, x in enumerate(r)] for i, r in enumerate(A)]
def ev(p, x): return sum(Fr(c) * Fr(x) ** e for e, c in p.items())
def evM(A, x): return [[ev(p, x) for p in r] for r in A]
def isI(A): return all(v == (1 if i == j else 0) for i, r in enumerate(A) for j, v in enumerate(r))

# ---------------- words ----------------
def inv(w): return [-a for a in reversed(w)]
def cm(x, y): return x + y + inv(x) + inv(y)
X = [1, 2] * 6
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
b = cm(cm(A14, A24), A34)
Phi0 = cm(X, b)
D3sq = [1, 2] * 3
assert len(Phi0) == 112
def mirror(w): return [-a for a in w]

# ---------------- conventions ----------------
def U_gen(n, a):
    i = abs(a) - 1; M = eye(n)
    if a > 0: blk = [[{0: 1, 1: -1}, T], [ONE, ZERO]]
    else:     blk = [[ZERO, ONE], [TI, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2): M[i + r][i + c] = blk[r][c]
    return M
def prod(gens, w, n0):
    M = eye(n0)
    for a in w: M = mm(M, gens(a))
    return M
def U(w, n): return prod(lambda a: U_gen(n, a), w, n)

# reduced Burau, standard form: row i of I_{n-1} replaced by (t, -t, 1) in cols i-1, i, i+1
def R_gen(n, a):
    i = abs(a) - 1; M = eye(n - 1)
    row = {i - 1: T, i: {1: -1}, i + 1: ONE}
    G = eye(n - 1)
    for c, v in row.items():
        if 0 <= c < n - 1: G[i][c] = v
    if a > 0: return G
    # inverse of G: solve by noting G differs from I only in row i
    # G = I + e_i (r - e_i)^T ; inverse row i: x with x G = e_i  ->  direct formula
    # simpler: inverse of s_i in reduced form is row i = (1, -t^-1, t^-1)
    H = eye(n - 1)
    rowi = {i - 1: ONE, i: {-1: -1}, i + 1: TI}
    for c, v in rowi.items():
        if 0 <= c < n - 1: H[i][c] = v
    return H
def R(w, n): return prod(lambda a: R_gen(n, a), w, n - 1)

# Fox calculus from the Artin action (right action, braids multiplied left to right)
def red(w):
    s = []
    for a in w:
        if s and s[-1] == -a: s.pop()
        else: s.append(a)
    return s
def artin_sub(a, direction):
    i = abs(a)
    if direction == 'A':   # s_i: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i
        pos = {i: [i, i + 1, -i], i + 1: [i]}
        ng = {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}
    else:                  # 'B': the other half twist: x_i -> x_{i+1}, x_{i+1} -> x_{i+1}^-1 x_i x_{i+1}
        pos = {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}
        ng = {i: [i, i + 1, -i], i + 1: [i]}
    return pos if a > 0 else ng
def artin(w, n, direction):
    img = {j: [j] for j in range(1, n + 1)}
    for a in w:
        sub = artin_sub(a, direction)
        for j in img:
            out = []
            for c in img[j]:
                s = sub.get(abs(c), [abs(c)])
                out += s if c > 0 else inv(s)
            img[j] = red(out)
    return img
def fox_row(word, n, var):     # var = T or TI: abelianization x_k -> var
    row = [dict() for _ in range(n)]
    e = 0                      # current exponent of the prefix (in units of var)
    sgn = 1 if var == T else -1
    for c in word:
        if c > 0:
            row[c - 1] = add(row[c - 1], {sgn * e: 1}); e += 1
        else:
            e -= 1; row[-c - 1] = add(row[-c - 1], {sgn * e: -1})
    return row
def FoxWhole(w, n, direction, var): return [fox_row(v, n, var) for _, v in sorted(artin(w, n, direction).items())]
# Whole-word Artin images of Phi0 have millions of letters, so use the chain rule: for a right action
# J(uv) = J(u) J(v) after abelianization (braid automorphisms preserve exponent sums).  Each letter's
# matrix is its own Fox Jacobian; the chain rule itself is tested on short words below.
_fox_cache = {}
def FoxGen(n, a, direction, var):
    key = (n, a, direction, var == T)
    if key not in _fox_cache: _fox_cache[key] = FoxWhole([a], n, direction, var)
    return _fox_cache[key]
def FoxM(w, n, direction, var): return prod(lambda a: FoxGen(n, a, direction, var), w, n)

CONVS = {
    'U  (s_i -> [[1-t,t],[1,0]], left-to-right)':      lambda w, n: U(w, n),
    'UT (transposed generators)':                        lambda w, n: prod(lambda a: tr(U_gen(n, a)), w, n),
    'Urev (right-to-left product)':                      lambda w, n: prod(lambda a: U_gen(n, a), list(reversed(w)), n),
    'R  (reduced, row i = (t,-t,1))':                    lambda w, n: R(w, n),
    'Fox A, x->t (homological, Artin dir A)':            lambda w, n: FoxM(w, n, 'A', T),
    '--- opposite orientation ---':                      None,
    'U with t -> 1/t':                                   lambda w, n: mapM(tinv, U(w, n)),
    'U of mirror word (s_i -> s_i^-1)':                  lambda w, n: U(mirror(w), n),
    'U contragredient (U(w)^-T)':                        lambda w, n: tr(U(inv(w), n)),
    'R of mirror word':                                  lambda w, n: R(mirror(w), n),
    'Fox B, x->t (homological, other half twist)':       lambda w, n: FoxM(w, n, 'B', T),
    'Fox A, x->1/t (other deck generator)':              lambda w, n: FoxM(w, n, 'A', TI),
}

random.seed(11)
short = [[random.choice([1, -1]) * random.randint(1, 3) for _ in range(random.randint(2, 12))] for _ in range(40)]
print("sanity: chain rule, whole-word Fox Jacobian == product of letter Jacobians (40 random words, both dirs, t and 1/t):",
      all(FoxWhole(w, 4, d, v) == FoxM(w, 4, d, v) for w in short for d in 'AB' for v in (T, TI)))
print("sanity: whole-word Fox A x->t equals U on the 40 short words:", all(FoxWhole(w, 4, 'A', T) == U(w, 4) for w in short))
print("sanity: Fox A x->t equals U for Phi0 (B4):", FoxM(Phi0, 4, 'A', T) == U(Phi0, 4))
print("sanity: Fox B x->t equals U(mirror) for Phi0 (B4):", FoxM(Phi0, 4, 'B', T) == U(mirror(Phi0), 4))
print("sanity: Fox A x->1/t equals U with t->1/t (B4):", FoxM(Phi0, 4, 'A', TI) == mapM(tinv, U(Phi0, 4)))
print("sanity: R satisfies braid relations in B4, B5:",
      all(R(u, n) == R(v, n) for n in (4, 5) for i in range(1, n - 1) for u, v in [([i, i + 1, i], [i + 1, i, i + 1])])
      and all(R([i, -i], n) == eye(n - 1) for n in (4, 5) for i in range(1, n)))
print()

TV = [Fr(-1), Fr(2), Fr(1, 2), Fr(3), Fr(1, 3)]
hdr = "  ".join(f"t={str(x):>4}" for x in TV)
for n in (4, 5):
    print(f"B_{n}: is Burau(Phi0) = I at  {hdr}   | (1+t^3) identity | (1+t^-3) identity")
    for name, f in CONVS.items():
        if f is None: print("   " + name); continue
        M = f(Phi0, n)
        vals = "  ".join(f"{('I' if isI(evM(M, x)) else 'notI'):>6}" for x in TV)
        if n == 4:
            MX, MD = minusI(f(X, n)), minusI(f(D3sq, n))
            id3 = MX == mapM(lambda p: mul({0: 1, 3: 1}, p), MD)
            idm3 = MX == mapM(lambda p: mul({0: 1, -3: 1}, p), MD)
            extra = f"  | {str(id3):>16} | {str(idm3):>17}"
        else: extra = ""
        print(f"   {name:46} {vals}{extra}")
    print()

# Mirror relation: U(mirror w)(t) = C(t) U(w)(1/t) C(t)^-1 with C independent of w
def Delta(n):
    w = []
    for k in range(n - 1, 0, -1): w += list(range(1, k + 1))
    return w
random.seed(7)
for n in (4, 5):
    J = [[ONE if i + j == n - 1 else ZERO for j in range(n)] for i in range(n)]
    D = Delta(n)
    C = mm(J, mapM(tinv, U(D, n)))
    Cinv = mm(mapM(tinv, U(inv(D), n)), J)
    assert mm(C, Cinv) == eye(n)
    words = [Phi0, X, D3sq, b] + [[random.choice([1, -1]) * random.randint(1, n - 1) for _ in range(random.randint(5, 25))] for _ in range(30)]
    ok = all(U(mirror(w), n) == mm(mm(C, mapM(tinv, U(w, n))), Cinv) for w in words)
    print(f"B_{n}: U(mirror w)(t) == C U(w)(1/t) C^-1 with C = J U(Delta)(1/t), for Phi0, X, Delta_3^2, b and 30 random words:", ok)

# show the opposite-orientation factor explicitly for one entry
MX, MD = minusI(mapM(tinv, U(X, 4))), minusI(mapM(tinv, U(D3sq, 4)))
print("\nexample entry (0,0) after t->1/t:  rho(X)-I =", dict(sorted(MX[0][0].items())), "  rho(D3^2)-I =", dict(sorted(MD[0][0].items())))
