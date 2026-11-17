#!/usr/bin/env python3
"""
common.py -- shared helpers for the cx-clasp computation (two-slot shell,
forced double corner C00*).

Everything is exact: Laurent polynomials in A are dicts {exponent: int}
(the representation used by cx-tools/bracket.py), and evaluations at
A = zeta_8 = exp(i pi/4) are done in Z[zeta_8] with integer 4-vectors.

Conventions are those of cx-tools/bracket.py (validated in VALIDATION.md):
  <X> = A <X_A> + A^-1 <X_B>,  <O> = 1 (reduced bracket),  delta = -A^2 - A^-2,
  PD [a,b,c,d] counterclockwise from the incoming under-strand,
  A-smoothing joins (a,b),(c,d);  V(t) = (-A^3)^(-w) <D>,  t = A^-4.
The "absolute" bracket (empty diagram = 1, <O> = delta) is delta times the
reduced one; every comparison below is done up to units +-A^k, so the two
normalisations never differ for our purposes except by the factor delta,
which we never need.
"""

import os
import sys
import math

TOOLS = "/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-tools"
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

from bracket import (pclean, padd, pneg, pscale, pshift, pmul, ppow, DELTA,  # noqa: E402
                     pstr, Diagram, pd_mirror, kauffman_bracket,
                     kauffman_bracket_naive, jones_from_bracket, jones_str,
                     jones_from_pd)
from twist import Builder, braid_closure_pd  # noqa: E402

WORKDIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
# Laurent polynomial extras
# ----------------------------------------------------------------------

ONE = {0: 1}


def psub(p, q):
    return padd(p, pneg(q))


def pmirror(p):
    """A -> A^-1 (bracket of the mirror-image diagram)."""
    return {-e: c for e, c in p.items()}


def pspan(p):
    return (max(p) - min(p)) if p else 0


def pclasses(p):
    """Set of residues mod 4 of the exponents that occur."""
    return sorted({e % 4 for e in p})


def normalise_unit(p):
    """Canonical representative of p up to units +-A^k: shift the lowest
    exponent to 0 and make the lowest coefficient positive.  Returns
    (canonical tuple of (exp, coef)), or () for 0."""
    p = pclean(p)
    if not p:
        return ()
    m = min(p)
    s = 1 if p[m] > 0 else -1
    return tuple(sorted((e - m, s * c) for e, c in p.items()))


def unit_equiv(p, q):
    """If p == sign * A^k * q return (sign, k), else None."""
    p = pclean(p)
    q = pclean(q)
    if not p or not q:
        return (1, 0) if p == q else None
    if normalise_unit(p) != normalise_unit(q):
        return None
    k = min(p) - min(q)
    sign = 1 if p[min(p)] * q[min(q)] > 0 else -1
    return (sign, k)


def poly_in_t(p):
    """Write p (all exponents in one class c mod 4) as A^c * P(t), t = A^-4,
    with 0 <= c < 4; returns (c, {m: coef}) where P = sum coef t^m.
    Raises ValueError if the exponents are not all congruent mod 4."""
    p = pclean(p)
    cl = pclasses(p)
    if len(cl) > 1:
        raise ValueError("exponents in several classes mod 4: %r" % cl)
    c = cl[0] if cl else 0
    out = {}
    for e, coef in p.items():
        out[-(e - c) // 4] = coef
    return c, out


def tstr(P, var="t"):
    """Pretty-print {m: coef} as a Laurent polynomial in t."""
    return pstr(P, var=var)


def t_up_to_units(p):
    """Canonical form in t up to units: lowest term t^0 with positive coefficient.
    Returns string, or None if p is not in a single class mod 4."""
    try:
        c, P = poly_in_t(p)
    except ValueError:
        return None
    if not P:
        return "0"
    m = min(P)
    s = 1 if P[m] > 0 else -1
    Q = {k - m: s * v for k, v in P.items()}
    return tstr(Q)


def half_t_str(p):
    """Any bracket as a polynomial in t^(1/2) = A^-2 (needs even exponents)."""
    V = {}
    for e, c in p.items():
        if e % 2:
            raise ValueError("odd exponent %d" % e)
        V[-e // 2] = c
    return jones_str(V)


# ----------------------------------------------------------------------
# Z[zeta_8] exact arithmetic (zeta^4 = -1); vectors [a0,a1,a2,a3]
# ----------------------------------------------------------------------

def z8_zero():
    return [0, 0, 0, 0]


def z8_power(k):
    """zeta_8^k as a vector."""
    k %= 8
    v = z8_zero()
    if k < 4:
        v[k] = 1
    else:
        v[k - 4] = -1
    return v


def z8_add(x, y):
    return [a + b for a, b in zip(x, y)]


def z8_scale(x, c):
    return [c * a for a in x]


def z8_mul(x, y):
    prod = [0] * 7
    for i in range(4):
        for j in range(4):
            prod[i + j] += x[i] * y[j]
    out = prod[:4]
    for k in range(4, 7):
        out[k - 4] -= prod[k]
    return out


def z8_conj(x):
    """Complex conjugation: zeta -> zeta^-1 = -zeta^3."""
    a0, a1, a2, a3 = x
    return [a0, -a3, -a2, -a1]


def z8_eval(p):
    """p(zeta_8) for a Laurent polynomial p in A."""
    v = z8_zero()
    for e, c in p.items():
        v = z8_add(v, z8_scale(z8_power(e), c))
    return v


def z8_norm2(x):
    """|x|^2 = x * conj(x); must be a rational integer (vector [N,0,0,0])."""
    n = z8_mul(x, z8_conj(x))
    assert n[1] == n[2] == n[3] == 0, "norm not rational: %r" % (n,)
    return n[0]


def z8_str(x):
    terms = []
    names = ["", "z", "z^2", "z^3"]
    for k in range(4):
        if x[k]:
            terms.append("%+d%s" % (x[k], ("*" + names[k]) if k else ""))
    return " ".join(terms) if terms else "0"


def det_from_bracket(p):
    """Determinant of the link = |<D>(zeta_8)| = |V(-1)|, exactly."""
    n2 = z8_norm2(z8_eval(p))
    r = math.isqrt(n2)
    assert r * r == n2, "|x|^2 = %d is not a perfect square" % n2
    return r


def det_from_jones(V):
    """|V(-1)| from the half-exponent Jones dict, using t^(1/2) = i."""
    re = im = 0
    for k, c in V.items():
        q = k % 4
        if q == 0:
            re += c
        elif q == 1:
            im += c
        elif q == 2:
            re -= c
        else:
            im -= c
    n2 = re * re + im * im
    r = math.isqrt(n2)
    assert r * r == n2
    return r


# ----------------------------------------------------------------------
# Diagram surgery on PD codes (Builder from cx-tools/twist.py)
# ----------------------------------------------------------------------

def _site_darts(pd, e1, e2, face=None):
    """Locate the identity 2-tangle formed by edges e1, e2 bounding a common
    face (same logic as twist.insert_full_twists).  Returns
    (P1, Q1, P2, Q2): e1 runs P1 -> Q1 and e2 runs P2 -> Q2 in the
    face-on-the-left walk, so P1,Q2 are the 'bottom' ends and Q1,P2 the
    'top' ends of the site."""
    D = Diagram(pd)
    faces = D.faces()
    for fi, f in enumerate(faces):
        if face is not None and fi != face:
            continue
        d1 = [(fr, to) for e, fr, to in f if e == e1]
        d2 = [(fr, to) for e, fr, to in f if e == e2]
        if d1 and d2:
            (P1, Q1), (P2, Q2) = d1[0], d2[0]
            return P1, Q1, P2, Q2
    raise ValueError("edges %r and %r do not bound a common face" % (e1, e2))


def turn_back_site(pd, e1, e2, face=None):
    """Replace the identity 2-tangle (edges e1, e2 bounding a common face)
    by the cup-cap tangle: the top ends are joined, the bottom ends are
    joined.  Returns a new PD code (labels 1..2n)."""
    P1, Q1, P2, Q2 = _site_darts(pd, e1, e2, face)
    b = Builder.from_pd(pd)
    b.disconnect(P1)
    b.disconnect(P2)
    b.connect(Q2, P1)       # cup: bottom ends
    b.connect(P2, Q1)       # cap: top ends
    return b.pd_code()


def connected_sum_links(pd1, pd2, e1=None, e2=None):
    """Connected sum of two link diagrams along edge e1 of pd1 and edge e2 of
    pd2 (defaults: first edge of the first component of each), splicing
    with consistent orientation.  Works for links (no knot restriction)."""
    D1 = Diagram(pd1)
    D2 = Diagram(pd2)
    n1 = len(pd1)
    if e1 is None:
        e1 = D1.components[0][0]
    if e2 is None:
        e2 = D2.components[0][0]
    b = Builder()
    b.ncross = n1 + len(pd2)
    for e, (p, q) in D1.occ.items():
        b.connect(p, q)
    for e, (p, q) in D2.occ.items():
        b.connect((p[0] + n1, p[1]), (q[0] + n1, q[1]))
    t1, h1 = D1.tail[e1], D1.head[e1]
    t2 = (D2.tail[e2][0] + n1, D2.tail[e2][1])
    h2 = (D2.head[e2][0] + n1, D2.head[e2][1])
    b.disconnect(t1)
    b.disconnect(t2)
    b.connect(t1, h2)
    b.connect(t2, h1)
    starts = [h1] + [D1.head[c[0]] for c in D1.components[1:]]
    starts += [(D2.head[c[0]][0] + n1, D2.head[c[0]][1]) for c in D2.components[1:]]
    return b.pd_code(starts=starts)


def disjoint_union_bracket(p, q):
    """Reduced bracket of a split union: delta * <D1> * <D2>."""
    return pmul(DELTA, pmul(p, q))


# ----------------------------------------------------------------------
# link data record
# ----------------------------------------------------------------------

def link_record(name, pd, naive_check=True):
    """Compute bracket, Jones, det, linking numbers, writhe for a PD code."""
    D = Diagram(pd)
    br = kauffman_bracket(pd)
    if naive_check and len(pd) <= 14:
        assert kauffman_bracket_naive(pd) == br, "naive state sum disagrees for %s" % name
    w = D.writhe()
    V = jones_from_bracket(br, w)
    det = det_from_bracket(br)
    det2 = det_from_jones(V)
    assert det == det2
    lk = D.linking_matrix()
    return {
        "name": name,
        "pd": [list(x) for x in pd],
        "crossings": len(pd),
        "components": D.num_components(),
        "writhe": w,
        "bracket": {str(e): c for e, c in sorted(br.items())},
        "bracket_str": pstr(br),
        "jones_str": jones_str(V),
        "det": det,
        "linking": {"%d,%d" % k: v for k, v in sorted(lk.items())},
        "lk_abs_sorted": sorted(abs(v) for v in lk.values()),
        "lk_total": sum(lk.values()),
        "span": pspan(br),
        "classes_mod4": pclasses(br),
        "_bracket": br,
    }


def strip_private(rec):
    return {k: v for k, v in rec.items() if not k.startswith("_")}
