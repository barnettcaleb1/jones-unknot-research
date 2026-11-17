"""Frontier records at their (at most two) candidate unit twists: closest approach to budget exhaustion.
For each frontier record (D classes sampled, d2pos, N-INF, positive-potential, near-miss products) with B != 0:
 candidates m in {nu_0 z, -nu_inf z}; at each: span f_m, H, (r0, rinf), (tau0, tauinf), deficit = span f_m.
Reports the records with the smallest span at a candidate, with complete eigenpair and the finite divisor of z."""
import sys, random, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/arb-resonance')
from common import *
rng = random.Random(4040)
_ = nested_random(rng, 200)          # keep the RNG stream identical to check3 (same frontier sample)
F = frontier(rng)
rows = []
for lab, v, T in F:
    s = th(v); A, B = eig(s)
    if iszero(B): continue
    g = gcdL(A, B); H = span(A) - span(g)
    nu0 = bot(B) - bot(A); ninf = top(A) - top(B)
    for m in sorted({nu0, -ninf}):
        f = sub(A, mul(tm(-m), B))
        r0 = nu0 - m; rinf = ninf + m
        tau0 = max(bot(f) - bot(A), 0); tauinf = max(top(A) - top(f), 0)
        rows.append((span(f), lab, m, H, (r0, rinf), (tau0, tauinf), nu0 + ninf, g == {0: 1}, T, A, B))
rows.sort(key=lambda r: r[0])
print('frontier records with B != 0: %d; candidate twists evaluated: %d' % (len(set(r[1] for r in rows)), len(rows)))
print('min span f_m at a candidate twist: %d; units: %d' % (rows[0][0], sum(1 for r in rows if r[0] == 0)))
hist = collections.Counter(min(10, r[0]) for r in rows); print('span histogram (10 = >=10):', dict(sorted(hist.items())))
for r in rows[:5]:
    sp_, lab, m, H, rr, tt, kap, prim, T, A, B = r
    fa, _ = factors(A); fb, _ = factors(B)
    print('\n%s  m=%d  span f=%d  H=%d  (r0,rinf)=%s  (tau0,tauinf)=%s  kappa=%d  primitive=%s' % (lab, m, sp_, H, rr, tt, kap, prim))
    print('  tree', T)
    print('  A =', sorted(A.items()))
    print('  B =', sorted(B.items()))
    print('  poles of z (factors of A):', [sorted(x.items()) for x in fa])
    print('  zeros of z (factors of B):', [sorted(x.items()) for x in fb])
