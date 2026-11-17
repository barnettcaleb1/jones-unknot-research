#!/usr/bin/env python3
"""Exact Kauffman bracket by planar contraction (NOT the 2^n state sum).

Conventions (fixed; see validate_bracket.py for how they were pinned down):
  * PD code: each crossing is [a, b, c, d], the four edge labels read
    COUNTERCLOCKWISE around the crossing starting at the INCOMING UNDER
    strand, so a -> c is the under strand and {b, d} is the over strand
    (KnotTheory / spherogram PD_code convention).
  * Crossing sign: +1 iff the over strand runs d -> b.
  * A-smoothing of [a,b,c,d] joins (a,b) and (c,d);
    B-smoothing joins (a,d) and (b,c).
    <X> = A <X_A> + A^-1 <X_B>;  <D u O> = delta <D>;  delta = -A^2 - A^-2.
    Reduced bracket: <O> = 1.  (Absolute bracket = reduced * delta.)
  * Jones: V = (-A^3)^(-w) <D>_reduced,  t = A^(-4).
    With these choices sigma_i (positive braid generator) = A I + A^-1 e_i.

Laurent polynomials in A are dicts {exponent: int}; all arithmetic is exact
Python integer arithmetic.
"""
from collections import defaultdict

# ---------------------------------------------------------------- Laurent


def pclean(p):
    return {e: c for e, c in p.items() if c}


def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        v = r.get(e, 0) + c
        if v:
            r[e] = v
        else:
            r.pop(e, None)
    return r


def psub(p, q):
    return padd(p, {e: -c for e, c in q.items()})


def pmul(p, q):
    r = defaultdict(int)
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1 + e2] += c1 * c2
    return pclean(r)


def pshift(p, k):
    return {e + k: c for e, c in p.items()}


def pscale(p, c):
    return pclean({e: c * v for e, v in p.items()})


def ppow(p, n):
    assert n >= 0
    r = {0: 1}
    for _ in range(n):
        r = pmul(r, p)
    return r


def pstr(p, var='A'):
    if not p:
        return '0'
    terms = []
    for e in sorted(p):
        c = p[e]
        if e == 0:
            terms.append(f'{c:+d}')
        elif e == 1:
            terms.append(f'{c:+d}*{var}')
        else:
            terms.append(f'{c:+d}*{var}^{e}')
    return ' '.join(terms)


DELTA = {2: -1, -2: -1}
ONE = {0: 1}


def pdivexact(p, q):
    """Exact division of Laurent polynomials; raises if not exact."""
    if not p:
        return {}
    q = pclean(q)
    qmax = max(q)
    qlead = q[qmax]
    rem = dict(p)
    quot = {}
    guard = 0
    while rem:
        rmax = max(rem)
        c = rem[rmax]
        if c % qlead:
            raise ArithmeticError('not exactly divisible (coefficient)')
        if rmax - qmax < min(rem) - max(q) - 1 and guard > 10 ** 5:
            raise ArithmeticError('division does not terminate')
        f = c // qlead
        quot[rmax - qmax] = f
        rem = psub(rem, pshift(pscale(q, f), rmax - qmax))
        guard += 1
        if guard > 10 ** 5:
            raise ArithmeticError('division does not terminate')
    # verify
    if pmul(quot, q) != pclean(p):
        raise ArithmeticError('not exactly divisible (verification)')
    return pclean(quot)


def peval_int(p, a):
    """Evaluate at an integer A=a (a != 0); returns a Fraction-free integer
    only if all exponents are >= 0, else a Fraction."""
    from fractions import Fraction
    s = Fraction(0)
    for e, c in p.items():
        s += c * Fraction(a) ** e
    return s


# ---------------------------------------------------------------- bracket


def _absorb_pairs(matching, pairs):
    """Absorb the arcs in `pairs` into the open-end matching (a dict
    label -> partner).  Returns (new_matching, loops_closed)."""
    m = dict(matching)
    loops = 0
    for x, y in pairs:
        if x == y:
            # an edge whose two ends are joined by this arc: closed loop
            if x in m:
                raise RuntimeError('label used three times')
            loops += 1
            continue
        xo, yo = x in m, y in m
        if xo and yo:
            px, py = m.pop(x), m.pop(y)
            if px == y:              # arc closes onto itself
                loops += 1
            else:
                m[px] = py
                m[py] = px
        elif xo:
            px = m.pop(x)
            m[px] = y
            m[y] = px
        elif yo:
            py = m.pop(y)
            m[py] = x
            m[x] = py
        else:
            m[x] = y
            m[y] = x
    return m, loops


def _order_crossings(pd):
    """Greedy order: repeatedly pick the crossing minimising the open
    frontier after absorption."""
    remaining = list(range(len(pd)))
    seen = defaultdict(int)       # label -> number of ends absorbed
    order = []
    open_count = 0
    while remaining:
        best, best_val = None, None
        for i in remaining:
            delta_open = 0
            for lab in pd[i]:
                delta_open += -1 if seen[lab] == 1 else +1
            # labels appearing twice within the same crossing: count once
            labs = list(pd[i])
            dup = len(labs) - len(set(labs))
            delta_open -= 2 * dup
            val = open_count + delta_open
            if best is None or val < best_val:
                best, best_val = i, val
        order.append(best)
        remaining.remove(best)
        for lab in pd[best]:
            seen[lab] += 1
        open_count = best_val
    return order


def bracket(pd, free_loops=0, reduced=True):
    """Kauffman bracket of a PD code.  `free_loops` = number of crossingless
    unknotted components not represented in the PD (each contributes a
    factor delta).  Returns a Laurent polynomial dict in A."""
    pd = [tuple(row) for row in pd]
    if not pd:
        # no crossings: a single circle (plus free loops)
        total = 1 + free_loops
        p = ppow(DELTA, total - 1) if reduced else ppow(DELTA, total)
        return p
    order = _order_crossings(pd)
    states = {frozenset(): {0: 1}}      # matching (frozenset of pairs) -> poly
    for i in order:
        a, b, c, d = pd[i]
        new_states = defaultdict(dict)
        for key, poly in states.items():
            matching = {}
            for pr in key:
                x, y = tuple(pr)
                matching[x] = y
                matching[y] = x
            for sm, (pairs, shift) in enumerate((( ((a, b), (c, d)), +1),
                                                  ( ((a, d), (b, c)), -1))):
                m2, loops = _absorb_pairs(matching, pairs)
                k2 = frozenset(frozenset((x, y)) for x, y in m2.items() if x < y)
                # for mixed-type labels fall back to a canonical pair key
                if len(k2) * 2 != len(m2):
                    k2 = frozenset(frozenset((x, y)) for x, y in m2.items())
                term = pshift(poly, shift)
                if loops:
                    term = pmul(term, ppow(DELTA, loops))
                new_states[k2] = padd(new_states[k2], term)
        states = {k: v for k, v in new_states.items() if v}
    assert len(states) == 1 and frozenset() in states, states.keys()
    absolute = states[frozenset()]
    if free_loops:
        absolute = pmul(absolute, ppow(DELTA, free_loops))
    if not reduced:
        return absolute
    return pdivexact(absolute, DELTA)


def pd_writhe(pd):
    """Writhe from a PD code whose labels run consecutively along each
    component (spherogram / KnotTheory numbering)."""
    w = 0
    for a, b, c, d in pd:
        if b == d + 1:
            w += 1
        elif d == b + 1:
            w -= 1
        else:                      # wrap-around at the end of a component
            w += 1 if b < d else -1
    return w


def jones_A(pd, writhe, free_loops=0):
    """V as a Laurent polynomial in A: (-A^3)^(-w) <D>_reduced."""
    br = bracket(pd, free_loops=free_loops, reduced=True)
    sign = (-1) ** (writhe % 2)
    return pscale(pshift(br, -3 * writhe), sign)


def A_to_t(pA):
    """Convert a Laurent polynomial in A with all exponents divisible by 4
    into one in t = A^-4.  Raises if some exponent is not divisible by 4
    (for links use A_to_sqrt_t)."""
    out = {}
    for e, c in pA.items():
        if e % 4:
            raise ValueError(f'exponent {e} not divisible by 4: not a polynomial in t')
        out[-e // 4] = c
    return out


def A_to_sqrt_t(pA):
    """Convert to a polynomial in s = t^(1/2) = A^-2 (links)."""
    out = {}
    for e, c in pA.items():
        if e % 2:
            raise ValueError(f'exponent {e} odd: not a polynomial in t^(1/2)')
        out[-e // 2] = c
    return out


def jones_t(pd, writhe, free_loops=0):
    return A_to_t(jones_A(pd, writhe, free_loops))


def eval_t(pt, t):
    """Exact evaluation of a polynomial in t (dict) at an integer t."""
    from fractions import Fraction
    s = Fraction(0)
    for e, c in pt.items():
        s += c * Fraction(t) ** e
    return s
