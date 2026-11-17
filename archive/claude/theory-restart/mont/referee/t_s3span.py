"""Referee: S3 span consequences when s1 != s3 at a first-order top tie; also B-side by mirror. Compare actual span with
   T1 mu>=2: spanA+mu-2; T1 mu=1: spanA-2 (n=2), spanA-3 (n>=3); T2: spanA+|mu|-2; T3: spanA-2 (n=2), spanA-3 (n>=3)."""
import random, sys, time
from rcore import *
from t_box import exact_state
from t_neck import gseq, boxdata, predict_top, tie_type_top
import t_neck
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1); t_neck.rnd=rnd
cnt=0; bad=0; cnt2=0; minex=10**9
t0=time.time()
for it in range(6000):
    n=rnd.randint(2,9); seqs=[gseq() for _ in range(n)]
    bd=[boxdata(s) for s in seqs]; rho=sum(1 for x in bd if x[2][0]=='R')
    cands=[(mu,N) for mu in [m for m in range(-8,9) if m] for N in range(-15,20) if tie_type_top(mu,rho,2*rho-3*N)]
    if not cands: continue
    mu,N=rnd.choice(cands); tt=tie_type_top(mu,rho,2*rho-3*N)
    pr=predict_top(mu,N,seqs); s1,s3=pr[1],pr[2]
    A=fprod([x[0] for x in bd]); B=fprod([x[1] for x in bd])
    G=ad(ml(w1(mu),A),ml(w3(mu),sh(B,-3*N))); spJ=sp(G)-2; sA=sum(sp(x[0]) for x in bd)
    if s1==s3: 
        cnt2+=1; minex=min(minex,spJ-(sA-3)); continue
    cnt+=1
    if tt=='T1': pred=sA+mu-2 if mu>=2 else (sA-2 if n==2 else sA-3)
    elif tt=='T2': pred=sA+abs(mu)-2
    else: pred=sA-2 if n==2 else sA-3
    if spJ!=pred: bad+=1; print('S3 span FAIL',tt,mu,N,seqs,spJ,pred)
print('first-order-only top ties',cnt,'span formula failures',bad,'| second-order ties (s1=s3)',cnt2,'min span-(spanA-3) there',minex,'time',round(time.time()-t0,1))
