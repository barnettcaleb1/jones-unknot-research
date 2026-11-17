from nt import *
import itertools
from collections import Counter, defaultdict
exec(open('explore9.py').read().split("Cnt=Counter()")[0])
Cnt=Counter(); zeros=[]
import random
rnd=random.Random(4)
for trial in range(150000):
    n=rnd.choice([2,3,3,4])
    ss=tuple(rnd.choice(seqs) for _ in range(n))
    mu=rnd.choice([m for m in range(-5,6) if m]); N=rnd.randint(-3,6)
    tt=tietype(mu,N,ss)
    ssm=tuple(mirror_seq(s) for s in ss)
    tb=tietype(-mu,n-N,ssm)
    if tt is None and tb is None: continue
    Jv=neck(mu,N,[B[s] for s in ss])
    if tt is not None:
        e=bot(Jv); c1=Jv.get(e); c2=Jv.get(e+1,0)
        key=(n,'top-tie',tt,c1*c2)
    else:
        e=top(Jv); c1=Jv.get(e); c2=Jv.get(e-1,0)
        key=(n,'bot-tie',tb,c1*c2)
    if tt and tb: key=key+('BOTH',)
    Cnt[key]+=1
    if c2==0 and len(zeros)<20: zeros.append((mu,N,ss,tt,tb))
for k,v in sorted(Cnt.items(),key=str): print(k,v)
for z in zeros[:10]: print(z)
