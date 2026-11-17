"""Per-step loss in the adapted basis (v_c,v_x,v_y) + H-orthogonal complement: rho(w) = A^{-12e}(M(w) (+) I_2),
D = max(maxdeg M,0) - min(minord M,0). Left and right appends, all reduced words up to Lmax."""
import sys, time
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
Lmax=int(sys.argv[2])
ctx=make_ctx(Lmax+2,{'c':[], 'x':[3], 'y':[4,3,2,3]}); names=ctx['names']; OFF=ctx['OFF']
def lmul3(X,s,e):
    si=names.index(s); kk=ctx['kp'] if e>0 else ctx['km']
    nX=np.zeros((3,ctx['LEN']),dtype=np.int64)
    for tj,t in enumerate(names):
        nst=ctx['N'][(s,t)]
        if nst: nX=(nX+smul(X[tj,:,:],nst))%P
    Y=X.copy(); Y[si,:,:]=(Y[si,:,:]+smul(nX,kk))%P
    return Y
def Dv(X):
    nz=np.nonzero((X!=0).any(axis=(0,1)))[0]
    hi=int(nz[-1]-OFF); lo=int(nz[0]-OFF)
    return max(hi,0)-min(lo,0)
letters=[(s,e) for s in names for e in (1,-1)]
layer=[((),unit3(ctx))]; t0=time.time()
f=lambda w:''.join(s if e>0 else s.upper() for s,e in w)
for L in range(1,Lmax+1):
    new=[]; mr=(-99,None); ml=(-99,None); minD=10**9
    for w,X in layer:
        DX=Dv(X) if w else 0
        for (s,e) in letters:
            if w and w[-1]==(s,-e): continue
            Y=rmul3(ctx,X,s,e); DY=Dv(Y); minD=min(minD,DY); new.append((w+((s,e),),Y))
            if w:
                if DX+24-DY>mr[0]: mr=(DX+24-DY,f(w)+'.'+f([(s,e)])+' %d->%d'%(DX,DY))
                if w[0]!=(s,-e):
                    Z=lmul3(X,s,e); DZ=Dv(Z)
                    if DX+24-DZ>ml[0]: ml=(DX+24-DZ,f([(s,e)])+'.'+f(w)+' %d->%d'%(DX,DZ))
    layer=new
    print('L=%d minD_v=%d  max right-loss %d (%s)  max left-loss %d (%s) t=%.0fs'%(L,minD,mr[0],mr[1],ml[0],ml[1],time.time()-t0),flush=True)
