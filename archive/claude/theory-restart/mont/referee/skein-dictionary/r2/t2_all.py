"""Run the raw-marking Section-8 check (t2_bodies.check_body) on all 50 general_boxes.json bodies,
rational bodies, and nested necklace bodies (depth 1-2), a = -4..4 (odd and even)."""
import json, random, sys
from t2_bodies import check_body
L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
gen=[B for B,_ in L]
rat=['y0','x0','y0.y0','x0.x0','y0.y0.y0','r1.y0.y2.u1','r1.x0.x2.u1','r1.y0.y2.y0.u1','l1.x0.x0.y2.u1',
     'r1.r1.y0.y2.y4.u1.u1','y0.r1.x0.x2.u1.y0']
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
rnd=random.Random(7)
nested=[]
for _ in range(10):
    k=rnd.choice([1,2]); Bs=[rnd.choice(gen+rat) for _ in range(k)]; m=rnd.choice([-2,-1,1,2])
    nested.append('r2.'+tw(m)+'.'.join(Bs)+'.u1')
for _ in range(4):   # depth 2
    inner='r2.'+tw(rnd.choice([-1,1]))+rnd.choice(gen)+'.u1'
    nested.append('r2.'+tw(rnd.choice([-1,1]))+inner+'.'+rnd.choice(rat)+'.u1')
tot=0; good=0; cnt=0
for kind,lst in (('gen',gen),('rat',rat),('nested',nested)):
    for B in lst:
        res,da,db=check_body(B, arange=range(-4,5))
        ok=all(res.values()); tot+=1; good+=ok; cnt+=sum(1 for k in res if isinstance(k,int))
        if not ok: print('FAIL',kind,B,res)
    print(kind,'done', len(lst))
print('bodies',tot,'all-pass',good,'(a-values per body 9; raw identities checked:',cnt,')')
