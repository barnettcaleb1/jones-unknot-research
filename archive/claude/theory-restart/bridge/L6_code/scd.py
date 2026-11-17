"""Signed chord diagrams: bracket via GF(2) nullity (Cohn-Lempel/Traldi), parity, R1/R2 reduction.
Convention: Gauss word = cyclic list of chord labels 0..n-1, each twice.  eps[c] in {+1,-1}.
Bracket: <D> = A^w * sum_R x^{eps(R)} d^{null(M+I_R)},  x=A^-2, d=-(x+1/x).  V = (-1)^w x^w S, t=x^2.
"""
import itertools, sys
from collections import defaultdict

def chords_of(word):
    pos = defaultdict(list)
    for i, c in enumerate(word):
        pos[c].append(i)
    return {c: tuple(p) for c, p in pos.items()}

def interlace(word):
    ch = chords_of(word); labs = sorted(ch); n = len(labs)
    idx = {c: i for i, c in enumerate(labs)}
    rows = [0]*n
    for a, b in itertools.combinations(labs, 2):
        (a1, a2), (b1, b2) = ch[a], ch[b]
        if (a1 < b1 < a2) != (a1 < b2 < a2):
            rows[idx[a]] |= 1 << idx[b]; rows[idx[b]] |= 1 << idx[a]
    return labs, rows

def rank_gf2(rows):
    rows = list(rows); r = 0
    basis = []
    for v in rows:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v); r += 1
    return r

def nullity_table(rows):
    n = len(rows)
    N = [0]*(1 << n)
    for R in range(1 << n):
        rr = [rows[i] ^ ((R >> i) & 1) << i for i in range(n)]
        N[R] = n - rank_gf2(rr)
    return N

# Laurent polynomials as dict exp->coeff
def padd(p, q, s=1):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + s*c
        if r[e] == 0: del r[e]
    return r
def pmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1+e2] = r.get(e1+e2, 0) + c1*c2
    return {e: c for e, c in r.items() if c}

D = {1: -1, -1: -1}  # d = -(x + x^-1)
_dpow = [{0: 1}]
def dpow(k):
    while len(_dpow) <= k: _dpow.append(pmul(_dpow[-1], D))
    return _dpow[k]

def jones_x(rows, eps, N=None):
    """returns V as Laurent poly in x (t = x^2)."""
    n = len(rows)
    if N is None: N = nullity_table(rows)
    S = {}
    for R in range(1 << n):
        e = sum(eps[i] for i in range(n) if (R >> i) & 1)
        S = padd(S, {k + e: c for k, c in dpow(N[R]).items()})
    w = sum(eps)
    return {k + w: c*(-1)**(w % 2) for k, c in S.items()}

def parity(rows):
    return [bin(r).count('1') % 2 for r in rows]

def show_t(Vx):
    """x-poly -> string in t (half-integer exponents allowed)."""
    terms = []
    for e in sorted(Vx):
        terms.append(f"{Vx[e]:+d}t^{e/2:g}")
    return ' '.join(terms)

if __name__ == '__main__':
    # sanity: right trefoil 123123 all +
    labs, rows = interlace([0,1,2,0,1,2])
    print('trefoil+', show_t(jones_x(rows, [1,1,1])))   # expect t + t^3 - t^4
    # figure eight: alternating, signs: 4_1 Gauss -1,2,-3,1,-4,3,-2,4 ; writhe 0, two + two -
    w = [0,1,2,0,3,2,1,3]
    labs, rows = interlace(w)
    for eps in itertools.product([1,-1], repeat=4):
        if sum(eps) == 0:
            V = jones_x(rows, list(eps))
            print('4_1 cand', eps, show_t(V))
