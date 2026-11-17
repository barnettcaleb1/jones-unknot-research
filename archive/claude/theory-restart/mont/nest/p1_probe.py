import sys, time
sys.path.insert(0,'nest')
from nlib import *
boxes=load_boxes()
t0=time.time()
# parity check: eps = b(v)(-1) vs number of axis crossings
bad=0
for B,v in boxes:
    eps=ev(b_of(v),-1)
    if eps!=(-1)**nax(B): bad+=1; print('PARITY MISMATCH',B,eps,nax(B))
print('parity check on',len(boxes),'boxes; mismatches',bad)
# outer map probe
for B,v in boxes[:12]:
    for m in (1,-1,2,-2,3):
        N=body(m,[B])
        c=vec(N)
        if c is None: print('N not knot',m,B); continue
        if len(c)!=1: print('nonunique',len(c),m,B); continue
        vN=c[0]
        pred=mvec(Xpow(-m),v)
        r=unit_ratio(vN,pred)
        print(m, 'nax',nax(B), 'ratio vN/(X^-m v) =',r, B)
print('time',round(time.time()-t0,1))
