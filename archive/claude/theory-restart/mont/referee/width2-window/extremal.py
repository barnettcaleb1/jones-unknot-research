import random
from wbf import SECT, Table, trim, IJ
from exhaustive import analyse_target
from construct import construct
rng = random.Random(1)
for W in (2, 4):
    m0, n0 = 3*W//2, -W
    ks = analyse_target(m0, n0, W, [1], 0)
    for attempt in range(50):
        p = construct(m0, n0, W, [1], ks[0], rng)
        if p and all(p[s] is not None for s in ['00','02','20','24','42','44']): break
    T = Table(p, (0, [1]))
    print('W=%d target (m,n)=(%d,%d) feasible k=%s; table:' % (W, m0, n0, ks))
    for s in SECT: print('   p%s =' % s, p[s])
    print('   B =', T.B, ' unit at target:', T.is_unit(m0, n0), ' numerator:', T.numerator(m0, n0))
    sig = {s: 2*IJ[s][0]*m0 + 2*IJ[s][1]*n0 for s in SECT}
    print('   shifts:', sig)
