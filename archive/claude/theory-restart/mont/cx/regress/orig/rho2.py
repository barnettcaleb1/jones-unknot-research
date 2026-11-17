"""rho2.py -- the width-k module H_k = Hom(V_1, V_1 (x) V_2^{(x)2k}) of the mixed (type-B) Artin group, built EXACTLY
from the plain Kauffman-bracket state space of the kht++ quotient picture (tools/flat_search.py), so that
        J(halfword)  =  normalise( PHI_suffix . rho(W) . V_prefix )      (= lp.J(halfword) exactly).
Width k = 2 gives the 9-dimensional module rho_2 (k = 1 reproduces the 2-dim TH-2BR module, dim 2).  (Claude, engineB, 17 Nov 2026)

CONVENTIONS (all inherited from tools/flat_search.py, so nothing is re-normalised by hand)
  * Quotient picture: strand POSITION 0 = the axis (colour 1); half-strand j (j = 0,1,...) = the band at positions 2j+1, 2j+2
    (colour 2 = band; f_2 is never inserted, see BASIS below).  A state is a crossingless matching, stored as a tuple m with
    m[i] = partner of index i; index 0 = the top end E of the quotient tangle (it is joined to the axis), index p+1 = position p.
  * Half letters -> quotient letters (flat_search.quotient_word):  x0/y0 -> (c,0),(c,1),(c,1),(c,0)  [full twist of the axis
    with band 0];  x_s/y_s (s>=1) -> (c,2s),(c,2s-1),(c,2s+1),(c,2s)  [crossing of bands s-1 and s];  l_s/r_s -> caps at 2s-1, 2s;
    u_s -> cups at 2s, 2s-1;  final implicit u0 -> cup at quotient position 0.  Plain crossing x at position i:
    A^{+1} (identity) + A^{-1} (cup-cap at i);  y: A^{-1} (identity) + A^{+1} (cup-cap);  closed loop = delta = -A^2 - A^-2.
  * BALL of width k: the axis and half-strands 0..2k-1 (quotient positions 0..4k), with the passing half-strand c (from the top
    vertex) at half position 2k and the auxiliary flat_search band after it.  During the braid part these outer bands are
    joined to each other (indices 4k+2 <-> 4k+5, 4k+3 <-> 4k+4) and are never touched.
  * The braid letters are x0,y0 (axis twist, mixed generator tau^{+-1}) and x_i,y_i, 1 <= i <= 2k-1 (sigma_i^{+-1} on the legs).
    Letters x_i and y_i are inverse to each other (CHECKED).
  * ORDER: a word W = L_1 L_2 ... L_n (left to right, i.e. top to bottom of the diagram) acts on a state vector v by
    rho(W) v = M[L_n] ... M[L_1] v  (column vectors; first letter acts first).

BASIS (k = 2: 9 elements).  The 42 crossingless matchings of the 10 ball points (E, axis, 8 band points) span the plain-bracket
  ball module; f_2^{(x)4} has kernel = span of the matchings in which some band (2j+1, 2j+2) is matched to ITSELF
  (a turnback on a band).  That span is invariant under every letter (CHECKED: all images of such matchings are again such
  matchings).  The NAIVE plain y-functional does NOT vanish on it (CHECKED: 14-16 of 33 such matchings have nonzero naive y);
  the correct closing functional is PHI := phi_y o P, P = f_2^{(x)4} (see FUNCTIONAL below), which does.
  So rho_k := the quotient module, with basis = the crossingless matchings having NO band self-matched.  For k = 2 these are the
  9 matchings listed by `basis_table()`; each is a valenced (colour-2) TL diagram V_1 -> V_1 (x) V_2^{(x)4} (Flores-Peltola
  L_{(1,2,2,2,2)}^{(1)}).  Entries of every matrix are Laurent polynomials in A with integer coefficients (no denominators).

LITERAL HALFWORDS (k = 2).  For W in {x0,y0,x1,y1,x2,y2,x3,y3}^*:
      PREFIXES  'l1.l1'  (= s.l1.l1, caps on half-strands (0,1),(2,3); same state as s.l1.l3)       -> vector V['l1.l1']
                'l1.l2'  (= s.l1.l2, nested caps (0,3),(1,2))                                       -> vector V['l1.l2']
      SUFFIXES  'u1.u2'  (bottom vertex on leg 2, legs 0-1 cupped, leg 3 joined to c)               -> covector PHI['u1.u2']
                'u2.u2'  (bottom vertex on leg 0, legs 1-2 cupped, leg 3 joined to c)               -> covector PHI['u2.u2']
                'u3.u2'  (bottom vertex on leg 0, legs 2-3 cupped, leg 1 joined to c)               -> covector PHI['u3.u2']
  e.g. halfword 's.l1.l1.y0.x2.y1.u2.u2':  J =. PHI['u2.u2'] . M[y1] M[x2] M[y0] . V['l1.l1']  (y0 acts first).
  Any prefix/suffix made of caps, cups and crossings that leaves the outer bands in the standard position can be used:
  vec_of_prefix(prefix_letters) and covec_of_suffix(suffix_letters) compute them by the same sweep.

NORMALISATION.  PHI gives the y-coefficient of the plain bracket (in flat_search's A).  J_raw = y / u with u = y + delta x a
  monomial (a unit; we never need it: lp.normalize removes any unit).  [B.PHIX[S] stores the naive plain y-functional on all 42
  matchings, for reference.]  We convert A -> t by t = A^4 exactly as lp.J_raw does (all exponents of y are congruent
  mod 4), then lp.normalize (J = 1 mod (t+1)^2).  So J here is EXACTLY lp.J (same t, no mirror): CHECKED on random width-two words.
  Matrices are reported in A; M[x0], M[y0] etc. are NOT rescaled (their eigenvalues are the raw bracket eigenvalues).

FUNCTIONAL (important).  The naive y-functional is NOT zero on band-self-matched matchings (only on physical states), so on the
  quotient module the correct closing functional is PHI(m) := phi_y(P m), P = prod_j (1 - delta^-1 e_j) (f_2 on every leg).
  We store NPHI = delta^4 PHI (integral);  y = NPHI . rho(W) V / delta^4  (exact division; delta^4 = t^-2 (1+t)^4).
  CHECKED: 269/269 and 1007/1007 random width-two knots (random prefixes/suffixes, words of length 1..16) give exactly lp.J,
  both in the A-form (J_split) and in the normalised t-form (J_t);  is_knot() agrees with lp.J's knot test 1500/1500.
  Relations CHECKED exactly: x_i y_i = 1, sigma braid relations, far commutation, type-B relation y0 y1 y0 y1 = y1 y0 y1 y0.

NORMALISED t-FORM (see normalised(), and rho2_matrices.json): gauge f_j = A^(-2c_j) e_j, c = (0,1,0,1,1,0,1,1,1);
  Y = t^-2 M[y0] (eigenvalues 1 x4, t^-3 x5),  X_i = t^2 M[x_i] (eigenvalues 1 x2, -t x4, t^3 x3), all entries in Z[t,1/t];
  V['l1.l1'] = f_0, V['l1.l2'] = f_2;  J_raw =. t^2 PHIT[S] . rho(W) V[P] / (1+t)^4 ; every PHIT entry has the factor (1+t)^2.

MODULAR USE: mats_mod(p, a) gives all generator matrices, V and NPHI at A = a mod p (NPHI still carries the delta^4 factor).
  For the t-form mod p see orbit_search.mats_at / mitm.py.  Width three: Ball(3) (dim 51) and fastJ3.py.
"""
import sys, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp

# ---------------- Laurent polynomials in A: dict exp -> int ----------------
def padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c * v
        if nv: p[e] = nv
        elif e in p: del p[e]
def pshift(p, k, c=1): return {e + k: c * v for e, v in p.items()}
def pdelta(p):
    r = {}
    padd(r, pshift(p, 2, -1)); padd(r, pshift(p, -2, -1)); return r
def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}

# ---------------- matchings (flat_search conventions) ----------------
def cap(m, i):
    j = i + 1
    m2 = [(x + 2 if x >= j else x) for x in m]
    m2[j:j] = [j + 1, j]
    return tuple(m2)
def cup(m, i):
    j = i + 1
    p, q = m[j], m[j + 1]
    m = list(m); loop = False
    if p == j + 1: loop = True
    else: m[p] = q; m[q] = p
    del m[j:j + 2]
    m = [(x - 2 if x > j + 1 else x) for x in m]
    return tuple(m), loop
def qletters(half):
    """half letters (c,s) -> quotient letters, as flat_search.quotient_word (without the initial r1,r2 and final u0)."""
    w = []
    for c, s in half:
        if c in 'xy':
            if s == 0: w += [(c, 0), (c, 1), (c, 1), (c, 0)]
            else: w += [(c, 2 * s), (c, 2 * s - 1), (c, 2 * s + 1), (c, 2 * s)]
        elif c in 'lr': w += [(c, 2 * s - 1), (c, 2 * s)]
        elif c == 'u': w += [(c, 2 * s), (c, 2 * s - 1)]
        else: raise ValueError(c)
    return w
def sweep(state, qw):
    """apply quotient letters to a state {matching: poly}"""
    for c, i in qw:
        new = {}
        for m, p in state.items():
            W = len(m) - 1
            if c in 'lr':
                if i > W: raise ValueError('cap out of range')
                padd(new.setdefault(cap(m, i), {}), p)
            elif c == 'u':
                if i + 1 >= W: raise ValueError('cup out of range')
                m2, loop = cup(m, i)
                padd(new.setdefault(m2, {}), pdelta(p) if loop else p)
            else:
                if i + 1 >= W: raise ValueError('crossing out of range')
                a, b = (1, -1) if c == 'x' else (-1, 1)
                padd(new.setdefault(m, {}), pshift(p, a))
                m2, loop = cup(m, i)
                q = pdelta(p) if loop else p
                padd(new.setdefault(cap(m2, i), {}), pshift(q, b))
        state = {m: p for m, p in new.items() if p}
    return state
def parse(word):
    w = word.strip()
    if w.startswith('s.'): w = w[2:]
    return [(tok[0], int(tok[1:])) for tok in w.split('.') if tok]

# ---------------- the width-k ball ----------------
def noncrossing_matchings(n):
    """all noncrossing perfect matchings of 0..n-1 as tuples"""
    if n == 0: return [()]
    out = []
    def rec(pts):
        if not pts: yield {}; return
        a = pts[0]
        for idx in range(1, len(pts), 2):
            b = pts[idx]
            inner = pts[1:idx]; outer = pts[idx + 1:]
            for m1 in rec(inner):
                for m2 in rec(outer):
                    d = dict(m1); d.update(m2); d[a] = b; d[b] = a
                    yield d
    for d in rec(list(range(n))):
        out.append(tuple(d[i] for i in range(n)))
    return out

class Ball:
    def __init__(self, k=2):
        self.k = k
        self.npts = 4 * k + 2                 # E, axis, 4k band points
        self.bands = [(2 * j + 2, 2 * j + 3) for j in range(2 * k)]   # indices of band j (positions 2j+1, 2j+2)
        allm = noncrossing_matchings(self.npts)
        self.all = allm
        self.selfm = [m for m in allm if any(m[a] == b for a, b in self.bands)]
        self.basis = [m for m in allm if not any(m[a] == b for a, b in self.bands)]
        self.index = {m: i for i, m in enumerate(self.basis)}
        self.dim = len(self.basis)
        self.letters = ['x0', 'y0'] + [c + str(i) for i in range(1, 2 * k) for c in 'xy']
        self.M = {L: self._matrix(L) for L in self.letters}
        # outer pattern: indices npts.. npts+3 : (c band)(aux band) joined as 0<->3, 1<->2
    def is_self(self, m):
        return any(m[a] == b for a, b in self.bands)
    def act_state(self, state, L):
        return sweep(state, qletters(parse(L)))
    def project(self, state):
        """state on ball matchings -> coordinate vector (list of polys), dropping band-self-matched terms"""
        v = [{} for _ in range(self.dim)]
        for m, p in state.items():
            if self.is_self(m): continue
            padd(v[self.index[m]], p)
        return v
    def _matrix(self, L):
        cols = []
        for b in self.basis:
            st = self.act_state({b: {0: 1}}, L)
            cols.append(self.project(st))
        return [[cols[j][i] for j in range(self.dim)] for i in range(self.dim)]
    def check_invariance(self):
        """images of band-self-matched matchings stay in the self-matched span"""
        bad = 0
        for L in self.letters:
            for m in self.selfm:
                st = self.act_state({m: {0: 1}}, L)
                if any(not self.is_self(m2) for m2 in st): bad += 1
        return bad
    # ----- embedding into the full flat_search state -----
    def embed(self, m):
        n = self.npts
        return tuple(list(m) + [n + 3, n + 2, n + 1, n])
    def split_full(self, fm):
        n = self.npts
        if len(fm) != n + 4: return None
        if tuple(fm[n:]) != (n + 3, n + 2, n + 1, n): return None
        if any(x >= n for x in fm[:n]): return None
        return tuple(fm[:n])
    def vec_of_prefix(self, prefix):
        """prefix: half-letter string without 's.', e.g. 'l1.l1'. Returns the ball vector of the state after s.prefix."""
        st = sweep({(1, 0): {0: 1}}, [('r', 1), ('r', 2)] + qletters(parse(prefix)))
        ball = {}
        for fm, p in st.items():
            m = self.split_full(fm)
            if m is None: raise ValueError('prefix does not leave the outer bands in standard position')
            padd(ball.setdefault(m, {}), p)
        return self.project(ball)
    def plain_covec(self, suffix):
        """y- and x-coefficient functionals of the plain bracket on ALL crossingless ball matchings"""
        qw = qletters(parse(suffix)) + [('u', 0)]
        phy, phx = {}, {}
        for b in self.all:
            st = sweep({self.embed(b): {0: 1}}, qw)
            if set(st) - {(3, 2, 1, 0), (1, 0, 3, 2)}: raise ValueError('suffix does not close to the 4-ended tangle')
            phy[b] = st.get((3, 2, 1, 0), {}); phx[b] = st.get((1, 0, 3, 2), {})
        return phy, phx
    def eS(self, m, S):
        """apply the band turnbacks e_j (j in S) to the matching m: returns (matching, number of closed loops)"""
        loops = 0
        for j in S:
            i = 2 * j + 1                      # quotient position of the first strand of band j
            m2, lp_ = cup(m, i)
            loops += lp_
            m = cap(m2, i)
        return m, loops
    def covec_of_suffix(self, suffix):
        """suffix: half letters after the braid part, e.g. 'u2.u2'.
        Returns NPHI: list of polys with  y = (NPHI . quotient_coords) / delta^(2k)  exactly, where
        NPHI(m) = delta^(2k) phi_y(P m),  P = prod_j (1 - delta^-1 e_j)  (f_2 on every leg).  phi_y is the plain y-functional."""
        phy, _ = self.plain_covec(suffix)
        nb = 2 * self.k
        out = []
        for b in self.basis:
            acc = {}
            for r in range(nb + 1):
                for S in itertools.combinations(range(nb), r):
                    m2, loops = self.eS(b, S)
                    val = phy[m2]
                    if not val: continue
                    # (-1)^r delta^(nb - r + loops) val
                    for _ in range(nb - r + loops): val = pdelta(val)
                    padd(acc, val, (-1) ** r)
            out.append(acc)
        return out, phy
    def covec_vanishes_on_self(self, suffix):
        qw = qletters(parse(suffix)) + [('u', 0)]
        bad = 0
        for m in self.selfm:
            st = sweep({self.embed(m): {0: 1}}, qw)
            if st.get((3, 2, 1, 0), {}): bad += 1
        return bad
    # ----- products -----
    def apply(self, W, v):
        """W: list/str of braid letters (first acts first); v: vector of polys"""
        if isinstance(W, str): W = [x for x in W.split('.') if x]
        for L in W:
            M = self.M[L]
            v = [self._row_dot(M[i], v) for i in range(self.dim)]
        return v
    @staticmethod
    def _row_dot(row, v):
        r = {}
        for a, b in zip(row, v):
            if a and b: padd(r, pmul(a, b))
        return r
    def pair(self, phi, v):
        return self._row_dot(phi, v)

def pdiv_delta(p, n):
    """exact division of a Laurent poly in A by delta^n, delta = -A^2 - A^-2 = -A^-2 (A^4 + 1). Raises if not exact."""
    p = dict(p)
    for _ in range(n):
        # divide by (A^4 + 1): long division from the top
        q = {}; r = dict(p)
        while r:
            e = max(r); c = r[e]
            if len(r) == 1 or e - 4 < min(r):
                raise ArithmeticError('not divisible by delta')
            q[e - 4] = q.get(e - 4, 0) + c
            padd(r, {e: c, e - 4: c}, -1)
        # p / delta = -A^2 * q
        p = {e + 2: -c for e, c in q.items() if c}
    return p
def A_to_t(y):
    """y(A) with all exponents congruent mod 4 -> J(t) up to a unit (t = A^4, lp convention)"""
    if not y: return None
    e0 = min(y)
    out = {}
    for e, c in y.items():
        if (e - e0) % 4: return None
        out[(e - e0) // 4] = c
    return out
def normJ(y):
    jt = A_to_t(y)
    return None if jt is None else lp.normalize(jt)

_cache = {}
def ball(k=2):
    if k not in _cache: _cache[k] = Ball(k)
    return _cache[k]

PREFIXES = ['l1.l1', 'l1.l2']
SUFFIXES = ['u1.u2', 'u2.u2', 'u3.u2']

def setup(k=2):
    B = ball(k)
    if not hasattr(B, 'V'):
        B.V = {P: B.vec_of_prefix(P) for P in (PREFIXES if k == 2 else [])}
        B.PHI = {}; B.PHIX = {}
        for S in (SUFFIXES if k == 2 else []):
            B.PHI[S], B.PHIX[S] = B.covec_of_suffix(S)   # PHIX[S] = plain y-functional on all 42 matchings
    return B

def J_split(prefix, W, suffix, k=2):
    """normalised J of the halfword s.prefix.W.suffix computed in the module"""
    B = setup(k)
    v = B.V[prefix] if prefix in getattr(B, 'V', {}) else B.vec_of_prefix(prefix)
    if suffix in getattr(B, 'PHI', {}): phi = B.PHI[suffix]
    else: phi = B.covec_of_suffix(suffix)[0]
    y = pdiv_delta(B.pair(phi, B.apply(W, v)), 2 * k)
    return normJ(y)

def halfword(prefix, W, suffix):
    if isinstance(W, (list, tuple)): W = '.'.join(W)
    return 's.' + '.'.join(x for x in [prefix, W, suffix] if x)

def basis_table(k=2):
    """human-readable basis: for each basis matching, list of pairs with names E, ax, b0a,b0b, b1a,..."""
    B = ball(k)
    names = ['E', 'ax'] + [nm for j in range(2 * k) for nm in ('b%da' % j, 'b%db' % j)]
    rows = []
    for i, m in enumerate(B.basis):
        pairs = sorted(set(tuple(sorted((a, m[a]))) for a in range(len(m))))
        rows.append('e%d: ' % i + ' '.join('%s-%s' % (names[a], names[b]) for a, b in pairs))
    return rows

# ---------------- modular evaluation ----------------
def ev_mod(poly, a, p):
    s = 0
    for e, c in poly.items():
        s += c * pow(a, e % (p - 1), p)
    return s % p
def mats_mod(p, a, k=2):
    B = setup(k)
    out = {}
    for L, M in B.M.items():
        out[L] = [[ev_mod(x, a, p) for x in row] for row in M]
    V = {P: [ev_mod(x, a, p) for x in v] for P, v in getattr(B, 'V', {}).items()}
    PHI = {S: [ev_mod(x, a, p) for x in v] for S, v in getattr(B, 'PHI', {}).items()}
    return out, V, PHI

if __name__ == '__main__':
    B = setup(2)
    print('k=2: all matchings', len(B.all), 'basis dim', B.dim, 'self-matched', len(B.selfm))
    print('invariance failures', B.check_invariance())
    for S in SUFFIXES: print('PHI', S, 'nonvanishing on self-matched:', B.covec_vanishes_on_self(S))
    for r in basis_table(2): print(r)

# ======================================================================================================================
# NORMALISED INTEGRAL FORM (k = 2), variable t = A^4 (lp convention).  Gauge f_j = A^(-2 c_j) e_j with
#   c = GAUGE = (0,1,0,1,1,0,1,1,1); then every entry lies in Z[t, 1/t].
#   Y   := t^-2 M[y0]   (axis full twist; eigenvalues 1 (x4, channel V_1) and t^-3 (x5, channel V_3)) = TH-2BR Y
#   X_i := t^2  M[x_i]  (leg crossing i-1,i; eigenvalues 1 (x2, legs fuse to V_0), -t (x4, V_2), t^3 (x3, V_4)) = TH-2BR X
#   (so y0 <-> Y, x0 <-> Y^-1, x_i <-> X_i, y_i <-> X_i^-1, exactly as the BRIEF's sign dictionary for width one).
#   V['l1.l1'] = e_0 (= f_0),  V['l1.l2'] = e_2 (= f_2):  the two prefix vectors are BASIS vectors.
#   PHI_t[S] (integral covector) with   J_raw(s.P.W.S) =. t^2 * PHI_t[S] . rho(W) V[P] / (1+t)^4     (=. : up to a unit)
#   (the (1+t)^4 = t^2 delta^4 is the f_2^{(x)4} denominator; it always divides on physical vectors).
# ======================================================================================================================
GAUGE = (0, 1, 0, 1, 1, 0, 1, 1, 1)
def _gauge_t(p, shift):
    """A-poly with exponents = shift mod 4 -> t-poly after multiplying by A^(-shift)"""
    out = {}
    for e, c in p.items():
        f = e - shift
        assert f % 4 == 0, (e, shift)
        out[f // 4] = out.get(f // 4, 0) + c
    return {e: c for e, c in out.items() if c}
def normalised(k=2):
    """returns (MT, VT, PHIT): MT[letter] 9x9 over Z[t^+-1] with the unit normalisations above, VT[prefix], PHIT[suffix]"""
    assert k == 2
    B = setup(2)
    c = GAUGE; n = B.dim
    MT = {}
    for L, M in B.M.items():
        unit = {'x': 8, 'y': -8}[L[0]] if L[1:] != '0' else {'y': -8, 'x': 8}[L[0]]
        # x_i -> t^2 M (A^8), y_i -> t^-2 M ; y0 -> t^-2 M (A^-8), x0 -> t^2 M
        MT[L] = [[_gauge_t(pshift(M[i][j], unit), -2 * (c[i] - c[j])) if M[i][j] else {}
                  for j in range(n)] for i in range(n)]
    # vectors: v'_i = v_i A^(2 c_i)
    VT = {P: [_gauge_t(pshift(v[i], 2 * c[i]), 0) if v[i] else {} for i in range(n)] for P, v in B.V.items()}
    # functionals: phi'_j = phi_j A^(-2 c_j)
    PHIT = {S: [_gauge_t(pshift(ph[j], -2 * c[j]), 0) if ph[j] else {} for j in range(n)] for S, ph in B.PHI.items()}
    return MT, VT, PHIT

def _tadd(p, q):
    r = dict(p)
    for e, cc in q.items():
        r[e] = r.get(e, 0) + cc
    return {e: cc for e, cc in r.items() if cc}
def _tmul(p, q):
    r = {}
    for e, a in p.items():
        for f, b in q.items(): r[e + f] = r.get(e + f, 0) + a * b
    return {e: cc for e, cc in r.items() if cc}
def tdiv_1pt(p, n):
    """exact division of a t-Laurent poly by (1+t)^n"""
    for _ in range(n):
        if not p: return {}
        lo = min(p); hi = max(p)
        q = {}; r = dict(p)
        for e in range(lo, hi):
            cc = r.get(e, 0)
            if cc:
                q[e] = cc; r[e] = 0; r[e + 1] = r.get(e + 1, 0) - cc
        r = {e: cc for e, cc in r.items() if cc}
        if r: raise ArithmeticError('not divisible by 1+t')
        p = q
    return p
_NT = None
def J_t(prefix, W, suffix):
    """normalised J computed in the integral t-form (same value as J_split / lp.J)"""
    global _NT
    if _NT is None: _NT = normalised()
    MT, VT, PHIT = _NT
    v = VT[prefix]
    if isinstance(W, str): W = [x for x in W.split('.') if x]
    for L in W:
        M = MT[L]
        v = [_rowdot_t(M[i], v) for i in range(9)]
    y = _rowdot_t(PHIT[suffix], v)
    y = tdiv_1pt(y, 4)
    return lp.normalize(y) if y else None
def _rowdot_t(row, v):
    r = {}
    for a, b in zip(row, v):
        if a and b:
            for e, x in a.items():
                for f, z in b.items():
                    r[e + f] = r.get(e + f, 0) + x * z
    return {e: cc for e, cc in r.items() if cc}

# ---------------- knot test by the leg permutation (k = 2) ----------------
_TOP = {'l1.l1': {0: 1, 1: 0, 2: 3, 3: 2}, 'l1.l3': {0: 1, 1: 0, 2: 3, 3: 2}, 'l1.l2': {0: 3, 3: 0, 1: 2, 2: 1}}
_BOT = {'u1.u2': ({0: 1, 1: 0}, 3, 2), 'u2.u2': ({1: 2, 2: 1}, 3, 0), 'u3.u2': ({2: 3, 3: 2}, 1, 0)}  # (cupped pairs, leg joined to c, leg to v_bot)
def perm_of(W):
    """bottom position of the leg that starts at top position p"""
    pos = list(range(4))   # pos[p] = current position of leg starting at p
    if isinstance(W, str): W = [x for x in W.split('.') if x]
    for L in W:
        i = int(L[1:])
        if i == 0: continue
        a, b = i - 1, i
        for p in range(4):
            if pos[p] == a: pos[p] = b
            elif pos[p] == b: pos[p] = a
    return pos
def is_knot(prefix, W, suffix):
    top = _TOP[prefix]; cups, cleg, bleg = _BOT[suffix]
    pos = perm_of(W); inv = {pos[p]: p for p in range(4)}
    seen = 0; j = cleg                              # arrive from c at bottom position cleg
    while True:
        p = inv[j]; seen += 1                       # go up the leg ending at bottom j, starting at top p
        q = top[p]; seen += 1                       # cap partner at the top, go down
        j = pos[q]
        if j == bleg: break
        if j not in cups: return False
        j = cups[j]
        if seen > 8: return False
    return seen == 4
