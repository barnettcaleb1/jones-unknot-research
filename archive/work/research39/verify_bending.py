#!/usr/bin/env python3
"""Exact standard-library check over Q[z]/(1+z+...+z^10)."""
from fractions import Fraction as F

def elt(c):
    if isinstance(c, (int, F)):
        c = [c]
    a = list(map(F, c)) + [F(0)] * max(0, 10-len(c))
    for k in range(len(a)-1, 9, -1):
        q = a[k]
        for j in range(10): a[k-10+j] -= q
    return tuple(a[:10])

O, Z = elt(1), elt(0)
def add(a,b): return elt([x+y for x,y in zip(a,b)])
def neg(a): return elt([-x for x in a])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*19
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return elt(c)
def power(a,n):
    r=O
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a); n//=2
    return r
def inv(a):
    cols=[mul(a,elt([0]*i+[1])) for i in range(10)]
    mat=[[cols[j][i] for j in range(10)]+[O[i]] for i in range(10)]
    for i in range(10):
        k=next(k for k in range(i,10) if mat[k][i])
        mat[i],mat[k]=mat[k],mat[i]
        q=mat[i][i]; mat[i]=[x/q for x in mat[i]]
        for j in range(10):
            if j!=i:
                q=mat[j][i]
                mat[j]=[x-q*y for x,y in zip(mat[j],mat[i])]
    return elt([row[-1] for row in mat])
def mm(a,b):
    return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def mp(a,n):
    r=I
    for _ in range(n): r=mm(r,a)
    return r
def det(a): return sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]))
def mi(a):
    assert det(a)==O
    return [[a[1][1],neg(a[0][1])],[neg(a[1][0]),a[0][0]]]
def tr(a): return add(a[0][0],a[1][1])

I=[[O,Z],[Z,O]]
minusI=[[neg(O),Z],[Z,neg(O)]]
z=elt([0,1]); zi=power(z,10)
a=inv(sub(zi,z)); c=neg(add(O,mul(a,a)))
M=[[z,Z],[Z,zi]]
X=[[a,O],[c,neg(a)]]
Y=mm(mi(M),X)
assert c!=Z and det(X)==O and det(Y)==O
assert mp(X,2)==minusI and mp(Y,3)==minusI
assert mm(X,mi(Y))==M
assert mp(M,11)==I
longitude=mm(minusI,mp(mi(M),6))
assert mm(M,mm(longitude,longitude))==I
traces=[]
for t in (1,2,3):
    D=[[elt(t),Z],[Z,elt(F(1,t))]]
    X2=mm(mm(D,X),mi(D))
    traces.append(tr(mm(X,X2)))
    expected=add(mul(elt(2),mul(a,a)),mul(c,elt(F(t*t)+F(1,t*t))))
    assert traces[-1]==expected
assert len(set(traces))==3
print('PASS: trefoil relations, common meridian, preferred +1 filling relation, and three distinct bent characters over Q(zeta_11).')
