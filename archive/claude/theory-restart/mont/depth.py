import sys, random, collections
sys.path.insert(0,'.')
from lp import *
rnd=random.Random(23)
def rword(L):
    w=''
    while len(w)<L:
        c=rnd.choice('XxYy')
        if w and {'X':'x','x':'X','Y':'y','y':'Y'}[w[-1]]==c: continue
        w+=c
    return w
pool=[]
while len(pool)<600:
    w=rword(rnd.randint(1,8)); v=apply(w)
    if len(v[0])>1: pool.append((w,v))
dep=collections.Counter(); worst=[]
minrest=99
for trial in range(60000):
    n=rnd.choice([2,2,2,3,3,4]); bs=rnd.sample(pool,n)
    mu=rnd.choice([m for m in range(-6,7) if m!=0]); k=rnd.randint(-5,5)
    p=bs[0][1]
    for _,v in bs[1:]: p=star(p,v)
    p=apply('Y'*k if k>=0 else 'y'*(-k), p)
    A=a_of(p); B=b_of(p)
    w1=add(mono(1),mul(P((1,0),(1,2)), mono(mu, (-1)**(mu%2))))
    w3=mul(P((1,0),(1,2)), sub(ONE, mono(mu,(-1)**(mu%2))))
    T1=mul(w1,A); T3=mul(w3,B); S=add(T1,T3)
    nat_top=max(top(T1),top(T3)); nat_bot=min(bot(T1),bot(T3))
    dt=nat_top-top(S); db=bot(S)-nat_bot
    dep[('top',dt)]+=1; dep[('bot',db)]+=1
    rest=(top(S)-bot(S))
    minrest=min(minrest,rest)
    if max(dt,db)>=3 and len(worst)<6: worst.append((mu,k,[w for w,_ in bs],dt,db,rest))
print(sorted(dep.items()))
print('min span of J*Phi3',minrest)
for x in worst: print(x)
