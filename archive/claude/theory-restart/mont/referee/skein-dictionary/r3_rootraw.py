# R3: root values of RAW (lp marking) channel amplitudes: a_raw(-1), b_raw(-1) vs (-1)^n0, over 50 general bodies + random bodies
import sys, json, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
import flat_search as fs
D=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
def n0(B): return sum(1 for tok in B.split('.') if tok in ('x0','y0'))
def divexact(p,d):
    p=dict(p); q={}
    dt=top(d); dc=d[dt]
    for _ in range(5000):
        if not p: return clean(q)
        pt=top(p); c=p[pt]
        if c%dc: return None
        e=pt-dt; q[e]=c//dc
        for f,g in d.items(): p[e+f]=p.get(e+f,0)-q[e]*g
        p=clean(p)
    return None
OMT4=P((1,0),(-1,4)); OMT3=P((1,0),(-1,3))
def rawvec(B):
    a0=J_raw('s.r2.'+B+'.u1'); am=J_raw('s.r2.x1.'+B+'.u1')
    if a0 is None or am is None: return None
    v2=divexact(sub(mul(mono(2),am),a0),OMT4)
    if v2 is None: return 'NONINT'
    return a0, add(a0,mul(OMT3,v2))
bodies=[B for B,_ in D]
rnd=random.Random(5)
while len(bodies)<250:
    w=fs.gen(rnd,rnd.randint(4,12))
    if w: bodies.append(w[2:])
stats={}; nonint=0; bad=[]
for B in bodies:
    r=rawvec(B)
    if r is None: continue
    if r=='NONINT': nonint+=1; continue
    a,b=r
    key=(ev(a,-1), ev(b,-1)*(-1)**n0(B))
    stats[key]=stats.get(key,0)+1
print('(a_raw(-1), b_raw(-1)*(-1)^n0) counts:',stats,' non-integral raw v2:',nonint)
