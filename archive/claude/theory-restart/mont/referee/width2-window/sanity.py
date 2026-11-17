import random, time
from wbf import *
rng = random.Random(1)
# cross-check is_unit against direct numerator construction
bad = 0; tot = 0; nunit = 0
for trial in range(300):
    W = rng.randint(0, 3)
    p = {s: rand_poly(rng, 0, W, 1) for s in SECT}
    if rng.random() < 0.5: p['22'] = None
    Dch = rng.choice([mono(0), (0,[1,1]), (0,[1,1,1]), (0,[1,0,1]), (0,[1,0,0,-1])])
    # make some sectors D-multiples so units occur
    for s in SECT:
        if p.get(s) is not None and rng.random() < 0.5:
            p[s] = pmul(Dch, rand_poly(rng, 0, rng.randint(0,1), 1))
    T = Table(p, Dch)
    for _ in range(200):
        m = rng.randint(-6, 6); n = rng.randint(-6, 6)
        P = T.numerator(m, n)
        direct = (P is not None) and proportional(P, Dch)
        u = T.is_unit(m, n)
        tot += 1; nunit += u
        if u != direct: bad += 1
print('crosscheck points', tot, 'units', nunit, 'mismatches', bad)
T = Table({s: mono(0) for s in SECT}, mono(0))
t0 = time.time(); us = T.units_in_box(200); dt = time.time() - t0
print('all-ones table units in |m|,|n|<=200:', us, 'time %.2fs for %d pts' % (dt, 401*401))
