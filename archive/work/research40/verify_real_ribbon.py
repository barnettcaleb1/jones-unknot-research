#!/usr/bin/env python3
"""Exact TL3 proof and rational checks; Python standard library only."""
from fractions import Fraction as F

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
def mm(a,b): return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def ms(a,p): return [[mul(v,p) for v in row] for row in a]
def ma(a,b): return [[add(a[i][j],b[i][j]) for j in range(2)] for i in range(2)]
def tr(a): return add(a[0][0],a[1][1])
I=[[{0:1},{}],[{},{0:1}]]
delta={2:-1,-2:-1}
e1=[[delta,{0:1}],[{},{}]]
e2=[[{},{}],[{0:1},delta]]
assert mm(e1,e1)==ms(e1,delta)
assert mm(e2,e2)==ms(e2,delta)
assert mm(mm(e1,e2),e1)==e1
assert mm(mm(e2,e1),e2)==e2
w=add(mul(delta,delta),{0:-2})
assert add(tr(I),w)==mul(delta,delta)
assert tr(e1)==delta and tr(mm(e1,e2))=={0:1}
C=mm(ma(ms(I,{1:1}),ms(e1,{-1:1})),ma(ms(I,{1:1}),ms(e2,{-1:1})))
assert C==[[{}, {-4:-1}],[{0:1},{-2:-1}]]
assert mm(mm(C,C),C)==ms(I,{-6:1})
for n in (1,2,3):
    q=6*n-1
    P=I
    for _ in range(q): P=mm(P,C)
    assert tr(P)=={-2*q:-1}
    bracket=add(tr(P),mul(w,{2*q:1}))
    jonesA=mul(bracket,{-6*q:1})
    assert jonesA=={-4*(q-1):1,-4*(q+1):1,-8*q:-1}

def torus(n,t): return t**(6*n-2)*(1+t*t-t**(6*n))
def ribbon(n,t): return torus(n,t)*torus(n,1/t)
for n in (1,2,3):
    assert ribbon(n,F(1))==1 and ribbon(n,F(-1))==1
for t in (F(11,10),F(5,4),F(3,2),F(2),F(10)):
    n=1
    while t**(6*n)<=1+t*t: n+=1
    r=ribbon(n,t)
    assert r<0
    assert ribbon(n,-t)==r==ribbon(n,1/t)==ribbon(n,-1/t)
    print(f'|t|={t} or reciprocal: n={n}, ribbon Jones negative at both signs')
print('PASS: exact TL3 relations, closure weights, torus formula, determinant one, and real-axis signs')
