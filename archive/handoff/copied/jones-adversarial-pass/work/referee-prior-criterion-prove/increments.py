"""Per-step two-place loss  D(X)+24 - D(X R)  (right append) and D(X)+24-D(R X) (left append) over all
reduced words up to length Lmax for the triple; reports the max loss (program's junction inequality claims <=16)."""
import sys, time
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
Lmax=int(sys.argv[2]); which=sys.argv[3] if len(sys.argv)>3 else 'A'
conjsets={'A':{'c':[], 'x':[3], 'y':[4,3,2,3]},
          'B':{'c':[], 'x':[-3,2,-4], 'y':[5,-3,4,2,-3]}}
ctx=make_ctx(Lmax+2,conjsets[which])
letters=[(s,e) for s in ctx['names'] for e in (1,-1)]
def lmul_gen(ctx,X,s,e):
    # R X = (X^T R^T)^T ; implement directly: R_s X = A^-12s (X + k v_s (n_s X))
    v=ctx['V'][s]; n=ctx['NV'][s]; k=ctx['kp'] if e>0 else ctx['km']
    nX=np.zeros((X.shape[1],ctx['LEN']),dtype=np.int64)
    for j in range(5):
        if n[j]: nX=(nX+smul(X[j,:,:],n[j]))%P
    nX=smul(nX,k)
    Y=X.copy()
    for i in range(5):
        if v[i]: Y[i,:,:]=(Y[i,:,:]+smul(nX,v[i]))%P
    return smul(Y,{-12*e:1})
t0=time.time()
layer=[((),unit5(ctx))]
for L in range(1,Lmax+1):
    new=[]; maxlossR=-99; maxlossL=-99; exR=None; exL=None; minD=10**9
    for w,X in layer:
        DX=Dspan(X) if w else 0
        for (s,e) in letters:
            if w and w[-1]==(s,-e): continue
            Y=rmul_gen(ctx,X,s,e); DY=Dspan(Y); minD=min(minD,DY)
            new.append((w+((s,e),),Y))
            if w:
                lr=DX+24-DY
                if lr>maxlossR: maxlossR=lr; exR=(w,(s,e),DX,DY)
                if not (w[0]==(s,-e)):
                    Z=lmul_gen(ctx,X,s,e); DZ=Dspan(Z); ll=DX+24-DZ
                    if ll>maxlossL: maxlossL=ll; exL=((s,e),w,DX,DZ)
    layer=new
    f=lambda w:''.join(s if e>0 else s.upper() for s,e in w)
    print('L=%d minD=%d | max right-append loss %d  e.g. %s.%s D %d->%d | max left-append loss %d e.g. %s.%s D %d->%d  t=%.0fs'%(
        L,minD,maxlossR,f(exR[0]) if exR else '-',f([exR[1]]) if exR else '-',exR[2] if exR else 0,exR[3] if exR else 0,
        maxlossL,f([exL[0]]) if exL else '-',f(exL[1]) if exL else '-',exL[2] if exL else 0,exL[3] if exL else 0,time.time()-t0),flush=True)
