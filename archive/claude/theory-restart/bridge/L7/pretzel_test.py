import cmath, math, itertools
from genon_test import *
t = cmath.exp(1j*math.pi/5); A = t**(-0.25)
th = cmath.exp(4j*math.pi/5)
# calibrate keychain normalisation: P(1,1,-1)=unknot (Sigma_2=S^3)
c0 = absZ_seifert_keychain([1, 1, -1], th)
cases = []
for ps in itertools.product(range(-7, 8), repeat=3):
    if 0 in ps: continue
    if sorted(ps) != list(ps): continue
    # knot iff at most one even entry (for 3-strand pretzel); skip links
    ev = sum(1 for p in ps if p % 2 == 0)
    if ev > 1: continue
    if ev == 0 and False: pass
    v = absV_pretzel(ps, A)
    for sgn in (1, -1):
        z = absZ_seifert_keychain([sgn*p for p in ps], th)/c0
        cases.append((ps, sgn, v, z))
for sgn in (1, -1):
    bad = [(ps, v, z) for (ps, s, v, z) in cases if s == sgn and abs(v - z) > 1e-8]
    print('framing sign', sgn, ': mismatches', len(bad), 'of', sum(1 for c in cases if c[1] == sgn))
    for b in bad[:5]: print('   ', b)
for ps in [(-2, 3, 7), (-2, 3, 5), (-2, 3, 3), (3, 3, -3), (5, -3, 3), (-3, 5, 7)]:
    v = absV_pretzel(ps, A); z = absZ_seifert_keychain([-p for p in ps], th)/c0
    print(ps, f'|V(z10)|={v:.6f}  Z-ratio={z:.6f}')
