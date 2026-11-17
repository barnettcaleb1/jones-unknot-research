#!/usr/bin/env python3
"""Referee library (independent of mech2/twobridge/scripts).
 - Laurent polynomials in one variable as dicts {exponent: integer coefficient}
 - Kauffman bracket of a kht++ Morse word by planar matchings (Temperley-Lieb states)
 - kht++ quotient-tangle word of a strongly invertible half-diagram (re-implemented from Tangle::quotient, Tangles.cpp:967)
 - full symmetric knot diagram of a half-diagram
 - J from saved Kh~ components (b-generator rule of BRIEF2 / tools/gtilde.py jset, re-implemented)
 - the 2x2 matrix formula of Theorem A
"""
from fractions import Fraction as Fr

# ---------- Laurent polynomials ----------
def padd(p, q, c=1):
    r = dict(p)
    for e, v in q.items():
        w = r.get(e, 0) + c * v
        if w: r[e] = w
        else: r.pop(e, None)
    return r
def pmul(p, q):
    r = {}
    for e1, v1 in p.items():
        for e2, v2 in q.items():
            e = e1 + e2
            w = r.get(e, 0) + v1 * v2
            if w: r[e] = w
            else: r.pop(e, None)
    return r
def pshift(p, k, c=1):
    return {e + k: c * v for e, v in p.items()}
def pstr(p, var='t'):
    if not p: return '0'
    out = []
    for e in sorted(p):
        v = p[e]
        s = '+' if v > 0 else '-'
        a = abs(v)
        mon = '' if e == 0 else (var if e == 1 else '%s^%d' % (var, e))
        out.append('%s %s%s' % (s, '' if (a == 1 and mon) else str(a), mon))
    s = ' '.join(out)
    return s[2:] if s.startswith('+ ') else s
def pnorm(p):
    """normalise up to a unit +-var^n: lowest exponent 0 with positive coefficient. returns tuple of coefficients"""
    if not p: return ()
    lo = min(p); hi = max(p)
    sgn = 1 if p[lo] > 0 else -1
    return tuple(sgn * p.get(e, 0) for e in range(lo, hi + 1))
def pflip(p):
    return {-e: v for e, v in p.items()}
def is_unit(p):
    return len(p) == 1 and abs(next(iter(p.values()))) == 1

# ---------- Kauffman bracket of a Morse word ----------
# state: tuple m, points 0..ntop-1 = top ends, ntop.. = current bottom ends (left to right); m[p] = partner of p.
# kht++ conventions (lit/kht/REPORT.md 2.2, 4.4): x_i = over-strand from top left: <x_i> = A*U_i + A^-1*id ;
#                                               y_i = over-strand from top right: <y_i> = A*id + A^-1*U_i .
DELTA = {2: -1, -2: -1}
def _cap(m, ntop, i):
    """insert two new bottom points at bottom positions i, i+1, matched to each other"""
    a = ntop + i
    if i < 0 or a > len(m): raise ValueError('cap out of range')
    def sh(p): return p if p < a else p + 2
    new = [None] * (len(m) + 2)
    for p, q in enumerate(m):
        new[sh(p)] = sh(q)
    new[a] = a + 1; new[a + 1] = a
    return tuple(new)
def _cup(m, ntop, i):
    """join bottom points i, i+1. returns (new state, number of closed loops created)"""
    a = ntop + i; b = a + 1
    if i < 0 or b >= len(m): raise ValueError('cup out of range')
    loops = 0
    m2 = list(m)
    if m2[a] == b:
        loops = 1
    else:
        p, q = m2[a], m2[b]
        m2[p] = q; m2[q] = p
    def sh(p): return p if p < a else p - 2
    new = [None] * (len(m) - 2)
    for p, q in enumerate(m2):
        if p in (a, b): continue
        new[sh(p)] = sh(q)
    return tuple(new), loops
def parse_word(word):
    out = []
    for tok in word.strip().strip('.').split('.'):
        if not tok: continue
        out.append((tok[0], int(tok[1:])))
    return out
def bracket(word, ntop):
    """Kauffman bracket state vector {state: Laurent poly in A} of the Morse word (list of (letter,index) or string),
    starting from ntop vertical strands."""
    if isinstance(word, str): word = parse_word(word)
    m0 = tuple(list(range(ntop, 2 * ntop)) + list(range(ntop)))
    vec = {m0: {0: 1}}
    for (c, i) in word:
        new = {}
        def acc(st, pol):
            if st in new:
                r = padd(new[st], pol)
                if r: new[st] = r
                else: del new[st]
            elif pol: new[st] = pol
        for st, pol in vec.items():
            if c in 'lr':
                acc(_cap(st, ntop, i), pol)
            elif c == 'u':
                s2, loops = _cup(st, ntop, i)
                acc(s2, pmul(pol, DELTA) if loops else pol)
            elif c in 'xy':
                s2, loops = _cup(st, ntop, i)
                s3 = _cap(s2, ntop, i)
                pu = pmul(pol, DELTA) if loops else pol
                if c == 'x':
                    acc(s3, pshift(pu, 1)); acc(st, pshift(pol, -1))
                else:
                    acc(st, pshift(pol, 1)); acc(s3, pshift(pu, -1))
            else:
                raise ValueError(c)
        vec = new
    return vec

# ---------- strongly invertible half-diagrams ----------
def half_letters(word):
    """'s.l1.y0.x1.u2' -> list of (letter,index) without the 's'"""
    w = word.strip()
    assert w.startswith('s.')
    return parse_word(w[2:])
def half_writhe(letters):
    """writhe of the full symmetric knot diagram, computed from scratch (orientations propagated on the full diagram)."""
    full = full_word(letters)
    return writhe_closed(full)
def quotient_word(letters, framing=None):
    """kht++ Tangle::quotient: 1-3 tangle word (one top end = axis). framing: number of pairs of twists on (b2,b3):
    None -> no framing correction (J is insensitive to it up to a unit)."""
    out = [('r', 1), ('r', 2)]
    for (c, i) in letters:
        if c in 'xy':
            if i == 0:
                out += [(c, 0), (c, 1), (c, 1), (c, 0)]
            else:
                out += [(c, 2 * i), (c, 2 * i - 1), (c, 2 * i + 1), (c, 2 * i)]
        elif c in 'lr':
            out += [(c, 2 * i - 1), (c, 2 * i)]
        elif c == 'u':
            out += [(c, 2 * i), (c, 2 * i - 1)]
    out.append(('u', 0))
    if framing:
        tw = 'x' if framing > 0 else 'y'
        out += [(tw, 1)] * (2 * abs(framing))
    return out
def J_bracket(letters):
    """coefficient of e_0 = (top-b3)(b1-b2) in the Kauffman bracket of the quotient tangle, as Laurent poly in A,
    and the coefficient of e_inf = (top-b1)(b2-b3)."""
    vec = bracket(quotient_word(letters), 1)
    e0 = (3, 2, 1, 0)       # top(0)-b3(3), b1(1)-b2(2)
    einf = (1, 0, 3, 2)     # top-b1, b2-b3
    assert set(vec) <= {e0, einf}, vec.keys()
    return vec.get(e0, {}), vec.get(einf, {})
def A_to_t(p):
    """p(A) = +-A^k * f(A^-4)  ->  f as Laurent poly in t = A^-4 (dict), up to a unit. raises if not of that form."""
    if not p: return {}
    e0 = min(p)
    r = {}
    for e, v in p.items():
        d = e - e0
        if d % 4: raise ValueError('not a polynomial in A^4 up to a unit: %r' % p)
        r[-(d // 4)] = v
    return r
def full_word(letters):
    """full symmetric knot diagram (closed: 0 top ends, 0 bottom ends) of a half-diagram. The half-diagram has an axis
    (position 0) and strands at positions 1..h; the full diagram has strands -h..-1, 1..h, indexed 0..2h-1:
    half position i (1..h) -> index h-1+i, its image under the rotation -> index h-i. The rotation about the vertical
    axis preserves the kht crossing type (x stays x)."""
    out = [('r', 0)]          # top cap through the axis; h = 1
    h = 1
    for (c, i) in letters:
        if c in 'xy':
            if i == 0:
                out.append((c, h - 1))
            else:
                # right copy on strands (h-1+i, h+i), left copy on strands (h-i-1, h-i); do the right one first
                out.append((c, h - 1 + i)); out.append((c, h - i - 1))
        elif c in 'lr':
            # new cap at half positions (i, i+1): right copy inserted at index h-1+i, left copy at mirrored place
            # insert right copy first: full index h-1+i ; then left copy at full index h-i+1 ... careful: positions
            # before insertion: half position i..h on the right sit at h-1+i.., on the left h-i..0.
            # right cap is inserted so that it occupies half positions i, i+1 -> pushes right strands >= i outward.
            out.append((c, h - 1 + i))
            # left cap occupies mirrored positions -(i+1), -i : it is inserted at full index (h - i + 1) counted from
            # the left: the left strands with half position >= i (indices 0..h-i) stay outside; so insert at h-i+1.
            oc = 'l' if c == 'r' else 'r'
            out.append((oc, h - i + 1))
            h += 2
        elif c == 'u':
            out.append((c, h - 1 + i)); out.append((c, h - i - 1))
            h -= 2
    assert h == 1, 'half diagram does not end with one strand'
    out.append(('u', 0))
    return out
def knot_bracket(letters):
    vec = bracket(full_word(letters), 0)
    assert list(vec.keys()) == [()], vec.keys()
    p = vec[()]
    # divide by delta (unknot normalised to 1): p = delta * r
    return pdiv_exact(p, DELTA)
def pdiv_exact(p, d):
    """exact division of Laurent polynomials (d with unit leading coefficient)"""
    p = dict(p); r = {}
    dh = max(d); dl = d[dh]
    assert abs(dl) == 1
    while p:
        ph = max(p)
        c = p[ph] * dl
        k = ph - dh
        r[k] = r.get(k, 0) + c
        p = padd(p, pshift(d, k), -c)
        if p and max(p) >= ph: raise ValueError('division failed')
        if p and (max(p) - min(p)) < (max(d) - min(d)): raise ValueError('not divisible')
    return r
def det_from_bracket(p):
    """|p(A)| at A = exp(i pi/4), must be an integer"""
    c = [0, 0, 0, 0]
    for e, v in p.items():
        k = e % 8
        if k >= 4: c[k - 4] -= v
        else: c[k] += v
    # z = c0 + c1 w + c2 w^2 + c3 w^3, w = e^{i pi/4};  |z|^2 = c0^2+c1^2+c2^2+c3^2 + sqrt2*(c0c1+c1c2+c2c3-c0c3)
    n2 = c[0]**2 + c[1]**2 + c[2]**2 + c[3]**2
    cross = c[0]*c[1] + c[1]*c[2] + c[2]*c[3] - c[0]*c[3]
    assert cross == 0, ('non-integer modulus', c)
    import math
    r = math.isqrt(n2)
    assert r * r == n2
    return r

# ---------- J from saved Kh~ components ----------
def J_from_khr(khr):
    """b-generators: (24j+2k, 4j) and, for every special at (c,d): (c+4, d-1), (c-4, d); (q,delta) labels.
    h = q/2 - delta; J = sum (-1)^h t^(q/2). returns (k, j, dict in t) or None if the record is not of the standard shape."""
    rs = [c for c in khr if c['type'] == 'r']
    if len(rs) != 1: return None
    r = rs[0]
    try: k = int(r['slope'])
    except Exception: return None
    qr = Fr(r['q']).limit_denominator(1000)
    j = (qr - Fr(k * (abs(k) + 2), abs(k) + 1)) / 24
    if j.denominator != 1: return None
    j = int(j)
    pts = [(24 * j + 2 * k, 4 * j)]
    for c in khr:
        if c['type'] == 's':
            if c['slope'] != '∞': return None
            L = int(c['len']) if c['len'] else 1
            if L != 4: return None
            q = Fr(c['q']).limit_denominator(1000); d = Fr(c['delta']).limit_denominator(1000)
            if q.denominator != 1 or d.denominator != 1: return None
            q = int(q); d = int(d)
            pts.append((q + 4, d - 1)); pts.append((q - 4, d))
    J = {}
    for (q, d) in pts:
        if q % 2: return None
        h = q // 2 - d
        J = padd(J, {q // 2: (-1) ** (h % 2)})
    return k, j, J, pts

# ---------- matrix formula of Theorem A ----------
# vectors (v1, v2) of Laurent polynomials in t.
def act(letter, v):
    v1, v2 = v
    if letter == 'Y':      # [[1,0],[t^-3,t^-3]]
        return (v1, pshift(padd(v1, v2), -3))
    if letter == 'y':      # inverse: [[1,0],[-1,t^3]]
        return (v1, padd(pshift(v2, 3), v1, -1))
    if letter == 'X':      # [[1,1-t^4],[0,-t]]
        return (padd(v1, padd(v2, pshift(v2, 4), -1)), pshift(v2, 1, -1))
    if letter == 'x':      # inverse: [[1, t^-1 - t^3],[0,-t^-1]]
        return (padd(v1, padd(pshift(v2, -1), pshift(v2, 3), -1)), pshift(v2, -1, -1))
    raise ValueError(letter)
def J_matrix(word):
    """word = string in X,Y,x,y; first letter nearest the cap (applied first)"""
    v = ({0: 1}, {})
    for L in word: v = act(L, v)
    return v[0]
def writhe_closed(word):
    """writhe of a closed diagram given as Morse word with 0 top ends (orient strands by tracing)."""
    # build the diagram as a list of arcs: track strand ids at each level; crossings join; orientation by traversal.
    # Each level: list of 'edge ids' for the current strands. Edges are created at caps/crossings.
    nxt = [0]
    def newid():
        nxt[0] += 1; return nxt[0]
    cur = []
    # adjacency of edge-ends: we build a graph whose vertices are (edge id, 'top'/'bot'); crossing connects through.
    # simpler: every strand segment between events is an edge with a top end and a bottom end. Record connections:
    conn = {}   # (edge,'t') or (edge,'b') -> (edge', end')
    cross = []  # (letter, top-left edge, top-right edge, bottom-left edge, bottom-right edge)
    def link(a, b):
        conn[a] = b; conn[b] = a
    for (c, i) in word:
        if c in 'lr':
            a, b = newid(), newid()
            link((a, 't'), (b, 't'))
            cur[i:i] = [a, b]
        elif c == 'u':
            a, b = cur[i], cur[i + 1]
            link((a, 'b'), (b, 'b'))
            del cur[i:i + 2]
        else:
            tl, tr = cur[i], cur[i + 1]
            bl, br = newid(), newid()
            # strands cross: top-left continues to bottom-right, top-right to bottom-left
            link((tl, 'b'), (br, 't')); link((tr, 'b'), (bl, 't'))
            cross.append((c, tl, tr, bl, br))
            cur[i], cur[i + 1] = bl, br
    assert not cur
    # orient: traverse from edge 1 top end
    direction = {}  # edge -> +1 if traversed top->bottom (downwards), -1 if upwards
    e, end = 1, 't'
    count = 0
    while True:
        # we are entering edge e at 'end'
        direction[e] = +1 if end == 't' else -1
        other = (e, 'b' if end == 't' else 't')
        e2, end2 = conn[other]
        e, end = e2, end2
        count += 1
        if (e, end) == (1, 't'): break
        if count > 10 ** 6: raise RuntimeError
    ncomp_edges = len(direction)
    total_edges = nxt[0]
    w = 0
    for (c, tl, tr, bl, br) in cross:
        if tl not in direction or tr not in direction:
            raise ValueError('diagram is a link, not a knot')
        dl, dr = direction[tl], direction[tr]   # +1 = downwards
        # x: over-strand is tl->br. y: over-strand is tr->bl.
        # sign: both strands pointing the same vertical direction: x (over from top-left to bottom-right, both down):
        # over direction (1,-1), under direction (-1,-1): cross(over,under) = 1*(-1) - (-1)*(-1) = -2 <0 -> negative? use
        # convention sign = sign of (over x under) z-component: positive crossing has over x under > 0.
        ox, oy = (1, -1) if c == 'x' else (-1, -1)
        ux, uy = (-1, -1) if c == 'x' else (1, -1)
        if c == 'x':
            ox, oy = ox * dl, oy * dl; ux, uy = ux * dr, uy * dr
        else:
            ox, oy = ox * dr, oy * dr; ux, uy = ux * dl, uy * dl
        z = ox * uy - oy * ux
        w += 1 if z > 0 else -1
    return w, (ncomp_edges == total_edges)
