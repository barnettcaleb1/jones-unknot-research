from nt import *
import itertools, time
from collections import Counter, defaultdict
t0=time.time()
seqs=[s for s in normal_seqs(3,3)]
B={s:box(s) for s in seqs}
CH={s:chan(B[s]) for s in seqs}
def spanA(ss): return sum(span(CH[s][0]) for s in ss)
res=[]
# n=2 pairs, mu in -5..5\0, N in -4..4
pairs=list(itertools.combinations_with_replacement(seqs,2))
import random
rnd=random.Random(1)
sample=rnd.sample(pairs,4000)
for (s1,s2) in sample:
    for mu in [m for m in range(-5,6) if m]:
        for N in range(-4,5):
            Jv=neck(mu,N,[B[s1],B[s2]])
            sp=span(Jv)
            res.append((sp,mu,N,s1,s2,spanA((s1,s2))))
print('time',round(time.time()-t0,1),'cases',len(res))
res.sort()
print('min spans:',Counter(r[0] for r in res).most_common()[-0:][:0], sorted(Counter(r[0] for r in res).items())[:8])
for r in res[:40]: print(r)
