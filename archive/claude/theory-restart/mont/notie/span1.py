from nt import *
from auto2 import run
import itertools, time
from collections import Counter, defaultdict
t0=time.time()
seqs=[s for s in normal_seqs(3,2)]
B={s:box(s) for s in seqs}
SA={s:span(B[s][0]) for s in seqs}
res=defaultdict(list); dif=Counter()
for n in (2,3):
    pool=seqs if n==2 else [s for s in seqs if len(s)<=2]
    for ss in itertools.combinations_with_replacement(pool,n):
        vs=[B[s] for s in ss]; P_=prod(vs); sA=sum(SA[s] for s in ss)
        for N in range(-3,n+3):
            PN=Ypow(N,P_)
            for mu in [m for m in range(-5,6) if m]:
                Jv=Xpow(mu,PN)[0]
                sp=span(Jv)
                res[n].append((sp,mu,N,ss,sA))
                dif[(n,sp-sA)]+=1
    res[n].sort()
    print('n',n,'cases',len(res[n]),'min span',res[n][0][0],'time',round(time.time()-t0,1))
    for r in res[n][:12]: print('  ',r)
print(sorted((k,v) for k,v in dif.items() if k[1]<=-4))
