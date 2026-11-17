import json, cmath, sys
import numpy as np
from fractions import Fraction
data=json.load(open(sys.argv[1]))
def P(d): return {int(Fraction(k)):v for k,v in d.items()}
data=[(w,P(J),P(V)) for w,J,V in data]
def ev(Pd,z): return sum(c*z**e for e,c in Pd.items())
print('samples',len(data))
for n in range(3,49):
    z=cmath.exp(2j*cmath.pi/n)
    Jv=np.array([ev(J,z) for _,J,_ in data])
    const = np.allclose(Jv,Jv[0],atol=1e-7)
    # regress J(z) on 1, V(z^k) for k in 0..n-1 (all Galois/power twists)
    ks=[k for k in range(1,n)]
    X=np.array([[1]+[ev(V,z**k) for k in ks] for _,_,V in data])
    coef,res,rank,sv=np.linalg.lstsq(X,Jv,rcond=None)
    r=np.abs(X@coef-Jv).max()
    # single-power tests J(z)=a+b V(z^k)
    singles=[]
    for k in range(-n+1,n):
        if k==0: continue
        X1=np.array([[1,ev(V,z**k)] for _,_,V in data])
        c1,_,_,_=np.linalg.lstsq(X1,Jv,rcond=None)
        if np.abs(X1@c1-Jv).max()<1e-6: singles.append((k,np.round(c1,6)))
    flag = 'CONST' if const else ''
    if r<1e-6 or singles or const:
        print(n, flag, 'span-residual %.2e'%r, 'rank',rank, 'singles',singles[:4])
    else:
        print(n, 'none (span residual %.2e, rank %d)'%(r,rank))
