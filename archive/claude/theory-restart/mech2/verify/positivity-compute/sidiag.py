#!/usr/bin/env python3
"""Referee's own diagram code (written from the kht++ source, Tangles.cpp; not derived from tools/alex.py or the lens's scripts).

Half-diagram word 's.<c><i>....'  (c in x,y,l,r,u; i = index of left strand; strand 0 = virtual axis strand).
  parse(word)            -> list of (letter, index)
  full_word(half)        -> Morse word of the complete symmetric diagram (2 top strands, closed by a top cap and final u0)
  Knot(full)             -> unoriented planar diagram, traced: components, crossing signs, Seifert circles, Alexander matrix
  half_signs(word)       -> per crossing of the half-diagram: sign (+1/-1) in the symmetric knot diagram
  band_word(half, twists)-> Morse word of the quotient band diagram D(T) (1 top end, 3 bottom ends), as in Tangle::quotient
  cube_counts(word1_3)   -> {type: {(|s|, k): number of states}} for the 1-3 tangle diagram, types 'b' (top-b3, b1-b2), 'c'
"""
import sys
from fractions import Fraction

# ---------------------------------------------------------------- words
def parse(word):
    w = word.strip()
    if w.startswith('s.'):
        w = w[2:]
    out = []
    for tok in w.split('.'):
        tok = tok.strip()
        if not tok:
            continue
        if tok[0] not in 'xylru':
            raise ValueError('bad token %r' % tok)
        out.append((tok[0], int(tok[1:])))
    return out

def full_word(half):
    """Complete symmetric diagram. hw = number of strands on each side of the axis.
    Right copy of half-strand s (s>=1) sits at position hw+s-1, its mirror image at hw-s."""
    hw = 1
    full = []
    for (c, s) in half:
        if s == 0:
            if c not in 'xy':
                raise ValueError('only crossings at position 0')
            full.append((c, hw - 1, 'axis'))
        elif c in 'xy':
            full.append((c, hw + s - 1, 'right'))
            full.append((c, hw - s - 1, 'left'))
        elif c in 'lr':
            full.append(('cap', hw + s - 1, 'right'))
            full.append(('cap', hw - s + 1, 'left'))
            hw += 2
        elif c == 'u':
            full.append(('u', hw + s - 1, 'right'))
            full.append(('u', hw - s - 1, 'left'))
            hw -= 2
    full.append(('u', 0, 'end'))
    return full

# ---------------------------------------------------------------- planar diagram
class UF:
    def __init__(self):
        self.p = {}
    def find(self, a):
        self.p.setdefault(a, a)
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb

class Knot:
    """Closed diagram from a Morse word that starts with two strands joined by a cap at the top.
    crossings: list of dict(type, TL, TR, BL, BR, tag, src) with edge ids (union-find roots).
    After trace(): ok (single component through all crossings), for each crossing 'odown','udown' (bool), 'sign'."""
    def __init__(self, full):
        self.valid = True
        self.reason = ''
        uf = UF()
        self.n_edges = 0
        def new():
            self.n_edges += 1
            return self.n_edges
        e0 = new()
        pos = [e0, e0]
        cr = []
        free_loops = 0
        for idx, tok in enumerate(full):
            c, i = tok[0], tok[1]
            tag = tok[2] if len(tok) > 2 else ''
            if i < 0:
                self.valid = False; self.reason = 'negative index'; return
            if c in ('x', 'y'):
                if i + 1 >= len(pos):
                    self.valid = False; self.reason = 'crossing out of range'; return
                a, b = pos[i], pos[i + 1]
                cc, d = new(), new()
                pos[i], pos[i + 1] = cc, d
                cr.append(dict(type=c, TL=a, TR=b, BL=cc, BR=d, tag=tag, src=idx))
            elif c in ('cap', 'l', 'r'):
                if i > len(pos):
                    self.valid = False; self.reason = 'cap out of range'; return
                e = new()
                pos[i:i] = [e, e]
            elif c == 'u':
                if i + 1 >= len(pos):
                    self.valid = False; self.reason = 'cup out of range'; return
                uf.union(pos[i], pos[i + 1])
                del pos[i:i + 2]
            else:
                raise ValueError(c)
        if pos:
            self.valid = False; self.reason = 'open ends at the bottom'; return
        for x in cr:
            for k in ('TL', 'TR', 'BL', 'BR'):
                x[k] = uf.find(x[k])
        self.cr = cr
        self.n = len(cr)
        roots = set(uf.find(e) for e in range(1, self.n_edges + 1))
        ends = {}
        for ci, x in enumerate(cr):
            for k in ('TL', 'TR', 'BL', 'BR'):
                ends.setdefault(x[k], []).append((ci, k))
        self.ends = ends
        self.free_loops = len([r for r in roots if r not in ends])
        if any(len(v) != 2 for v in ends.values()):
            self.valid = False; self.reason = 'edge with != 2 ends'; return
        self.components = None
        self.trace()

    OPP = {'TL': 'BR', 'BR': 'TL', 'TR': 'BL', 'BL': 'TR'}

    def trace(self):
        """Walk along the diagram. direction of a passage: 'down' if it enters at a top corner."""
        cr = self.cr
        for x in cr:
            x['dirs'] = {}      # entering corner -> True, for the strand through that corner pair
        seen = set()            # (crossing, frozenset of corner pair)
        comps = 0
        order = []              # sequence of (crossing index, entry corner) along component 0
        if self.n == 0:
            self.components = 1 if self.free_loops <= 1 else self.free_loops
            self.ok = (self.free_loops <= 1)
            return
        for ci0 in range(self.n):
            for ent0 in ('TL', 'TR'):
                key0 = (ci0, frozenset((ent0, self.OPP[ent0])))
                if key0 in seen:
                    continue
                comps += 1
                ci, ent = ci0, ent0
                while True:
                    key = (ci, frozenset((ent, self.OPP[ent])))
                    if key in seen:
                        break
                    seen.add(key)
                    cr[ci]['dirs'][frozenset((ent, self.OPP[ent]))] = ent   # entry corner
                    if comps == 1:
                        order.append((ci, ent))
                    out = self.OPP[ent]
                    e = cr[ci][out]
                    a, b = self.ends[e]
                    nxt = b if a == (ci, out) else a
                    if a == b:
                        raise RuntimeError('edge with identical ends')
                    ci, ent = nxt
        self.components = comps + self.free_loops
        self.ok = (self.components == 1)
        self.order = order
        if not self.ok:
            return
        # signs
        for x in cr:
            if x['type'] == 'x':
                over, under = frozenset(('TL', 'BR')), frozenset(('TR', 'BL'))
            else:
                over, under = frozenset(('TR', 'BL')), frozenset(('TL', 'BR'))
            def vec(pair, entry):
                # direction vector of the passage in the plane (x to the right, y up)
                base = {'TL': (1, -1), 'TR': (-1, -1), 'BL': (1, 1), 'BR': (-1, 1)}
                return base[entry]
            o = vec(over, x['dirs'][over]); u = vec(under, x['dirs'][under])
            x['over'] = over; x['under'] = under
            x['sign'] = 1 if o[0] * u[1] - o[1] * u[0] > 0 else -1
            x['o_entry'] = x['dirs'][over]; x['u_entry'] = x['dirs'][under]

    def writhe(self):
        return sum(x['sign'] for x in self.cr)

    def seifert_circles(self):
        """oriented smoothing: the edge entering along one strand continues on the edge leaving along the other."""
        nxt = {}
        for x in self.cr:
            oe, ue = x['o_entry'], x['u_entry']
            o_in, o_out = x[oe], x[self.OPP[oe]]
            u_in, u_out = x[ue], x[self.OPP[ue]]
            nxt[o_in] = u_out
            nxt[u_in] = o_out
        seen = set(); cyc = 0
        for e in nxt:
            if e in seen:
                continue
            cyc += 1
            while e not in seen:
                seen.add(e); e = nxt[e]
        return cyc

    def diagram_genus(self):
        if self.n == 0:
            return 0
        s = self.seifert_circles()
        g2 = self.n - s + 1
        assert g2 % 2 == 0
        return g2 // 2

    def alexander_rows(self):
        """rows (sign, over arc, under-in arc, under-out arc); arcs = edges glued through over-passages."""
        uf = UF()
        for x in self.cr:
            oe = x['o_entry']
            uf.union(x[oe], x[self.OPP[oe]])
        arcs = {}
        def arc(e):
            r = uf.find(e)
            if r not in arcs:
                arcs[r] = len(arcs)
            return arcs[r]
        rows = []
        for x in self.cr:
            oe, ue = x['o_entry'], x['u_entry']
            rows.append((x['sign'], arc(x[oe]), arc(x[ue]), arc(x[self.OPP[ue]])))
        return rows, len(arcs)

    def alexander_at(self, t):
        rows, na = self.alexander_rows()
        if self.n == 0:
            return 1
        assert na == self.n, (na, self.n)
        M = [[0] * na for _ in rows]
        for r, (sg, o, uin, uout) in enumerate(rows):
            # Fox calculus of the Wirtinger relation: x_out = x_o x_in x_o^-1 (one sign), x_in = x_o x_out x_o^-1 (other sign)
            if sg > 0:
                M[r][o] += 1 - t; M[r][uin] += t; M[r][uout] -= 1
            else:
                M[r][o] += 1 - t; M[r][uout] += t; M[r][uin] -= 1
        m = [row[:-1] for row in M[:-1]]
        return det_int(m)

    def alexander_poly(self):
        """returns list of coefficients (low to high), normalised: lowest coefficient positive, no t factor."""
        if self.n == 0:
            return [1]
        deg = self.n          # degree bound of the minor determinant
        xs = list(range(0, deg + 1))
        ys = [self.alexander_at(t) for t in xs]
        coeffs = interpolate(xs, ys)
        while coeffs and coeffs[-1] == 0:
            coeffs.pop()
        while coeffs and coeffs[0] == 0:
            coeffs.pop(0)
        if coeffs and coeffs[0] < 0:
            coeffs = [-c for c in coeffs]
        return coeffs

def det_int(M):
    """Bareiss, exact for integer matrices."""
    n = len(M)
    if n == 0:
        return 1
    M = [r[:] for r in M]
    sign = 1; prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]

def interpolate(xs, ys):
    """Newton interpolation with exact fractions; returns integer coefficient list (low to high)."""
    n = len(xs)
    dd = [Fraction(y) for y in ys]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) / (xs[i] - xs[i - j])
    # expand Newton form
    poly = [Fraction(0)]
    for i in range(n - 1, -1, -1):
        # poly = poly * (x - xs[i]) + dd[i]
        new = [Fraction(0)] * (len(poly) + 1)
        for k, c in enumerate(poly):
            new[k + 1] += c
            new[k] -= c * xs[i]
        new[0] += dd[i]
        poly = new
    out = []
    for c in poly:
        assert c.denominator == 1
        out.append(int(c))
    return out

# ---------------------------------------------------------------- half-diagram quantities
def half_signs(word):
    """returns None if the completed diagram is not a knot; else dict with per-half-crossing signs etc."""
    half = parse(word)
    full = full_word(half)
    K = Knot(full)
    if not K.valid or not K.ok:
        return None
    # map crossings of the full diagram back to slices of the half-diagram
    # full tokens were produced in order; rebuild the correspondence
    src_half = []
    for hi, (c, s) in enumerate(half):
        if s == 0:
            src_half.append(hi)
        else:
            src_half.append(hi); src_half.append(hi)
    src_half.append(None)
    per = {}
    for x in K.cr:
        hi = src_half[x['src']]
        per.setdefault(hi, []).append(x['sign'])
    signs = []
    for hi, (c, s) in enumerate(half):
        if c in 'xy':
            v = per[hi]
            if s == 0:
                assert len(v) == 1
            else:
                assert len(v) == 2
                if v[0] != v[1]:
                    raise RuntimeError('mirror pair with different signs: %s' % word)
            signs.append((c, s, v[0]))
    c_axis = sum(1 for c, s, sg in signs if s == 0)
    c_off = sum(1 for c, s, sg in signs if s != 0)
    return dict(K=K, signs=signs, c=len(signs), c_axis=c_axis, c_off=c_off,
                wr=sum(sg for _, _, sg in signs),
                one_sign=(len(set(sg for _, _, sg in signs)) == 1) if signs else False)

# ---------------------------------------------------------------- band diagram (quotient)
def band_word(half, twists=0):
    """as Tangle::quotient: one top end (axis image A), doubled cap, every strand doubled, hooks at axis crossings, final u0.
    twists: kht++ adds |wr| pairs x1.x1 (wr>0) or y1.y1 (wr<=0); pass twists=wr to include them, 0 for the twist-free D."""
    w = [('cap', 1), ('cap', 2)]
    for (c, s) in half:
        if c in 'xy':
            if s == 0:
                w += [(c, 0), (c, 1), (c, 1), (c, 0)]
            else:
                w += [(c, 2 * s), (c, 2 * s - 1), (c, 2 * s + 1), (c, 2 * s)]
        elif c in 'lr':
            w += [('cap', 2 * s - 1), ('cap', 2 * s)]
        elif c == 'u':
            w += [('u', 2 * s), ('u', 2 * s - 1)]
    w.append(('u', 0))
    if twists > 0:
        w += [('x', 1), ('x', 1)] * twists
    elif twists < 0:
        w += [('y', 1), ('y', 1)] * (-twists)
    return w

# ---------------------------------------------------------------- state sums over planar matchings
TOP = -1
def _cap(m, i):
    m2 = [(p + 2 if p >= i else p) for p in m]
    m2[i:i] = [i + 1, i]
    return tuple(m2)

def _cup(m, i):
    """join strands i,i+1 at the bottom. returns (matching, closed circle created?)"""
    a, b = m[i], m[i + 1]
    m = list(m)
    loop = False
    if a == i + 1:
        loop = True
    else:
        if a != TOP:
            m[a] = b
        if b != TOP:
            m[b] = a
    del m[i:i + 2]
    m = [(p - 2 if p > i + 1 else p) for p in m]
    return tuple(m), loop

def cube_counts(word, ntop=1):
    """word: list of (letter, index) of a tangle diagram with ntop=1 top end (or ntop=2 joined by a cap: closed diagram).
    Returns dict: final matching -> {(|s|, k): count}, |s| = number of 1-smoothings, k = closed circles.
    Smoothings (kht++): x: 0 = turnback, 1 = vertical;  y: 0 = vertical, 1 = turnback."""
    if ntop == 1:
        state = {(TOP,): {(0, 0): 1}}
    else:
        state = {(1, 0): {(0, 0): 1}}
    def add(d, key, poly, ds=0, dk=0):
        t = d.setdefault(key, {})
        for (a, k), v in poly.items():
            kk = (a + ds, k + dk)
            t[kk] = t.get(kk, 0) + v
    for (c, i) in word:
        new = {}
        for m, poly in state.items():
            if c in ('cap', 'l', 'r'):
                if i > len(m):
                    raise ValueError('cap out of range')
                add(new, _cap(m, i), poly)
            elif c == 'u':
                if i + 1 >= len(m):
                    raise ValueError('cup out of range')
                m2, loop = _cup(m, i)
                add(new, m2, poly, 0, 1 if loop else 0)
            elif c in 'xy':
                if i + 1 >= len(m):
                    raise ValueError('crossing out of range')
                # vertical smoothing
                add(new, m, poly, (1 if c == 'x' else 0), 0)
                # turnback smoothing
                m2, loop = _cup(m, i)
                add(new, _cap(m2, i), poly, (0 if c == 'x' else 1), 1 if loop else 0)
            else:
                raise ValueError(c)
        state = new
    return state

TYPE_B = (1, 0, TOP)      # b1-b2, top-b3
TYPE_C = (TOP, 2, 1)      # top-b1, b2-b3

# ---------------------------------------------------------------- Laurent polynomials in q (dict exp -> coeff)
def padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c * v
        if nv:
            p[e] = nv
        elif e in p:
            del p[e]
    return p

def pmul(p, q):
    r = {}
    for e1, v1 in p.items():
        for e2, v2 in q.items():
            r[e1 + e2] = r.get(e1 + e2, 0) + v1 * v2
    return {e: v for e, v in r.items() if v}

def ppow(p, n):
    r = {0: 1}
    for _ in range(n):
        r = pmul(r, p)
    return r

def euler_from_counts(counts):
    """sum over states of (-q)^|s| (q + 1/q)^k"""
    circ = {1: 1, -1: 1}
    pw = {0: {0: 1}}
    kmax = max((k for (a, k) in counts), default=0)
    for k in range(1, kmax + 1):
        pw[k] = pmul(pw[k - 1], circ)
    P = {}
    for (a, k), v in counts.items():
        sg = -1 if a % 2 else 1
        padd(P, {e + a: c for e, c in pw[k].items()}, sg * v)
    return P

def unit_of(P):
    """P Laurent polynomial in q. Returns (sign, d) with P = sign*q^d mod (q^2+1)^2, or None.
    Method: reduce mod (q^2+1)^2:  q^(2m) = (-1)^m (1 - m*eps), eps = q^2+1;  q^(2m+1) = q * q^(2m).
    So P = (A0 + A1 eps) + q (B0 + B1 eps); sign*q^d has the same form with exactly one of the two parts non-zero."""
    A0 = A1 = B0 = B1 = 0
    for e, v in P.items():
        m, r = divmod(e, 2)
        s = -1 if m % 2 else 1
        if r == 0:
            A0 += s * v; A1 += -s * m * v
        else:
            B0 += s * v; B1 += -s * m * v
    if (B0, B1) == (0, 0) and A0 in (1, -1):
        # A0 = sign*(-1)^m, A1 = -sign*(-1)^m*m  => m = -A1/A0
        m = -A1 * A0
        sign = A0 * (-1 if m % 2 else 1)
        return (sign, 2 * m)
    if (A0, A1) == (0, 0) and B0 in (1, -1):
        m = -B1 * B0
        sign = B0 * (-1 if m % 2 else 1)
        return (sign, 2 * m + 1)
    return None

def pstr(P):
    return ' '.join('%+dq^%d' % (P[e], e) for e in sorted(P))

if __name__ == '__main__':
    for w in sys.argv[1:]:
        hs = half_signs(w)
        if hs is None:
            print(w, 'not a knot'); continue
        K = hs['K']
        print(w, 'c', hs['c'], 'axis', hs['c_axis'], 'off', hs['c_off'], 'wr', hs['wr'], 'one-sign', hs['one_sign'],
              'full crossings', K.n, 'Seifert circles', K.seifert_circles(), 'diagram genus', K.diagram_genus(),
              'Alexander', K.alexander_poly())
