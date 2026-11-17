"""Stress: large |m| (up to 30), large |mu| (up to 30), large |N|, forced ties; main-theorem predicates only."""
import random, sys, time
from rcore import *
import t_neck
from t_neck import boxdata, predict_top, tie_type_top, tie_type_bot, mirror
rnd=random.Random(5); t0=time.time(); cnt=0; bad=0; units=0; twoend=0
def gs():
    k=rnd.randint(1,4); s=[rnd.choice([1,-1])*rnd.randint(1,30) for _ in range(k)]
    if s[0]==-1: s[0]=-rnd.randint(2,30)
    return tuple(s)
for it in range(1500):
    n=rnd.randint(2,6); seqs=[gs() for _ in range(n)]
    bd=[boxdata(s) for s in seqs]; rho=sum(1 for x in bd if x[2][0]=='R')
    cands=[(mu,N) for mu in [m for m in range(-30,31) if m] for N in range(-40,40) if tie_type_top(mu,rho,2*rho-3*N) or tie_type_bot(mu,rho,2*rho-3*N,n)]
    if not cands or rnd.random()<0.2: mu=rnd.choice([m for m in range(-30,31) if m]); N=rnd.randint(-40,40)
    else: mu,N=rnd.choice(cands)
    A=fprod([x[0] for x in bd]); B=fprod([x[1] for x in bd]); P1_=ml(w1(mu),A); P3_=ml(w3(mu),sh(B,-3*N)); G=ad(P1_,P3_)
    J=pdiv_exact(G,PHI3); cnt+=1
    if len(J)<2: units+=1
    at=tp(P1_)==tp(P3_) and P1_[tp(P1_)]==-P3_[tp(P3_)]; ab=bt(P1_)==bt(P3_) and P1_[bt(P1_)]==-P3_[bt(P3_)]
    if at and ab: twoend+=1
    for end in ('top','bot'):
        pr=predict_top(mu,N,seqs) if end=='top' else predict_top(-mu,n-N,[mirror(s) for s in seqs])
        tied=at if end=='top' else ab
        if (pr[0]=='tie')!=tied: bad+=1; continue
        if pr[0]=='gen':
            cJ=xs(J,2,end)
            if cJ[1]+1!=pr[1]: bad+=1
            if (at or ab) and cJ[1]==0: bad+=1; print('c2=0 at clean end of tie case',mu,N,seqs)
print('stress necklaces',cnt,'prediction failures',bad,'units',units,'two-ended',twoend,'time',round(time.time()-t0,1))
