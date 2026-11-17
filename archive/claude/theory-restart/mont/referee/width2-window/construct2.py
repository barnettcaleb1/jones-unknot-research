import random
from wbf import SECT, Table, trim
from exhaustive import analyse_target, BOUND
from construct import construct
rng = random.Random(11)
Dlist = [('1', [1]), ('1+t', [1, 1]), ('1+t+t^2', [1, 1, 1]), ('(1+t^2)(1+t+t^2)', [1, 1, 2, 1, 1]), ('1-t^3', [1,0,0,-1])]
nt = 0; nunits = 0; miss = 0
for name, Dco in Dlist:
    SD = len(Dco)-1; D = trim(0, list(Dco))
    for Wn in range(0, 4):
        B = max(1, Wn, SD); Rb = 3*B + 3
        targets = [(m0, n0) for m0 in range(-Rb, Rb+1) for n0 in range(-Rb, Rb+1) if m0 and n0]
        for (m0, n0) in targets:
            ks = analyse_target(m0, n0, Wn, Dco, SD)
            if not ks: continue
            for attempt in range(3):
                p = construct(m0, n0, Wn, Dco, rng.choice(ks), rng)
                if p is None or any(p[s] is None for s in BOUND): continue
                T = Table(p, D); nt += 1
                for (a, b) in targets:
                    if T.is_unit(a, b):
                        nunits += 1
                        if not analyse_target(a, b, Wn, Dco, SD):
                            miss += 1; print('MISSED', name, Wn, (a, b))
print('constructed tables', nt, 'off-axis units found in their boxes', nunits, 'missed', miss)
