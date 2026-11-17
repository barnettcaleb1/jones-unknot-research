"""Fast exact J for width-two words via the integral t-form of rho_2, with list-based Laurent polynomials, plus the
tropical (extreme-degree) cancellation analysis.  A poly is (lo, [c_lo, c_lo+1, ...]) or None for 0."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rho2, lp
def tolist(d):
    if not d: return None
    lo = min(d); hi = max(d)
    return (lo, [d.get(e, 0) for e in range(lo, hi + 1)])
def todict(p):
    if p is None: return {}
    lo, c = p
    return {lo + i: x for i, x in enumerate(c) if x}
def norm(p):
    if p is None: return None
    lo, c = p
    i = 0
    while i < len(c) and c[i] == 0: i += 1
    if i == len(c): return None
    j = len(c)
    while c[j - 1] == 0: j -= 1
    return (lo + i, c[i:j])
def mul(p, q):
    if p is None or q is None: return None
    (a, x), (b, y) = p, q
    r = [0] * (len(x) + len(y) - 1)
    for i, xi in enumerate(x):
        if xi:
            for j, yj in enumerate(y):
                r[i + j] += xi * yj
    return (a + b, r)
def addto(acc, p):
    """acc, p polys; returns acc + p"""
    if p is None: return acc
    if acc is None: return p
    (a, x), (b, y) = acc, p
    lo = min(a, b); hi = max(a + len(x), b + len(y))
    r = [0] * (hi - lo)
    for i, v in enumerate(x): r[a - lo + i] += v
    for i, v in enumerate(y): r[b - lo + i] += v
    return (lo, r)
MT, VT, PHIT = rho2.normalised()
LET = ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']
SM = {L: [[(j, tolist(MT[L][i][j])) for j in range(9) if MT[L][i][j]] for i in range(9)] for L in LET}
V0 = {P: [tolist(x) for x in v] for P, v in VT.items()}
PH = {S: [tolist(x) for x in ph] for S, ph in PHIT.items()}
def step(L, v):
    out = []
    for row in SM[L]:
        acc = None
        for j, m in row:
            if v[j] is not None: acc = addto(acc, mul(m, v[j]))
        out.append(norm(acc))
    return out
def Jraw(prefix, W, suffix):
    v = V0[prefix]
    for L in W: v = step(L, v)
    acc = None
    for j in range(9):
        if v[j] is not None and PH[suffix][j] is not None: acc = addto(acc, mul(PH[suffix][j], v[j]))
    return norm(acc)      # = (1+t)^4 t^-2 J_raw ; division not needed for span/shape (span J = span - 4)
def J(prefix, W, suffix):
    r = Jraw(prefix, W, suffix)
    if r is None: return None
    y = rho2.tdiv_1pt(todict(r), 4)
    return lp.normalize(y)
def top(p): return p[0] + len(p[1]) - 1
def bot(p): return p[0]
def tropical(prefix, W, suffix):
    """global max-plus / min-plus prediction of top/bottom degree of PHI.rho(W).v ignoring all cancellation, and the
    per-step local cancellation events: list of (step k, letter, component i, top_loss, bot_loss)"""
    v = V0[prefix]
    tt = [top(x) if x else None for x in v]; tb = [bot(x) if x else None for x in v]
    events = []
    for k, L in enumerate(W):
        nv = step(L, v)
        # local prediction from the actual previous vector
        for i, row in enumerate(SM[L]):
            pt = [top(m) + top(v[j]) for j, m in row if v[j] is not None]
            pb = [bot(m) + bot(v[j]) for j, m in row if v[j] is not None]
            if not pt: continue
            at = top(nv[i]) if nv[i] else None
            ab = bot(nv[i]) if nv[i] else None
            lt = (max(pt) - at) if at is not None else 'zero'
            lb = (ab - min(pb)) if ab is not None else 'zero'
            if lt != 0 or lb != 0: events.append((k, L, i, lt, lb))
        # global tropical
        ntt = []; ntb = []
        for row in SM[L]:
            c = [top(m) + tt[j] for j, m in row if tt[j] is not None]
            d = [bot(m) + tb[j] for j, m in row if tb[j] is not None]
            ntt.append(max(c) if c else None); ntb.append(min(d) if d else None)
        tt, tb = ntt, ntb
        v = nv
    ph = PH[suffix]
    ft = max(top(ph[j]) + tt[j] for j in range(9) if ph[j] and tt[j] is not None)
    fb = min(bot(ph[j]) + tb[j] for j in range(9) if ph[j] and tb[j] is not None)
    r = Jraw(prefix, W, suffix)
    # final local event
    pt = max(top(ph[j]) + top(v[j]) for j in range(9) if ph[j] and v[j])
    pb = min(bot(ph[j]) + bot(v[j]) for j in range(9) if ph[j] and v[j])
    events.append(('close', None, None, pt - top(r), bot(r) - pb))
    return {'trop_top': ft, 'trop_bot': fb, 'top': top(r), 'bot': bot(r), 'trop_span': ft - fb, 'span': top(r) - bot(r),
            'deficit': (ft - fb) - (top(r) - bot(r)), 'events': events}
if __name__ == '__main__':
    import random, time
    rnd = random.Random(1); n = 0; t0 = time.time()
    for it in range(300):
        W = [rnd.choice(LET) for _ in range(rnd.randint(1, 20))]
        if not rho2.is_knot('l1.l1', W, 'u2.u2'): continue
        a = J('l1.l1', W, 'u2.u2'); b = lp.J(rho2.halfword('l1.l1', W, 'u2.u2'))
        assert a == b, (W, a, b)
        n += 1
    print('fastJ == lp.J on', n, 'random knots; time', round(time.time() - t0, 2))
    W = 'y0.x1.x2.y3.x0.y1.x2'.split('.')
    print(tropical('l1.l1', W, 'u2.u2'))
