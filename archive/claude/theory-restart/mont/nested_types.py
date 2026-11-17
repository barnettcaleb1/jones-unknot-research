import sys, random, collections, time
sys.path.insert(0,'.'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *; from words import row
exec(open('test_general.py').read().split('def box_vector')[0].split('rnd=random.Random(7)')[1])  # D, divexact
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def vec(B):
    a=J('s.'+B)
    if a is None: return None
    Js={m:J('s.r2.'+tw(m)+B+'.u1') for m in (1,2,-1)}
    if any(v is None for v in Js.values()): return None
    cands=[]
    for k in range(-80,81):
        for s in (1,-1):
            q=divexact(sub(mul(mono(k,s),Js[1]),a),D)
            if q is None: continue
            v=[a,q]
            if all(normalize(close(-m,v))==Js[m] for m in (2,-1)): cands.append(v)
    return cands[0] if len(cands)==1 else None
rnd=random.Random(3)
cnt=collections.Counter(); ex={}
t0=time.time()
for trial in range(40):
    n=rnd.choice([2,2,3]); m=rnd.choice([-2,-1,1,2])
    rows=[rnd.choice([-5,-3,3,5]) for _ in range(n)]
    body='r2.'+tw(m)+'.'.join('.'.join(row(r)) for r in rows)+'.u1'
    v=vec(body)
    if v is None: cnt['unpinned']+=1; continue
    a=a_of(v); b=b_of(v)
    if len(a)==1: cnt['integral']+=1; continue
    key=(top(a)-top(b), bot(a)-bot(b), a[top(a)]*b[top(b)], a[bot(a)]*b[bot(b)])
    cnt[key]+=1; ex.setdefault(key,(m,rows))
print(dict(cnt), 'time', round(time.time()-t0))
for k,e in ex.items(): print(k,e)
