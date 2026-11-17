# LIT lane: how many random Montesinos necklaces (same generator as mont/survey_formula.py, seed 5) have a2(K)=0,
# i.e. the only cases where Lemma Q is not automatic from J''(-1) = -24 a2(K)?  Exact lp.py arithmetic.
import sys, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from lp import *
rnd=random.Random(5)
def rword(L):
    w=''
    while len(w)<L:
        c=rnd.choice('XxYy')
        if w and ((w[-1]=='X' and c=='x') or (w[-1]=='x' and c=='X') or (w[-1]=='Y' and c=='y') or (w[-1]=='y' and c=='Y')): continue
        w+=c
    return w
def Jneck(mu,k,vs):
    p=vs[0]
    for v in vs[1:]: p=star(p,v)
    p=apply('Y'*k if k>=0 else 'y'*(-k), p)
    return normalize(close(mu,p))
N=int(sys.argv[1]) if len(sys.argv)>1 else 20000
t0=time.time(); pool=[]
while len(pool)<400:
    w=rword(rnd.randint(1,7)); v=apply(w)
    if len(v[0])>1: pool.append((w,v))
tot=0; z=0; zmin={}; zunits=0; ex=[]
for trial in range(N):
    n=rnd.choice([2,2,3,3,4]); bs=rnd.sample(pool,n)
    mu=rnd.choice([m for m in range(-5,6) if m!=0]); k=rnd.randint(-4,4)
    J_=Jneck(mu,k,[v for _,v in bs])
    if J_ is None: continue
    tot+=1
    if abs(a2(J_))<1e-9:
        z+=1; s=span(J_); zmin[n]=min(zmin.get(n,99),s)
        if s==0: zunits+=1
        if len(ex)<3: ex.append((mu,k,[w for w,_ in bs],sorted(J_.items())))
print('necklaces with J defined',tot,' with a2=0:',z,' units among them:',zunits,' min span of J (a2=0) by n:',zmin,' time',round(time.time()-t0,1))
for e in ex: print('EX',e)
