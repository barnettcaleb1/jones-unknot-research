"""Independent exact W(6,0) Temperley-Lieb model (referee check). Laurent polys = dict exp->int.
sigma_i -> A + A^-1 e_i ; rho(word) v applies rightmost letter first."""
import itertools
def ladd(p,q,s=1):
    r=dict(p)
    for e,c in q.items():
        r[e]=r.get(e,0)+s*c
        if r[e]==0: del r[e]
    return r
def lmul(p,q):
    r={}
    for a,x in p.items():
        for b,y in q.items():
            r[a+b]=r.get(a+b,0)+x*y
    return {e:c for e,c in r.items() if c}
def lbar(p): return {-e:c for e,c in p.items()}
def lsh(p,k): return {e+k:c for e,c in p.items()}
DELTA={2:-1,-2:-1}
def lpow(p,k):
    r={0:1}
    for _ in range(k): r=lmul(r,p)
    return r
NP=6
def ncm(pts):
    if not pts: return [()]
    a=pts[0]; out=[]
    for k in range(1,len(pts),2):
        for mi in ncm(pts[1:k]):
            for mo in ncm(pts[k+1:]):
                out.append(((a,pts[k]),)+mi+mo)
    return out
def partner(m):
    p=[None]*NP
    for a,b in m: p[a]=b; p[b]=a
    return tuple(p)
BASIS=[partner(m) for m in ncm(list(range(NP)))]
IDX={m:i for i,m in enumerate(BASIS)}
DIM=len(BASIS)
def e_act(i,m):  # e_i joins points i-1,i (0-indexed)
    a,b=i-1,i
    if m[a]==b: return True,m
    p=list(m); x,y=p[a],p[b]
    p[a],p[b]=b,a; p[x],p[y]=y,x
    return False,tuple(p)
def nloops(m,n):
    par=list(range(NP))
    def f(x):
        while par[x]!=x: x=par[x]
        return x
    for x in range(NP):
        for y in (m[x],n[x]):
            rx,ry=f(x),f(y)
            if rx!=ry: par[rx]=ry
    return len({f(x) for x in range(NP)})
GRAM=[[lpow(DELTA,nloops(m,n)) for n in BASIS] for m in BASIS]
def sig(g,v):
    i=abs(g); out=[{} for _ in range(DIM)]
    for j,c in enumerate(v):
        if not c: continue
        isd,m2=e_act(i,BASIS[j]); k=IDX[m2]
        ec=lmul(c,DELTA) if isd else c
        if g>0:
            out[j]=ladd(out[j],lsh(c,1)); out[k]=ladd(out[k],lsh(ec,-1))
        else:
            out[j]=ladd(out[j],lsh(c,-1)); out[k]=ladd(out[k],lsh(ec,1))
    return out
def rvec(word,v):
    for g in reversed(word): v=sig(g,v)
    return v
def rmat(word):
    cols=[]
    for j in range(DIM):
        e=[{} for _ in range(DIM)]; e[j]={0:1}
        cols.append(rvec(word,e))
    return [[cols[j][i] for j in range(DIM)] for i in range(DIM)]
def H(a,b):
    acc={}
    for i in range(DIM):
        if not a[i]: continue
        ai=lbar(a[i])
        for j in range(DIM):
            if b[j]: acc=ladd(acc,lmul(lmul(ai,GRAM[i][j]),b[j]))
    return acc
def lstr(p):
    if not p: return '0'
    return ' '.join('%+d*A^%d'%(p[e],e) for e in sorted(p,reverse=True))
