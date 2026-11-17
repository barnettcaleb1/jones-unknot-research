import sys, time
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import vc, lib, lp
t0=time.time(); R6=lib.rational(6); print('R(6):',len(R6), round(time.time()-t0,2), flush=True)
import random
random.seed(1)
def body(boxes,N):
    parts=[vc.word(b[2]) for b in boxes]
    if N: parts=[('y0' if N>0 else 'x0')]*abs(N)+parts
    return '.'.join(p for p in parts if p)
for (n,N,a) in [(1,0,3),(1,3,3),(2,0,3),(2,0,5),(2,6,5),(2,12,9),(3,0,3),(4,0,3)]:
    boxes=[random.choice(R6) for _ in range(n)]
    w=vc.vert_word(a,body(boxes,N))
    t0=time.time(); J=lp.J(w); dt=time.time()-t0
    p=vc.Ypow(N,vc.starall([b[1] for b in boxes]))
    J2=vc.J_vert(a,p)
    print(n,N,a,'len',len(w.split('.')),'time %.3f'%dt, 'match', J==J2, flush=True)
