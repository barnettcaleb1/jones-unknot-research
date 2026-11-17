#!/usr/bin/env python3
"""Referee check B1: Kauffman bracket of the tangle T_w AS DRAWN in REPORT 1.3(b) / Tangle::quotient (cap (T 0)(1 4)(2 3), letters
Y = y0.y1.y1.y0, X = x2.x1.x3.x2, closing arc (0,1)) against the matrix formula of Theorem A.
Claim to test:  coefficient of b  =  +-A^k * J_w(t)  with t = A^{4 eps}, one global eps."""
import sys, itertools
from lp import *
from skein import *
def to_t(p,eps):
    """return (k, sign, poly in t) if p(A) = sign*A^k*q(A^(4 eps)) with the convention that q's lowest t-exponent... else None"""
    if not p: return None
    es=sorted(p); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    return {eps*((e-r)//4):c for e,c in p.items()}
def same_up_to_unit(p,q):
    if not p or not q: return p==q
    sh=min(p)-min(q)
    q1={e+sh:c for e,c in q.items()}
    return p==q1 or p=={e:-c for e,c in q1.items()}
maxlen=int(sys.argv[1]) if len(sys.argv)>1 else 6
res={1:0,-1:0}; tot=0; bad_unknot=0; notpoly=0
for m in range(0,maxlen+1):
    for word in itertools.product('YXyx',repeat=m):
        w=''.join(word); tot+=1
        b,c=tangle_vector(w)
        # T(infinity): b closes to 1 loop, c to 2 loops
        tinf=add(b,mul(c,DELTA))
        if not (len(tinf)==1 and abs(list(tinf.values())[0])==1): bad_unknot+=1
        J=Jword(w)
        for eps in (1,-1):
            bt=to_t(b,eps)
            if bt is None: notpoly+=1; continue
            if same_up_to_unit(bt,J): res[eps]+=1
print('words of length <=',maxlen,':',tot)
print('T_w(infinity) not a unit (not the unknot bracket):',bad_unknot)
print('coefficient of b not of the form A^k * poly(A^4):',notpoly//2)
print('agreement with Theorem A up to a unit, t = A^4:',res[1],'   t = A^-4:',res[-1])
