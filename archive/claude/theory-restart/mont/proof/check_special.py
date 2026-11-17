"""Cor 5.4: J(s.l1.B.W.u2) = norm(e1^T rho(W) v(B)) for words W in y0,x0,x1,y1 (TH-2BR letters), bodies with known vectors."""
import sys, json, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from lp import *
rnd=random.Random(23)
data=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
mp={'y0':'Y','x0':'y','x1':'X','y1':'x'}
ok=bad=skip=0
for B,v in data[:30]:
    v=[dict(v[0]),dict(v[1])]
    for trial in range(4):
        W=[rnd.choice(list(mp)) for _ in range(rnd.randint(1,5))]
        Jw=J('s.l1.'+B+'.'+'.'.join(W)+'.u2')
        if Jw is None: skip+=1; continue
        p=apply(''.join(mp[l] for l in reversed(W)),v)   # chronological: first letter acts first
        F=normalize(p[0])
        if F==Jw: ok+=1
        else: bad+=1; print('MISMATCH',B,W)
print('two-bridge special regions: ok',ok,'bad',bad,'skip',skip)
