"""Verify the main theorem's mechanism: tie at one end -> second (or third, case P1) coefficient at the other end nonzero."""
from neck2 import *
from auto2 import run
import random, time
from fractions import Fraction
def isP1(mu,N,ss):
    sts=[run(s) for s in ss]
    return mu==-2 and all(st[0]=='S' and r==0 for st,r in sts) and len(ss)%6==0 and 3*N==len(ss)
def x2a(s):
    a=box(s)[0]; e=top(a); return Fraction(a.get(e-2,0),a[e])
rnd=random.Random(2026)
pool=normal_seqs(3,3)
for _ in range(400):
    k=rnd.randint(4,8); s=[rnd.choice([m for m in range(-5,6) if m]) for _ in range(k)]
    if s[0]==-1: s[0]=-2
    pool.append(tuple(s))
altS=[s for s in pool if run(s)[0][0]=='S' and run(s)[1]==0]
t0=time.time(); stats={'bottie':0,'toptie':0,'c2zero_nonP1':0,'P1':0,'P1_c3zero':0,'bad_pred':0}
for trial in range(6000):
    nb=rnd.choice([2,3,4,5,6,6,7])
    if trial%10==0:   # force P1 configurations
        nb=6; ss=[rnd.choice(altS) for _ in range(6)]; mu=-2; N=2
    else:
        ss=[rnd.choice(pool) for _ in range(nb)]
        mu=rnd.choice([m for m in range(-6,7) if m]); N=rnd.randint(-4,8)
    kt,rt=predict_top(mu,N,ss)
    ssm=[mirror_seq(s) for s in ss]
    kb,rb=predict_top(-mu,nb-N,ssm)
    if kt=='tie' and kb=='tie': print('BOTH ENDS TIE?!',mu,N,ss); continue
    if kt!='tie' and kb!='tie' and not isP1(mu,N,ss): continue
    Jv=neck(mu,N,[box(s) for s in ss])
    if kb=='tie' or isP1(mu,N,ss):
        e=top(Jv); c=[Jv.get(e-i,0) for i in range(3)]; stats['bottie']+=1
        if Fraction(c[1],c[0])+1!=rt: stats['bad_pred']+=1
        if c[1]==0:
            if isP1(mu,N,ss):
                stats['P1']+=1
                Y=sum(x2a(s) for s in ss)
                if c[2]==0 or Fraction(c[2],c[0])!=Y-1: stats['P1_c3zero']+=1; print('P1 c3 issue',ss,c,Y)
            else: stats['c2zero_nonP1']+=1; print('c2=0 non-P1',mu,N,ss)
    if kt=='tie':
        e=bot(Jv); c=[Jv.get(e+i,0) for i in range(3)]; stats['toptie']+=1
        if c[1]==0:
            ssm_P1=isP1(-mu,nb-N,ssm)
            if ssm_P1:
                stats['P1']+=1
                if c[2]==0: stats['P1_c3zero']+=1
            else: stats['c2zero_nonP1']+=1; print('c2=0 bottom non-P1',mu,N,ss)
print(stats,'time',round(time.time()-t0,1))
