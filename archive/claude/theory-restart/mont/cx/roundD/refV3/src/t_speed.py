import sys, time
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import vc, lib, lp
t0=time.time(); R6=lib.rational(6); print('R(6):',len(R6), time.time()-t0)
import random
random.seed(1)
# timing lp.J on vertical closures
def body(boxes,N):
    parts=[vc.word(b[2]) for b in boxes]
    if N: parts=[('y0' if N>0 else 'x0')]*abs(N)+parts
    return '.'.join(p for p in parts if p)
cnt=0; t0=time.time(); mism=0
for it in range(200):
    n=random.randint(1,4)
    boxes=[random.choice(R6) for _ in range(n)]
    N=random.randint(-12,12); a=random.choice([x for x in range(-9,10,2)])
    w=vc.vert_word(a,body(boxes,N))
    J=lp.J(w)
    p=vc.Ypow(N,vc.starall([b[1] for b in boxes]))
    J2=vc.J_vert(a,p)
    if J!=J2: mism+=1
    cnt+=1
dt=time.time()-t0
print('lp.J calls',cnt,'time',dt,'per call',dt/cnt,'mismatch formula vs lp.J',mism)
print('example word',w, len(w.split('.')))
