"""Fast mod-p engine for the triple <R_c,R_x,R_y>, R_s = rho(T_s^2) on W(6,0) (matching basis, 5x5)
and the 3x3 block on span(v_c,v_x,v_y). Laurent polys as numpy int64 arrays (index i <-> exponent i-OFF)."""
import sys, numpy as np
sys.path.insert(0, sys.argv[1] if len(sys.argv)>1 else '.')
from w60 import *
P = 2147483647
def make_ctx(Lmax, conjs):
    OFF = 12*Lmax + 60; LEN = 2*OFF+1
    vc=[{2:1,-2:1},{0:1},{0:1},{2:1,-2:1},{4:1,0:1,-4:1}]
    T34=lmul({4:1,0:1,-4:1},{6:1,2:1,-2:1,-6:1})
    def exdiv(p,q):
        p=dict(p); out={}; qh=max(q); qc=q[qh]; lo=min(p)-max(q)+min(q) if p else 0
        while p:
            ph=max(p); c=p[ph]; assert c%qc==0; k=ph-qh; out[k]=c//qc
            p=ladd(p,lsh({e:cc*(c//qc) for e,cc in q.items()},k),-1)
            assert k>=lo-5
        return out
    V={k:rvec(w,vc) for k,w in conjs.items()}
    # n_s[j] = N(s,e_j) = H(v_s,e_j)/(-[3][4])
    NV={}
    for k in conjs:
        row=[]
        for j in range(DIM):
            e=[{} for _ in range(DIM)]; e[j]={0:1}
            h=H(V[k],e); row.append(exdiv({x:-c for x,c in h.items()},T34) if h else {})
        NV[k]=row
    Ngram={(a,b):(exdiv({x:-c for x,c in H(V[a],V[b]).items()},T34)) for a in conjs for b in conjs}
    kp=lmul(lmul({12:1},{6:1,-6:1}),{2:1,-2:-1})      # (A^24-1)/[3]
    km=lmul(lmul({-12:1},{-6:1,6:1}),{-2:1,2:-1})     # (A^-24-1)/[3]
    return dict(OFF=OFF,LEN=LEN,V=V,NV=NV,N=Ngram,kp=kp,km=km,names=list(conjs))
def smul(X, poly):
    """X: array (...,LEN) ; poly dict small -> X*poly (mod P)"""
    out=np.zeros_like(X)
    for e,c in poly.items():
        c%=P
        if e>=0: out[...,e:]+= (X[...,:X.shape[-1]-e]*c)%P
        else: out[...,:e]+= (X[...,-e:]*c)%P
        out%=P
    return out
def unit5(ctx):
    X=np.zeros((5,5,ctx['LEN']),dtype=np.int64)
    for i in range(5): X[i,i,ctx['OFF']]=1
    return X
def rmul_gen(ctx, X, s, sign):
    """X -> X * R_s^{sign} (5x5 matching basis)"""
    v=ctx['V'][s]; n=ctx['NV'][s]
    Xv=np.zeros((X.shape[0],ctx['LEN']),dtype=np.int64)
    for j in range(5):
        if v[j]: Xv=(Xv+smul(X[:,j,:],v[j]))%P
    k=ctx['kp'] if sign>0 else ctx['km']
    Xv=smul(Xv,k)
    Y=X.copy()
    for j in range(5):
        if n[j]: Y[:,j,:]=(Y[:,j,:]+smul(Xv,n[j]))%P
    return smul(Y,{-12*sign:1})
def Dspan(X):
    nz=np.nonzero((X!=0).any(axis=tuple(range(X.ndim-1))))[0]
    return int(nz[-1]-nz[0])
# 3x3 block in basis (v_s): M_s^{+-} = I + k_{+-} e_s (N(s,.)) ; returns unnormalized (no A^-12 factor)
def unit3(ctx):
    X=np.zeros((3,3,ctx['LEN']),dtype=np.int64)
    for i in range(3): X[i,i,ctx['OFF']]=1
    return X
def rmul3(ctx, X, s, sign):
    names=ctx['names']; si=names.index(s)
    k=ctx['kp'] if sign>0 else ctx['km']
    col=smul(X[:,si,:],k)          # X e_s * k
    Y=X.copy()
    for tj,t in enumerate(names):
        nst=ctx['N'][(s,t)]
        if nst: Y[:,tj,:]=(Y[:,tj,:]+smul(col,nst))%P
    return Y
def degs(p, OFF):
    nz=np.nonzero(p)[0]
    if len(nz)==0: return None
    return int(nz[-1]-OFF), int(nz[0]-OFF)
