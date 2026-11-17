import sys, random, time, json
sys.path.insert(0,'.'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
import flat_search as fs
exec(open('test_general.py').read().split('def box_vector')[0].split('rnd=random.Random(7)')[1])  # D, divexact
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def vec(B):
    a=J('s.'+B)
    if a is None: return None,None
    Js={m:J('s.r2.'+tw(m)+B+'.u1') for m in (1,2,-1)}
    if any(v is None for v in Js.values()): return None,None
    cands=[]
    for k in range(-60,61):
        for s in (1,-1):
            q=divexact(sub(mul(mono(k,s),Js[1]),a),D)
            if q is None: continue
            v=[a,q]
            if all(normalize(close(-m,v))==Js[m] for m in (2,-1)): cands.append(v)
    return cands, a
rnd=random.Random(11)
boxes=[]; t0=time.time(); nores=0
while len(boxes)<50 and time.time()-t0<1200:
    w=fs.gen(rnd,rnd.randint(4,14))
    if w is None: continue
    B=w[2:]
    c,a=vec(B)
    if c is None: continue
    if len(c)!=1: nores+=1; print('candidates',len(c),B); continue
    if len(a)==1: continue   # skip boxes with unit J (trivial-looking)
    boxes.append((B,c[0]))
print('boxes',len(boxes),'non-unique',nores,'time',round(time.time()-t0))
ok=bad=0
for B,v in boxes:
    for m in (3,-2,-3):
        Jw=J('s.r2.'+tw(m)+B+'.u1')
        if Jw is None: continue
        if normalize(close(-m,v))==Jw: ok+=1
        else: bad+=1; print('SINGLE MISMATCH',m,B)
print('single-box extra twists ok',ok,'bad',bad)
ok=bad=0
for i in range(120):
    k=rnd.choice([2,2,3])
    bs=rnd.sample(boxes,k)
    m=rnd.choice([-2,-1,1,2,3])
    w='s.r2.'+tw(m)+'.'.join(B for B,_ in bs)+'.u1'
    Jw=J(w)
    if Jw is None: continue
    p=bs[0][1]
    for _,v in bs[1:]: p=star(p,v)
    if normalize(close(-m,p))==Jw: ok+=1
    else: bad+=1; print('MULTI MISMATCH',m,[B for B,_ in bs])
print('multi-box ok',ok,'bad',bad,'time',round(time.time()-t0))
json.dump([[B,[sorted(v[0].items()),sorted(v[1].items())]] for B,v in boxes],open('general_boxes.json','w'))
