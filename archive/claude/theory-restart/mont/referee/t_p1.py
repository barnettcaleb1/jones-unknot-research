"""P1 configuration: mu=-2, n=0 mod 6, N=n/3, all boxes alternating S-boxes. Check c2(J)=0, c3(J)=c1(J)(Y-1), Y=sum x2(a_i)."""
import random, sys, time
from rcore import *
from fractions import Fraction
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
def altS(kmax,M):
    k=rnd.randint(1,kmax)
    # signs alternate and end negative: last sign -, so sign of m_i = (-1)^(k-1-i) * (-1)
    s=[]
    for i in range(k):
        sg=-1 if (k-1-i)%2==0 else 1
        mag=rnd.randint(1,M)
        if i==0 and sg<0: mag=max(mag,2)
        s.append(sg*mag)
    return tuple(s)
t0=time.time(); n_ok=0; bad=0
for n in (6,12,18):
    for trial in range(40 if n<18 else 10):
        seqs=[altS(14 if n==6 else 8, 8 if n==6 else 5) for _ in range(n)]
        bd=[(ach(u),bch(u)) for u in (ubox(s) for s in seqs)]
        A=fprod([a for a,b in bd]); B=fprod([b for a,b in bd]); N=n//3; mu=-2
        G=ad(ml(w1(mu),A),ml(w3(mu),sh(B,-3*N))); J=pdiv_exact(G,PHI3)
        cJ=xs(J,3,'top')
        Yv=sum(xs(a,3)[2] for a,b in bd)
        xa1=[xs(a,2)[1] for a,b in bd]
        if any(x!=0 for x in xa1) or cJ[1]!=0 or cJ[2]!=Yv-1: bad+=1; print('P1 FAIL',n,seqs,cJ,Yv,xa1)
        n_ok+=1
        # also bottom end of P1 necklace: must be... (not claimed) record
print('P1 instances',n_ok,'bad',bad,'time',round(time.time()-t0,1))
