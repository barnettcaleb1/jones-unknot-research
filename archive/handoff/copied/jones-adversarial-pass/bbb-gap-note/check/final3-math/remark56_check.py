#!/usr/bin/env python3
"""Checks for Remark 5 (new sentences) and Remark 6(3) (new definition of e).

Remark 5:
 (5a) t+1 is prime in Z[t^+-1] (Z[t^+-1]/(t+1) = Z) and does not divide 1-t, 1-1/t (values 2 at -1).
 (5b) a nonzero Laurent polynomial divisible by (t+1)^d has exponent span >= d (random tests).
 (5c) c*p(-t) == c'*p'(-t) mod (t+1)^d  <=>  c = c' and p^(j)(1) = p'^(j)(1) for j < d,
      when both multisets are nonempty (random tests incl. sign agreement from j = 0).
 (5d) for each d there are equal-size exponent multisets with equal factorial moments for j < d
      but different spans (so the span is not determined by moments up to a fixed order).
Remark 6(3):
 (6a) of s3 s2^2 s3^-1 and s3^-1 s2^2 s3, exactly one fixes x3 (that twist is about e, the curve
      around p2, p4 on the far side of p3 from p*); T_c1 = s1^2 fixes x3.
 (6b) the braid applying T_c1, then T_e^-1, then T_c2 sends x3 to s3^2(x3), and s1^2 (= T_c1,
      c1 = boundary of a neighbourhood of alpha) fixes that image, so the image arc misses alpha.
 (6c) word-length growth of iterates on F_4 approaches Penner's dilatation 5 + 2 sqrt 6 = 9.899.
"""
import random
from fractions import Fraction
from math import comb, factorial, sqrt

random.seed(7)
res = []
def report(name, ok):
    res.append(ok); print(('PASS  ' if ok else 'FAIL  ') + name)

def ev(p, x): return sum(c * Fraction(x) ** e for e, c in p.items())
def lmul(a, b):
    r = {}
    for e, c in a.items():
        for f, d in b.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}
def lsub(a, b):
    r = dict(a)
    for e, c in b.items(): r[e] = r.get(e, 0) - c
    return {e: c for e, c in r.items() if c}
def mult_at_minus1(p):
    k, q = 0, dict(p)
    while q and ev(q, -1) == 0:
        lo, hi = min(q), max(q)
        cs = [q.get(e, 0) for e in range(lo, hi + 1)]
        out, acc = [], 0
        for c in reversed(cs):
            acc = c - acc; out.append(acc)
        out = out[:-1][::-1]
        q = {lo + i: c for i, c in enumerate(out) if c}
        k += 1
    return k

# (5a)
report("(5a) 1-t and 1-1/t are nonzero at t=-1 (value 2), so t+1 divides neither", ev({0: 1, 1: -1}, -1) == 2 and ev({0: 1, -1: -1}, -1) == 2)
# (5b)
ok = True
for _ in range(500):
    d = random.randint(1, 6)
    Q = {e: random.randint(-3, 3) for e in range(random.randint(-4, 0), random.randint(0, 4) + 1)}
    Q = {e: c for e, c in Q.items() if c}
    if not Q: continue
    P = dict(Q)
    for _ in range(d): P = lmul(P, {0: 1, 1: 1})
    ok &= (max(P) - min(P)) >= d
report("(5b) (t+1)^d * Q, Q != 0: exponent span >= d (500 random cases)", ok)
# (5c)
def ffm(ks, j):   # factorial moment p^(j)(1) = sum_k k(k-1)...(k-j+1)
    s = 0
    for k in ks:
        v = 1
        for r in range(j): v *= (k - r)
        s += v
    return s
def poly_from(ks, c):    # c * sum_i (-t)^{k_i}
    P = {}
    for k in ks:
        P[k] = P.get(k, 0) + c * (-1) ** (k % 2)
    return {e: v for e, v in P.items() if v}
ok, tested, hits = True, 0, 0
for _ in range(4000):
    d = random.randint(1, 4)
    m = random.randint(1, 6)
    ks = [random.randint(-3, 3) for _ in range(m)]
    # build a partner with equal moments sometimes: add (1-s)^d * s^a pattern
    if random.random() < 0.5:
        a = random.randint(-2, 2)
        pos = [a + j for j in range(d + 1) for _ in range(comb(d, j)) if j % 2 == 0]
        neg = [a + j for j in range(d + 1) for _ in range(comb(d, j)) if j % 2 == 1]
        ks2 = ks + pos
        ks = ks + neg
    else:
        ks2 = [random.randint(-3, 3) for _ in range(random.randint(1, 6))]
    c, c2 = random.choice((1, -1)), random.choice((1, -1))
    diff = lsub(poly_from(ks, c), poly_from(ks2, c2))
    congruent = (not diff) or mult_at_minus1(diff) >= d
    moments = (c == c2) and all(ffm(ks, j) == ffm(ks2, j) for j in range(d))
    ok &= (congruent == moments)
    tested += 1; hits += congruent
report(f"(5c) congruence mod (t+1)^d <=> same sign and equal factorial moments j<d ({tested} cases, {hits} congruent)", ok)
# (5d)
ok = True
for d in range(1, 9):
    dd = d if d % 2 == 0 else d + 1        # use (1-s)^dd, dd even, so the spans differ
    A = [j for j in range(dd + 1) for _ in range(comb(dd, j)) if j % 2 == 0]
    B = [j for j in range(dd + 1) for _ in range(comb(dd, j)) if j % 2 == 1]
    same = len(A) == len(B) and all(ffm(A, j) == ffm(B, j) for j in range(d))
    spans = (max(A) - min(A), max(B) - min(B))
    ok &= same and spans[0] != spans[1]
report("(5d) for d = 1..8: multisets with equal factorial moments j<d and different spans exist", ok)

# ---------- Remark 6(3) ----------
def red(s):
    o = []
    for a in s:
        if o and o[-1] == -a: o.pop()
        else: o.append(a)
    return o
def inv(w): return [-a for a in reversed(w)]
def act(w, word):
    """right Artin action of braid word w on a free-group word (x_k = k)."""
    cur = list(word)
    for a in w:
        i = abs(a)
        sub = {i: [i, i + 1, -i], i + 1: [i]} if a > 0 else {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}
        o = []
        for c in cur:
            s = sub.get(abs(c), [abs(c)])
            o += s if c > 0 else inv(s)
        cur = red(o)
    return cur
x3 = [3]
Te_far = [3, 2, 2, -3]
Te_near = [-3, 2, 2, 3]
f1, f2 = act(Te_far, x3) == x3, act(Te_near, x3) == x3
report(f"(6a) exactly one of s3 s2^2 s3^-1, s3^-1 s2^2 s3 fixes x3 (found {f1}, {f2})", f1 != f2)
Te = Te_far if f1 else Te_near
report("(6a) T_c1 = s1^2 fixes x3", act([1, 1], x3) == x3)
Phi = [1, 1] + inv(Te) + [3, 3]            # apply T_c1, then T_e^-1, then T_c2 (left to right)
img = act(Phi, x3)
report(f"(6b) the braid sends x3 to s3^2(x3) = {img}", img == act([3, 3], x3))
report("(6b) s1^2 = T_c1 fixes the image loop, so the image arc is disjoint from c1, hence from alpha",
       act([1, 1], img) == img)
report("(6b) the image is not x3 (the braid moves the arc)", img != x3)
# (6c) growth
lens = []
words = {k: [k] for k in range(1, 5)}
for it in range(7):
    words = {k: act(Phi, v) for k, v in words.items()}
    lens.append(sum(len(v) for v in words.values()))
ratios = [lens[i + 1] / lens[i] for i in range(len(lens) - 1)]
report(f"(6c) word-length growth ratios {[round(r, 3) for r in ratios]} -> 5+2sqrt6 = {5 + 2 * sqrt(6):.4f}",
       abs(ratios[-1] - (5 + 2 * sqrt(6))) < 0.05)
# Penner matrix: curves (c1, c2, e), i(c1,e) = i(c2,e) = 2
import itertools
Om = [[0, 0, 2], [0, 0, 2], [2, 2, 0]]
def Q(a):
    M = [[int(i == j) for j in range(3)] for i in range(3)]
    for j in range(3): M[a][j] += Om[a][j]
    return M
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
P = mm(mm(Q(0), Q(2)), Q(1))
# PF eigenvalue by power iteration
v = [1.0, 1.0, 1.0]
for _ in range(200):
    w = [sum(P[i][j] * v[j] for j in range(3)) for i in range(3)]
    s = max(w); v = [x / s for x in w]
lam = sum(P[0][j] * v[j] for j in range(3)) / v[0]
report(f"(6c) Penner matrix PF eigenvalue {lam:.4f} == 5+2sqrt6", abs(lam - (5 + 2 * sqrt(6))) < 1e-6)

print(f"\n{sum(res)} PASS, {len(res) - sum(res)} FAIL")
