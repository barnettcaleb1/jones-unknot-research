import sys, random, time
sys.path.insert(0,'nest')
from nlib import *
Phi3=P((1,0),(1,1),(1,2)); Phi5=P((1,0),(1,1),(1,2),(1,3),(1,4)); Q2=P((1,0),(1,2))
def mt(a): return mono(a,(-1)**(a%2))
def vert(a,v):
    A=a_of(v); B=b_of(v)
    num=add(mul(mono(1),A), mul(mt(a),add(mul(Q2,A),mul(mono(1),B))), mul(mono(3*a-1),mul(Phi5,B)))
    q=divexact(num,Phi3)
    return None if q is None else normalize(q)
rnd=random.Random(23)
def rword(L):
    w=''
    while len(w)<L:
        c=rnd.choice('XxYy')
        if w and (w[-1]+c in ('Xx','xX','Yy','yY')): continue
        w+=c
    return w
pool=[]
while len(pool)<300:
    w=rword(rnd.randint(1,7)); v=apply(w)
    if not v[0]: continue
    nv=normalize(v[0])
    if nv is None: continue
    s,k=unit_ratio([nv,{}],[v[0],{}])
    pool.append((w,[shift({e:s*c for e,c in v[0].items()},k),shift({e:s*c for e,c in v[1].items()},k)]))
t0=time.time(); minspan={}; units=[]; n=0
for trial in range(30000):
    nb=rnd.choice([1,1,2,2,3])
    bs=rnd.sample(pool,nb)
    p=bs[0][1]
    for _,v in bs[1:]: p=star(p,v)
    if rnd.random()<0.5:  # optional necklace-body wrapping (iterated)
        m=rnd.choice([-2,-1,1,2]); p=F(m,p)
    a=rnd.choice([-9,-7,-5,-3,3,5,7,9])
    Jv=vert(a,p)
    if Jv is None: print('NONDIV',a,[w for w,_ in bs]); continue
    n+=1
    key=(abs(a),nb)
    s_=span(Jv); minspan[key]=min(minspan.get(key,99),s_)
    if s_==0: units.append((a,[w for w,_ in bs]))
print('vertical-closure survey: checked',n,'unit J found',len(units),'time',round(time.time()-t0,1))
for k in sorted(minspan): print('  |a|=%d boxes=%d  min span %d'%(k[0],k[1],minspan[k]))
for u in units[:10]: print('UNIT',u)
