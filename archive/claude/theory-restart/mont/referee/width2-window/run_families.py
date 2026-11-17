"""Random + adversarial synthetic tables; brute force over |m|,|n| <= 10B + max(5,B); checks window (A),
line step (B) and the 10B square (C) via wbf.check_table.  Also records how close units come."""
import random, json, sys, time
from wbf import SECT, Table, trim, rand_poly, pmul, mono, pshift, pscale, check_table, proportional
from exhaustive import analyse_target, BOUND
from construct import construct

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 2026)
Dlist = [[1], [1, 1], [1, -1], [1, 1, 1], [1, 0, 1], [1, 0, 0, -1], [1, 1, 2, 1, 1], [1, 0, 0, 0, 1], [1,0,0,0,0,0,0,1]]
stats = []
allviol = []

def record(T, fam):
    r = check_table(T, tag=fam)
    stats.append({k: v for k, v in r.items() if k != 'units_sample'})
    if r['viol']:
        allviol.append((fam, r['viol'][:5], {s: T.p.get(s) for s in SECT}, T.D))
        print('VIOLATION', fam, r['viol'][:5], flush=True)
    return r

t0 = time.time()
# F0: signed monomial tables at arbitrary exponents within [0,W] (W<=3), D = 1 +- t^K
for trial in range(600):
    W = rng.randint(0, 3)
    p = {s: mono(rng.randint(0, W), rng.choice([-1, 1])) for s in SECT}
    if rng.random() < 0.4: p['22'] = None
    K = rng.randint(0, 6)
    D = mono(0) if K == 0 else (0, [1] + [0]*(K-1) + [rng.choice([-1, 1])])
    record(Table(p, D), 'F0')
print('F0 done %.1fs' % (time.time()-t0), flush=True)
# F1: random small polys, some sectors D-multiples
for trial in range(300):
    D = trim(0, rng.choice(Dlist))
    W = rng.randint(0, 3)
    p = {}
    for s in SECT:
        if rng.random() < 0.5: p[s] = rand_poly(rng, 0, W, 1)
        else: p[s] = pmul(D, rand_poly(rng, 0, rng.randint(0, 1), 1))
    if rng.random() < 0.4: p['22'] = None
    record(Table(p, D), 'F1')
print('F1 done %.1fs' % (time.time()-t0), flush=True)
# F2: wall-cancelling structure: 42 = -t^a 20, 24 = -t^b 02, 44 = +-t^c 00, 22 tied to 00 or 0
for trial in range(300):
    D = trim(0, rng.choice(Dlist[:6]))
    W0 = rng.randint(0, 2)
    base = {s: rand_poly(rng, 0, W0, 1) for s in ['00', '02', '20']}
    if rng.random() < 0.5:
        base = {s: pmul(D, v) for s, v in base.items()}
    a, b, c, f = (rng.randint(-2, 2) for _ in range(4))
    p = dict(base)
    p['42'] = pshift(pscale(base['20'], -1), a)
    p['24'] = pshift(pscale(base['02'], -1), b)
    p['44'] = pshift(pscale(base['00'], rng.choice([-1, 1])), c)
    p['22'] = rng.choice([None, pshift(pscale(base['00'], rng.choice([-1, 1])), f), pshift(base['20'], f)])
    record(Table(p, D), 'F2')
print('F2 done %.1fs' % (time.time()-t0), flush=True)
# F3: planted units from the exact linear-algebra construction (all off-axis feasible targets, W<=4) and on
#     axis lines with large free parameter, then brute force the whole box of the resulting table
for trial in range(250):
    Dco = rng.choice(Dlist[:7]); SD = len(Dco)-1; D = trim(0, list(Dco))
    Wn = rng.randint(0, 4); B = max(1, Wn, SD)
    if rng.random() < 0.5:
        m0 = rng.randint(-3*B-2, 3*B+2); n0 = rng.randint(-3*B-2, 3*B+2)
    else:   # axis-line target: |n0| <= 3B, free parameter around the claimed line bound
        n0 = rng.randint(-3*B, 3*B); bnd = (Wn + 6*abs(n0) + SD)//2
        m0 = rng.choice([-1, 1]) * rng.randint(max(1, bnd-4), bnd+4)
        if rng.random() < 0.5: m0, n0 = n0, m0
    ks = analyse_target(m0, n0, Wn, Dco, SD)
    if not ks: continue
    p = construct(m0, n0, Wn, Dco, rng.choice(ks), rng)
    if p is None or any(p[s] is None for s in BOUND): continue
    record(Table(p, D), 'F3')
print('F3 done %.1fs' % (time.time()-t0), flush=True)
# F4: planted far unit by solving ONE sector exactly (support blows up; B large) - checks the claimed scaling
for trial in range(40):
    Dco = rng.choice(Dlist[:7]); D = trim(0, list(Dco))
    p = {s: rand_poly(rng, 0, rng.randint(0, 2), 1) for s in SECT}
    m0 = rng.choice([-1, 1]) * rng.randint(1, 4); n0 = rng.choice([-1, 1]) * rng.randint(1, 4)
    x = rng.choice(SECT)
    from wbf import IJ, padd
    sig = {s: 2*IJ[s][0]*m0 + 2*IJ[s][1]*n0 for s in SECT}
    rest = padd(*[pshift(p[s], sig[s]) for s in SECT if s != x])
    k = rng.randint(-3, 3)
    px = padd(pshift(D, k), pscale(rest, -1) if rest else None)
    if px is None: continue
    p[x] = pshift(px, -sig[x])
    T = Table(p, D)
    if not T.boundary_ok(): continue
    assert T.is_unit(m0, n0)
    record(T, 'F4')
print('F4 done %.1fs' % (time.time()-t0), flush=True)

import collections
summ = collections.defaultdict(lambda: dict(n=0, units=0, whole=0, max_ratio_window=0, max_ratio_square=0, worst=None))
for s in stats:
    d = summ[s['tag']]; d['n'] += 1; d['units'] += s['nunits']; d['whole'] += s['nwhole']
    if s['ratio_window'] > d['max_ratio_window']:
        d['max_ratio_window'] = s['ratio_window']; d['worst'] = (s['W'], s['SD'], s['B'], s['max_min_coord'])
    d['max_ratio_square'] = max(d['max_ratio_square'], s['ratio_square'])
for k, v in summ.items(): print(k, dict(v))
print('TOTAL VIOLATIONS:', len(allviol))
json.dump(dict(summary={k: dict(v) for k, v in summ.items()}, violations=[str(v) for v in allviol]),
          open('families_%s.json' % (sys.argv[1] if len(sys.argv) > 1 else '2026'), 'w'), indent=1)
