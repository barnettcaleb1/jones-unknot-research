"""diagram.py -- the covering knot K of a halfword as an oriented PD code; Kauffman bracket, V_K and Alexander from the PD code.

DEFINITION OF K (project convention, not re-invented here): the Morse word  full = alex.symmetrize(alex.parse(halfword))
(tools/alex.py; the same word tools/kauffman.py sweeps).  Semantics of full = [(c, i), ...], read in order:
  start: one cap (two strands at positions 0, 1);
  ('l', i) / ('r', i): cap, two new strands inserted at positions i, i+1;
  ('u', i): cup joining the strands at positions i, i+1;
  ('x', i) / ('y', i): crossing of the strands at positions i, i+1.  Slots: TL, TR = the strands at i, i+1 before the
      crossing, BL, BR = at i, i+1 after it; the two strands are TL-BR and TR-BL.  'x': TL-BR passes OVER; 'y': TR-BL over.
PLANAR PICTURE (fixed once, CHECKED to reproduce kauffman.bracket exactly, see validate_pd.py): the word is drawn upwards
  (earlier letters lower), positions left to right.  Then around a crossing the slots in counterclockwise order are
  TL(before,left) -> TR(before,right) -> BR(after,right) -> BL(after,left).  (Reading the word downwards gives the mirror
  diagram; that would replace V_K(t) by V_K(1/t) and changes neither the knot group nor any certificate.)
PD CODE: edges labelled 0..2n-1 consecutively along a fixed orientation (edge e is followed by e+1 mod 2n); crossing k
  (= the k-th crossing of the Morse word) is the 4-tuple (a, b, c, d) of labels read counterclockwise starting at the
  INCOMING UNDER edge a (so c = a+1 is the outgoing under edge, {b, d} the over edges); sign(k) = +1 iff the over strand
  runs d -> b.  The sign is also stored explicitly (needed for 1-crossing diagrams where the labels are ambiguous).
Kauffman bracket: A-smoothing joins (a,b),(c,d), B-smoothing (a,d),(b,c); <O> = 1, delta = -A^2 - A^-2;
  V_K(t) = (-A^3)^(-w) <D> at t = A^-4 (standard: V(right trefoil) = t + t^3 - t^4).
"""
import sys
TOOLS = '/Users/calebbarnett/jones-lanes/theory-restart/tools'
if TOOLS not in sys.path: sys.path.insert(0, TOOLS)
import alex

# ---------------------------------------------------------------- Morse word -> PD
CCW = ('TL', 'TR', 'BR', 'BL')            # counterclockwise slot order (see PLANAR PICTURE)
OPP = {'TL': 'BR', 'BR': 'TL', 'TR': 'BL', 'BL': 'TR'}


class UF:
    def __init__(self): self.p = {}
    def find(self, a):
        p = self.p
        p.setdefault(a, a)
        r = a
        while p[r] != r: r = p[r]
        while p[a] != r: p[a], a = r, p[a]
        return r
    def union(self, a, b): self.p[self.find(a)] = self.find(b)


def morse_word(halfword):
    return alex.symmetrize(alex.parse(halfword))


def morse_crossings(full):
    """Sweep the Morse word.  Returns (crossings, ncomp_info) where crossings[k] = {'ty': 'x'|'y', 'pos': i,
    'TL','TR','BL','BR': edge class}, or None if the word is invalid.  Edge classes are union-find roots."""
    uf = UF(); nid = [0]
    def new():
        nid[0] += 1; return nid[0]
    e0 = new(); pos = [e0, e0]; cr = []
    for c, i in full:
        if i < 0: return None
        if c in 'xy':
            if i + 1 >= len(pos): return None
            a, b = pos[i], pos[i + 1]; bl, br = new(), new()
            pos[i], pos[i + 1] = bl, br
            cr.append({'ty': c, 'pos': i, 'TL': a, 'TR': b, 'BL': bl, 'BR': br})
        elif c in 'lr':
            if i > len(pos): return None
            e = new(); pos[i:i] = [e, e]
        elif c == 'u':
            if i + 1 >= len(pos): return None
            uf.union(pos[i], pos[i + 1]); del pos[i:i + 2]
        else:
            return None
    if pos: return None
    for x in cr:
        for s in CCW: x[s] = uf.find(x[s])
    # number of closed components without crossings is irrelevant for knots with >= 1 crossing; for 0 crossings
    # we need the number of components of the crossing-free diagram:
    roots = set(uf.find(e) for e in range(1, nid[0] + 1))
    return cr, len(roots)


class PD:
    """Oriented PD code.  X[k] = (a,b,c,d), sign[k] = +-1.  n crossings, 2n edges labelled 0..2n-1.
    For n = 0 the diagram is a single circle (unknot)."""
    def __init__(self, X, sign):
        self.X = [tuple(x) for x in X]; self.sign = list(sign)
    @property
    def n(self): return len(self.X)
    def writhe(self): return sum(self.sign)
    def over_in(self, k):
        a, b, c, d = self.X[k]
        return d if self.sign[k] > 0 else b
    def over_out(self, k):
        a, b, c, d = self.X[k]
        return b if self.sign[k] > 0 else d
    def copy(self): return PD(list(self.X), list(self.sign))
    def __repr__(self): return 'PD(%r, %r)' % (self.X, self.sign)
    def to_json(self): return {'X': [list(x) for x in self.X], 'sign': list(self.sign)}
    @staticmethod
    def from_json(d): return PD([tuple(x) for x in d['X']], d['sign'])


def pd_from_halfword(halfword):
    """Returns PD or None (invalid word / not a knot)."""
    full = morse_word(halfword)
    if full is None: return None
    res = morse_crossings(full)
    if res is None: return None
    cr, ncomp0 = res
    n = len(cr)
    if n == 0:
        return PD([], []) if ncomp0 == 1 else None
    ends = {}
    for k, x in enumerate(cr):
        for s in CCW: ends.setdefault(x[s], []).append((k, s))
    if any(len(v) != 2 for v in ends.values()): return None
    # traverse: arrive at crossing 0 along its over strand, entering at the earlier (top-of-word) slot, with label 0.
    # (Same orientation as alex.diagram, which starts at crossing 0 on the over strand going down the word.)
    lab = {}
    under_in = [None] * n; over_in = [None] * n
    s0 = 'TL' if cr[0]['ty'] == 'x' else 'TR'
    k, s, L = 0, s0, 0
    for step in range(2 * n + 1):
        if (k, s) in lab:
            if (k, s) == (0, s0) and step == 2 * n and L == 2 * n: break
            return None                          # revisited early: more than one component
        lab[(k, s)] = L
        under = (s in ('TR', 'BL')) if cr[k]['ty'] == 'x' else (s in ('TL', 'BR'))
        if under: under_in[k] = s
        else: over_in[k] = s
        o = OPP[s]
        lab[(k, o)] = (L + 1) % (2 * n)
        e = cr[k][o]
        a, b = ends[e]
        nxt = b if a == (k, o) else a
        if a == b: return None
        k, s = nxt; L += 1
    else:
        return None
    if len(lab) != 4 * n: return None
    X = []; sign = []
    for k in range(n):
        st = CCW.index(under_in[k])
        order = [CCW[(st + j) % 4] for j in range(4)]
        tup = tuple(lab[(k, s)] for s in order)
        X.append(tup)
        # over strand enters at slot over_in[k]; positive iff it enters at position d (index 3)
        sign.append(+1 if order[3] == over_in[k] else -1)
    return PD(X, sign)


# ---------------------------------------------------------------- consistency / planarity checks
def check_pd(pd):
    """Structural validity: labels 0..2n-1 each used twice, under strand a -> a+1, over strand in -> in+1,
    and the planar Euler characteristic of the 4-valent graph with the given rotation system is 2 (faces = n + 2)."""
    n = pd.n
    if n == 0: return True
    m = 2 * n
    cnt = {}
    for x in pd.X:
        for e in x: cnt[e] = cnt.get(e, 0) + 1
    if sorted(cnt) != list(range(m)) or any(v != 2 for v in cnt.values()): return False
    for k, (a, b, c, d) in enumerate(pd.X):
        if c != (a + 1) % m: return False
        oi, oo = pd.over_in(k), pd.over_out(k)
        if oo != (oi + 1) % m: return False
    return len(faces(pd)) == n + 2


def faces(pd):
    """Faces of the diagram as cyclic lists of (crossing, slot) 'corners'.  Rotation system: at crossing k the slots
    0..3 are counterclockwise.  A face is traced by: arrive at crossing k through slot j, turn to slot (j-1) mod 4
    (the next slot clockwise), leave along that edge.  Returns list of faces, each a list of (k, j_out)."""
    n = pd.n
    # where does each (k, slot) lead: the other occurrence of the same label
    occ = {}
    for k, x in enumerate(pd.X):
        for j, e in enumerate(x): occ.setdefault(e, []).append((k, j))
    other = {}
    for e, l in occ.items():
        (k1, j1), (k2, j2) = l
        other[(k1, j1)] = (k2, j2); other[(k2, j2)] = (k1, j1)
    seen = set(); out = []
    for k in range(n):
        for j in range(4):
            if (k, j) in seen: continue
            face = []; cur = (k, j)
            while cur not in seen:
                seen.add(cur); face.append(cur)
                k2, j2 = other[cur]
                cur = (k2, (j2 - 1) % 4)
            out.append(face)
    return out


# ---------------------------------------------------------------- Laurent polynomials (dict exp -> int)
def padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c * v
        if nv: p[e] = nv
        elif e in p: del p[e]

def pshift(p, k, c=1): return {e + k: c * v for e, v in p.items()}

def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}

DELTA = {2: -1, -2: -1}

def pdiv_delta(p):
    """exact division by delta = -A^2 - A^-2"""
    p = dict(p); r = {}
    while p:
        e = max(p); v = p[e]
        r[e - 2] = -v
        padd(p, {e: -v, e - 4: -v})
    return r


def crossing_order(pd):
    """greedy order keeping the frontier small (Morse order is already good; this helps for simplified PD codes)"""
    n = pd.n
    if n == 0: return []
    occ = {}
    for k, x in enumerate(pd.X):
        for e in x: occ.setdefault(e, set()).add(k)
    done = [False] * n; order = []; openl = set()
    order.append(0); done[0] = True
    for e in pd.X[0]:
        if e in openl: openl.discard(e)
        else: openl.add(e)
    while len(order) < n:
        best = None; bs = None
        cand = set()
        for e in openl:
            for k in occ[e]:
                if not done[k]: cand.add(k)
        if not cand: cand = set(k for k in range(n) if not done[k])
        for k in cand:
            x = pd.X[k]
            inside = sum(1 for e in x if e in openl)
            sc = (len(openl) - inside + (4 - inside), -inside, k)
            if bs is None or sc < bs: bs, best = sc, k
        k = best; order.append(k); done[k] = True
        for e in pd.X[k]:
            if e in openl: openl.discard(e)
            else: openl.add(e)
    return order


def bracket(pd, order=None):
    """Kauffman bracket <D> (normalised <O> = 1) as dict A-exponent -> coeff."""
    n = pd.n
    if n == 0: return {0: 1}
    if order is None: order = crossing_order(pd)
    states = {(): {0: 1}}           # matching (sorted tuple of pairs) -> poly (loops already multiplied in)
    for k in order:
        a, b, c, d = pd.X[k]
        new = {}
        for M, poly in states.items():
            for pairs, ex in ((((a, b), (c, d)), 1), (((a, d), (b, c)), -1)):
                m = dict()
                for (p, q) in M: m[p] = q; m[q] = p
                loops = 0
                for (p, q) in pairs:
                    if p == q:
                        loops += 1; continue
                    if p in m and q in m:
                        pp, qq = m.pop(p), m.pop(q)
                        if pp == q:
                            loops += 1
                        else:
                            m[pp] = qq; m[qq] = pp
                    elif p in m:
                        pp = m.pop(p); m[pp] = q; m[q] = pp
                    elif q in m:
                        qq = m.pop(q); m[qq] = p; m[p] = qq
                    else:
                        m[p] = q; m[q] = p
                key = tuple(sorted((x, y) for x, y in m.items() if x < y))
                pl = pshift(poly, ex)
                for _ in range(loops): pl = pmul(pl, DELTA)
                tgt = new.setdefault(key, {})
                padd(tgt, pl)
        states = {M: p for M, p in new.items() if p}
    tot = states.get((), {})
    assert set(states) <= {()}
    return pdiv_delta(tot)


def jones(pd):
    """V_K(t) as dict t-exponent -> coeff, t = A^-4, V = (-A^3)^(-w) <D>."""
    br = bracket(pd)
    w = pd.writhe()
    f = pshift(br, -3 * w, (-1) ** (w % 2))
    out = {}
    for e, c in f.items():
        if e % 4: raise ValueError('bracket exponents not divisible by 4 after normalisation')
        out[-e // 4] = c
    return out


# ---------------------------------------------------------------- Alexander polynomial from the PD code
def alexander_matrix_rows(pd):
    """Alexander matrix (Fox calculus of the Wirtinger presentation, generators -> t), rows = crossings,
    columns = arcs.  Entries are polys in t as dicts."""
    from wirtinger import wirtinger
    gens, rels = wirtinger(pd)
    return fox_matrix(gens, rels, {g: 1 for g in gens})


def fox_matrix(gens, rels, ab):
    """Fox Jacobian of the relators abelianised by generator g -> t^ab[g] (ab[g] in Z).  Entries dict exp->int."""
    col = {g: j for j, g in enumerate(gens)}
    M = []
    for r in rels:
        row = [dict() for _ in gens]
        e = 0                                   # exponent of the abelianised prefix
        for s in r:
            g = abs(s)
            if s > 0:
                padd(row[col[g]], {e: 1})
                e += ab[g]
            else:
                e -= ab[g]
                padd(row[col[g]], {e: -1})
        M.append(row)
    return M


def _det_int(M):
    """exact integer determinant (Bareiss)"""
    n = len(M)
    if n == 0: return 1
    M = [r[:] for r in M]; sign = 1; prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None: return 0
            M[k], M[sw] = M[sw], M[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def poly_det(M):
    """determinant of a square matrix of Laurent polys (dicts) with small exponent range, exactly, by evaluation at
    integer points and Lagrange interpolation.  Returns dict."""
    from fractions import Fraction
    n = len(M)
    if n == 0: return {0: 1}
    lo = min((min(p) for row in M for p in row if p), default=0)
    hi = max((max(p) for row in M for p in row if p), default=0)
    # shift each row so that exponents >= 0
    sh = []
    MM = []
    for row in M:
        rl = min((min(p) for p in row if p), default=0)
        sh.append(rl)
        MM.append([{e - rl: c for e, c in p.items()} for p in row])
    deg = sum(max((max(p) for p in row if p), default=0) for row in MM)
    pts = list(range(1, deg + 2))
    vals = []
    for x in pts:
        A = [[sum(c * x ** e for e, c in p.items()) for p in row] for row in MM]
        vals.append(_det_int(A))
    # Newton interpolation (exact)
    coef = [Fraction(v) for v in vals]
    m = len(pts)
    for j in range(1, m):
        for i in range(m - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (pts[i] - pts[i - j])
    poly = [Fraction(0)] * m
    for i in range(m - 1, -1, -1):
        # poly = poly * (x - pts[i]) + coef[i]
        newp = [Fraction(0)] * m
        for e in range(m - 1):
            newp[e + 1] += poly[e]
        for e in range(m):
            newp[e] -= pts[i] * poly[e]
        newp[0] += coef[i]
        poly = newp
    out = {}
    s = sum(sh)
    for e, c in enumerate(poly):
        if c:
            assert c.denominator == 1
            out[e + s] = int(c)
    return out


def normalize_alex(p):
    """Delta up to +-t^k: shift so min exponent 0, sign so that Delta(1) > 0; then symmetric centring not needed."""
    if not p: return ()
    lo = min(p)
    q = {e - lo: c for e, c in p.items()}
    s = sum(q.values())
    if s < 0: q = {e: -c for e, c in q.items()}
    return tuple(sorted(q.items()))


def alexander(pd):
    """Alexander polynomial of the PD code via Fox calculus on its Wirtinger presentation (delete last row & column)."""
    if pd.n == 0: return ((0, 1),)
    M = alexander_matrix_rows(pd)
    m = [row[:-1] for row in M[:-1]]
    return normalize_alex(poly_det(m))
