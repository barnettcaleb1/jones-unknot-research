"""Two-closure recipe for body vectors with raw brackets: v = (al0(B)/al0(0), [al_{-1}(B)/al_{-1}(0) - al0(B)/al0(0)]/(1-t^4))
compared with the brief's three-closure vectors (general_boxes.json), up to a common unit."""
import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from lp import *
exec(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/test_general.py').read().split('def box_vector')[0].split('rnd=random.Random(7)')[1])  # D, divexact
def raw(m,B):
    w='s.r2.'+''.join(('y1.' if m>0 else 'x1.')*abs(m))+(B+'.' if B else '')+'u1'
    return J_raw(w)
def ratio(p,q):   # exact Laurent division p/q (q a monomial)
    assert len(q)==1
    (e,c),=q.items()
    out={}
    for f,d in p.items():
        assert d%c==0
        out[f-e]=d//c
    return out
data=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
ok=bad=0
r0=raw(0,''); rm=raw(-1,'')
print('empty-body raw units (m=0,-1):',r0,rm)
for B,v in data:
    v=[dict(v[0]),dict(v[1])]
    a0=ratio(raw(0,B),r0); a1=ratio(raw(-1,B),rm)
    num=sub(a1,a0)
    v2=divexact(num,P((1,0),(-1,4)))
    if v2 is None: bad+=1; print('NOT DIVISIBLE',B); continue
    w=[a0,v2]
    # compare up to a unit +-t^k
    found=False
    for k in range(-60,61):
        for s in (1,-1):
            if [shift({e:s*c for e,c in w[0].items()},k),shift({e:s*c for e,c in w[1].items()},k)]==[clean(v[0]),clean(v[1])]: found=True
    ok+=found; bad+= (not found)
print('two-closure raw recipe matches brief vectors:',ok,'bad',bad)
