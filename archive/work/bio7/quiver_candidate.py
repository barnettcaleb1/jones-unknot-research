"""Exact colored-series stress test. ABSTRACT QUIVER, not a known knot."""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json

def clean(P): return {e:c for e,c in P.items() if c}
def add(P,Q):
    R=defaultdict(int,P)
    for e,c in Q.items():R[e]+=c
    return clean(R)
def shift(P,k,c=1): return {e+k:c*v for e,v in P.items() if c*v}
def mul(P,Q):
    R=defaultdict(int)
    for e,c in P.items():
        for f,d in Q.items():R[e+f]+=c*d
    return clean(R)
@lru_cache(None)
def binom(n,k):
    if k<0 or k>n:return {}
    if k==0 or k==n:return {0:1}
    return add(binom(n-1,k-1),shift(binom(n-1,k),k))
def compositions(n,k):
    if k==1:yield(n,);return
    for i in range(n+1):
        for tail in compositions(n-i,k-1):yield(i,)+tail
def colored(C,r):
    n=len(C);R={}
    for d in compositions(r,n):
        E=sum(C[i][i]*d[i]*(d[i]-1)//2 for i in range(n))
        E+=sum(C[i][j]*d[i]*d[j] for i in range(n) for j in range(i+1,n))
        sign=(-1)**sum(C[i][i]*d[i] for i in range(n))
        P={0:1};left=r
        for di in d:P=mul(P,binom(left,di));left-=di
        R=add(R,shift(P,E,sign))
    return R
def habiro_factor(N,k):
    P={0:1}
    for j in range(1,k+1):
        P=mul(P,{0:1,N+j:-1})
        P=mul(P,{0:1,j-N:-1})
    return P
def divide(P,Q):
    if not P:return {},{}
    # Shift the divisor's smallest exponent to zero. Standard exact Laurent division.
    lo=min(Q);D=shift(Q,-lo);R=dict(P);quo={}
    bottom=min(P)
    while R and max(R)>=bottom+max(D):
        k=max(R)-max(D);v=R[max(R)]
        assert v%D[max(D)]==0
        c=v//D[max(D)];quo[k-lo]=quo.get(k-lo,0)+c
        R=add(R,shift(D,k,-c))
    return clean(quo),R

C=[[0]*7 for _ in range(7)]
for i in range(4,7):C[i][i]=1
same=iter([0,0,0,0,2,5,6,9,11])
opp=iter([0,0,0,0,0,0,1,1,4,7,10,10])
for i in range(7):
    for j in range(i+1,7):
        C[i][j]=C[j][i]=next(same if (i<4)==(j<4) else opp)
H={N:colored(C,N-1) for N in range(1,6)}
assert H[1]==H[2]=={0:1}
F={0:1}
for n in (1,2,4,5):F=mul(F,{n:1,0:-1})
assert H[3]==add({0:1},F)
coeffs={0:{0:1},1:{}}
audit=[]
for N in range(3,6):
    residual=dict(H[N])
    for k,P in coeffs.items():residual=add(residual,mul({e:-c for e,c in P.items()},habiro_factor(N,k)))
    quotient,remainder=divide(residual,habiro_factor(N,N-1))
    audit.append({'N':N,'remainder':remainder,'passes':not remainder})
    if remainder:break
    coeffs[N-1]=quotient
report={'warning':'ABSTRACT symmetric quiver; no knot realization claimed',
 'C':C,'variable':'y=q^2; x_i=q^(-C_ii)x',
 'normalization':'H_N=(y;y)_(N-1) [x^(N-1)] Z_C',
 'H':H,'Habiro_coefficients':coeffs,'Habiro_audit':audit,
 'derivatives_at_1':{N:[sum(c*e for e,c in P.items()),sum(c*e*(e-1) for e,c in P.items())] for N,P in H.items()}}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='H'},indent=2))
