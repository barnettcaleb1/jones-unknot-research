"""Referee ARB-CONTENT / ARB-RESONANCE-BUDGET (17 Nov 2026).  Shared helpers.
Laurent polynomials are {exp: coeff} dicts (lp.py / vc.py conventions).  vc stores box vectors in CHANNEL coordinates (a, b);
TH-2BR / integral-state coordinates are (a, c) with b = a + (1-t^3) c.  Codex's eigenpair: A = a + C c, B = C c,
C = (1-t)(1+t^2), e = -t/(1+t^2)."""
import sys, random, pickle, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, vc, lib
from lp import clean, add, neg, sub, mul, mono, ONE, shift, top, bot, span
import sympy as sp
t = sp.Symbol('t')

C   = {0:1, 1:-1, 2:1, 3:-1}          # (1-t)(1+t^2)
D3  = {0:1, 3:-1}                      # d = 1 - t^3
PHI3= {0:1, 1:1, 2:1}
PHI5= {0:1, 1:1, 2:1, 3:1, 4:1}
T2P1= {0:1, 2:1}                       # 1 + t^2
OMT = {0:1, 1:-1}                      # 1 - t
def tm(k): return {k: (-1)**(k % 2)}   # (-t)^k
def scale(p, c): return clean({e: c*v for e, v in p.items()})
def iszero(p): return not clean(dict(p))
def eqp(p, q): return clean(dict(p)) == clean(dict(q))
def isunit(p): p = clean(dict(p)); return len(p) == 1 and abs(next(iter(p.values()))) == 1
def to_sym(p): return sum(sp.Integer(c)*t**e for e, c in p.items()) if p else sp.Integer(0)
def from_sym(x):
    x = sp.expand(sp.cancel(sp.together(x)))
    num, den = sp.fraction(sp.together(x))
    num = sp.Poly(sp.expand(num), t); den = sp.Poly(sp.expand(den), t)
    q, r = sp.div(num, den)
    if not r.is_zero: return None                          # not a polynomial in t (after clearing t-power denominators below)
    return None
def laurent_from_sym(x):
    """exact conversion of a sympy rational function that IS a Laurent polynomial; None otherwise"""
    x = sp.cancel(sp.together(x))
    num, den = sp.fraction(x)
    den = sp.Poly(den, t); num = sp.Poly(num, t)
    # den must be c * t^k
    terms = den.terms()
    if len(terms) != 1: return None
    (k,), c = terms[0]
    out = {}
    for (e,), v in num.terms():
        if v % c: return None
        out[e - k] = int(v // c)
    return clean(out)

def th(v):
    """channel (a,b) -> integral state (a,c)"""
    c = vc.divexact(sub(v[1], v[0]), D3)
    assert c is not None
    return (clean(dict(v[0])), c)
def chan(s):
    a, c = s
    return (a, add(a, mul(D3, c)))
def eig(s):
    a, c = s
    B = mul(C, c)
    return (add(a, B), B)
def star_th(s1, s2):
    a1, c1 = s1; a2, c2 = s2
    return (mul(a1, a2), add(mul(a1, c2), mul(c1, a2), mul(D3, mul(c1, c2))))

# ---------- valuations
def nu_int(f, p):
    f = clean(dict(f))
    if not f: return 10**9
    best = 10**9
    for c in f.values():
        k = 0
        while c % p == 0: c //= p; k += 1
        best = min(best, k)
    return best
def nu_poly(f, P):
    f = clean(dict(f))
    if not f: return 10**9
    k = 0
    while True:
        q = vc.divexact(f, P)
        if q is None: return k
        f = q; k += 1
def nu(f, p):
    return nu_int(f, p) if isinstance(p, int) else nu_poly(f, p)
def gamma(s, p):
    return min(nu(s[0], p), nu(s[1], p))

# ---------- sympy gcd / factor over Z[t] (Laurent: shift to a polynomial first)
def to_poly(f):
    f = clean(dict(f)); lo = bot(f)
    return sp.Poly(sum(sp.Integer(c)*t**(e-lo) for e, c in f.items()), t, domain='ZZ')
def poly_to_dict(P):
    return clean({e: int(c) for (e,), c in P.terms()})
def gcdL(f, g):
    """gcd in Z[t,1/t] up to units (+-t^k), normalised: lowest exponent 0, positive leading coeff"""
    G = sp.gcd(to_poly(f), to_poly(g))
    d = poly_to_dict(G)
    if d and d[top(d)] < 0: d = scale(d, -1)
    return shift(d, -bot(d)) if d else d
def factors(f):
    """irreducible factors over Z of a Laurent poly (non-monomial ones, primitive) and integer primes of its content"""
    P = to_poly(f)
    cont, lst = sp.factor_list(P)
    out = []
    for fac, mult in lst:
        d = poly_to_dict(fac)
        if len(d) == 1:   # t or integer
            continue
        if d[top(d)] < 0: d = scale(d, -1)
        out.append(shift(d, -bot(d)))
    ints = [int(q) for q in sp.factorint(abs(int(cont))).keys()] if abs(int(cont)) > 1 else []
    return out, ints
def pkey(P): return tuple(sorted(P.items())) if isinstance(P, dict) else P

# ---------- box library (actual bodies)
R5 = lib.rational(5); R4 = lib.rational(4)
def tree_of(rep, R):
    idx, N, m = rep
    return ('n', m, [R[i][2] for i in idx] + ([('w', ('Y' if N > 0 else 'y')*abs(N))] if N else []))
def general_all():
    out = []
    for i, (Bw, v) in enumerate(vc.gboxes()):
        out.append(('G%d' % i, v, ('g', i)))
    return out
def rational_all():
    return [('R:' + str(T[1]), v, T) for (k, v, T, tag) in R5]
def nested_random(rng, n, depth2_frac=0.4):
    base = [(T, v) for (k, v, T, tag) in R4] + [(T, v) for (lab, v, T) in general_all() if int(lab[1:]) in lib.NONRAT]
    out = []
    tries = 0
    while len(out) < n and tries < 50*n:
        tries += 1
        k = rng.choice([1, 2, 2, 3])
        kids = [rng.choice(base) for _ in range(k)]
        m = rng.choice([x for x in range(-4, 5) if x]); N = rng.randint(-2, 2)
        T = ('n', m, [c[0] for c in kids] + ([('w', ('Y' if N > 0 else 'y')*abs(N))] if N else []))
        try:
            v = vc.vec(T)
        except AssertionError:
            continue
        if rng.random() < depth2_frac:
            u = rng.choice(base); m2 = rng.choice([x for x in range(-3, 4) if x])
            T = ('n', m2, [T, u[0]])
            try: v = vc.vec(T)
            except AssertionError: continue
        if eqp(v[0], v[1]): continue
        out.append(('N%d' % len(out), v, T))
    return out
def frontier(rng, nD=150, nd2=100):
    arb = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb/'
    out = []
    g = pickle.load(open(arb + 'greedy_n2.pkl', 'rb'))
    labs = sorted(g['D'].keys(), key=lambda s: int(s.split('_')[1]))
    for lab in rng.sample(labs, min(nD, len(labs))):
        rep = g['D'][lab][1][1]
        T = tree_of(rep, R5)
        out.append(('D:' + lab, vc.vec(T), T))
    d2 = pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl', 'rb'))
    for i, (k, v, T, tag) in enumerate(rng.sample(d2, min(nd2, len(d2)))):
        out.append(('d2pos:%d' % i, v, T))
    # N-INF family (arb REPORT section 2): u = B(XY), P_k = Y^(-k/3) u^k, F_{+-1}, F_{+2}
    u = vc.rat('XY')
    for k in (6, 12):
        Pk = vc.Ypow(-k//3, vc.starall([u]*k))
        out.append(('NINF:P%d' % k, Pk, ('p', [('w', 'XY')]*k + [('w', 'y'*(k//3))])))
        for m in (-1, 1, 2):
            out.append(('NINF:F%d(P%d)' % (m, k), vc.F(m, Pk), ('n', m, [('w', 'XY')]*k + [('w', 'y'*(k//3))])))
    # positive-potential depth-one examples (arb REPORT section 3)
    for m, w1, w2 in ((-5, 'XY', 'xy'), (5, 'XY', 'xy'), (-4, 'XY', 'xy'), (6, 'XXY', 'xxy'), (-6, 'XXY', 'xxy'), (7, 'XXXY', 'xxxy'), (-7, 'XXXY', 'xxxy')):
        T = ('n', m, [('w', w1), ('w', w2)])
        out.append(('POS:F%d(%s,%s)' % (m, w1, w2), vc.vec(T), T))
    # near-miss products recorded by the exact frontier searches (minspan trees)
    for f in ('ex_d1', 'ex_d2', 'ex_d3', 'ex_d4', 'ex_d5', 'ex_d6', 'ex_o3', 'ex_o3b', 'ex_s2'):
        d = pickle.load(open(arb + f + '.pkl', 'rb'))
        trees = d['minspan'][2]
        T = ('p', list(trees))
        out.append(('MIN:' + f, vc.vec(T), T))
    return out
