"""Independent referee engine (skein-dictionary referee, 17 Nov 2026).
Written from scratch; does NOT import flat_search / kauffman / lp (those are only used by the
comparison scripts).  Laurent polynomials in A are dicts {exp: int}.

Conventions (the note's Section 1): x-crossing = A*I + A^-1*e (I = vertical smoothing, e = cup-cap),
y-crossing = A^-1*I + A*e, circle delta = -A^2 - A^-2, empty diagram = 1.
"""
from itertools import product

# ---------------- Laurent polynomials in A ----------------
def pclean(p): return {e: c for e, c in p.items() if c}
def padd(*ps):
    r = {}
    for p in ps:
        for e, c in p.items(): r[e] = r.get(e, 0) + c
    return pclean(r)
def pneg(p): return {e: -c for e, c in p.items()}
def psub(p, q): return padd(p, pneg(q))
def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items(): r[e + f] = r.get(e + f, 0) + c * d
    return pclean(r)
def pmono(e, c=1): return {e: c}
def pshift(p, k): return {e + k: c for e, c in p.items()}
ONE = {0: 1}
DELTA = {2: -1, -2: -1}              # -A^2 - A^-2
DELTA2 = {4: 1, 0: 1, -4: 1}         # delta^2 - 1 = A^4 + 1 + A^-4

def pdiv(p, d):
    """exact division p/d in Z[A,A^-1]; returns None if not exact (long division from the top)"""
    p = pclean(p); d = pclean(d)
    if not p: return {}
    if not d: raise ZeroDivisionError
    dt, db = max(d), min(d); dc = d[dt]
    pb = min(p)
    q = {}
    while p:
        e = max(p)
        if e - dt < pb - db: return None          # quotient term would be below the lowest possible degree
        c = p[e]
        if c % dc: return None
        k = e - dt
        q[k] = q.get(k, 0) + c // dc
        p = psub(p, pmul({k: c // dc}, d))
    return pclean(q)

# ---------------- sweep evaluator ----------------
# A state is a tuple `m` over slots: n_top fixed top points, then the current strands (left to right).
# m[i] = partner slot of i.  Ops: ('cap',i) inserts new joined strands at strand positions i,i+1;
# ('cup',i) joins strands i,i+1; ('x',i)/('y',i) crossing of strands i,i+1.
def _cap(m, nt, i):
    j = nt + i
    m2 = [x + 2 if x >= j else x for x in m]
    m2[j:j] = [j + 1, j]
    return tuple(m2)

def _cup(m, nt, i):
    j = nt + i
    p, q = m[j], m[j + 1]
    m2 = list(m); loop = False
    if p == j + 1: loop = True
    else: m2[p] = q; m2[q] = p
    del m2[j:j + 2]
    m2 = [x - 2 if x > j + 1 else x for x in m2]
    return tuple(m2), loop

def sweep(ops, n_top=0):
    """Kauffman bracket state sweep.  Returns {final matching tuple: Laurent poly in A}."""
    m0 = []
    for i in range(n_top): m0.append(n_top + i)
    for i in range(n_top): m0.append(i)
    state = {tuple(m0): ONE}
    for op, i in ops:
        new = {}
        for m, p in state.items():
            W = len(m) - n_top
            if op == 'cap':
                if not (0 <= i <= W): raise ValueError('bad cap')
                k = _cap(m, n_top, i); new[k] = padd(new.get(k, {}), p)
            elif op == 'cup':
                if not (0 <= i and i + 1 < W): raise ValueError('bad cup')
                k, loop = _cup(m, n_top, i)
                new[k] = padd(new.get(k, {}), pmul(p, DELTA) if loop else p)
            elif op in ('x', 'y'):
                if not (0 <= i and i + 1 < W): raise ValueError('bad crossing')
                av, ah = (1, -1) if op == 'x' else (-1, 1)
                new[m] = padd(new.get(m, {}), pshift(p, av))
                k, loop = _cup(m, n_top, i)
                q = pmul(p, DELTA) if loop else p
                k2 = _cap(k, n_top, i)
                new[k2] = padd(new.get(k2, {}), pshift(q, ah))
            else: raise ValueError(op)
        state = {m: p for m, p in new.items() if p}
    return state

def closed_bracket(ops):
    st = sweep(ops, 0)
    assert set(st) <= {()}, st.keys()
    return st.get((), {})

# ---------------- half-words and their ribbon doubling ----------------
def parse(word):
    w = word.strip()
    if w.startswith('s.'): w = w[2:]
    return [(tok[0], int(tok[1:])) for tok in w.split('.') if tok]

def ribbon_ops(half, off=0):
    """Ribbon (2-cable) of the quotient arc together with the axis.
    Quotient strand positions: axis at off, band of half-strand j at off+2j+1, off+2j+2.
    x0/y0 : full monodromy of the axis with band 0 (axis crosses the band and comes back);
    x_s/y_s (s>=1): band of half-strand s-1 crosses band of half-strand s (4 crossings);
    l_s/r_s: band cap at half-positions s-1,s; u_s: band cup there."""
    ops = []
    for c, s in half:
        if c in 'xy':
            if s == 0:
                ops += [(c, off), (c, off + 1), (c, off + 1), (c, off)]
            else:
                a = off + 2 * s - 1     # left strand of the left band
                ops += [(c, a + 1), (c, a), (c, a + 2), (c, a + 1)]
        elif c in 'lr':
            a = off + 2 * s - 1
            ops += [('cap', a), ('cap', a + 1)]
        elif c == 'u':
            a = off + 2 * s - 1
            ops += [('cup', a + 1), ('cup', a)]
        else: raise ValueError(c)
    return ops

# ---------------- theta-graph closures built directly (my own vertex marking) ----------------
# Slots: A2 (the outer axis edge) on the far left at position 0; A1 (inner axis edge, the drawn axis) at 1;
# band of half-strand 0 at 2,3.  Planar (1,1,2) vertices: A1 joins the inner band strand, A2 the outer one.
def D_I_ops(word):
    half = parse(word)
    top = [('cap', 0), ('cap', 1)]               # [A2 | b2] then inner cap [A1 | b1]  ->  A2 A1 b1 b2
    bot = [('cup', 1), ('cup', 0)]               # A1-b1 at v_bot, then A2-b2
    return top + ribbon_ops(half, off=1) + bot

def D_e_top_ops(word):
    half = parse(word)
    top = [('cap', 0), ('cap', 2)]               # A2-A1 joined (axis restored), band turned back (e at v_top)
    bot = [('cup', 1), ('cup', 0)]
    return top + ribbon_ops(half, off=1) + bot

def D_e_bot_ops(word):
    half = parse(word)
    top = [('cap', 0), ('cap', 1)]
    bot = [('cup', 2), ('cup', 0)]               # band turned back at v_bot, A1-A2 joined
    return top + ribbon_ops(half, off=1) + bot

def theta_data(word):
    """Returns dict with L_b=<D_I>, L_c=<D_e>, theta=<Theta;1,1,2>=L_b-delta^-1 L_c, y, x, u (all in A)."""
    Lb = closed_bracket(D_I_ops(word))
    Lc = closed_bracket(D_e_top_ops(word))
    Lc2 = closed_bracket(D_e_bot_ops(word))
    Lc_over_d = pdiv(Lc, DELTA)
    assert Lc_over_d is not None
    theta = psub(Lb, Lc_over_d)                      # L_b - delta^-1 L_c
    y = pdiv(theta, DELTA2)
    assert y is not None, 'theta not divisible by Delta2'
    u = Lc_over_d                                    # L_c = delta*u
    # x from L_c = delta y + delta^2 x
    x = pdiv(psub(Lc, pmul(DELTA, y)), pmul(DELTA, DELTA))
    return dict(Lb=Lb, Lc=Lc, Lc_bot=Lc2, theta=theta, y=y, u=u, x=x)

# ---------------- conversion to t = A^4 and preferred normalization ----------------
def to_t(p):
    """p in A^r Z[A^4]: return (r mod 4, poly in t) with p = A^r * f(A^4) for the minimal representative r."""
    if not p: return None, {}
    rs = {e % 4 for e in p}
    if len(rs) != 1: return 'mixed', None
    r = rs.pop()
    return r, {(e - r) // 4: c for e, c in p.items()}

def tev(f, x):
    if x in (1, -1): return sum(c * (x ** (e % 2)) for e, c in f.items())
    from fractions import Fraction
    return sum(c * Fraction(x) ** e for e, c in f.items())
def tder_m1(f):  # f'(-1)
    return sum(c * e * (-1) ** ((e - 1) % 2) for e, c in f.items())

def norm_unit(f):
    """unit (sgn,k) with Norm(f) = sgn * t^k * f: value 1 and derivative 0 at t=-1; None if f(-1) != +-1"""
    v = tev(f, -1)
    if v not in (1, -1): return None
    d = tder_m1(f)
    # g = s t^k f: g(-1) = s (-1)^k v ; g'(-1) = s[(k)(-1)^(k-1) v + (-1)^k d] = 0 -> k v = d
    if d % v: return None
    k = d // v
    s = v * (-1) ** (k % 2)
    return s, k

def tshift(f, k, s=1): return {e + k: s * c for e, c in f.items()}
def Norm(f):
    u = norm_unit(f)
    return None if u is None else tshift(f, u[1], u[0])

def tdiv(p, d):
    """exact division in Z[t,t^-1] (dict polys); None if not exact"""
    return pdiv(p, d)

def tmul(p, q): return pmul(p, q)
def tadd(*ps): return padd(*ps)
def tsub(p, q): return psub(p, q)

# ---------------- body TL3 expansion ----------------
# TL3 basis matchings on top points T0,T1,T2 (slots 0,1,2) and bottom strands B0,B1,B2 (slots 3,4,5)
TL3 = {
    'I':    (3, 4, 5, 0, 1, 2),
    'e1':   (1, 0, 5, 4, 3, 2),     # T0-T1, B0-B1, T2-B2
    'e2':   (3, 2, 1, 0, 5, 4),     # T1-T2, B1-B2, T0-B0
    'e1e2': (1, 0, 3, 2, 5, 4),     # T0-T1, T2-B0, B1-B2
    'e2e1': (5, 2, 1, 4, 3, 0),     # T1-T2, T0-B2, B0-B1
}
def body_TL3(B):
    """Expand the 2-cabled body (axis + band of half-strand 0) in TL3.  Returns dict name->poly in A."""
    half = parse(B)
    st = sweep(ribbon_ops(half, off=0), n_top=3)
    inv = {v: k for k, v in TL3.items()}
    out = {k: {} for k in TL3}
    for m, p in st.items():
        if m not in inv: raise ValueError('unexpected final matching %r (closed component or bad body?)' % (m,))
        out[inv[m]] = padd(out[inv[m]], p)
    return out

def body_channels(B):
    """raw channel amplitudes (a,b) in A with beta = a P1 + b P3 (f2 sandwiched); also c1, c_e, c_e/delta"""
    c = body_TL3(B)
    c1, ce = c['I'], c['e1']
    cep = pdiv(ce, DELTA)
    if cep is None: return dict(c=c, ok=False)
    a = padd(c1, pmul(cep, DELTA2))
    b = c1
    return dict(c=c, c1=c1, ce=ce, cep=cep, a=a, b=b, ok=True)

def nax(B): return sum(1 for c, s in parse(B) if c in 'xy' and s == 0)

# ---------------- macro sweep: insert a known TL3 element on strands pos..pos+2 ----------------
TL3_WORDS = {'I': [], 'e1': [('cup', 0), ('cap', 0)], 'e2': [('cup', 1), ('cap', 1)],
             'e1e2': [('cup', 0), ('cap', 1)], 'e2e1': [('cup', 1), ('cap', 0)]}
def _apply_ops(state, ops, n_top):
    for op, i in ops:
        new = {}
        for m, p in state.items():
            if op == 'cap':
                k = _cap(m, n_top, i); new[k] = padd(new.get(k, {}), p)
            elif op == 'cup':
                k, loop = _cup(m, n_top, i)
                new[k] = padd(new.get(k, {}), pmul(p, DELTA) if loop else p)
            else:
                av, ah = (1, -1) if op == 'x' else (-1, 1)
                new[m] = padd(new.get(m, {}), pshift(p, av))
                k, loop = _cup(m, n_top, i)
                q = pmul(p, DELTA) if loop else p
                k2 = _cap(k, n_top, i)
                new[k2] = padd(new.get(k2, {}), pshift(q, ah))
        state = {m: p for m, p in new.items() if p}
    return state

def sweep_macro(items, n_top):
    """items: list of ('ops', [ops]) or ('box', pos, tl3dict)"""
    m0 = [n_top + i for i in range(n_top)] + list(range(n_top))
    state = {tuple(m0): ONE}
    for it in items:
        if it[0] == 'ops':
            state = _apply_ops(state, it[1], n_top)
        else:
            _, pos, el = it
            acc = {}
            for name, coef in el.items():
                if not coef: continue
                ops = [(o, pos + j) for o, j in TL3_WORDS[name]]
                st2 = _apply_ops(state, ops, n_top)
                for m, p in st2.items():
                    acc[m] = padd(acc.get(m, {}), pmul(p, coef))
            state = {m: p for m, p in acc.items() if p}
    return state

def tl3_from_state(st):
    inv = {v: k for k, v in TL3.items()}
    out = {k: {} for k in TL3}
    for m, p in st.items():
        out[inv[m]] = padd(out[inv[m]], p)
    return out

def tl3_product(*els):
    return tl3_from_state(sweep_macro([('box', 0, e) for e in els], 3))

def tl3_necklace(m, inner):
    """TL3 element of r2.(y1)^m.<inner>.u1 with inner given as a TL3 element (locality only)"""
    tw = [('y', 1)] * m if m > 0 else [('x', 1)] * (-m)
    pre = ribbon_ops([('r', 2)] + tw)
    post = ribbon_ops([('u', 1)])
    return tl3_from_state(sweep_macro([('ops', pre), ('box', 0, inner), ('ops', post)], 3))

def channels_from_tl3(c):
    c1, ce = c['I'], c['e1']
    cep = pdiv(ce, DELTA)
    if cep is None: return dict(c=c, ok=False)
    return dict(c=c, c1=c1, ce=ce, cep=cep, a=padd(c1, pmul(cep, DELTA2)), b=c1, ok=True)
