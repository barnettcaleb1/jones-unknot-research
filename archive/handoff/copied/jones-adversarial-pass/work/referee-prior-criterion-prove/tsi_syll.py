"""Test TSI: D(rho(w)) >= 24 sum|e_j| - 16(L-1) for syllable words in R_c,R_x,R_y with |e_j|<=Emax, L<=Lmax syllables
(matching basis, 5x5)."""
import sys, time
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
from w60 import lmul as Lm, ladd as La
Lmax=int(sys.argv[2]); Emax=int(sys.argv[3])
ctx=make_ctx(Lmax*Emax+2,{'c':[], 'x':[3], 'y':[4,3,2,3]}); names=ctx['names']
def kappa(e):
    # (A^{24e}-1)/[3] as dict: exact division
    num={24*e:1,0:-1}
    q={4:1,0:1,-4:1}; p=dict(num); out={}
    while p:
        ph=max(p); c=p[ph]; k=ph-4; out[k]=c
        p=La(p,{x+k:cc*c for x,cc in q.items()},-1)
    return out
KAP={e:kappa(e) for e in range(-Emax,Emax+1) if e}
def rmul_pow(X,s,e):
    v=ctx['V'][s]; n=ctx['NV'][s]
    Xv=np.zeros((5,ctx['LEN']),dtype=np.int64)
    for j in range(5):
        if v[j]: Xv=(Xv+smul(X[:,j,:],v[j]))%P
    Xv=smul(Xv,KAP[e]); Y=X.copy()
    for j in range(5):
        if n[j]: Y[:,j,:]=(Y[:,j,:]+smul(Xv,n[j]))%P
    return smul(Y,{-12*e:1})
exps=[e for e in range(-Emax,Emax+1) if e]
t0=time.time(); worst=(10**9,None); cnt=0
stack=[((),unit5(ctx),0)]
while stack:
    w,X,se=stack.pop()
    if w:
        D=Dspan(X); b=24*se-16*(len(w)-1); cnt+=1
        if D-b<worst[0]: worst=(D-b,w,D,b)
    if len(w)<Lmax:
        for s in names:
            if w and w[-1][0]==s: continue
            for e in exps: stack.append((w+((s,e),),rmul_pow(X,s,e),se+abs(e)))
print('words',cnt,'min D - TSI bound =',worst[0],'at',worst[1],'D=%d bound=%d'%(worst[2],worst[3]),'t=%.0fs'%(time.time()-t0))
