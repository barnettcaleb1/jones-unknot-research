"""VALIDATION of the F-C pipeline on the referee's known cases (referee/arb-resonance check3/nearmiss library, same RNG seed 4040):
 * unit events at the two candidates must reproduce check3: 49 events in 36 bodies, 13 bodies with units at both candidates;
 * B(xy): units at m = -2, -1;  D:g1_353 at m = 1: kappa 0, H 10, (tau0, tauinf) = (1, 3), span 6;
 * ideal test vs sympy gcd(a, c) (content), N-INF P_6 / P_12 proper (witness must contain 7), span identity at candidates;
 * f_m vs vc.Xpow route and vs direct lp.J of the half-word on a sample.
"""
import sys, random, time, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/arb-resonance')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundG/fc')
import common as CM
import fc_core as fc
rng = random.Random(4040)
t0 = time.time()
L = CM.rational_all() + CM.general_all() + CM.nested_random(rng, 200) + CM.frontier(rng)
base = [x for x in L if not CM.eqp(x[1][0], x[1][1])]
prods = []
for j in range(120):
    k = rng.choice([2, 2, 3])
    kids = rng.sample(base, k)
    prods.append(('PROD%d' % j, CM.vc.starall([c[1] for c in kids]), ('p', [c[2] for c in kids])))
P1 = {0: -1, 3: -1, 4: 1}
cp = []
for lab, v, T in base:
    r = CM.nu(v[1], P1) - CM.nu(v[0], P1)
    if r: cp.append((lab, v, T, r))
pos = [x for x in cp if x[3] > 0]; neg = [x for x in cp if x[3] < 0]
for j in range(min(12, len(pos) * len(neg))):
    x = rng.choice(pos); y = rng.choice(neg)
    prods.append(('CONTENT%d' % j, CM.vc.starall([x[1], y[1]]), ('p', [x[2], y[2]])))
bodies = L + prods
st = collections.Counter(); unit_bodies = []; fails = []; rows = {}
for lab, v, T in bodies:
    a, b = fc.chan_from_vc(v)
    a, c = fc.state_from_channel(a, b)
    A, B = fc.eigen(a, c)
    if not B[1]: st['scalar'] += 1; continue
    st['bodies'] += 1
    status, info = fc.ideal_test(a, c)
    g = CM.gcdL(fc.todict(a), fc.todict(c)); prim = (g == {0: 1})
    st['ideal_' + status] += 1
    if (status == 'CONTENT') != (not prim): fails.append(('content-vs-gcd', lab, status, prim))
    kappa, H, cands = fc.analyze(A, B)
    us = [x[0] for x in cands if x[1]]
    st['cand_twists'] += len(cands)
    for x in cands:
        m, unit, sf, tau0, tauinf, r0, rinf, Dd, Delta = x
        if status == 'UNIT' and sf != Delta: fails.append(('span-identity', lab, m))
        # cross-check f_m with independent Xpow route (vc) on the channel vector
        f = fc.sub(A, fc.tmono_mul(-m, B))
        w = CM.vc.Xpow(-m, v)[0]
        # vc.Xpow is the raw X^-m on channel coords: a-channel equals f_m up to the common normalisation unit
        fw = fc.D(w)
        if not (fc.span(fw) == fc.span(f) and (sorted(fw[1]) == sorted(f[1]) or sorted([-x for x in fw[1]]) == sorted(f[1]))):
            fails.append(('Xpow', lab, m))
    if us:
        unit_bodies.append((lab, us, [x[0] for x in cands], kappa, H, status))
        st['unit_events'] += len(us)
        if len(us) == 2: st['two_unit_bodies'] += 1
    rows[lab] = (A, B, kappa, H, cands, status, info, T, v)
print('bodies', dict(st), 'time %.1f' % (time.time() - t0), flush=True)
print('unit bodies', len(unit_bodies), '(check3: 36 bodies, 49 events, 13 with two)')
print('  families:', dict(collections.Counter(u[0].split(':')[0][:4] for u in unit_bodies)))
print('  all unit bodies have status UNIT ideal:', all(u[5] == 'UNIT' for u in unit_bodies), ' kappas:', collections.Counter(u[3] for u in unit_bodies))
# specific cases
A, B, kappa, H, cands, status, info, T, v = rows['R:xy']
print('R:xy  A=%s B=%s kappa=%d H=%d cands=%s ideal=%s' % (fc.todict(A), fc.todict(B), kappa, H, cands, status))
for lab in rows:
    if lab == 'D:g1_353':
        A, B, kappa, H, cands, status, info, T, v = rows[lab]
        print('D:g1_353 kappa=%d H=%d ideal=%s cands=%s' % (kappa, H, status, cands))
        print('   A =', sorted(fc.todict(A).items())); print('   B =', sorted(fc.todict(B).items()))
for lab in rows:
    if lab.startswith('NINF'):
        A, B, kappa, H, cands, status, info, T, v = rows[lab]
        print(lab, 'ideal', status, 'witness q =', (info[0] if isinstance(info, tuple) else info), 'G =', (info[1] if isinstance(info, tuple) else None))
print('content-carrying (CONTENT) labels:', [l for l in rows if rows[l][5] == 'CONTENT'][:30])
print('PROPER (coprime but proper ideal) labels:', [(l, rows[l][6][0]) for l in rows if rows[l][5] == 'PROPER'][:30])
# direct lp.J on a sample of candidate twists (units and non-units)
import lp
dj = collections.Counter()
samp = [l for l in rows if l.startswith('R:') or l.startswith('D:') or l.startswith('POS')][:40]
for lab in samp:
    A, B, kappa, H, cands, status, info, T, v = rows[lab]
    for x in cands:
        m = x[0]
        if abs(m) > 6: continue
        T2 = ('n', m, [T]) if T[0] != 'p' else ('n', m, T[1])
        w = CM.vc.hw(T2)
        Jd = lp.J(w)
        Jc = CM.vc.norm(fc.todict(fc.sub(A, fc.tmono_mul(-m, B))))
        dj['match' if Jd == Jc else 'MISMATCH'] += 1
        if x[1]: dj['unit_J=1' if Jd == {0: 1} else 'unit_J!=1'] += 1
print('direct lp.J at candidates:', dict(dj))
print('failures', len(fails), fails[:10])
print('time %.1f' % (time.time() - t0))
