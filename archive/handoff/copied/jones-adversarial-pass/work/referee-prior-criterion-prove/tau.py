"""Asymptotic two-place growth tau(u) = lim D(rho(u^n))/n for cyclically reduced u, from the char poly of the
3x3 (or k x k) block on span(v_s): coefficients tr M, det M * tr M^-1, det M (det = A^{24(p-n)})."""
import sys, time
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
from fractions import Fraction as F
mmax=int(sys.argv[2]); which=sys.argv[3]
conjsets={'A':{'c':[], 'x':[3], 'y':[4,3,2,3]},
          'B':{'c':[], 'x':[-3,2,-4], 'y':[5,-3,4,2,-3]},
          'Q':{'c':[], 'x':[3], 'y':[4,3,2,3], 'z':[-2,4,3,-5]},
          'P':{'c':[], 'x':[3], 'y':[4,3,2,3], 'z':[-2,4,3,-5], 'u':[5,4,-2,3]}}
ctx=make_ctx(mmax,conjsets[which]); names=ctx['names']; k=len(names)
OFF=ctx['OFF']; LEN=ctx['LEN']
def unitk():
    X=np.zeros((k,k,LEN),dtype=np.int64)
    for i in range(k): X[i,i,OFF]=1
    return X
def rmulk(X,s,e):
    si=names.index(s); kk=ctx['kp'] if e>0 else ctx['km']
    col=smul(X[:,si,:],kk); Y=X.copy()
    for tj,t in enumerate(names):
        nst=ctx['N'][(s,t)]
        if nst: Y[:,tj,:]=(Y[:,tj,:]+smul(col,nst))%P
    return Y
def lmulk(X,s,e):
    si=names.index(s); kk=ctx['kp'] if e>0 else ctx['km']
    # (I + kk e_s n_s) X : row s += kk * (n_s X)
    nX=np.zeros((X.shape[1],LEN),dtype=np.int64)
    for tj,t in enumerate(names):
        nst=ctx['N'][(s,t)]
        if nst: nX=(nX+smul(X[tj,:,:],nst))%P
    Y=X.copy(); Y[si,:,:]=(Y[si,:,:]+smul(nX,kk))%P
    return Y
def trdeg(X):
    t=np.zeros(LEN,dtype=np.int64)
    for i in range(k): t=(t+X[i,i,:])%P
    nz=np.nonzero(t)[0]
    if len(nz)==0: return None
    return int(nz[-1]-OFF), int(nz[0]-OFF)
letters=[(s,e) for s in names for e in (1,-1)]
best={}  # m -> (ratio, tau, word)
t0=time.time(); count=0
# check symmetric matrices sanity: verify dims by gram rank? skip
def tau_of(M,Minv,dexp):
    a=trdeg(M); b=trdeg(Minv)
    cand_hi=[F(dexp, k)]; cand_lo=[F(dexp,k)]
    if k!=3: raise SystemExit('tau via tr only valid for k=3; use power method for k>3')
    if a: cand_hi.append(F(a[0])); cand_lo.append(F(a[1]))
    if b: cand_hi.append(F(dexp+b[0],2)); cand_lo.append(F(dexp+b[1],2))
    hi=max(cand_hi); lo=min(cand_lo)
    return max(hi,0)-min(lo,0)
stack=[((),unitk(),unitk(),0)]
while stack:
    w,M,Mi,dexp=stack.pop()
    m=len(w)
    if m>=1 and not (w[0][0]==w[-1][0] and w[0][1]==-w[-1][1]):
        t=tau_of(M,Mi,dexp); count+=1
        r=t/m
        if m not in best or r<best[m][0]: best[m]=(r,t,w)
    if m<mmax:
        for (s,e) in letters:
            if w and w[-1]==(s,-e): continue
            stack.append((w+((s,e),),rmulk(M,s,e),lmulk(Mi,s,-e),dexp+24*e))
f=lambda w:''.join(s if e>0 else s.upper() for s,e in w)
for m in sorted(best):
    r,t,w=best[m]; print('m=%d  min tau/m = %s = %.3f  (tau=%s)  word=%s'%(m,r,float(r),t,f(w)))
print('words',count,'time %.0fs'%(time.time()-t0))
