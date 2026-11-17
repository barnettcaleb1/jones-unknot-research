"""CHECK 3 (ARB-RESONANCE-BUDGET).
 For every actual body p (rational, general, nested, frontier records, and random 2-3 factor products) with eigenpair (A,B), B != 0:
  * f_m := first coordinate of rho(X)^-m (a,c) (independent matrix powers), m in [-40,40]; assert f_m = A - (-t)^-m B and f_m(-1) = 1;
  * ALL unit m in the window; each must lie in {nu_0(z), -nu_inf(z)}, z = B/A;
  * span identity span f_m = H + (-r0)_+ + (-rinf)_+ - tau0 - tauinf at EVERY m of the window (H = pole count of z in C*,
    r0 = nu_0 z - m, rinf = nu_inf z + m, tau_e = (nu_e(1 - (-t)^-m z))_+); for non-primitive pairs the corrected form
    span f_m = span(gcd) + H + ... is tested and the uncorrected one is reported (primitivity is a hypothesis of (5)).
 Formal adversarial pairs (any Laurent A, B; units planted at a chosen twist; A monomial = H = 0) test (7) beyond actual bodies.
 Direct half-diagram J (lp.J) cross-check of unit events on small bodies."""
import sys, random, time, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/arb-resonance')
from common import *
rng = random.Random(4040)
t0 = time.time()
W = 40
L = rational_all() + general_all() + nested_random(rng, 200) + frontier(rng)
base = [x for x in L if not eqp(x[1][0], x[1][1])]
prods = []
for j in range(120):
    k = rng.choice([2, 2, 3])
    kids = rng.sample(base, k)
    T = ('p', [c[2] for c in kids])
    prods.append(('PROD%d' % j, vc.starall([c[1] for c in kids]), T))
# content-carrying (non-primitive) products found in check 2 style: opposite-sign children at prime t^4 - t^3 - 1
P1 = {0: -1, 3: -1, 4: 1}
cp = []
for lab, v, T in base:
    r = nu(v[1], P1) - nu(v[0], P1)
    if r: cp.append((lab, v, T, r))
pos = [x for x in cp if x[3] > 0]; neg = [x for x in cp if x[3] < 0]
for j in range(min(12, len(pos) * len(neg))):
    x = rng.choice(pos); y = rng.choice(neg)
    prods.append(('CONTENT%d' % j, vc.starall([x[1], y[1]]), ('p', [x[2], y[2]])))
bodies = L + prods
stats = collections.Counter(); units = []; fails = []; kappa0 = []; H0 = []
nonprim = collections.Counter()
for lab, v, T in bodies:
    s = th(v); A, B = eig(s)
    if iszero(B): stats['scalar_skipped'] += 1; continue
    stats['bodies'] += 1
    nu0 = bot(B) - bot(A); ninf = top(A) - top(B); cands = {nu0, -ninf}; kappa = nu0 + ninf
    g = gcdL(A, B); prim = (g == {0: 1}); H = span(A) - span(g)
    stats['primitive' if prim else 'NONPRIMITIVE'] += 1
    if prim and H == 0: H0.append(lab)
    # matrix route, m = 0..W and 0..-W  (f_m = e1^T X^-m s)
    fm = {}
    cur = list(s)
    for m in range(0, W + 1):           # X^-m with m >= 0: apply Xi
        fm[m] = clean(dict(cur[0])); cur = lp.mvec(lp.Xi, cur)
    cur = lp.mvec(lp.Xm, list(s))
    for m in range(-1, -W - 1, -1):
        fm[m] = clean(dict(cur[0])); cur = lp.mvec(lp.Xm, cur)
    bunits = []
    for m in range(-W, W + 1):
        f = fm[m]
        if not eqp(f, sub(A, mul(tm(-m), B))): fails.append(('formula', lab, m)); continue
        if vc.ev(f, -1) != 1: fails.append(('f(-1)', lab, m))
        if isunit(f):
            bunits.append(m)
            stats['unit_events'] += 1
            if m in cands: stats['unit_in_cands'] += 1
            else: fails.append(('UNIT_OUTSIDE', lab, m, nu0, -ninf))
        # span identity
        r0 = nu0 - m; rinf = ninf + m
        tau0 = max(bot(f) - bot(A), 0); tauinf = max(top(A) - top(f), 0)
        rhs = H + max(-r0, 0) + max(-rinf, 0) - tau0 - tauinf
        if prim:
            stats['span_ok' if span(f) == rhs else 'span_FAIL'] += 1
            if span(f) != rhs: fails.append(('span', lab, m))
        else:
            nonprim['corrected_ok' if span(f) == rhs + span(g) else 'corrected_FAIL'] += 1
            nonprim['uncorrected_holds' if span(f) == rhs else 'uncorrected_fails'] += 1
        # positive contact only at aligned ends
        if tau0 > 0 and r0 != 0: fails.append(('tau0', lab, m))
        if tauinf > 0 and rinf != 0: fails.append(('tauinf', lab, m))
    if bunits:
        units.append((lab, bunits, sorted(cands), prim, H, kappa))
        if len(set(bunits)) == 2: stats['bodies_with_two_unit_twists'] += 1
    if kappa == 0:
        f = fm.get(nu0) if abs(nu0) <= W else None
        kappa0.append((lab, nu0, H, None if f is None else (max(bot(f) - bot(A), 0), max(top(A) - top(f), 0), isunit(f))))
print('bodies (nonscalar): %d; stats %s' % (stats['bodies'], dict(stats)), flush=True)
print('non-primitive bodies: span identity WITHOUT gcd correction %s' % dict(nonprim))
print('unit events: %d in %d bodies; all in candidate set: %s' % (stats['unit_events'], len(units), stats['unit_events'] == stats['unit_in_cands']))
cls = collections.Counter(u[0].split(':')[0][:4] for u in units)
print('  bodies with units by family:', dict(cls))
for u in units:
    if not u[0].startswith('R:'): print('  NON-RATIONAL unit body:', u)
print('  sample rational unit bodies:', units[:6])
print('primitive bodies with H = 0 (A a monomial):', len(H0), H0[:10])
print('kappa = 0 bodies (simultaneous resonance possible):', len(kappa0), kappa0[:12])
print('failures:', len(fails), fails[:10], flush=True)
# formal adversarial pairs for (7)
fstat = collections.Counter(); ffails = []
def rpoly(k, lo=-6, hi=6, cmax=2):
    p = {}
    for _ in range(k):
        e = rng.randint(lo, hi); p[e] = p.get(e, 0) + rng.choice([c for c in range(-cmax, cmax + 1) if c])
    return clean(p)
for trial in range(3000):
    kind = trial % 3
    A = {rng.randint(-4, 4): rng.choice([1, -1, 2])} if kind == 0 else rpoly(rng.randint(1, 6))
    if not A: continue
    u = {rng.randint(-8, 8): rng.choice([1, -1])}
    m0 = rng.randint(-12, 12)
    B = mul(tm(m0), sub(A, u)) if kind != 2 else rpoly(rng.randint(1, 6))
    if iszero(B): continue
    nu0 = bot(B) - bot(A); ninf = top(A) - top(B); cands = {nu0, -ninf}
    fstat['pairs' + ('_H0' if len(A) == 1 else '')] += 1
    for m in range(-W, W + 1):
        f = sub(A, mul(tm(-m), B))
        if isunit(f):
            fstat['unit_events'] += 1
            if m in cands: fstat['in_cands'] += 1
            else: ffails.append((A, B, m))
print('formal pairs: %s; outside candidates: %d %s' % (dict(fstat), len(ffails), ffails[:3]), flush=True)
# direct J cross-check of unit / non-unit events on small rational and general bodies
dj = collections.Counter(); djfail = []
small = [u for u in units if u[0].startswith('R:')][:12]
byl = {lab: (v, T) for lab, v, T in bodies}
for lab, bunits, cands, prim, H, kappa in small:
    v, T = byl[lab]
    w = vc.word(T)
    for m in sorted(set(bunits + [rng.randint(-3, 3)])):
        tw = ('y1.' * m if m > 0 else 'x1.' * (-m))
        Jd = lp.J('s.r2.' + tw + w + '.u1')
        Jc = vc.norm(sub(eig(th(v))[0], mul(tm(-m), eig(th(v))[1])))
        ok = (Jd == Jc)
        dj['match' if ok else 'MISMATCH'] += 1
        if m in bunits: dj['unit_events_confirmed_J=1' if Jd == {0: 1} else 'unit_event_J!=1'] += 1
        if not ok: djfail.append((lab, m, Jd, Jc))
print('direct half-diagram J cross-check:', dict(dj), djfail[:3])
print('time %.1f' % (time.time() - t0))
