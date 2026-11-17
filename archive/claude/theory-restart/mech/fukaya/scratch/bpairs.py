import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch')
from khtio import *
from collections import Counter, defaultdict
found = []
for name, bn, kh in all_tangles():
    cps = [c for c in bn if c.cyclic]
    pos = Counter((c.q[0], c.h[0]) for c in cps)
    pairs = [(q, h) for (q, h) in pos if (q, h + 1) in pos]
    if pairs:
        found.append((len(cps), name, pairs[:3], len(pairs)))
found.sort()
print(len(found), 'tangles contain two compact components of BN at (q,h) and (q,h+1)')
for f in found[:12]: print(f)
# show the smallest fully
import subprocess
name = found[0][1]
print('smallest:', name)
for nm, bn, kh in all_tangles():
    if nm == name:
        for c in bn:
            print('   ', 'compact' if c.cyclic else 'arc    ', '(h,q)=', (c.h[0], c.q[0]), 'delta', Fraction(c.q[0],2)-c.h[0], '' if c.cyclic else c.word().replace('b-S>c-D>c-S2>c-D>c-S>b','R'))
        for c in kh: print('    Kh:', c.label)
