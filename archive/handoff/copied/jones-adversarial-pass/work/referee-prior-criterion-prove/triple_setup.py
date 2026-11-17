import sys; sys.path.insert(0,sys.argv[1])
from w60 import *
from fractions import Fraction
vc=[{2:1,-2:1},{0:1},{0:1},{2:1,-2:1},{4:1,0:1,-4:1}]
T3={4:1,0:1,-4:1}; T4={6:1,2:1,-2:1,-6:1}
def ldiv_exact(p,q):
    # exact division of Laurent polys (integer coeffs), raises if not exact
    p=dict(p); out={}
    qh=max(q); qc=q[qh]
    while p:
        ph=max(p); c=p[ph]
        if c%qc: raise ValueError('not exact')
        k=ph-qh; out[k]=c//qc
        p=ladd(p,lsh({e:cc*(c//qc) for e,cc in q.items()},k),-1)
        if p and max(p)<min(q)+k-10**6: raise ValueError
        if p and (max(p)-min(p))<(max(q)-min(q)) and p and max(p)<qh+min(p)-min(p)+k: pass
        if len(out)>10000: raise ValueError('runaway')
    return out
T34=lmul(T3,T4)
G={'c':[], 'x':[3], 'y':[4,3,2,3]}
V={k:rvec(w,vc) for k,w in G.items()}
def perm(word):
    p=list(range(6))
    for g in reversed(word):
        i=abs(g)-1
        p=[(i+1 if x==i else i if x==i+1 else x) for x in p]
    return p
for k,w in G.items():
    p=perm(w); print(k,'encloses',sorted(p[i]+1 for i in range(3)))
N={}
for a in G:
    for b in G:
        h=H(V[a],V[b]); n=ldiv_exact({e:-c for e,c in h.items()},T34); N[(a,b)]=n
for a in G:
    print(a,[lstr(N[(a,b)]) for b in G])
# check rank-one formula: R_s = rho(g T_c^2 g^-1) ; R_s w = A^-12 (w + kappa' N(s,w) v_s)
TC=[1,2]*3
def inv(w): return [-g for g in reversed(w)]
import random
random.seed(1)
kap={12:1,0:0}
kap=lmul(lmul({12:1},{6:1,-6:1}),{2:1,-2:-1})  # (A^24-1)/[3]
for s in G:
    word=G[s]+TC*2+inv(G[s])
    for trial in range(3):
        w=[{e:random.randint(-3,3) for e in range(-2,3)} for _ in range(DIM)]
        lhs=rvec(word,w)
        hs=H(V[s],w); Ns=ldiv_exact({e:-c for e,c in hs.items()},T34)
        rhs=[lsh(ladd(w[i],lmul(lmul(kap,Ns),V[s][i])),-12) for i in range(DIM)]
        assert all(ladd(lhs[i],rhs[i],-1)=={} for i in range(DIM)), s
print('rank-one formula verified for c,x,y')
# cyclic product
cyc=lmul(lmul(N[('c','x')],N[('x','y')]),N[('y','c')])
print('cyclic N(c,x)N(x,y)N(y,c) =',lstr(cyc))
