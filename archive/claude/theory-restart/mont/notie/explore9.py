from nt import *
import itertools
from collections import Counter, defaultdict
seqs=[s for s in normal_seqs(3,3)]
B={s:box(s) for s in seqs}
CH={s:chan(B[s]) for s in seqs}
def isR(s): return s[-1]>0
def tietype(mu,N,ss):
    rho=sum(isR(s) for s in ss); d=2*rho-3*N
    if mu>0 and d==0 and rho%2==0: return 'T1'
    if mu<=-2 and d==-1 and rho%2==1: return 'T2'
    if mu==-1 and d==-3 and rho%2==0: return 'T3'
    return None
Cnt=Counter(); zeros=[]
import random
rnd=random.Random(3)
for trial in range(200000):
    n=2
    ss=tuple(rnd.choice(seqs) for _ in range(n))
    mu=rnd.choice([m for m in range(-5,6) if m]); N=rnd.randint(-3,5)
    tt=tietype(mu,N,ss)
    ssm=tuple(mirror_seq(s) for s in ss)
    tb=tietype(-mu,n-N,ssm)
    if tt is None and tb is None: continue
    Jv=neck(mu,N,[B[s] for s in ss])
    if tt is not None:  # tie at top -> generic end bottom
        e=bot(Jv); c1=Jv.get(e); c2=Jv.get(e+1,0); c3=Jv.get(e+2,0)
        key=('top-tie',tt,abs(c1),c2!=0)
    else:
        e=top(Jv); c1=Jv.get(e); c2=Jv.get(e-1,0); c3=Jv.get(e-2,0)
        key=('bot-tie',tb,abs(c1),c2!=0)
    Cnt[key]+=1
    if c2==0 and len(zeros)<20: zeros.append((mu,N,ss,tt,tb,sorted(Jv.items())))
for k,v in sorted(Cnt.items(),key=str): print(k,v)
for z in zeros[:10]: print(z)
