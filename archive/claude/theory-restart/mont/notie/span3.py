"""Random tie cases with larger boxes: minimum of span(J)-4n and span(J)-span(A)."""
from neck2 import *
from auto2 import run
import random, time
from collections import defaultdict
rnd=random.Random(99)
pool=normal_seqs(3,3)
for _ in range(600):
    k=rnd.randint(2,9); s=[rnd.choice([m for m in range(-4,5) if m]+[-1,-1,1,1]) for _ in range(k)]
    if s[0]==-1: s[0]=-2
    pool.append(tuple(s))
SA={}
def sa(s):
    if s not in SA: SA[s]=span(box(s)[0])
    return SA[s]
mins=defaultdict(lambda:(99,None)); minsA=defaultdict(lambda:(99,None)); t0=time.time(); cnt=0
for trial in range(15000):
    nb=rnd.choice([2,2,3,3,4,5])
    ss=[rnd.choice(pool) for _ in range(nb)]
    rho=sum(1 for s in ss if run(s)[0][0]=='R')
    cands=[]
    for mu in [m for m in range(-6,7) if m]:
        for N in range(-6,12):
            d=2*rho-3*N
            if (mu>=1 and d==0 and rho%2==0) or (mu<=-2 and d==-1 and rho%2==1) or (mu==-1 and d==-3 and rho%2==0) or \
               (mu<=-1 and d==-nb and (rho-nb)%2==0) or (mu>=2 and d==1-nb and (rho-nb)%2==1) or (mu==1 and d==3-nb and (rho-nb)%2==0):
                cands.append((mu,N))
    if not cands: continue
    mu,N=rnd.choice(cands)
    sp=span(neck(mu,N,[box(s) for s in ss])); cnt+=1
    sA=sum(sa(s) for s in ss)
    if sp-4*nb<mins[nb][0]: mins[nb]=(sp-4*nb,(mu,N,ss,sp))
    if sp-sA<minsA[nb][0]: minsA[nb]=(sp-sA,(mu,N,ss,sp,sA))
print('tie cases',cnt,'time',round(time.time()-t0,1))
for nb in sorted(mins): print(nb,'min span-4n',mins[nb]); print('   min span-spanA',minsA[nb])
