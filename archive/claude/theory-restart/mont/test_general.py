import sys, random, time, json
sys.path.insert(0,'.'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
import flat_search as fs
rnd=random.Random(7)
D=P((1,-1),(-1,3))   # t^-1 - t^3  (e1^T X^-1 = (1, D))
def divexact(p,d):
    """exact Laurent division p/d, None if not exact"""
    p=dict(p); q={}
    if not p: return {}
    lo=bot(p)-bot(d)
    dt=top(d); dc=d[dt]
    while p:
        e=top(p); c=p[e]; k=e-dt
        if k<lo or c%dc: return None
        q[k]=c//dc
        p=sub(p,mul(mono(k,c//dc),d))
    return clean(q)
def box_vector(B):
    a=J('s.'+B)
    if a is None: return None
    J1=J('s.r2.y1.'+B+'.u1')
    if J1 is None: return None
    cands=[]
    for k in range(-40,41):
        for s in (1,-1):
            r=sub(mul(mono(k,s),J1),a)
            q=divexact(r,D)
            if q is not None: cands.append([a,q])
    return cands
boxes=[]
t0=time.time()
while len(boxes)<40 and time.time()-t0<900:
    w=fs.gen(rnd,rnd.randint(4,12))
    if w is None: continue
    B=w[2:]
    if J('s.'+B) is None: continue
    c=box_vector(B)
    if not c: print('NO VECTOR',B); continue
    boxes.append((B,c))
print('boxes',len(boxes),'ambiguous',sum(len(c)>1 for _,c in boxes),'time',round(time.time()-t0))
ok=bad=0
for B,c in boxes:
    for m in (-2,2,-1):
        Jw=J('s.r2.'+('y1.' if m>0 else 'x1.')*abs(m)+B+'.u1') if m!=-1 else J('s.r2.x1.'+B+'.u1')
        preds=[normalize(close(-m,v)) for v in c]
        if Jw in preds: ok+=1
        else: bad+=1; print('SINGLE MISMATCH',m,B)
print('single-box twists ok',ok,'bad',bad)
ok=bad=0
for i in range(60):
    (B1,c1),(B2,c2)=rnd.sample(boxes,2)
    m=rnd.choice([-2,-1,1,2])
    w='s.r2.'+('y1.' if m>0 else 'x1.')*abs(m)+B1+'.'+B2+'.u1'
    Jw=J(w)
    if Jw is None: continue
    preds=[normalize(close(-m,star(v1,v2))) for v1 in c1 for v2 in c2]
    if Jw in preds: ok+=1
    else: bad+=1; print('PAIR MISMATCH',m,B1,'|',B2)
print('pairs ok',ok,'bad',bad,'time',round(time.time()-t0))
json.dump([[B,[[sorted(v[0].items()),sorted(v[1].items())] for v in c]] for B,c in boxes],open('general_boxes.json','w'))
