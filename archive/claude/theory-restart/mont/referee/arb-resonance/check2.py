"""CHECK 2 (ARB-CONTENT).  gamma_p(v) = min(nu_p(a), nu_p(c)) on the integral state (a,c).
 (i) exact gain formula gamma_p(prod) - sum gamma_p(v_i) = (sum|r_i| - |sum r_i|)/2, r_i = nu_p(b_i) - nu_p(a_i), p not | 1-t^3,
     LHS computed from the integral star product (TH-2BR coordinates), RHS from the factors; >= 500 products of actual bodies,
     primes harvested from the factorisations of the children's channel amplitudes (so that r_i != 0), plus 2, 3, and the
     excluded primes 1-t, Phi3 (inequality (2) only; exact formula reported for information);
 (ii) invariance of gamma_p under F_m (normalised vc.F) and Y^N on content-carrying products;
 (iii) every horizontal and vertical closure of a content-carrying product is divisible by p^gamma;
 (iv) vertical identity (w1 a + wV b)/Phi3 = [(w1+wV)/Phi3] a + (1-t) wV c, Phi3 | w1 + wV, for all l in [-15,15]."""
import sys, random, time, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/arb-resonance')
from common import *
rng = random.Random(7)
t0 = time.time()
L = rational_all() + general_all() + nested_random(rng, 200) + frontier(rng)
L = [(lab, v, T) for lab, v, T in L if not eqp(v[0], v[1])]          # drop scalar states
print('bodies', len(L), flush=True)
# harvest primes
idx = collections.defaultdict(list); P = {}
nfac = 0
for i, (lab, v, T) in enumerate(L):
    a, b = v
    if span(a) > 60 or span(b) > 60: continue
    fa, _ = factors(a); fb, _ = factors(b); nfac += 1
    for f in set(pkey(x) for x in fa + fb):
        Pd = dict(f); P[f] = Pd
        r = nu(b, Pd) - nu(a, Pd)
        if r: idx[f].append((i, r))
print('factored %d bodies, %d distinct primes, %.1fs' % (nfac, len(P), time.time() - t0), flush=True)
both = [f for f in idx if any(r > 0 for _, r in idx[f]) and any(r < 0 for _, r in idx[f])]
print('primes with children of both signs:', len(both), flush=True)
EXCL = [('1-t', OMT), ('Phi3', PHI3)]
INTS = [2, 3]
res = collections.Counter(); gains = collections.Counter(); bad = []; content_prods = []
excl_formula = collections.Counter()
def evaluate(kids, plist):
    states = [th(L[i][1]) for i in kids]
    prod = states[0]
    for s in states[1:]: prod = star_th(prod, s)
    out = []
    for name, p in plist:
        lhs = gamma(prod, p)
        gs = sum(gamma(s, p) for s in states)
        rs = [nu(L[i][1][1], p) - nu(L[i][1][0], p) for i in kids]
        rhs = gs + (sum(abs(r) for r in rs) - abs(sum(rs))) // 2
        out.append((name, lhs, gs, rhs, rs))
    return prod, out
nprod = 0
def run(kids, plist, tag):
    global nprod
    nprod += 1
    prod, out = evaluate(kids, plist)
    for name, lhs, gs, rhs, rs in out:
        if name in ('1-t', 'Phi3'):
            res['excl_ineq_ok' if lhs >= gs else 'excl_ineq_FAIL'] += 1
            excl_formula['holds' if lhs == rhs else 'fails'] += 1
            if lhs < gs: bad.append((tag, kids, name, lhs, gs))
            continue
        res['ok' if lhs == rhs else 'FAIL'] += 1
        if lhs != rhs: bad.append((tag, kids, name, lhs, rhs, rs))
        gains[lhs - gs] += 1
        if lhs > 0: content_prods.append((kids, name, lhs))
# (a) targeted products: opposite-sign children at a shared prime
for f in both:
    print('  prime', sorted(P[f].items()), 'children r>0:', [(L[i][0], r) for i, r in idx[f] if r > 0][:6], 'r<0:', [(L[i][0], r) for i, r in idx[f] if r < 0][:6], flush=True)
for j in range(400):
    f = both[j % len(both)]
    pos = [i for i, r in idx[f] if r > 0]; negs = [i for i, r in idx[f] if r < 0]
    npos = rng.choice([1, 1, 2, 3]); nneg = rng.choice([1, 1, 2, 3])
    kids = [rng.choice(pos) for _ in range(npos)] + [rng.choice(negs) for _ in range(nneg)]
    if rng.random() < 0.3: kids.append(rng.randrange(len(L)))
    rng.shuffle(kids)
    others = rng.sample(list(P), min(2, len(P)))
    plist = [('P', P[f])] + [('Q', P[g]) for g in others] + [(str(q), q) for q in INTS] + EXCL
    run(kids, plist, 'targeted')
ntarg = nprod
# (b) random products, primes = those dividing some child's channel amplitude
for _ in range(400):
    kids = [rng.randrange(len(L)) for _ in range(rng.choice([2, 2, 3, 4]))]
    cand = [f for f in idx if any(i in kids for i, r in idx[f])]
    plist = [('P', P[f]) for f in rng.sample(cand, min(3, len(cand)))] + [(str(q), q) for q in INTS] + EXCL
    run(kids, plist, 'random')
print('products: %d (targeted %d, random %d); evaluations at primes not dividing 1-t^3: %s; gains histogram %s' % (
    nprod, ntarg, nprod - ntarg, dict(res), dict(sorted(gains.items()))), flush=True)
print('excluded primes 1-t, Phi3: inequality (2) %s; exact formula (3) there (not claimed) %s' % (
    {k: v for k, v in res.items() if k.startswith('excl')}, dict(excl_formula)), flush=True)
# (ii)-(iii) invariance and divisibility of closures on content-carrying products
inv = collections.Counter()
seen = set()
for kids, name, g in content_prods[:150]:
    key = tuple(kids)
    if key in seen: continue
    seen.add(key)
    vs = [L[i][1] for i in kids]
    p = vc.starall(vs)
    # the prime: recover from the evaluation list (re-run to find which prime)
    for f in idx:
        Pd = P[f]
        gp = gamma(th(p), Pd)
        if gp <= 0: continue
        for m in (-2, -1, 1, 2):
            inv['F_ok' if gamma(th(vc.F(m, p)), Pd) == gp else 'F_FAIL'] += 1
        for N in (-2, -1, 1, 2):
            inv['Y_ok' if gamma(th(vc.Ypow(N, p)), Pd) == gp else 'Y_FAIL'] += 1
        s = th(p); A, B = eig(s)
        for mu in range(-6, 7):
            f_mu = sub(A, mul(tm(mu), B))
            inv['H_div' if nu(f_mu, Pd) >= gp else 'H_NOTDIV'] += 1
        for l in (-7, -5, -3, -1, 1, 3, 5, 7):
            inv['V_div' if nu(vc.raw_vert(l, p), Pd) >= gp else 'V_NOTDIV'] += 1
        # nested further: F_m(prod * child) keeps >= gp
        u = L[rng.randrange(len(L))][1]
        q = vc.F(rng.choice([-2, -1, 1, 2]), vc.starall([p, u]))
        inv['nest_ok' if gamma(th(q), Pd) >= gp else 'nest_FAIL'] += 1
print('content-carrying products used: %d; invariance/divisibility: %s' % (len(seen), dict(inv)), flush=True)
# (iv) vertical identity
vv = collections.Counter()
for l in range(-15, 16):
    w1 = add(shift(ONE, 1), mul(T2P1, tm(l)))
    wV = add(shift(tm(l), 1), shift(PHI5, 3*l - 1))
    q = vc.divexact(add(w1, wV), PHI3)
    vv['Phi3|w1+wV' if q is not None else 'NOT'] += 1
    for lab, v, T in rng.sample(L, 20):
        a, c = th(v)
        lhs = vc.divexact(add(mul(w1, v[0]), mul(wV, v[1])), PHI3)
        rhs = add(mul(q, a), mul(OMT, mul(wV, c)))
        vv['id_ok' if lhs is not None and eqp(lhs, rhs) else 'id_FAIL'] += 1
        if l % 2: vv['raw_vert_match' if eqp(lhs, vc.raw_vert(l, v)) else 'raw_vert_MISMATCH'] += 1
print('vertical: %s' % dict(vv))
print('failures:', len(bad), bad[:8])
print('time %.1f' % (time.time() - t0))
