#!/usr/bin/env python3
"""harness.py -- builders and exact corner-bracket machinery for the EKT
fusion survey (cx-survey).

Conventions
  * ABSOLUTE Kauffman bracket throughout: <empty> = 1, <unknot> = delta,
    delta = -A^2 - A^-2.  bracket.py returns the reduced bracket (<O> = 1);
    we multiply back by delta, and by delta^k for k crossing-free components
    that spherogram drops from the PD code (unlinked_unknot_components).
  * PD code = spherogram Link.PD_code(): [a,b,c,d] counterclockwise from the
    incoming under-strand; A-smoothing joins (a,b),(c,d)   (validated in
    cx-tools/VALIDATION.md).
  * A 2-string site is a (2,2) tangle slot.  Local states:
        'I'  identity (IdentityBraid(2), the vertical through state)
        'e'  Temperley-Lieb turnback (ZeroTangle(): cup over cap)
        k    k full twists = BraidTangle([+-1]*2|k|, 2)
        'ring' identity with a crossing circle around both strands
    For a HORIZONTAL (rotated) site the same local states are rotated by 90
    degrees, so the local identity is the global ZeroTangle and the local
    turnback is the global IdentityBraid(2)  (this is the c1 seam box).
  * Four corners B00 = F(I,I), B10 = F(e,I), B01 = F(I,e), B11 = F(e,e),
    all from the SAME diagram with only the two boxes replaced (same outside
    framing; no per-corner writhe normalisation).
    With sigma^(2m) = A^(2m) [ I + (A^(-8m) - 1)/delta e ]  (one handedness;
    the other is A -> 1/A), the raw bracket of K(m,n) is
        <K(m,n)> = A^(-6(s1 m + s2 n)) * Q(x, y),
        Q = xy B00 + (1-x) y/delta B10 + x (1-y)/delta B01
            + (1-x)(1-y)/delta^2 B11,     x = A^(8 s1 m), y = A^(8 s2 n),
    s1, s2 in {+1,-1} the handedness of each box relative to the A-smoothing.
    Q = a' + b' x + c' y + d' xy with
        a' = B11/delta^2,  b' = (delta B01 - B11)/delta^2,
        c' = (delta B10 - B11)/delta^2,
        d' = B00 - B10/delta - B01/delta + B11/delta^2,
    and V(K(m,n)) = (unit) * Q/delta.  So b' = c' = 0  iff
        delta B10 = B11 = delta B01.
"""
import sys
import warnings

PKG = ('/Users/calebbarnett/Documents/Codex/2026-10-31/'
       'it-is-an-open-problem-whether-4/work/braid_classification/packages')
CX = ('/private/tmp/claude-501/-Users-calebbarnett/'
      '7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-tools')
for p in (PKG, CX):
    if p not in sys.path:
        sys.path.insert(0, p)

warnings.filterwarnings('ignore')
from spherogram.links.tangles import (  # noqa: E402
    IdentityBraid, BraidTangle, IntegerTangle, RationalTangle, ZeroTangle,
    CapTangle, CupTangle, Tangle, join_strands,
)
from spherogram.links.links import Crossing, Link, Strand  # noqa: E402
from bracket import (  # noqa: E402
    kauffman_bracket, Diagram, pmul, padd, pneg, pshift, pscale, pstr,
    pclean, ppow, DELTA, pdiv_delta, jones_from_bracket, jones_str,
)

ONE = {0: 1}
DELTA2 = pmul(DELTA, DELTA)
DELTA3 = pmul(DELTA2, DELTA)


# ---------------------------------------------------------------- tangles

def braid2_power(k):
    """Vertical 2-braid sigma_1^k (k may be negative)."""
    if k == 0:
        return IdentityBraid(2)
    return BraidTangle([1 if k > 0 else -1] * abs(k), 2)


def labeled_identity(label):
    """IdentityBraid(2) whose two Strand objects carry `label` (survives copy/rotate)."""
    s = [Strand(label), Strand(label)]
    return Tangle(2, s, [(s[0], 0), (s[1], 0), (s[0], 1), (s[1], 1)], f'Site({label})')


def ring_box():
    """(2,2) tangle: two vertical strands encircled by a crossing circle
    (strand 3 of sigma_2 sigma_1 sigma_1 sigma_2 wraps the pair, closed by cap/cup).
    Checked: its braid closure is the 3-component chain with lk = (-1, -1)."""
    top = IdentityBraid(2) | CapTangle()
    bot = IdentityBraid(2) | CupTangle()
    return top * BraidTangle([2, 1, 1, 2], 4) * bot


def box2(state, label=None):
    """Local (vertical) 2-string site in state 'I', 'e', 'ring' or int k (k full twists)."""
    if state == 'I':
        return labeled_identity(label) if label is not None else IdentityBraid(2)
    if state == 'e':
        return ZeroTangle()
    if state == 'ring':
        return ring_box()
    assert isinstance(state, int)
    return braid2_power(2 * state)


def omega(T):
    """Literal EKT operation (c1_nonunit_turnback.py): r -> (3r+8)/(r+3)."""
    return ((T + IntegerTangle(2)) * IntegerTangle(1)) + IntegerTangle(2)


def omega_bar(T):
    """Mirror image of omega: r -> (3r-8)/(3-r)  (= omega^-1 on fractions);
    omega_bar(infinity) = -3, the U slot of the designer's shell."""
    return ((T + IntegerTangle(-2)) * IntegerTangle(-1)) + IntegerTangle(-2)


def h_block():
    return BraidTangle([-2, -3, -1, -2], 4)


def sigma2(sign=1):
    return BraidTangle([2 * sign], 4)


def T_piece(kind, state, seed=None, label=None):
    """The top 4-strand piece  A = IdentityBraid(2) | rot90(T)  carrying the T site.

    kind = 'none': A0 = I2 | rot90(IntegerTangle(3))  (or rot90(omega(seed))), no site.
    kind = 'lit' : T = IntegerTangle(3) (or omega(seed)); the site box is a
                   vertical 2-string box on strands 3,4 immediately below the
                   rotated T  (full twists 'inside the rotated T').
    kind = 'seed': T = omega(S) with S = box2(state) [* seed]; the site is the
                   top of the EKT seed, the c1 n-site (rotated with T).
    """
    if kind == 'none':
        T = IntegerTangle(3) if seed is None else omega(seed)
        return IdentityBraid(2) | T.rotate(1)
    if kind == 'lit':
        T = IntegerTangle(3) if seed is None else omega(seed)
        A = IdentityBraid(2) | T.rotate(1)
        return A * (IdentityBraid(2) | box2(state, label))
    if kind == 'seed':
        S = box2(state, label) if seed is None else box2(state, label) * seed
        return IdentityBraid(2) | omega(S).rotate(1)
    raise ValueError(kind)


def U_piece(kind, state, label=None):
    """The bottom 4-strand piece  B = rot90(U) | IdentityBraid(2)  carrying the U site.
    kind = 'none': B0 = rot90(IntegerTangle(-3)) | I2, no site.
    kind = 'lit' : U = IntegerTangle(-3), vertical box on strands 1,2 just above it.
    kind = 'seed': U = omega_bar(box2(state))  (omega_bar(I) = -3 up to isotopy)."""
    if kind == 'none':
        return IntegerTangle(-3).rotate(1) | IdentityBraid(2)
    if kind == 'lit':
        B = IntegerTangle(-3).rotate(1) | IdentityBraid(2)
        return (box2(state, label) | IdentityBraid(2)) * B
    if kind == 'seed':
        return omega_bar(box2(state, label)).rotate(1) | IdentityBraid(2)
    raise ValueError(kind)


def seam_band(state, label=None):
    """c1-type seam site: horizontal box on strands 2,3 between the two h blocks.
    Local 'I' = global ZeroTangle (the band fusion), local 'e' = global
    IdentityBraid(2) (the unfused link), k = rot90(sigma^(2k))."""
    return IdentityBraid(1) | box2(state, label).rotate(1) | IdentityBraid(1)


def assemble(A, B, top=None, seam=None, bottom=None):
    """(4,4) tangle  A * [top] * h * [seam] * h * [bottom] * B  (top to bottom)."""
    X = A
    if top is not None:
        X = X * top
    X = X * h_block()
    if seam is not None:
        X = X * seam
    X = X * h_block()
    if bottom is not None:
        X = X * bottom
    X = X * B
    return X


def boundary_mates(T):
    """Trace actual strands (from c1_nonunit_turnback.py)."""
    ans = []
    for boundary in range(sum(T.boundary)):
        obj, port = T.adjacent[boundary]
        while obj is not T:
            port = (port + 2) % 4 if isinstance(obj, Crossing) else 1 - port
            obj, port = obj.adjacent[port]
        ans.append(port)
    return ans


def braid_closure_traced(X, site_labels=()):
    """Braid closure of the (n,n) tangle X; returns (Link, {label: [PD edge labels]}).

    The labelled site strands are located before Link() fuses them; the edge
    label is read back afterwards.  Link() may rotate a crossing by 180 degrees
    while orienting it, which preserves slot parity, so the edge is identified
    among the edges joining the two neighbouring crossings by slot parity."""
    T = X.copy()
    m, n = T.boundary
    assert m == n
    for i in range(n):
        join_strands(T.adjacent[i], T.adjacent[m + i])
    site_ends = {}
    for s in T.crossings:
        if isinstance(s, Strand) and s.label in site_labels:
            ends = []
            for port in (0, 1):
                obj, p = s.adjacent[port]
                guard = 0
                while isinstance(obj, Strand):
                    if obj is s or guard > 10000:
                        obj = None
                        break
                    obj, p = obj.adjacent[1 - p]
                    guard += 1
                ends.append((obj, p))
            site_ends.setdefault(s.label, []).append(ends)
    L = Link(T.crossings, check_planarity=False)
    L.PD_code()
    edges = {}
    for lab, lst in site_ends.items():
        labs = []
        for (c1, p1), (c2, p2) in lst:
            if c1 is None or c2 is None:
                labs.append('free-loop')
                continue
            cands = set()
            for q1 in (p1 % 4, (p1 + 2) % 4):
                d, q2 = c1.adjacent[q1]
                if d is c2 and q2 % 2 == p2 % 2:
                    cands.add(int(c1.strand_labels[q1]))
            cands = sorted(cands)
            labs.append(cands[0] if len(cands) == 1 else ('ambiguous', cands))
        edges[lab] = labs
    return L, edges


# ---------------------------------------------------------------- brackets

def abs_bracket(link):
    """Absolute bracket of a spherogram Link (crossing-free components included)."""
    pd = [tuple(int(x) for x in row) for row in link.PD_code()]
    free = int(getattr(link, 'unlinked_unknot_components', 0))
    if pd:
        br = pmul(kauffman_bracket(pd), DELTA)
        w = link.writhe()
        ncomp = len(link.link_components) + free
    else:
        br = dict(ONE)
        w = 0
        ncomp = free
    br = pmul(br, ppow(DELTA, free))
    return dict(bracket=br, pd=pd, crossings=len(pd), components=ncomp,
                free_loops=free, writhe=w)


def is_unit(p):
    p = pclean(p)
    return len(p) == 1 and abs(next(iter(p.values()))) == 1


def unit_times_delta(p):
    """Return the unit u (dict) with p = u * delta, or None."""
    try:
        q = pdiv_delta(p)
    except ArithmeticError:
        return None
    return q if is_unit(q) else None


def divisible_by(p, k):
    """exact division of p by delta^k; returns quotient or None."""
    r = dict(p)
    for _ in range(k):
        try:
            r = pdiv_delta(r)
        except ArithmeticError:
            return None
    return r


def jones_from_abs(br, writhe):
    """V (dict in powers of t^(1/2)) from an ABSOLUTE bracket and the writhe."""
    return jones_from_bracket(pdiv_delta(br), writhe)


def poly_json(p):
    return {str(e): c for e, c in sorted(pclean(p).items())}


def minus_A3_power(w):
    """(-A^3)^w as a Laurent polynomial."""
    return {3 * w: (-1) ** (w % 2)}


def analyze_corners(B, w0):
    """B: dict '00','10','01','11' -> absolute brackets; w0 = writhe of K(0,0).
    Returns the identity table (three exact polynomials) and the delta^3 x
    coefficients of V = unit * (a + b x + c y + d xy)."""
    B00, B10, B01, B11 = B['00'], B['10'], B['01'], B['11']
    dB10 = pmul(DELTA, B10)
    dB01 = pmul(DELTA, B01)
    dB00 = pmul(DELTA, B00)
    out = {}
    u = minus_A3_power(w0)
    E0 = padd(B00, pneg(pmul(u, DELTA)))       # B00 - (-A^3)^w0 delta
    E1 = padd(dB10, pneg(B11))                  # delta B10 - B11
    E2 = padd(dB01, pneg(B11))                  # delta B01 - B11
    out['unit_u'] = pstr(u)
    out['poly_B00_minus_u_delta'] = pstr(E0) if E0 else '0'
    out['poly_dB10_minus_B11'] = pstr(E1) if E1 else '0'
    out['poly_dB01_minus_B11'] = pstr(E2) if E2 else '0'
    out['unknot_seed_eq'] = (not E0)
    out['id_dB10_eq_B11'] = (not E1)           # c = 0
    out['id_dB01_eq_B11'] = (not E2)           # b = 0
    out['flat_site1_at_I'] = (dB00 == B10)     # site 1 flat when site 2 = I
    out['flat_site2_at_I'] = (dB00 == B01)     # site 2 flat when site 1 = I
    uu = unit_times_delta(B00)
    out['B00_unit_times_delta'] = (uu is not None)
    out['B00_unit'] = pstr(uu) if uu is not None else None
    d3a = B11
    d3b = E2
    d3c = E1
    d3d = padd(padd(pmul(DELTA2, B00), pneg(dB10)), padd(pneg(dB01), B11))
    coeffs = {}
    for name, val in (('a', d3a), ('b', d3b), ('c', d3c), ('d', d3d)):
        q3 = divisible_by(val, 3)
        q2 = divisible_by(val, 2) if q3 is None else None
        q1 = divisible_by(val, 1) if (q3 is None and q2 is None) else None
        coeffs[name] = dict(
            delta3_times=pstr(val) if val else '0',
            zero=(not val),
            exact=('delta^3 | it: coefficient = ' + pstr(q3)) if q3 is not None else
                  ('delta^2 | it: coefficient = (' + pstr(q2) + ')/delta') if q2 is not None else
                  ('delta | it: coefficient = (' + pstr(q1) + ')/delta^2') if q1 is not None else
                  'not divisible by delta: coefficient = (above)/delta^3',
        )
    out['coeffs'] = coeffs
    return out


def check_knot_hfk(pd):
    """HFK total rank / genus for a knot PD (knot_floer_homology); and snappy identify."""
    res = {}
    try:
        import snappy  # noqa: F401
        import spherogram
        L = spherogram.Link(pd)
        L2 = L.copy()
        L2.simplify('global')
        res['simplified_crossings'] = len(L2.crossings)
        res['simplified_free_unknots'] = int(getattr(L2, 'unlinked_unknot_components', 0))
        if len(L2.crossings) == 0:
            res['hfk_total_rank'] = 1
            res['hfk_genus'] = 0
            res['hfk_note'] = 'spherogram global simplification reached 0 crossings'
        else:
            try:
                h = L2.knot_floer_homology()
                res['hfk_total_rank'] = h['total_rank']
                res['hfk_genus'] = h['seifert_genus']
            except Exception as ex:
                res['hfk_error'] = repr(ex)
        try:
            E = L.exterior()
            res['volume'] = round(float(E.volume()), 6)
            res['solution_type'] = E.solution_type()
            res['identify'] = [str(m) for m in E.identify()]
        except Exception as ex:
            res['identify_error'] = repr(ex)
    except Exception as ex:
        res['error'] = repr(ex)
    return res


def link_geometry(link):
    """Volume / solution type of a spherogram Link exterior (any number of components)."""
    res = {}
    try:
        E = link.exterior()
        res['volume'] = round(float(E.volume()), 6)
        res['solution_type'] = E.solution_type()
        res['num_cusps'] = E.num_cusps()
    except Exception as ex:
        res['error'] = repr(ex)
    return res
