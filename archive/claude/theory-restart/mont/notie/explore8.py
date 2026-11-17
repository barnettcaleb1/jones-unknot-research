from nt import *
import itertools
from collections import Counter, defaultdict
seqs=[s for s in normal_seqs(3,2)]
B={s:box(s) for s in seqs}
CH={s:chan(B[s]) for s in seqs}
SPA={s:span(CH[s][0]) for s in seqs}
single={}
for s in seqs:
    for mu in range(-5,6):
        for N in range(-4,6):
            single[(mu,N,s)]=span(neck(mu,N,[B[s]]))
C=Counter(); worst=[]
for s1,s2 in itertools.product(seqs,repeat=2):
    for mu in [m for m in range(-4,5) if m]:
        for N in range(-3,5):
            sp=span(neck(mu,N,[B[s1],B[s2]]))
            # compare to single closures of s1 with N or N-1 etc
            cand=[single[(mu,N-d,s1)] for d in (0,1) ]
            ex=sp-SPA[s2]-min(cand)
            C[ex]+=1
            if ex<=-2: worst.append((ex,mu,N,s1,s2,sp,SPA[s2],cand))
print(sorted(C.items()))
for w in sorted(worst)[:20]: print(w)
