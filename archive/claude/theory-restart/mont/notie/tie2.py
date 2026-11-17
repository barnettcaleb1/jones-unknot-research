"""Second-order tie-end lemma: at a cancelling top tie, next coefficient of J*Phi3 is c*(s1-s3)."""
from neck2 import *
from auto2 import run, rhoq
import random
from lp import ev
rnd=random.Random(31)
pool=normal_seqs(3,3)
for _ in range(400):
    k=rnd.randint(3,8); s=[rnd.choice([m for m in range(-4,5) if m]) for _ in range(k)]
    if s[0]==-1: s[0]=-2
    pool.append(tuple(s))
ok=bad=0; deficit1=0; deeper=0; mod4bad=0
for trial in range(8000):
    nb=rnd.choice([2,3,3,4,5])
    ss=[rnd.choice(pool) for _ in range(nb)]
    sts=[run(s) for s in ss]; rho=sum(1 for st,_ in sts if st[0]=='R')
    cands=[(mu,N) for mu in [m for m in range(-6,7) if m] for N in range(-6,12)
           if (lambda d:(mu>=1 and d==0 and rho%2==0) or (mu<=-2 and d==-1 and rho%2==1) or (mu==-1 and d==-3 and rho%2==0))(2*rho-3*N)]
    if not cands: continue
    mu,N=rnd.choice(cands)
    w1,w3=wdata(mu)
    s1=w1[2]+sum(r for _,r in sts); s3=w3[2]+sum(r+rhoq(st) for st,r in sts)
    vs=[box(s) for s in ss]; Jv=neck(mu,N,vs); A=prod(vs)[0]
    JP=mul(Jv,P((1,0),(1,1),(1,2)))
    D=w1[0]+top(A)  # tie degree of J*Phi3
    c=w1[1]*A[top(A)]
    # mod 4 check
    if any(sum(cc for e,cc in Jv.items() if e%4==r)!=(1 if r==0 else 0) for r in range(4)): mod4bad+=1
    if JP.get(D,0)!=0: bad+=1; continue
    if JP.get(D-1,0)==c*(s1-s3): ok+=1
    else: bad+=1
    if s1!=s3: deficit1+=1
    else: deeper+=1
print('ok',ok,'bad',bad,'deficit exactly 1:',deficit1,'second-order tie:',deeper,'mod4 violations',mod4bad)
