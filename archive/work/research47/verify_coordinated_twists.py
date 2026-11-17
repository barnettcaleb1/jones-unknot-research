#!/usr/bin/env python3
"""Exact integer-Laurent verification of an actual two-disk braid family."""
from fractions import Fraction

def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def mul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items(): out[i+j]=out.get(i+j,0)+a*b
    return {k:v for k,v in out.items() if v}
def sc(p,k,s=1): return {i+k:s*a for i,a in p.items()}
delta={2:-1,-2:-1}
Delta2={4:1,0:1,-4:1}
def tm(x,y):
    a,b=x;c,d=y
    return (mul(a,c),add(mul(a,d),mul(b,c),mul(delta,mul(b,d))))
def power(x,n):
    out=({0:1},{})
    for _ in range(n):out=tm(out,x)
    return out
def closure(x):return add(mul(x[0],mul(delta,delta)),mul(x[1],delta))
b=({1:1},{-1:1});bi=({-1:1},{1:1});I=({0:1},{})
assert tm(b,bi)==I==tm(bi,b)
assert add(mul(delta,delta),{0:-1})==Delta2
# delta*b = -A^-3 e + A(delta*I-e): projector eigenvalues.
assert (mul(delta,b[0]),mul(delta,b[1]))==(sc(delta,1),add({-3:-1},{1:-1}))
# Source {3}/{1}=Delta2: no division needed to check this identity.
assert mul({2:1,-2:-1},Delta2)=={6:1,-6:-1}
# At m=n=0 the unreduced zero-framed value is exactly delta.
assert add({-6:1},sc(Delta2,-2,-1))==delta
# Independent word computation at illustrative signed mixed parameters.
for m,n in ((0,0),(1,-1),(-3,3),(1,0),(0,-2),(2,-1),(-2,3)):
    def bp(k):return power(b,k) if k>=0 else power(bi,-k)
    word=tm(tm(bp(2*m),b),bp(2*n))
    p=2*(m+n)+1
    normalized_unreduced=sc(closure(word),-3*p,-1)
    formula=add({-6*p:1},sc(Delta2,-2*p,-1))
    assert normalized_unreduced==formula,(m,n)
    if n==-m:assert formula==delta
c0=Fraction(1,-2);c2=Fraction(-3,-2)
assert c0+c2==1
print('PASS: exact TL2 inverse, projector weights, source quantum-dimension relation, framing, and two-disk identities')
print('Opposite twists are actual braid cancellation; both channels survive with A=1 weights',c0,c2)
