"""validate jbox signatures against exact vectors (C1's bdata) on random depth-1 and depth-2 boxes."""
import sys, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import jbox, vc, lib, ser, jets
from fractions import Fraction as Fr
def bdata(v):
    out={}; lcok=True
    for end in ('top','bot'):
        da=ser.pdata(v[0],end,2); db=ser.pdata(v[1],end,2)
        la=jets.logs(da[2]); lb=jets.logs(db[2])
        out[end]=(la[0],la[1],lb[0],lb[1])
        if abs(Fr(db[1],da[1]))!=1: lcok=False
    tq=ser.slope(v,'top',1); bq=ser.slope(v,'bot',1)
    return (out['top'],out['bot'],tq[2][0]+bq[2][0],tq[0]-bq[0]),lcok and vc.span(v[0])>=1
R=lib.rational(5); random.seed(1)
ok=bad=low=0; t0=time.time()
for it in range(1500):
    n=random.randint(2,4); kids=[random.choice(R) for _ in range(n)]
    m=random.choice([x for x in range(-6,7) if x]); N=random.randint(-3,3)
    p=vc.Ypow(N,vc.starall([k[1] for k in kids]))
    if p[0]==p[1]: continue
    v=vc.Xpow(-m,p)
    x=jbox.nest(m,jbox.ypow(N,jbox.star_all([jbox.from_vec(k[1]) for k in kids]) if hasattr(jbox,'star_all') else None)) if False else None
    jx=jbox.from_vec(kids[0][1])
    for k in kids[1:]: jx=jbox.star(jx,jbox.from_vec(k[1]))
    jx=jbox.nest(m,jbox.ypow(N,jx))
    key,el,info=jbox.signature(jx)
    if key is None: low+=1; continue
    if it%2==0:   # depth 2: nest again with a rational partner
        u=random.choice(R); m2=random.choice([x for x in range(-4,5) if x]); N2=random.randint(-2,2)
        v=vc.Xpow(-m2,vc.Ypow(N2,vc.star(v,u[1])))
        jx=jbox.nest(m2,jbox.ypow(N2,jbox.star(jx,jbox.from_vec(u[1]))))
        key,el,info=jbox.signature(jx)
        if key is None: low+=1; continue
    ek,eel=bdata(v)
    if ek==key and eel==el: ok+=1
    else:
        bad+=1
        if bad<5: print('MISMATCH',ek,key,eel,el)
print('validation: agree %d, disagree %d, lowprec %d, time %.1f'%(ok,bad,low,time.time()-t0))
