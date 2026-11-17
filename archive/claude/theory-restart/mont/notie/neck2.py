"""Necklace-level second coefficient prediction at a generic top."""
from nt import *
from auto2 import run, rhoq
from fractions import Fraction
def wdata(mu):
    """(top, c1, rho) of w1 and w3"""
    if mu>=1: w1=(mu+2,(-1)**mu,0); w3=(mu+2,-(-1)**mu, 1 if mu==1 else 0)
    elif mu==-1: w1=(-1,-1,0); w3=(2,1,1)
    else: w1=(1,1,1 if mu==-2 else 0); w3=(2,1,0)
    return w1,w3
def predict_top(mu,N,seqs):
    """returns ('tie',None) or ('gen', ratio(J*Phi3)) for the top end"""
    w1,w3=wdata(mu)
    sts=[run(s) for s in seqs]
    rho=sum(1 for st,_ in sts if st[0]=='R')
    d=2*rho-3*N
    Delta=w3[0]-w1[0]+d
    eps=w3[1]*(-1)**rho*w1[1]   # c1(w3B')/c1(w1A), all +-1
    s1=w1[2]+sum(r for _,r in sts)
    s3=w3[2]+sum(r+rhoq(st) for st,r in sts)
    if Delta<=-2: return ('gen',s1)
    if Delta==-1: return ('gen',s1+eps)
    if Delta==0:
        if eps==-1: return ('tie',None)
        return ('gen',Fraction(s1+s3,2))
    if Delta==1: return ('gen',s3+eps)
    return ('gen',s3)
if __name__=='__main__':
    import random
    rnd=random.Random(11)
    pool=normal_seqs(3,3)
    for _ in range(300):
        k=rnd.randint(4,7); s=[rnd.choice([m for m in range(-4,5) if m]) for _ in range(k)]
        if s[0]==-1: s[0]=-2
        pool.append(tuple(s))
    bad=0; n=0; zero=0
    for trial in range(20000):
        nb=rnd.choice([2,2,3,3,4,5])
        ss=[rnd.choice(pool) for _ in range(nb)]
        mu=rnd.choice([m for m in range(-6,7) if m]); N=rnd.randint(-4,6)
        kind,ratio=predict_top(mu,N,ss)
        if kind=='tie': continue
        Jv=neck(mu,N,[box(s) for s in ss])
        e=top(Jv); act=Fraction(Jv.get(e-1,0),Jv[e])+1
        n+=1
        if act!=ratio or abs(Jv[e])!=1 and kind=='gen' and ratio is not None and False:
            bad+=1
            if bad<8: print('BAD',mu,N,ss,ratio,act,Jv[e])
        if act==1: zero+=1
    print('generic tops checked',n,'mismatch',bad,'c2(J)=0 cases',zero)
