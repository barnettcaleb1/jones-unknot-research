import random
from rcore import *
from t_neck import mirror
rnd=random.Random(17); bad=0; cnt=0
def J_of(mu,N,seqs):
    bd=[(ach(u),bch(u)) for u in (ubox(s) for s in seqs)]
    A=fprod([a for a,b in bd]); B=fprod([b for a,b in bd])
    return pdiv_exact(ad(ml(w1(mu),A),ml(w3(mu),sh(B,-3*N))),PHI3)
for it in range(400):
    n=rnd.randint(2,6)
    seqs=[]
    for _ in range(n):
        k=rnd.randint(1,8); s=[rnd.choice([1,-1])*rnd.randint(1,9) for _ in range(k)]
        if s[0]==-1: s[0]=-2
        seqs.append(tuple(s))
    mu=rnd.choice([m for m in range(-9,10) if m]); N=rnd.randint(-10,12); K=sum(len(s) for s in seqs)
    if bar(J_of(mu,N,seqs))!=sh(J_of(-mu,n-N,[mirror(s) for s in seqs]),-4*K): bad+=1
    cnt+=1
print('necklace mirror identity checked',cnt,'bad',bad)
