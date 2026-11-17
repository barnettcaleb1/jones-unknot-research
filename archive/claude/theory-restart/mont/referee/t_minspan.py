"""Exhaustive search for minimal span J over tie configurations (only ties can go below 4n-2)."""
import itertools, sys, time
from rcore import *
from t_box import exact_state
K=int(sys.argv[1]); M=int(sys.argv[2]); n=int(sys.argv[3]); MU=int(sys.argv[4]) if len(sys.argv)>4 else 6
pool=[]
vals=[m for m in range(-M,M+1) if m]
for k in range(1,K+1):
    for s in itertools.product(vals,repeat=k):
        if s[0]==-1: continue
        u=ubox(s); pool.append((s,ach(u),bch(u),exact_state(u)[0]=='R'))
print('pool',len(pool))
t0=time.time(); best={}; cnt=0
W1={mu:w1(mu) for mu in range(-MU,MU+1) if mu}; W3={mu:w3(mu) for mu in range(-MU,MU+1) if mu}
for combo in itertools.combinations_with_replacement(range(len(pool)),n):
    rho=sum(1 for i in combo if pool[i][3])
    cands=[]
    for mu in W1:
        for N in range(-3*n-3,3*n+4):
            d=2*rho-3*N
            if (mu>=1 and d==0 and rho%2==0) or (mu<=-2 and d==-1 and rho%2==1) or (mu==-1 and d==-3 and rho%2==0) \
               or (mu<=-1 and d==-n and (rho-n)%2==0) or (mu>=2 and d==1-n and (rho-n)%2==1) or (mu==1 and d==3-n and (rho-n)%2==0):
                cands.append((mu,N))
    if not cands: continue
    A=fprod([pool[i][1] for i in combo]); B=fprod([pool[i][2] for i in combo])
    for mu,N in cands:
        G=ad(ml(W1[mu],A),ml(W3[mu],sh(B,-3*N)))
        s_=sp(G)-2; cnt+=1
        if s_<best.get('min',(10**9,))[0]: best['min']=(s_,mu,N,[pool[i][0] for i in combo])
        if s_<3*n: print('SPAN < 3n !!!',s_,mu,N,[pool[i][0] for i in combo])
print('n',n,'K',K,'M',M,'tie necklaces',cnt,'min span',best.get('min'),'3n',3*n,'time',round(time.time()-t0,1))
