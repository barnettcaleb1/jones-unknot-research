# Planar Moody polynomials and disk sequences from reduced cut-words.
# Model: punctures p1..pn on a horizontal line, base point p* on the bottom boundary.
# Cuts e_0=[left bdry,p1], e_1=[p1,p2]=alpha, ..., e_{n-1}=[p_{n-1},p_n].  The complement is a disk,
# so pi_1(D_n,p*) is free on the dual loops u_0..u_{n-1} (u_j crosses e_j upward once, and is
# clockwise around p_{j+1..n}).  A reduced u-word = crossing sequence of a representative in minimal
# position with every cut simultaneously (geodesic argument), so the letters +-u_1 of the arc's word
# are exactly the iota(alpha,beta) points of alpha cap beta, in order along beta.
# Letter encoding: u_j <-> j+1.   x_k = u_k u_{k-1}^-1 (k<n), x_n = u_{n-1}^-1.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lp import *

def to_u(w, n):
    out = []
    for x in w:
        k = abs(x)
        img = [k + 1, -k] if k < n else [-n]
        out += img if x > 0 else finv(img)
    return fred(out)

def ab_u(L, n):
    """abelianisation (vector over punctures 1..n) of letter u_{L-1}^{+-1}"""
    j = abs(L) - 1
    v = [0] * n
    for m in range(j + 1, n + 1):
        v[m - 1] = -1
    return v if L > 0 else [-a for a in v]

def arc_from_loop(w_u, end=3):
    """w_u = reduced u-word of the boundary loop of the arc (conjugate of x_end). return v."""
    L = len(w_u)
    assert L % 2 == 0, "loop word must have even length"
    h = (L - 2) // 2
    v, c, vb = w_u[:h], w_u[h:h + 2], w_u[h + 2:]
    assert vb == finv(v), "not of the form v c v^-1"
    return v, c

def crossings(v, n):
    """alpha-crossings of the arc with cut-word v: list of (eps, labelvector)"""
    K = [0] * n
    a1 = ab_u(2, n)
    out = []
    for L in v:
        if L == 2:
            out.append((-1, tuple(K)))          # upward crossing: beta directed up, eps=-1
            K = [a + b for a, b in zip(K, a1)]
        elif L == -2:
            K = [a - b for a, b in zip(K, a1)]
            out.append((+1, tuple(K)))          # downward crossing: eps=+1, label = sheet below
        else:
            d = ab_u(L, n)
            K = [a + b for a, b in zip(K, d)]
    return out

def analyse(braid, n, end=3):
    w = to_u(act_word(braid, [end]), n)
    v, c = arc_from_loop(w, end)
    cr = crossings(v, n)
    ks = [sum(lab) for _, lab in cr]
    k0 = ks[0] if ks else 0
    terms = [(e, k - k0) for (e, _), k in zip(cr, ks)]
    disks = []
    for i in range(len(cr) - 1):
        D = [b - a for a, b in zip(cr[i][1], cr[i + 1][1])]
        nz = [x for x in D if x]
        simple = len(set(nz)) == 1 and abs(nz[0]) == 1 if nz else False
        P = frozenset(m + 1 for m, x in enumerate(D) if x)
        W = sum(D)
        changing = cr[i][0] != cr[i + 1][0]
        disks.append(dict(P=P, W=W, changing=changing, simple=simple))
    return dict(v=v, core=c, terms=terms, disks=disks, loop=w)

def moody_poly(terms):
    M = {}
    for e, k in terms:
        M[k] = M.get(k, 0) + e
    return lp(M)

def parity_ok(disks):
    return all(d['changing'] == (len(d['P']) % 2 == 1) for d in disks)

def M_at_minus1(terms):
    return sum(e * (-1) ** (k % 2) for e, k in terms)

def homological_pairing(w_u, n):
    """sum over all u_1 letters of the LOOP of eps * t^label (Z-exponent); should be (1 - t^{+-1}) M"""
    K = 0
    a1 = sum(ab_u(2, n))
    P = {}
    for L in w_u:
        if L == 2:
            P[K] = P.get(K, 0) - 1; K += a1
        elif L == -2:
            K -= a1; P[K] = P.get(K, 0) + 1
        else:
            K += sum(ab_u(L, n))
    return lp(P)
