"""tl.py -- exact Kauffman-bracket engine for planar diagrams with boundary, abstract boxes, cabling.
(GADGET-A, JT_2 project, 17 Nov 2026.)  Own code; conventions:

Items of a diagram (labels are ints; a label occurring twice is an internal edge, once a boundary point):
  ('X', (a,b,c,d))          crossing; a,b,c,d counterclockwise, a-c is the UNDER strand.
                            A-smoothing joins (a,b),(c,d); B-smoothing joins (a,d),(b,c)   (KnotTheory convention)
  ('I', (p,q))              plain arc joining p and q
  ('B', (nw,sw,se,ne), f, g)  abstract 4-ended box with bracket vector (f,g):  f*[0] + g*[inf]
                            [0] = (nw,ne),(sw,se) ;  [inf] = (nw,sw),(ne,se)
Laurent polynomials in A: dict exp -> int.  Unnormalised bracket: every closed loop = delta.  For closed diagrams the
normalised bracket is unnormalised/delta.  Tangle bracket vectors are unnormalised (EKT convention).
V_L(t) = (-A^3)^(-w) <D>,  t = A^-4.  Returned in q = t^(1/2) = A^-2 as dict q-exp -> int.
"""
import itertools, random

# ------------------------------------------------------------------ Laurent polynomials
def P(*pairs):
    d = {}
    for e, c in pairs:
        d[e] = d.get(e, 0) + c
    return {e: c for e, c in d.items() if c}

ONE = {0: 1}
ZERO = {}
DELTA = {2: -1, -2: -1}


def padd(p, q, c=1):
    r = dict(p)
    for e, v in q.items():
        nv = r.get(e, 0) + c * v
        if nv:
            r[e] = nv
        elif e in r:
            del r[e]
    return r


def psub(p, q):
    return padd(p, q, -1)


def pacc(r, q, c=1):
    """in-place r += c*q"""
    for e, v in q.items():
        nv = r.get(e, 0) + c * v
        if nv:
            r[e] = nv
        elif e in r:
            del r[e]


def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}


def ppow(p, k):
    r = ONE
    for _ in range(k):
        r = pmul(r, p)
    return r


def pshift(p, k, c=1):
    return {e + k: c * v for e, v in p.items()}


def pscale(p, c):
    return {e: c * v for e, v in p.items() if c * v}


def pbar(p):
    """A -> A^-1"""
    return {-e: v for e, v in p.items()}


def pmono(e, c=1):
    return {e: c}


def peval(p, x):
    return sum(c * x ** e for e, c in p.items())


def pdivexact(p, q):
    """exact division of Laurent polys p/q (raises if not exact)"""
    p = dict(p)
    if not q:
        raise ZeroDivisionError
    qe = max(q); qc = q[qe]
    qlo = min(q)
    out = {}
    while p:
        e = max(p); c = p[e]
        if c % qc:
            raise ValueError('not exact (coefficient)')
        k = e - qe; m = c // qc
        out[k] = m
        pacc(p, pshift(q, k), -m)
        if p and max(p) < qlo + k and min(p) < qlo + min(out) - 10 ** 6:
            break
        if len(out) > 10 ** 5:
            raise ValueError('runaway division')
        if p and max(p) - qe < min(p) - qlo:
            raise ValueError('not exact (degree)')
    return out


def pdiv_delta(p):
    return pdivexact(p, DELTA)


def pstr(p, var='A'):
    if not p:
        return '0'
    s = []
    for e in sorted(p):
        c = p[e]
        s.append('%+d*%s^%d' % (c, var, e))
    return ' '.join(s)


def is_unit(p):
    return len(p) == 1 and abs(list(p.values())[0]) == 1


def unit_multiple(p, q):
    """return (sign, shift) if p == sign*A^shift*q else None"""
    if not p or not q or len(p) != len(q):
        return None
    ep, eq = max(p), max(q)
    k = ep - eq
    s = p[ep] // q[eq] if q[eq] and p[ep] % q[eq] == 0 else None
    if s not in (1, -1):
        return None
    if pshift(q, k, s) == p:
        return (s, k)
    return None


def ord_at_1(p):
    """order of vanishing of the Laurent polynomial p(A) at A = 1 (p != 0)"""
    if not p:
        return float('inf')
    lo = min(p)
    coeffs = [0] * (max(p) - lo + 1)
    for e, c in p.items():
        coeffs[e - lo] = c
    k = 0
    while True:
        if sum(coeffs) != 0:
            return k
        # divide by (A - 1): synthetic division
        n = len(coeffs) - 1
        b = [0] * n
        acc = 0
        for i in range(n, 0, -1):
            acc = acc + coeffs[i]
            b[i - 1] = acc
        coeffs = b
        k += 1


# ------------------------------------------------------------------ labels
_LAB = [0]


def fresh():
    _LAB[0] += 1
    return _LAB[0]


# ------------------------------------------------------------------ diagrams
class Diagram:
    """items + named boundary (dict name -> label).  Internal edge = label occurring twice."""
    def __init__(self, items, bd=None):
        self.items = list(items)
        self.bd = dict(bd or {})

    def labels(self):
        s = []
        for it in self.items:
            s.extend(it[1])
        return s

    def copy_fresh(self):
        mp = {}
        def m(x):
            if x not in mp:
                mp[x] = fresh()
            return mp[x]
        items = []
        for it in self.items:
            if it[0] == 'B':
                items.append(('B', tuple(m(x) for x in it[1]), it[2], it[3]))
            else:
                items.append((it[0], tuple(m(x) for x in it[1])))
        bd = {k: m(v) for k, v in self.bd.items()}
        return Diagram(items, bd)

    def subst(self, mp):
        def m(x):
            while x in mp:
                x = mp[x]
            return x
        items = []
        for it in self.items:
            if it[0] == 'B':
                items.append(('B', tuple(m(x) for x in it[1]), it[2], it[3]))
            else:
                items.append((it[0], tuple(m(x) for x in it[1])))
        return Diagram(items, {k: m(v) for k, v in self.bd.items()})

    def ncross(self):
        return sum(1 for it in self.items if it[0] == 'X')


def glue(D1, D2, pairs, newbd):
    """disjoint union of fresh copies, identify boundary label pairs [(name1 in D1, name2 in D2)], new boundary
    newbd: dict newname -> ('1' or '2', oldname)"""
    a = D1.copy_fresh(); b = D2.copy_fresh()
    mp = {}
    for n1, n2 in pairs:
        mp[b.bd[n2]] = a.bd[n1]
    b2 = b.subst(mp)
    bd = {}
    for k, (w, nm) in newbd.items():
        bd[k] = a.bd[nm] if w == '1' else b2.bd[nm]
    return Diagram(a.items + b2.items, bd)


def self_glue(D, pairs, newbd=None):
    """identify boundary labels of one diagram: pairs [(name1, name2)]"""
    a = D.copy_fresh()
    mp = {}
    for n1, n2 in pairs:
        x, y = a.bd[n1], a.bd[n2]
        if x != y:
            mp[y] = x
    c = a.subst(mp)
    bd = {k: c.bd[v] for k, v in (newbd or {}).items()}
    return Diagram(c.items, bd)


# ------------------------------------------------------------------ the bracket engine
def item_terms(it):
    if it[0] == 'X':
        a, b, c, d = it[1]
        return [(((a, b), (c, d)), {1: 1}), (((a, d), (b, c)), {-1: 1})]
    if it[0] == 'I':
        p, q = it[1]
        return [(((p, q),), ONE)]
    if it[0] == 'B':
        nw, sw, se, ne = it[1]
        out = []
        if it[2]:
            out.append((((nw, ne), (sw, se)), it[2]))
        if it[3]:
            out.append((((nw, sw), (ne, se)), it[3]))
        return out
    raise ValueError(it)


def greedy_order(items):
    n = len(items)
    if n == 0:
        return []
    occ = {}
    for k, it in enumerate(items):
        for e in it[1]:
            occ.setdefault(e, set()).add(k)
    done = [False] * n
    openl = set()
    order = []
    def add(k):
        done[k] = True; order.append(k)
        for e in items[k][1]:
            if e in openl:
                openl.discard(e)
            else:
                openl.add(e)
    add(0)
    while len(order) < n:
        cand = set()
        for e in openl:
            for k in occ[e]:
                if not done[k]:
                    cand.add(k)
        if not cand:
            cand = set(k for k in range(n) if not done[k])
        best = None; bs = None
        for k in cand:
            labs = items[k][1]
            inside = sum(1 for e in labs if e in openl)
            sc = (len(labs) - 2 * inside, -inside, k)
            if bs is None or sc < bs:
                bs, best = sc, k
        add(best)
    return order


def bracket_raw(items, order=None):
    """returns dict: matching (tuple of sorted pairs of open labels) -> unnormalised poly"""
    if order is None:
        order = greedy_order(items)
    states = {(): {0: 1}}
    for k in order:
        terms = item_terms(items[k])
        new = {}
        for M, poly in states.items():
            for pairs, w in terms:
                m = {}
                for (p, q) in M:
                    m[p] = q; m[q] = p
                loops = 0
                for (p, q) in pairs:
                    if p == q:
                        loops += 1
                        continue
                    pin = p in m; qin = q in m
                    if pin and qin:
                        pp = m.pop(p); qq = m.pop(q)
                        if pp == q:
                            loops += 1
                        else:
                            m[pp] = qq; m[qq] = pp
                    elif pin:
                        pp = m.pop(p); m[pp] = q; m[q] = pp
                    elif qin:
                        qq = m.pop(q); m[qq] = p; m[p] = qq
                    else:
                        m[p] = q; m[q] = p
                key = tuple(sorted((x, y) for x, y in m.items() if x < y))
                pl = pmul(poly, w) if w != ONE else poly
                for _ in range(loops):
                    pl = pmul(pl, DELTA)
                tgt = new.get(key)
                if tgt is None:
                    new[key] = dict(pl)
                else:
                    pacc(tgt, pl)
        states = {M: p for M, p in new.items() if p}
    return states


def bracket_closed(D, normalised=True):
    st = bracket_raw(D.items)
    assert set(st) <= {()}, 'diagram not closed'
    p = st.get((), {})
    return pdiv_delta(p) if normalised else p


def brvec(T):
    """bracket vector (f,g) of a 4-ended tangle with boundary names NW,NE,SW,SE (unnormalised)"""
    st = bracket_raw(T.items)
    nw, ne, sw, se = T.bd['NW'], T.bd['NE'], T.bd['SW'], T.bd['SE']
    k0 = tuple(sorted([tuple(sorted((nw, ne))), tuple(sorted((sw, se)))]))
    ki = tuple(sorted([tuple(sorted((nw, sw))), tuple(sorted((ne, se)))]))
    extra = set(st) - {k0, ki}
    assert not extra, ('crossing matching in 4-ended tangle?', extra)
    return st.get(k0, {}), st.get(ki, {})


# ------------------------------------------------------------------ orientation, writhe, Jones (closed, no boxes)
def strands(D):
    """traverse components.  Returns (comps, info) where comps = list of lists of (item, slot_in) and
    info[item] = {'under_in': slot, 'over_in': slot, 'comp_under': c, 'comp_over': c} for crossings."""
    items = D.items
    occ = {}
    for k, it in enumerate(items):
        assert it[0] in 'XI', 'boxes not allowed for orientation'
        for s, e in enumerate(it[1]):
            occ.setdefault(e, []).append((k, s))
    for e, l in occ.items():
        assert len(l) == 2, ('open diagram', e, l)
    def partner(k, s):
        if items[k][0] == 'X':
            return (s + 2) % 4
        return 1 - s
    seen = set()
    comps = []
    info = {}
    for k0, it in enumerate(items):
        for s0 in range(len(it[1])):
            if (k0, s0) in seen:
                continue
            comp = []
            k, s = k0, s0
            cidx = len(comps)
            while (k, s) not in seen:
                so = partner(k, s)
                seen.add((k, s)); seen.add((k, so))
                comp.append((k, s))
                if items[k][0] == 'X':
                    d = info.setdefault(k, {})
                    if s in (0, 2):
                        d['under_in'] = s; d['comp_under'] = cidx
                    else:
                        d['over_in'] = s; d['comp_over'] = cidx
                e = items[k][1][so]
                (k1, s1), (k2, s2) = occ[e]
                if (k1, s1) == (k, so):
                    k, s = k2, s2
                else:
                    k, s = k1, s1
            comps.append(comp)
    return comps, info


def crossing_signs(D, reverse=()):
    """signs of crossings; reverse = set of component indices whose orientation is reversed"""
    comps, info = strands(D)
    signs = {}
    for k, d in info.items():
        ui, oi = d['under_in'], d['over_in']
        if d['comp_under'] in reverse:
            ui = (ui + 2) % 4
        if d['comp_over'] in reverse:
            oi = 1 if oi == 3 else 3
        s = 1 if (ui == 0 and oi == 3) or (ui == 2 and oi == 1) else -1
        signs[k] = (s, d['comp_under'], d['comp_over'])
    return comps, signs


def link_data(D, reverse=()):
    comps, signs = crossing_signs(D, reverse)
    w = sum(s for s, _, _ in signs.values())
    nc = len(comps)
    lk = {}
    for s, cu, co in signs.values():
        if cu != co:
            key = tuple(sorted((cu, co)))
            lk[key] = lk.get(key, 0) + s
    lk = {k: v // 2 for k, v in lk.items()}
    return nc, w, lk


def jones(D, reverse=()):
    """V_L in q = t^(1/2) = A^-2 as dict q-exp -> int"""
    br = bracket_closed(D)
    nc, w, lk = link_data(D, reverse)
    f = pshift(br, -3 * w, (-1) ** (w % 2))
    out = {}
    for e, c in f.items():
        assert e % 2 == 0, 'odd A exponent'
        out[-e // 2] = c
    return out


def unlink_jones(c):
    """V of the c-component unlink in q: (-(q+q^-1))^(c-1)"""
    r = {0: 1}
    for _ in range(c - 1):
        r = pmul(r, {1: -1, -1: -1})
    return r


# ------------------------------------------------------------------ elementary tangles and Conway operations
def t_cross(s=1):
    """[1] (s=+1): br = (A, A^-1);  [-1]: br = (A^-1, A)"""
    nw, ne, sw, se = fresh(), fresh(), fresh(), fresh()
    if s == 1:
        it = ('X', (sw, se, ne, nw))
    else:
        it = ('X', (se, ne, nw, sw))
    return Diagram([it], {'NW': nw, 'NE': ne, 'SW': sw, 'SE': se})


def t_zero():
    nw, ne, sw, se = fresh(), fresh(), fresh(), fresh()
    return Diagram([('I', (nw, ne)), ('I', (sw, se))], {'NW': nw, 'NE': ne, 'SW': sw, 'SE': se})


def t_inf():
    nw, ne, sw, se = fresh(), fresh(), fresh(), fresh()
    return Diagram([('I', (nw, sw)), ('I', (ne, se))], {'NW': nw, 'NE': ne, 'SW': sw, 'SE': se})


def t_box(f, g):
    nw, ne, sw, se = fresh(), fresh(), fresh(), fresh()
    return Diagram([('B', (nw, sw, se, ne), f, g)], {'NW': nw, 'NE': ne, 'SW': sw, 'SE': se})


def tsum(T, U):
    return glue(T, U, [('NE', 'NW'), ('SE', 'SW')], {'NW': ('1', 'NW'), 'SW': ('1', 'SW'), 'NE': ('2', 'NE'), 'SE': ('2', 'SE')})


def tprod(T, U):
    """T on top of U (EKT's T*U)"""
    return glue(T, U, [('SW', 'NW'), ('SE', 'NE')], {'NW': ('1', 'NW'), 'NE': ('1', 'NE'), 'SW': ('2', 'SW'), 'SE': ('2', 'SE')})


def rho(T):
    """reflection in the NW-SE axis (crossings keep over/under, planar orientation reverses)"""
    items = []
    for it in T.items:
        if it[0] == 'X':
            a, b, c, d = it[1]
            items.append(('X', (a, d, c, b)))
        elif it[0] == 'I':
            items.append(it)
        else:
            nw, sw, se, ne = it[1]
            # reflected box: positions: new ccw order of the same 4 labels is reversed
            # box [0]=(nw,ne),(sw,se) as label pairs is unchanged; only geometry mirrored; bracket conj needed
            raise ValueError('rho of abstract box not supported')
    bd = dict(T.bd)
    bd['NE'], bd['SW'] = T.bd['SW'], T.bd['NE']
    return Diagram(items, bd)


def mirror(T):
    items = []
    for it in T.items:
        if it[0] == 'X':
            a, b, c, d = it[1]
            items.append(('X', (b, c, d, a)))
        elif it[0] == 'B':
            items.append(('B', it[1], pbar(it[2]), pbar(it[3])))
        else:
            items.append(it)
    return Diagram(items, dict(T.bd))


def rot90(T):
    """rotate the tangle by 90 degrees counterclockwise"""
    bd = {'SW': T.bd['NW'], 'SE': T.bd['SW'], 'NE': T.bd['SE'], 'NW': T.bd['NE']}
    return Diagram(list(T.items), bd)


def twist(n):
    """horizontal integer tangle n = [1]+...+[1] (|n| crossings); 0 -> [0]"""
    if n == 0:
        return t_zero()
    s = 1 if n > 0 else -1
    T = t_cross(s)
    for _ in range(abs(n) - 1):
        T = tsum(T, t_cross(s))
    return T


def dot(T, U):
    """EKT's T . U = T^rho + U"""
    return tsum(rho(T), U)


def dots(*ts):
    """left-associated T1 . T2 . ... ; integers allowed"""
    ts = [twist(t) if isinstance(t, int) else t for t in ts]
    R = ts[0]
    for U in ts[1:]:
        R = dot(R, U)
    return R


def numerator(T):
    return self_glue(T, [('NW', 'NE'), ('SW', 'SE')])


def denominator(T):
    return self_glue(T, [('NW', 'SW'), ('NE', 'SE')])


def omega(T):
    """EKT: T^omega = ((T+2)*1)+2"""
    return tsum(tprod(tsum(T, twist(2)), t_cross(1)), twist(2))


def omegabar(T):
    """EKT: T^omegabar = ((T-2)*(-1))-2"""
    return tsum(tprod(tsum(T, twist(-2)), t_cross(-1)), twist(-2))


# ------------------------------------------------------------------ 2-cabling with cut slots
def cable2(D, cuts=()):
    """blackboard 2-cable of a closed diagram made of X and I items.  cuts: list of edge labels; each cut edge gives
    a slot (NW,SW,SE,NE) [names 'NWk','SWk','SEk','NEk' for the k-th cut] such that inserting [0] restores the cable
    and [inf] makes the cable turn back on both sides."""
    items = D.items
    occ = {}
    for k, it in enumerate(items):
        assert it[0] in 'XI'
        for s, e in enumerate(it[1]):
            occ.setdefault(e, []).append((k, s))
    first = {}
    copies = {}
    for e, l in occ.items():
        assert len(l) == 2
        l.sort()
        first[e] = l[0]
        copies[e] = (fresh(), fresh())
    cutcopies = {}
    bd = {}
    for j, e in enumerate(cuts):
        e1 = (fresh(), fresh()); e2 = (fresh(), fresh())
        cutcopies[e] = (e1, e2)
        bd['NW%d' % j] = e1[0]; bd['SW%d' % j] = e1[1]
        bd['NE%d' % j] = e2[0]; bd['SE%d' % j] = e2[1]
    def outcopy(k, s):
        e = items[k][1][s]
        isfirst = (first[e] == (k, s))
        if e in cutcopies:
            e1, e2 = cutcopies[e]
            return (e1[0], e1[1]) if isfirst else (e2[1], e2[0])
        c = copies[e]
        return (c[0], c[1]) if isfirst else (c[1], c[0])
    out = []
    for k, it in enumerate(items):
        if it[0] == 'I':
            p0 = outcopy(k, 0); p1 = outcopy(k, 1)
            for i in range(2):
                out.append(('I', (p0[i], p1[1 - i])))
            continue
        A_ = outcopy(k, 0); B_ = outcopy(k, 1); C_ = outcopy(k, 2); D_ = outcopy(k, 3)
        vmid = [fresh(), fresh()]     # vertical copy x between y=0 and y=1
        hmid = [fresh(), fresh()]     # horizontal copy y between x=0 and x=1
        for x in range(2):
            for y in range(2):
                south = A_[1 - x] if y == 0 else vmid[x]
                north = C_[x] if y == 1 else vmid[x]
                west = D_[y] if x == 0 else hmid[y]
                east = B_[1 - y] if x == 1 else hmid[y]
                out.append(('X', (south, east, north, west)))
    return Diagram(out, bd)


def plug(F, slotnames, T):
    """insert tangle T (NW,NE,SW,SE) into slot with boundary names slotnames=(nw,sw,se,ne) of diagram F"""
    nw, sw, se, ne = slotnames
    rest = {k: ('1', k) for k in F.bd if k not in slotnames}
    return glue(F, T, [(nw, 'NW'), (sw, 'SW'), (se, 'SE'), (ne, 'NE')], rest)


# ------------------------------------------------------------------ standard closed diagrams
def braid_closure(word, n):
    """closure of braid word on n strands (letters +-i, 1<=i<n), built from crossings + arcs.
    sigma_i (positive letter) uses [1]-type geometry for strands i,i+1 (see notes on sign)."""
    tops = [fresh() for _ in range(n)]
    cur = list(tops)
    items = []
    for L in word:
        i = abs(L) - 1
        tl, tr = cur[i], cur[i + 1]
        bl, br_ = fresh(), fresh()
        # local tangle: NW=tl, NE=tr, SW=bl, SE=br
        if L > 0:
            items.append(('X', (bl, br_, tr, tl)))
        else:
            items.append(('X', (br_, tr, tl, bl)))
        cur[i], cur[i + 1] = bl, br_
    for j in range(n):
        items.append(('I', (cur[j], tops[j])))
    return Diagram(items, {})
