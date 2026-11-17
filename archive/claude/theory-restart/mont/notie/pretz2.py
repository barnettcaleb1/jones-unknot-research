"""Pretzel spans (k=0): min span vs 3n; uses the closed form G."""
from pretz import *
import itertools, time
from collections import defaultdict
t0=time.time()
PHI3=P((1,0),(1,1),(1,2))
best=defaultdict(lambda:(99,None))
rowsset=[3,5,7,9,11,-3,-5,-7,-9,-11]
for n in (2,3,4,5):
    for rows in itertools.combinations_with_replacement(rowsset,n):
        for mu in [m for m in range(-6,7) if m]:
            g=G(mu,list(rows)); sp=span(g)-2
            if sp-3*n<best[n][0]: best[n]=(sp-3*n,(sp,mu,rows))
print('time',round(time.time()-t0,1))
for n in sorted(best): print(n,best[n])
