# Kauffman bracket vectors of 4-ended tangles: <T> = v*V + e*H, Laurent polys in A as dict{exp:coeff}
from collections import defaultdict
def P(*terms):
    d = defaultdict(int)
    for c, e in terms: d[e] += c
    return {e: c for e, c in d.items() if c}
def add(p, q):
    d = defaultdict(int)
    for e, c in p.items(): d[e] += c
    for e, c in q.items(): d[e] += c
    return {e: c for e, c in d.items() if c}
def mul(p, q):
    d = defaultdict(int)
    for e1, c1 in p.items():
        for e2, c2 in q.items(): d[e1+e2] += c1*c2
    return {e: c for e, c in d.items() if c}
def neg(p): return {e: -c for e, c in p.items()}
def show(p):
    if not p: return '0'
    return ' '.join(f'{c:+d}*A^{e}' for e, c in sorted(p.items()))
d = P((-1, 2), (-1, -2))
ONE = P((1, 0)); ZERO = {}
V = (ONE, ZERO); H = (ZERO, ONE)
def stack(X, Y):   # vertical composition: V unit, H o H = d H
    (v1, h1), (v2, h2) = X, Y
    return (mul(v1, v2), add(add(mul(v1, h2), mul(h1, v2)), mul(d, mul(h1, h2))))
def hsum(X, Y):    # horizontal sum: H unit, V + V = d V
    (v1, h1), (v2, h2) = X, Y
    return (add(add(mul(v1, h2), mul(h1, v2)), mul(d, mul(v1, v2))), mul(h1, h2))
c_pos = (P((1, 1)), P((1, -1)))     # A V + A^-1 H
c_neg = (P((1, -1)), P((1, 1)))     # A^-1 V + A H
def column(a):
    X = V
    for _ in range(abs(a)): X = stack(X, c_pos if a > 0 else c_neg)
    return X
def Ncl(X): return add(X[0], mul(d, X[1]))   # N(V)=1, N(H)=d   (unknot normalised to 1)
def Dcl(X): return add(mul(d, X[0]), X[1])   # D(V)=d, D(H)=1
def ev(p, A):
    return sum(c * A**e for e, c in p.items())
import cmath
A8 = cmath.exp(1j*cmath.pi/4)   # A^4 = -1, d = 0 : |bracket| = determinant
def divide(p, q):
    # exact division of Laurent polys (returns None if not exact)
    p = dict(p); res = {}
    qe = max(q); qc = q[qe]
    while p:
        pe = max(p); pc = p[pe]
        if pc % qc: return None
        e = pe - qe; c = pc // qc
        if e < min(p) - (max(q) - min(q)) - 1: return None
        res[e] = c
        p = add(p, neg(mul({e: c}, q)))
        if len(res) > 2000: return None
    return res
if __name__ == '__main__':
    import sys
    a, b = int(sys.argv[1]), int(sys.argv[2])
    X = hsum(column(a), column(b))
    print('pretzel tangle P(%d,%d): N-closure bracket' % (a, b), show(Ncl(X)), ' det N =', round(abs(ev(Ncl(X), A8)), 6))
    for m in range(-8, 9):
        Xm = stack(X, column(m))
        detD = round(abs(ev(Dcl(Xm), A8)), 6)
        # compare with pretzel link P(a,b,+-m)
        l1 = Ncl(hsum(X, column(m))); l2 = Ncl(hsum(X, column(-m)))
        print('m=%3d det D(X o c^m) = %s   [det P(a,b,m) = %s, det P(a,b,-m) = %s]' % (m, detD, round(abs(ev(l1, A8)), 6), round(abs(ev(l2, A8)), 6)))
