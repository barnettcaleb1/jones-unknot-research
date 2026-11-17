import sys, random, itertools, collections
sys.path.insert(0,'.')
from lp import *
rnd=random.Random(29)
def rword(L):
    w=''
    while len(w)<L:
        c=rnd.choice('XxYy')
        if w and {'X':'x','x':'X','Y':'y','y':'Y'}[w[-1]]==c: continue
        w+=c
    return w
def Jneck(mu,k,vs):
    p=vs[0]
    for v in vs[1:]: p=star(p,v)
    p=apply('Y'*k if k>=0 else 'y'*(-k), p)
    return normalize(close(mu,p))
# 1) pure pretzels P(-2m; rows) with |rows|>=3: how often a2 = 0
def vrow(r):
    j=(abs(r)-1)//2
    return apply(('X'*j+'Y') if r>0 else ('x'*j+'y'))
z=0; tot=0; zex=[]
for n in (2,3):
    for rows in itertools.product([-9,-7,-5,-3,3,5,7,9],repeat=n):
        if list(rows)!=sorted(rows): continue
        for mu in range(-6,7):
            if mu==0: continue
            Jn=Jneck(mu,0,[vrow(r) for r in rows]); tot+=1
            if a2(Jn)==0:
                z+=1
                if len(zex)<12: zex.append((mu,rows,span(Jn)))
print('pure pretzels: a2=0 in',z,'of',tot); print(zex)
# 2) general Montesinos with random rational boxes: a2 = 0 cases and their spans
pool=[]
while len(pool)<500:
    w=rword(rnd.randint(1,7)); v=apply(w)
    if len(v[0])>1: pool.append((w,v))
z=0; tot=0; spans=collections.Counter()
for trial in range(60000):
    n=rnd.choice([2,2,3,3,4]); bs=rnd.sample(pool,n)
    mu=rnd.choice([m for m in range(-5,6) if m!=0]); k=rnd.randint(-4,4)
    Jn=Jneck(mu,k,[v for _,v in bs]); tot+=1
    if a2(Jn)==0: z+=1; spans[span(Jn)]+=1
print('random Montesinos: a2=0 in',z,'of',tot,'; spans of those:',sorted(spans.items())[:10])
