#!/usr/bin/env python3
"""Phi0 = [X, b] is a nontrivial Brunnian 4-braid whose Burau image is I at t = -1.

  X = (s1 s2)^6,  A14 = s3 s2 s1 s1 s2^-1 s3^-1,  A24 = s3 s2 s2 s3^-1,  A34 = s3 s3,
  b = [[A14, A24], A34],  Phi0 = [X, b],  where [x, y] = x y x^-1 y^-1.
Pure Python 3, exact integer/rational arithmetic, no dependencies.  Run: python3 phi0_check.py

Conventions.  A braid word is a list of nonzero ints (k = s_k, -k = s_k^-1), multiplied left to right.
Artin action (a right action, faithful): s_i sends x_i -> x_i x_{i+1} x_i^-1 and x_{i+1} -> x_i.
Burau over Z[t, 1/t] (Laurent polynomials are dicts {exponent: coefficient}):
  U  unreduced, s_i -> I with block [[1-t, t], [1, 0]] in rows/cols i, i+1;   UT  transpose of each U(s_i);
  R  reduced (n-1 x n-1), s_i -> I with row i replaced by (t, -t, 1) in cols i-1, i, i+1;  RT  transposes.
Check (S) confirms that each is a representation of B_4 and B_5 and that, letter by letter, U is the Fox
Jacobian of the Artin action with x_k -> t, i.e. the matrix of the action on H_1(D~_n, {p~_*}) in the basis of
lifts of x_1..x_n.  U is the matrix form in Birman-Brendle, Braids: a survey (2005), Section 4.2, which
Section 2 of the paper cites for Burau's definition.  Reversing every half twist, or replacing t by 1/t,
amounts to t -> 1/t up to conjugation; this changes nothing at t = -1 or for the (t+1)-adic depth, so the
evaluations at t = 2, 3 are repeated at t = 1/2, 1/3.
"""
from fractions import Fraction
from functools import reduce

def inv(w): return [-a for a in reversed(w)]
def comm(x, y): return x + y + inv(x) + inv(y)
def red(w):                                    # free reduction of a word
    s = []
    for a in w: s.pop() if s and s[-1] == -a else s.append(a)
    return s

def artin(w, n):                               # images of x_1..x_n under w (right action)
    img = {j: [j] for j in range(1, n + 1)}
    for a in w:
        i = abs(a)
        sub = {i: [i, i + 1, -i], i + 1: [i]} if a > 0 else {i: [i + 1], i + 1: [-i - 1, i, i + 1]}
        for j in img:
            out = []
            for c in img[j]:
                s = sub.get(abs(c), [abs(c)])
                out += s if c > 0 else inv(s)
            img[j] = red(out)
    return img
def trivial(w, n): return all(v == [j] for j, v in artin(w, n).items())
def commute(u, v, n): return artin(u + v, n) == artin(v + u, n)
def pure(w, n):
    p = list(range(n))
    for a in w: k = abs(a); p[k - 1], p[k] = p[k], p[k - 1]
    return p == list(range(n))
def delete(w, n, d):                           # erase the strand starting at position d
    p, out = list(range(1, n + 1)), []
    for a in w:
        k = abs(a)
        if d not in (p[k - 1], p[k]):          # crossing between two kept strands
            kk = k - 1 if p.index(d) < k - 1 else k
            out.append(kk if a > 0 else -kk)
        p[k - 1], p[k] = p[k], p[k - 1]
    return out

# ---------- exact Laurent-polynomial matrices ----------
def padd(a, b):
    r = dict(a)
    for e, c in b.items(): r[e] = r.get(e, 0) + c
    return {e: c for e, c in r.items() if c}
def pmul(a, b):
    r = {}
    for e, c in a.items():
        for f, d in b.items(): r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}
def ident(m): return [[{0: 1} if i == j else {} for j in range(m)] for i in range(m)]
def mmul(A, B):
    m = len(A)
    return [[reduce(padd, (pmul(A[i][k], B[k][j]) for k in range(m)), {}) for j in range(m)] for i in range(m)]
def gen(n, a, conv):                           # Burau matrix of the letter a
    i = abs(a)
    if conv[0] == 'U':
        M = ident(n)
        blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]] if a > 0 else [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
        for r in range(2):
            for c in range(2): M[i - 1 + r][i - 1 + c] = blk[r][c]
    else:
        M, r = ident(n - 1), i - 1
        vals = ({1: 1}, {1: -1}, {0: 1}) if a > 0 else ({0: 1}, {-1: -1}, {-1: 1})
        for c, v in zip((r - 1, r, r + 1), vals):
            if 0 <= c < n - 1: M[r][c] = v
    return [list(x) for x in zip(*M)] if conv.endswith('T') else M
def burau(w, n, conv): return reduce(mmul, (gen(n, a, conv) for a in w), ident(n - (conv[0] == 'R')))
def at(M, t): return [[sum(c * Fraction(t) ** e for e, c in p.items()) for p in row] for row in M]
def is_I(M): return all(x == (i == j) for i, row in enumerate(M) for j, x in enumerate(row))
def mult(p):                                   # multiplicity of the root t = -1 of p != 0
    c, k = [p.get(e, 0) for e in range(min(p), max(p) + 1)], 0
    while sum(x * (-1) ** i for i, x in enumerate(c)) == 0:
        q, acc = [], 0
        for x in reversed(c): acc = x - acc; q.append(acc)     # divide by (t + 1)
        c, k = q[:-1][::-1], k + 1
    return k
def depth(M):                                  # largest k with M = I mod (t+1)^k (inf if M = I)
    D = [[padd(p, {0: -1} if i == j else {}) for j, p in enumerate(row)] for i, row in enumerate(M)]
    return min((mult(p) for row in D for p in row if p), default=float('inf'))
def fox(word, n):                              # (d word / d x_j) at x_k = t, for j = 1..n
    row, e = [{} for _ in range(n)], 0
    for c in word:
        e -= c < 0
        row[abs(c) - 1] = padd(row[abs(c) - 1], {e: 1 if c > 0 else -1})
        e += c > 0
    return row

FAILS = []
def check(name, ok):
    print(('PASS  ' if ok else 'FAIL  ') + name)
    if not ok: FAILS.append(name)
CONVS = ('U', 'UT', 'R', 'RT')
REL = lambda n: [([i, i + 1, i], [i + 1, i, i + 1]) for i in range(1, n - 1)] + \
                [([i, j], [j, i]) for i in range(1, n) for j in range(i + 2, n)]
check("(S) U, UT, R, RT satisfy the B_4 and B_5 relations and s_i s_i^-1 = I",
      all(burau(u, n, c) == burau(v, n, c) for n in (4, 5) for c in CONVS for u, v in REL(n))
      and all(burau([i, -i], n, c) == ident(n - (c[0] == 'R')) for n in (4, 5) for c in CONVS for i in range(1, n)))
check("(S) for every letter s_i^(+-1), n = 4, 5, the Fox Jacobian of its Artin automorphism is its U matrix",
      all([fox(v, n) for v in artin([a], n).values()] == burau([a], n, 'U')
          for n in (4, 5) for i in range(1, n) for a in (i, -i)))
w = [1, -2, 3, 3, -1, 2, -3, 2, 1]
check("(S) Fox Jacobian of the Artin action of a test word equals U",
      [fox(v, 4) for v in artin(w, 4).values()] == burau(w, 4, 'U'))

def Aij(i, j):                                 # Artin's s_{j-1}..s_{i+1} s_i^2 s_{i+1}^-1..s_{j-1}^-1
    left = list(range(j - 1, i, -1)); return left + [i, i] + inv(left)
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
X = [1, 2] * 6
b = comm(comm(A14, A24), A34)
Phi0 = comm(X, b)
D3sq, D4sq = [1, 2] * 3, [1, 2, 3] * 4         # full twists Delta_3^2, Delta_4^2
delta = inv(D3sq) + D4sq
inK4 = lambda v: pure(v, 4) and trivial(delete(v, 4, 4), 3)

check("(0) A14, A24, A34 are Artin's A_14, A_24, A_34", [A14, A24, A34] == [Aij(1, 4), Aij(2, 4), Aij(3, 4)])
check("(0) each A_i4 lies in K_4 (pure, trivial after deleting strand 4)", all(inK4(A) for A in (A14, A24, A34)))
check("(1) Phi0 is a pure braid", pure(Phi0, 4))
check("(2) Artin action: X and b do not commute, i.e. Phi0 != 1", not commute(X, b, 4))
for d in (1, 2, 3, 4):
    v = delete(Phi0, 4, d)
    check(f"(3) deleting strand {d}: word freely reduces to empty and acts trivially on F_3", red(v) == [] and trivial(v, 3))
check(f"(4) unreduced concatenation has {len(Phi0)} letters (expected 112)", len(Phi0) == 112)
check(f"(4) freely reduced word has {len(red(Phi0))} letters (expected 76)", len(red(Phi0)) == 76)
TVALS = (Fraction(2), Fraction(1, 2), Fraction(3), Fraction(1, 3))
for n in (4, 5):                               # n = 5: the inclusion f(Phi0), s_i -> s_i
    tag = 'Phi0' if n == 4 else 'f(Phi0)'
    for conv in CONVS:
        M = burau(Phi0, n, conv)
        check(f"(5) B_{n} {conv:2}: Burau({tag}) = I at t=-1", is_I(at(M, -1)))
        check(f"(6) B_{n} {conv:2}: Burau({tag}) != I as a Laurent matrix, and at t = 2, 1/2, 3, 1/3",
              depth(M) != float('inf') and not any(is_I(at(M, x)) for x in TVALS))
        check(f"(7) B_{n} {conv:2}: (t+1)-adic depth is exactly 1 (found {depth(M)})", depth(M) == 1)
check("(8) (s1 s2)^6 == (s1 s2 s1)^4 = Delta_3^4 (Artin action)", trivial(X + inv([1, 2, 1] * 4), 4))
check("(8) Burau(X) = I at t=-1 in U, UT, R, RT", all(is_I(at(burau(X, 4, c), -1)) for c in CONVS))
check("(9) Delta_4^2 is central in B_4", all(commute(D4sq, [i], 4) for i in (1, 2, 3)))
# [X,b] = [delta^-2,b]  <=>  X b X^-1 = delta^-2 b delta^2  <=>  delta^2 X commutes with b
check("(9) delta^2 X commutes with b, hence Phi0 == [delta^-2, b]", commute(delta + delta + X, b, 4))
check("(10) delta and b lie in K_4, so Phi0 = [delta^-2, b] lies in [K_4, K_4]", inK4(delta) and inK4(b))
kw = red(comm([-3, -2, -1] * 2, comm(comm([1], [2]), [3])))   # same word in the free basis a_i = A_i4
check("(10) delta == A14 A24 A34 (Artin action)", trivial(delta + inv(A14 + A24 + A34), 4))
check(f"(10) in the free basis a_i = A_i4 of K_4, [delta^-2, b] is a reduced word of {len(kw)} letters (expected 28), exponent sums 0",
      len(kw) == 28 and all(sum((c == i) - (c == -i) for c in kw) == 0 for i in (1, 2, 3)))
def msub_I(M): return [[padd(p, {0: -1} if i == j else {}) for j, p in enumerate(row)] for i, row in enumerate(M)]
check("(11) Burau(X) - I == (1 + t^3)(Burau(Delta_3^2) - I) exactly, in U, UT, R, RT",
      all(msub_I(burau(X, 4, c)) == [[pmul({0: 1, 3: 1}, p) for p in row] for row in msub_I(burau(D3sq, 4, c))]
          for c in CONVS))
mirror = lambda w: [-a for a in w]             # every half twist reversed
check("(11) with every half twist reversed, the identity holds with 1 + t^-3 in place of 1 + t^3",
      all(msub_I(burau(mirror(X), 4, c)) == [[pmul({0: 1, -3: 1}, p) for p in row] for row in msub_I(burau(mirror(D3sq), 4, c))]
          for c in CONVS))
s3conj = [3] + Phi0 + [-3]
P, Q = burau(Phi0, 4, 'U'), burau(s3conj, 4, 'U')
check("(12) U(Phi0) and U(s3 Phi0 s3^-1) do not commute, so neither do the braids (both lie in Brun_4 < K_4, free)",
      mmul(P, Q) != mmul(Q, P))
dC = depth(burau(comm(Phi0, s3conj), 4, 'UT'))
check(f"(12) [Phi0, s3 Phi0 s3^-1] has (t+1)-adic depth exactly 2 (found {dC})", dC == 2)
# Section 7 of arXiv:2607.05283v2 (pp. 26-27): the printed unsimplified Moody polynomials, as (sign, exponent)
M_Phi = [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (1, -3), (1, -1), (1, 1)]
M_PhiGamma = [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (1, -4), (1, -2), (1, 0)]
M_Gamma = [(-1, 0), (-1, 2), (1, 1), (1, -1), (-1, 0), (-1, 2), (1, 3), (1, 1), (1, -1), (-1, -2),
           (-1, 0), (1, -1), (1, -3), (-1, -2), (-1, 0), (1, 1), (1, -1), (1, -3), (-1, -2), (-1, 0)]
at_m1 = lambda P: sum(e * (-1) ** (k % 2) for e, k in P)
check("(13) paper Sec. 7: M_{Phi.Gamma}, M_Gamma, M_Phi have 8, 20, 8 terms and values 8, -20, 2 at t=-1",
      [(len(P), at_m1(P)) for P in (M_PhiGamma, M_Gamma, M_Phi)] == [(8, 8), (20, -20), (8, 2)])
signs = lambda P: {e * (-1) ** (k % 2) for e, k in P}               # the values eps_i (-1)^k_i
check("(13) eps_i (-1)^k_i is constant for the two parity arcs and not for beta (Lemma 1)",
      len(signs(M_PhiGamma)) == 1 and len(signs(M_Gamma)) == 1 and len(signs(M_Phi)) == 2)
print("\nfreely reduced word of Phi0 (" + str(len(red(Phi0))) + " letters, k = s_k, -k = s_k^-1):")
print(" ".join(map(str, red(Phi0))))
print("\nALL CHECKS PASSED" if not FAILS else f"\n{len(FAILS)} CHECK(S) FAILED")
raise SystemExit(1 if FAILS else 0)
