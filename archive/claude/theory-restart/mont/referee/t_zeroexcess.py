"""Zero-excess necklaces u(-2)^p u(1)^(n-p): min span - 3n over tie configurations, n up to NMAX, |mu|<=MU."""
import sys, time
from rcore import *
NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 40; MU=int(sys.argv[2]) if len(sys.argv)>2 else 8
uS=ubox((-2,)); uR=ubox((1,))
aS,bS,aR,bR=ach(uS),bch(uS),ach(uR),bch(uR)
t0=time.time()
W1={mu:w1(mu) for mu in range(-MU,MU+1) if mu}; W3={mu:w3(mu) for mu in range(-MU,MU+1) if mu}
powS_a=[ONE]; powS_b=[ONE]; powR_a=[ONE]; powR_b=[ONE]
for i in range(NMAX):
    powS_a.append(fml(powS_a[-1],aS)); powS_b.append(fml(powS_b[-1],bS)); powR_a.append(fml(powR_a[-1],aR)); powR_b.append(fml(powR_b[-1],bR))
overall=[]
for n in range(2,NMAX+1):
    best=None
    for p in range(0,n+1):
        rho=n-p
        A=fml(powS_a[p],powR_a[n-p]); B=fml(powS_b[p],powR_b[n-p])
        for mu in W1:
            for N in range(-n-3,2*n+4):
                d=2*rho-3*N
                if not ((mu>=1 and d==0 and rho%2==0) or (mu<=-2 and d==-1 and rho%2==1) or (mu==-1 and d==-3 and rho%2==0) \
                   or (mu<=-1 and d==-n and (rho-n)%2==0) or (mu>=2 and d==1-n and (rho-n)%2==1) or (mu==1 and d==3-n and (rho-n)%2==0)):
                    continue
                G=ad(ml(W1[mu],A),ml(W3[mu],sh(B,-3*N)))
                s_=sp(G)-2
                if best is None or s_<best[0]: best=(s_,p,mu,N)
    overall.append((n,best[0]-3*n,best[0]-4*n,best))
    print('n',n,'min span',best[0],'span-3n',best[0]-3*n,'span-4n',best[0]-4*n,'(p=#u(-2),mu,N)=',best[1:],flush=True)
print('time',round(time.time()-t0,1))
