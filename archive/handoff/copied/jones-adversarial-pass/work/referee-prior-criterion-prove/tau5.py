"""tau(u) for cyclically reduced u in a k-curve system, from the char poly of the full 5x5 rho(u):
e1,e2 of X and X^-1, det = A^{-36 e(u)}; e3 = det*e2(X^-1), e4 = det*e1(X^-1). tau = max_j deg(e_j)/j - min_j ord(e_j)/j."""
import sys, time, random
d=sys.argv[1]; sys.path.insert(0,d)
import fastD
fastD.P=1048573
from fastD import make_ctx, unit5, rmul_gen, smul, np
from fractions import Fraction as F
P=1048573
mmax=int(sys.argv[2]); which=sys.argv[3]; mode=sys.argv[4] if len(sys.argv)>4 else 'exh'
sets={'cxy':{'c':[], 'x':[3], 'y':[4,3,2,3]},
      'cxyu':{'c':[], 'x':[3], 'y':[4,3,2,3], 'u':[5,4,-2,3]},
      'cxyuv':{'c':[], 'x':[3], 'y':[4,3,2,3], 'u':[5,4,-2,3], 'v':[2,3,4,5,1]},
      'cxyz':{'c':[], 'x':[3], 'y':[4,3,2,3], 'z':[-2,4,3,-5]}}
ctx=make_ctx(mmax,sets[which]); OFF=ctx['OFF']; LEN=ctx['LEN']
def lmul_gen(X,s,e):
    v=ctx['V'][s]; n=ctx['NV'][s]; k=ctx['kp'] if e>0 else ctx['km']
    nX=np.zeros((5,LEN),dtype=np.int64)
    for j in range(5):
        if n[j]: nX=(nX+smul(X[j,:,:],n[j]))%P
    nX=smul(nX,k); Y=X.copy()
    for i in range(5):
        if v[i]: Y[i,:,:]=(Y[i,:,:]+smul(nX,v[i]))%P
    return smul(Y,{-12*e:1})
def e1e2(X):
    t=np.zeros(LEN,dtype=np.int64)
    for i in range(5): t=(t+X[i,i])%P
    e2=np.zeros(2*LEN-1,dtype=np.int64)
    for i in range(5):
        for j in range(i+1,5):
            e2=(e2+np.convolve(X[i,i],X[j,j])%P-np.convolve(X[i,j],X[j,i])%P)%P
    return t,e2
def dd(arr,off):
    nz=np.nonzero(arr)[0]
    if len(nz)==0: return None
    return int(nz[-1]-off), int(nz[0]-off)
def tau(X,Xi,eu):
    det=-36*eu
    a1,a2=e1e2(X); b1,b2=e1e2(Xi)
    his=[F(det,5)]; los=[F(det,5)]
    for arr,off,j,add in ((a1,OFF,1,0),(a2,2*OFF,2,0),(b2,2*OFF,3,det),(b1,OFF,4,det)):
        r=dd(arr,off)
        if r: his.append(F(r[0]+add,j)); los.append(F(r[1]+add,j))
    return max(his)-min(los)
names=ctx['names']; letters=[(s,e) for s in names for e in (1,-1)]
best={}; t0=time.time(); cnt=0
def visit(w,X,Xi,eu):
    global cnt
    m=len(w)
    if m and not (w[0][0]==w[-1][0] and w[0][1]==-w[-1][1]):
        t=tau(X,Xi,eu); cnt+=1; r=t/m
        if m not in best or r<best[m][0]: best[m]=(r,t,w)
if mode=='exh':
    stack=[((),unit5(ctx),unit5(ctx),0)]
    while stack:
        w,X,Xi,eu=stack.pop(); visit(w,X,Xi,eu)
        if len(w)<mmax:
            for (s,e) in letters:
                if w and w[-1]==(s,-e): continue
                stack.append((w+((s,e),),rmul_gen(ctx,X,s,e),lmul_gen(Xi,s,-e),eu+e))
else:
    random.seed(3); nsamp=int(mode)
    for it in range(nsamp):
        m=random.randint(4,mmax); w=[]
        while len(w)<m:
            l=random.choice(letters)
            if w and w[-1]==(l[0],-l[1]): continue
            if len(w)==m-1 and w[0]==(l[0],-l[1]): continue
            w.append(l)
        X=unit5(ctx); Xi=unit5(ctx); eu=0
        for (s,e) in w: X=rmul_gen(ctx,X,s,e); Xi=lmul_gen(Xi,s,-e); eu+=e
        visit(tuple(w),X,Xi,eu)
f=lambda w:''.join(s if e>0 else s.upper() for s,e in w)
for m in sorted(best):
    r,t,w=best[m]; print(which,'m=%d min tau/m=%.3f (tau=%s) %s'%(m,float(r),t,f(w)))
print('count',cnt,'t=%.0fs'%(time.time()-t0))
