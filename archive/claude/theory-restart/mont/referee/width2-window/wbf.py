"""Referee brute force for WIDTH2-WINDOW (Codex msg 20261117-022221, two_ended_potential_referee.md sec 3).

Independent exact checker.  Nothing here uses the theorem's case analysis: a point (m,n) is declared a unit
iff the exact numerator P(m,n) = sum_s p_s t^(2 e_a m + 2 e_b n) equals c t^k D for a rational c and integer k.

Laurent polys: (lo, [c_lo, ..., c_hi]) trimmed (nonzero ends); None = 0.
Sector labels are fusion colours ab; exponent index e = (0,1,3) for colours (0,2,4).
"""
import random

SECT = ['00', '02', '20', '22', '24', '42', '44']
EIDX = {'0': 0, '2': 1, '4': 3}
IJ = {s: (EIDX[s[0]], EIDX[s[1]]) for s in SECT}


def trim(lo, cs):
    i = 0
    n = len(cs)
    while i < n and cs[i] == 0:
        i += 1
    if i == n:
        return None
    j = n
    while cs[j - 1] == 0:
        j -= 1
    return (lo + i, list(cs[i:j]))


def from_dict(d):
    d = {e: c for e, c in d.items() if c}
    if not d:
        return None
    lo, hi = min(d), max(d)
    return (lo, [d.get(e, 0) for e in range(lo, hi + 1)])


def to_dict(p):
    if p is None:
        return {}
    return {p[0] + k: c for k, c in enumerate(p[1]) if c}


def padd(*ps):
    d = {}
    for p in ps:
        for e, c in to_dict(p).items():
            d[e] = d.get(e, 0) + c
    return from_dict(d)


def pmul(a, b):
    if a is None or b is None:
        return None
    r = [0] * (len(a[1]) + len(b[1]) - 1)
    for i, x in enumerate(a[1]):
        if x:
            for j, y in enumerate(b[1]):
                r[i + j] += x * y
    return trim(a[0] + b[0], r)


def pshift(p, k):
    return None if p is None else (p[0] + k, list(p[1]))


def pscale(p, c):
    return None if (p is None or c == 0) else (p[0], [c * x for x in p[1]])


def mono(e, c=1):
    return (e, [c])


def span(p):
    return len(p[1]) - 1


def top(p):
    return p[0] + len(p[1]) - 1


def proportional(p, q):
    """p = c t^k q for some rational c != 0, integer k (p, q nonzero, trimmed)."""
    if p is None or q is None or len(p[1]) != len(q[1]):
        return False
    a0, b0 = p[1][0], q[1][0]
    return all(x * b0 == y * a0 for x, y in zip(p[1], q[1]))


class Table:
    def __init__(self, p, D):
        self.p = {s: p[s] for s in SECT if p.get(s) is not None}
        self.D = D
        lows = [v[0] for v in self.p.values()]
        highs = [top(v) for v in self.p.values()]
        self.L, self.U = min(lows), max(highs)
        self.W = self.U - self.L
        self.SD = span(D)
        self.B = max(1, self.W, self.SD)
        self.items = [(2 * IJ[s][0], 2 * IJ[s][1], v[0], v[1]) for s, v in self.p.items()]

    def boundary_ok(self):
        return all(s in self.p for s in ['00', '02', '20', '24', '42', '44'])

    def numerator(self, m, n):
        d = {}
        for a2, b2, lo, cs in self.items:
            st = lo + a2 * m + b2 * n
            for k, x in enumerate(cs):
                if x:
                    d[st + k] = d.get(st + k, 0) + x
        return from_dict(d)

    def is_unit(self, m, n):
        wins = []
        for a2, b2, lo, cs in self.items:
            st = lo + a2 * m + b2 * n
            wins.append((st, st + len(cs) - 1, cs))
        wins.sort(key=lambda w: w[0])
        clusters = []
        cur = [wins[0]]
        hi = wins[0][1]
        for w in wins[1:]:
            if w[0] <= hi:
                cur.append(w)
                if w[1] > hi:
                    hi = w[1]
            else:
                clusters.append(cur)
                cur = [w]
                hi = w[1]
        clusters.append(cur)
        cache = {}

        def val(i):
            if i in cache:
                return cache[i]
            cl = clusters[i]
            if len(cl) == 1:
                v = (cl[0][0], cl[0][2])
            else:
                lo = cl[0][0]
                h = max(w[1] for w in cl)
                r = [0] * (h - lo + 1)
                for st, en, c in cl:
                    off = st - lo
                    for k, x in enumerate(c):
                        r[off + k] += x
                v = trim(lo, r)
            cache[i] = v
            return v

        nc = len(clusters)
        bi = None
        for i in range(nc):
            if val(i) is not None:
                bi = i
                break
        if bi is None:
            return False
        ti = None
        for i in range(nc - 1, bi - 1, -1):
            if val(i) is not None:
                ti = i
                break
        b = val(bi)[0]
        t = top(val(ti))
        if t - b != self.SD:
            return False
        r = [0] * (self.SD + 1)
        for i in range(bi, ti + 1):
            v = val(i)
            if v is None:
                continue
            for k, x in enumerate(v[1]):
                r[v[0] - b + k] += x
        return proportional((b, r), self.D)

    def units_in_box(self, R):
        out = []
        for m in range(-R, R + 1):
            for n in range(-R, R + 1):
                if self.is_unit(m, n):
                    out.append((m, n))
        return out

    def line_groups(self, axis, c0):
        """axis 'h': n=c0 fixed, vary m, group by 2*e_a; axis 'v': m=c0 fixed, vary n, group by 2*e_b."""
        groups = {}
        for a2, b2, lo, cs in self.items:
            if axis == 'h':
                key, sh = a2, b2 * c0
            else:
                key, sh = b2, a2 * c0
            d = groups.setdefault(key, {})
            for k, x in enumerate(cs):
                d[lo + sh + k] = d.get(lo + sh + k, 0) + x
        res = {}
        for key, d in groups.items():
            v = from_dict(d)
            if v is not None:
                res[key] = v
        return res


def check_table(T, R=None, tag=''):
    """Brute-force all units in |m|,|n|<=R (default 10B+max(5,B)), test every claim of the theorem.
    Returns dict of stats and a list of violations (should be empty)."""
    B = T.B
    C = 3 * B
    if R is None:
        R = 10 * B + max(5, B)
    units = T.units_in_box(R)
    uset = set(units)
    viol = []
    # (A) window
    for (m, n) in units:
        if abs(m) > C and abs(n) > C:
            viol.append(('WINDOW', m, n))
    # (B) line step
    whole_lines = set()
    for axis in ('h', 'v'):
        for c0 in range(-C, C + 1):
            g = T.line_groups(axis, c0)
            if axis == 'h':
                pts = [(m, c0) for m in range(-R, R + 1)]
                free = lambda pt: pt[0]
            else:
                pts = [(c0, n) for n in range(-R, R + 1)]
                free = lambda pt: pt[1]
            on = [pt for pt in pts if pt in uset]
            if len(g) == 0:
                if on:
                    viol.append(('ZEROLINE', axis, c0, on[:3]))
            elif len(g) == 1:
                (gv,) = g.values()
                predicted = proportional(gv, T.D)
                if predicted:
                    whole_lines.add((axis, c0))
                    if len(on) != len(pts):
                        viol.append(('WHOLELINE_MISSING', axis, c0, len(on), len(pts)))
                else:
                    if on:
                        viol.append(('ONEGROUP_NONUNIT_BUT_UNIT', axis, c0, on[:3]))
            else:
                lo = min(v[0] for v in g.values())
                hi = max(top(v) for v in g.values())
                Wl = hi - lo
                if Wl > T.W + 6 * abs(c0):
                    viol.append(('WLINE', axis, c0, Wl, T.W + 6 * abs(c0)))
                bound = (Wl + T.SD) // 2
                for pt in on:
                    if abs(free(pt)) > bound:
                        viol.append(('LINEBOUND', axis, c0, pt, bound))
    # (C) finite square: units not on a whole unit line lie in |m|,|n| <= 10B
    for (m, n) in units:
        if ('h', n) in whole_lines or ('v', m) in whole_lines:
            continue
        if abs(m) > 10 * B or abs(n) > 10 * B:
            viol.append(('SQUARE10B', m, n))
    # stats: how close to the window do units come
    fin = [(m, n) for (m, n) in units if not (('h', n) in whole_lines or ('v', m) in whole_lines)]
    mx = max([min(abs(m), abs(n)) for (m, n) in units], default=0)
    mxfin = max([max(abs(m), abs(n)) for (m, n) in fin], default=0)
    return dict(tag=tag, W=T.W, SD=T.SD, B=B, R=R, nunits=len(units), nwhole=len(whole_lines),
                max_min_coord=mx, ratio_window=mx / B, max_fin_coord=mxfin, ratio_square=mxfin / B,
                viol=viol, units_sample=units[:6])


def rand_poly(rng, lo, hi, cmax=2, nonzero=True):
    while True:
        cs = [rng.randint(-cmax, cmax) for _ in range(hi - lo + 1)]
        p = trim(lo, cs)
        if p is not None or not nonzero:
            return p
