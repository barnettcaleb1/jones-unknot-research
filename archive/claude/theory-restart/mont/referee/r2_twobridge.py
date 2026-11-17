"""Referee P5a: 2-bridge J-classes per knot type, knot type from the SLOPE (Schubert classification), not Alexander.
Box of word w has slope M(w)(0); closure D(p/q) = S(q, p) up to mirror; type key = q and min of {+-p, +-p^-1 mod q}.
J of the closure = normalize(e1^T rho(w) e1) (Theorem N for one box, realised 728/728 by the builder).
Both sign conventions for X tried; a correct convention must give <= 2 J-classes per knot type (Sakuma) and 1 for T(2,q)."""
import itertools, sys
from rlib import *
from math import gcd

def mob(word, MX):
    M = [[1, 0], [0, 1]]
    mats = {'Y': [[1, 1], [0, 1]], 'y': [[1, -1], [0, 1]], 'X': MX, 'x': [[MX[1][1], -MX[0][1]], [-MX[1][0], MX[0][0]]]}
    for ch in word:
        A = mats[ch]
        M = [[M[0][0]*A[0][0] + M[0][1]*A[1][0], M[0][0]*A[0][1] + M[0][1]*A[1][1]],
             [M[1][0]*A[0][0] + M[1][1]*A[1][0], M[1][0]*A[0][1] + M[1][1]*A[1][1]]]
    return M[0][1], M[1][1]          # image of (0,1)^T

def keyof(p, q):
    q = abs(q)
    if q == 1:
        return (1, 0)
    p %= q
    inv_ = pow(p, -1, q)
    return (q, min(x % q for x in (p, -p, inv_, -inv_)))

def jkey(Jn):
    a = tuple(sorted(Jn.items())); b = tuple(sorted(normalize({-e: c for e, c in Jn.items()}).items()))
    return min(a, b)

for name, MX in [('X: s->s/(2s+1)', [[1, 0], [2, 1]]), ('X: s->s/(1-2s)', [[1, 0], [-2, 1]])]:
    classes = {}
    nwords = 0
    for L in range(1, 8):
        for w in itertools.product('XxYy', repeat=L):
            if any(w[i].lower() == w[i + 1].lower() and w[i] != w[i + 1] for i in range(L - 1)):
                continue
            w = ''.join(w)
            nwords += 1
            p, q = mob(w, MX)
            if q % 2 == 0:
                print('EVEN q?!', w); continue
            Jn = normalize(apply(w)[0])
            classes.setdefault(keyof(p, q), set()).add(jkey(Jn))
    over = {k: len(v) for k, v in classes.items() if len(v) > 2}
    torus_bad = {k: len(v) for k, v in classes.items() if k[0] > 1 and k[1] == 1 and len(v) != 1}
    hist = {}
    for k, v in classes.items():
        if k[0] > 1:
            hist[len(v)] = hist.get(len(v), 0) + 1
    print(name, ': words', nwords, ' knot types', len(classes), ' #J-classes histogram', hist,
          ' types with >2 classes:', len(over), ' T(2,q) with !=1 class:', len(torus_bad))
    sample = {k: len(classes[k]) for k in [(7, 2), (9, 2), (11, 3), (11, 2), (13, 3), (15, 4), (13, 5), (5, 2)] if k in classes}
    print('   (q,p) -> #classes:', sample, '  [5_2=(7,2) or (7,3); 6_1=(9,2); 6_2=(11,3); 7_2=(11,2); 7_3=(13,3); 7_4=(15,4); 6_3=(13,5); 4_1=(5,2)]')
