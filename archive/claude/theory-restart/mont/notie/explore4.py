from nt import *
import itertools, time
from collections import Counter, defaultdict
exec(open('explore3.py').read().split("res=[]")[0])
# deep top deficits: list configurations with T-Tgen<=-3
res=[]
for ss in itertools.combinations_with_replacement(seqs,2):
    A=mul(CH[ss[0]][0],CH[ss[1]][0])
    for mu in [m for m in range(-4,5) if m]:
        for N in range(-3,5):
            Jv=neck(mu,N,[B[s] for s in ss])
            T=top(Jv)+2-top(A)
            if T-Tgen(mu,N,ss)<=-3: res.append((T-Tgen(mu,N,ss),mu,N,ss,T))
C=Counter((r[1],r[2]) for r in res)
print(sorted(C.items()))
for r in sorted(res)[:40]: print(r)
