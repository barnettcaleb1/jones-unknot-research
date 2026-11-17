"""refs.py -- reference implementations from the project (read-only imports) + random halfword generators.
VK_ref(word) is a verbatim copy of mont/ft/ident3.py::VK (ident3.py runs a script at import time, so it is copied)."""
import sys, random
TOOLS = '/Users/calebbarnett/jones-lanes/theory-restart/tools'
MONT = '/Users/calebbarnett/jones-lanes/theory-restart/mont'
for p in (TOOLS, MONT):
    if p not in sys.path: sys.path.insert(0, p)
import kauffman, alex, flat_search as fs


def VK_ref(word):
    kb = kauffman.bracket(word)
    if not kb: return None
    kb = {e: c for e, c in kb.items() if c}
    es = sorted(kb); r = es[0] % 4
    if any((e - r) % 4 for e in es): return None
    V = {-(e - r) // 4: c for e, c in kb.items()}          # t = A^-4 up to a unit
    s = sum(V.values())
    if s not in (1, -1): return None
    V = {e: c * s for e, c in V.items()}
    d = sum(e * c for e, c in V.items())               # V'(1); shift t^-d to make it 0
    return {e - d: c for e, c in V.items()}


def alex_ref(word):
    """alex.alex_poly (sympy) normalised to a tuple ((exp, coeff), ...) with min exp 0 and Delta(1) > 0."""
    import sympy as sp
    t = sp.symbols('t')
    d = alex.alex_poly(word)
    if d is None: return None
    p = sp.Poly(sp.expand(d * t ** 200), t)       # clear any negative powers
    dd = {}
    for (e,), c in p.terms(): dd[int(e)] = int(c)
    lo = min(dd)
    q = {e - lo: c for e, c in dd.items()}
    if sum(q.values()) < 0: q = {e: -c for e, c in q.items()}
    return tuple(sorted(q.items()))


LET2 = ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']
INV2 = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}


def rand_width2(rnd, n, prefix='l1.l1', suffix='u2.u2'):
    W = []
    while len(W) < n:
        L = rnd.choice(LET2)
        if W and INV2[W[-1]] == L: continue
        W.append(L)
    return 's.' + prefix + '.' + '.'.join(W) + '.' + suffix


def is_knot(word):
    full = alex.symmetrize(alex.parse(word))
    return full is not None and alex.diagram(full) is not None


def random_halfwords(seed, count, minlen=4, maxlen=16, width2_frac=0.5, w2len=(2, 14)):
    """mix of flat_search.gen words (general grammar) and width-two words s.P.W.S; knots only."""
    rnd = random.Random(seed); out = []; seen = set()
    pre = ['l1.l1', 'l1.l2']; suf = ['u1.u2', 'u2.u2', 'u3.u2']
    while len(out) < count:
        if rnd.random() < width2_frac:
            w = rand_width2(rnd, rnd.randint(*w2len), rnd.choice(pre), rnd.choice(suf))
        else:
            w = fs.gen(rnd, rnd.randint(minlen, maxlen))
            if not w: continue
        if w in seen or not is_knot(w): continue
        seen.add(w); out.append(w)
    return out


def _interp(pts, vals):
    """exact Newton interpolation -> dict exp -> int"""
    from fractions import Fraction
    coef = [Fraction(v) for v in vals]; m = len(pts)
    for j in range(1, m):
        for i in range(m - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (pts[i] - pts[i - j])
    poly = [Fraction(0)] * m
    for i in range(m - 1, -1, -1):
        newp = [Fraction(0)] * m
        for e in range(m - 1): newp[e + 1] += poly[e]
        for e in range(m): newp[e] -= pts[i] * poly[e]
        newp[0] += coef[i]; poly = newp
    out = {}
    for e, c in enumerate(poly):
        if c:
            assert c.denominator == 1
            out[e] = int(c)
    return out


def alex_ref_fast(word):
    """alex.py's Alexander polynomial EXACTLY: the same matrix as alex.alex_poly (alex.alex_matrix, last row and column
    deleted) and alex.py's own Bareiss determinant, evaluated at integer t = 2..n+1 and interpolated exactly
    (sympy's symbolic determinant is too slow beyond ~15 crossings).  Normalised like alex_ref."""
    full = alex.symmetrize(alex.parse(word)); cr = alex.diagram(full)
    if cr is None: return None
    if not cr: return ((0, 1),)
    n = len(cr)
    pts = list(range(2, n + 2)); vals = []
    for x in pts:
        M, w = alex.alex_matrix(cr, x)
        vals.append(alex.bareiss([r[:-1] for r in M[:-1]]))
    dd = _interp(pts, vals)
    if not dd: return ()
    lo = min(dd)
    q = {e - lo: c for e, c in dd.items()}
    if sum(q.values()) < 0: q = {e: -c for e, c in q.items()}
    return tuple(sorted(q.items()))
