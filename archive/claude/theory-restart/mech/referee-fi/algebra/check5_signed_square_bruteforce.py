# Independent brute-force probe of the signed-square sign rule on ACTUAL (generally non-rational) two-box diagrams.
# Diagram: closure of a random braid word; the two "boxes" are two chosen crossings, filled by the two
# crossingless tangles (label 0 = vertical/identity smoothing, label 1 = cup-cap smoothing).
# C_ij = common reduced raw bracket (state sum over the other crossings, delta^(loops-1)), evaluated at zeta_8,
# where delta=0 so only one-loop states contribute.  Exact arithmetic in Z[zeta_8] = Z[A]/(A^4+1).
# Claim tested: for every nonzero anchor, det C(zeta)/C_ij(zeta)^2 is a rational number of sign (-1)^(i+j) (or 0),
# and a rational square in absolute value.
import random, itertools
from fractions import Fraction
import sympy as sp
A = sp.symbols('A'); PHI = sp.Poly(A**4+1, A, domain='QQ')

def zpow(k):            # A^k in Z[zeta8] as 4-tuple
    k %= 8; v = [0,0,0,0]
    if k < 4: v[k] = 1
    else: v[k-4] = -1
    return v
def loops(n, smooth):   # smooth: list of (i, type) ; type 0 = identity, 1 = cup-cap at strands i,i+1
    m = len(smooth); parent = list(range((m+1)*n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(x,y):
        x,y = find(x),find(y)
        if x != y: parent[x] = y
    for k,(i,t) in enumerate(smooth):
        for j in range(n):
            if t == 1 and j in (i,i+1): continue
            union(k*n+j, (k+1)*n+j)
        if t == 1:
            union(k*n+i, k*n+i+1); union((k+1)*n+i, (k+1)*n+i+1)
    for j in range(n): union(j, m*n+j)
    return len({find(x) for x in range((m+1)*n)})

def tensor_at_zeta(n, word, p, q):
    # word: list of (i, sign). crossing sign s: identity smoothing weight A^s, cup-cap weight A^-s
    others = [k for k in range(len(word)) if k not in (p,q)]
    C = {}
    for bi in (0,1):
        for bj in (0,1):
            tot = [0,0,0,0]
            for bits in itertools.product((0,1), repeat=len(others)):
                sm = [None]*len(word); e = 0
                sm[p] = (word[p][0], bi); sm[q] = (word[q][0], bj)
                for k,b in zip(others,bits):
                    sm[k] = (word[k][0], b); e += word[k][1] if b == 0 else -word[k][1]
                if loops(n, sm) == 1:
                    z = zpow(e); tot = [x+y for x,y in zip(tot,z)]
            C[(bi,bj)] = tot
    return C
def topoly(v): return sp.Poly(sum(c*A**k for k,c in enumerate(v)), A, domain='QQ')
def mulp(a,b): return (a*b).rem(PHI)
def is_square_rational(r):
    r = abs(Fraction(int(r.p), int(r.q)))
    import math
    return math.isqrt(r.numerator)**2 == r.numerator and math.isqrt(r.denominator)**2 == r.denominator

random.seed(1115)
tested = 0; anchors = 0; viol = []; unit_anchor = 0; nontrivial = 0
for trial in range(300):
    n = random.choice((3,4,5)); m = random.randint(6,11)
    word = [(random.randrange(n-1), random.choice((1,-1))) for _ in range(m)]
    p,q = random.sample(range(m), 2)
    C = tensor_at_zeta(n, word, p, q)
    P = {k: topoly(v) for k,v in C.items()}
    if all(pp.is_zero for pp in P.values()): continue
    tested += 1
    det = (mulp(P[(0,0)],P[(1,1)]) - mulp(P[(0,1)],P[(1,0)])).rem(PHI)
    if not det.is_zero: nontrivial += 1
    for (i,j),pp in P.items():
        if pp.is_zero: continue
        r = mulp(det, sp.invert(mulp(pp,pp), PHI))
        if r.degree() > 0: viol.append(('nonrational', n, word, p, q, (i,j), r)); continue
        r = sp.Rational(r.as_expr()); anchors += 1
        if r != 0 and sp.sign(r) != (-1)**(i+j): viol.append(('sign', n, word, p, q, (i,j), r))
        if not is_square_rational(r): viol.append(('nonsquare', n, word, p, q, (i,j), r))
        # unit-modulus anchor => integer square
        nrm = mulp(pp, sp.Poly(pp.as_expr().subs(A, -A**3), A, domain='QQ'))   # p * conj(p), conj: A -> A^-1 = -A^3
        if nrm.rem(PHI).as_expr() == 1:
            unit_anchor += 1
            if r.q != 1: viol.append(('unit anchor non-integer', n, word, p, q, (i,j), r))
print('diagrams with a nonzero corner:', tested, '| with det C(zeta) != 0:', nontrivial,
      '| nonzero anchors tested:', anchors, '| unit-modulus anchors:', unit_anchor)
print('violations:', len(viol))
for v in viol[:5]: print(v)
