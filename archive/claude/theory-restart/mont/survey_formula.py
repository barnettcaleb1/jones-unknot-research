import sys, random, itertools, time
sys.path.insert(0,'.')
from lp import *
rnd=random.Random(5)
def rword(L):
    w=''
    while len(w)<L:
        c=rnd.choice('XxYy')
        if w and ((w[-1]=='X' and c=='x') or (w[-1]=='x' and c=='X') or (w[-1]=='Y' and c=='y') or (w[-1]=='y' and c=='Y')): continue
        w+=c
    return w
def vec(w): return apply(w)
def Jneck(mu,k,vs):
    p=vs[0]
    for v in vs[1:]: p=star(p,v)
    p=apply('Y'*k if k>=0 else 'y'*(-k), p)
    return normalize(close(mu,p))
t0=time.time()
units=[]; nchk=0; minspan={}
# pool of non-integral rational boxes: a(v) non-unit
pool=[]
while len(pool)<400:
    w=rword(rnd.randint(1,7)); v=vec(w)
    if len(v[0])>1: pool.append((w,v))
for trial in range(60000):
    n=rnd.choice([2,2,3,3,4])
    bs=rnd.sample(pool,n)
    mu=rnd.choice([m for m in range(-5,6) if m!=0])
    k=rnd.randint(-4,4)
    J_=Jneck(mu,k,[v for _,v in bs])
    nchk+=1
    if J_ is None: continue
    s=span(J_)
    key=(n,)
    minspan[key]=min(minspan.get(key,99),s)
    if s==0: units.append((mu,k,[w for w,_ in bs]))
print('checked',nchk,'units',len(units),'minspan by n',minspan,'time',round(time.time()-t0))
for u in units[:10]: print('UNIT',u)
