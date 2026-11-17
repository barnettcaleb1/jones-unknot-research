"""Zero-excess necklaces: boxes (-2,)^a (1,)^b ; J*Phi3 = w1 A + w3 t^{-3N} B. Find min span - 3n and min span - (4n-3)."""
from nt import *
from neck2 import wdata
import time
def ppow(p,k):
    r=ONE
    for _ in range(k): r=mul(r,p)
    return r
def w1(mu): return add(mono(1),mul(P((1,0),(1,2)),mono(mu,(-1)**abs(mu))))
def w3(mu): return mul(P((1,0),(1,2)),sub(ONE,mono(mu,(-1)**abs(mu))))
PHI=P((1,0),(1,1),(1,2))
def divPhi(p):
    # exact division by 1+t+t^2
    p=dict(p); q={}
    while p:
        e=max(p); c=p[e]
        q[e-2]=c
        for f,d in PHI.items():
            p[e-2+f]=p.get(e-2+f,0)-c*d
            if p[e-2+f]==0: del p[e-2+f]
    return q
aS,bS=chan(box((-2,))); aR,bR=chan(box((1,)))
t0=time.time(); worst=[]
powA={}; 
for a in range(0,15):
    for b in range(0,15):
        n=a+b
        if n<2: continue
        A=mul(ppow(aS,a),ppow(aR,b)); B=mul(ppow(bS,a),ppow(bR,b))
        for mu in [m for m in range(-4,5) if m]:
            W1=mul(w1(mu),A); W3=mul(w3(mu),B)
            for N in range(-3,n+4):
                JP=add(W1,shift(W3,-3*N))
                Jv=divPhi(JP)
                sp=span(Jv)
                worst.append((sp-3*n,sp,n,a,b,mu,N))
worst.sort()
print('time',round(time.time()-t0,1))
for w in worst[:15]: print(w)
print('min span-(4n-3):',min((w[1]-(4*w[2]-3),w) for w in worst))
