#!/usr/bin/env python3
"""Standard-library check of trefoil defect and slope-1/2 cap factor.
Geometric markings are audited separately; this file checks exact algebra.
"""
from collections import defaultdict

def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
    r=defaultdict(int)
    for p in ps:
        for k,v in p.items(): r[k]+=v
    return clean(r)
def scale(p,c): return clean({k:c*v for k,v in p.items()})
def mul(*ps):
    r={0:1}
    for p in ps:
        q=defaultdict(int)
        for i,a in r.items():
            for j,b in p.items():q[i+j]+=a*b
        r=clean(q)
    return r
def sh(p,n):return {k+n:v for k,v in p.items()}
def sub(p,q):return add(p,scale(q,-1))
def power(p,n):
    assert n>=0
    r={0:1}
    for _ in range(n):r=mul(r,p)
    return r

one={0:1};delta={2:-1,-2:-1}
R={2:-1,6:1,22:-1,30:-1}
x=mul({2:1},{4:1,0:-1},{0:1,8:1},{0:1,12:1})
assert mul(x,sub(one,mul(delta,delta)))==sub(R,delta)
assert sub(R,delta)==mul({-2:1},{0:1,8:1},{0:1,24:-1})
# Q_(1/2) = rotate(Q_-2): coefficients (1-A^4,A^-2).
c={0:1,4:-1};d={-2:1}
u0=add(mul(delta,c),d)
uinf=add(c,mul(delta,d))
assert u0=={6:1}
cap=sub(sh(uinf,-6),delta)
assert cap=={2:1,-10:-1} # A^-10(A^12-1)
base=sub(R,delta)
dWh=mul({0:1,4:-1},{0:1,8:1},{0:1,12:1})
# A-inversion t=A^-4 turns each displayed factor into a Laurent unit
# times the asserted ordinary-t polynomial. Check factor-by-factor.
assert sh({0:1,4:-1},-4)=={0:-1,-4:1}
assert sh({0:1,8:1},-8)=={0:1,-8:1}
assert sh({0:1,12:1},-12)=={0:1,-12:1}
assert sh(cap,-2)=={0:1,-12:-1}
# Thus cap*x*dWh^r is a signed monomial times
# (t-1)^(r+2)(t^2+t+1)(1+t^2)^(r+1)(1+t^3)^(r+1).
tminus={-4:1,0:-1};cyclo3={-8:1,-4:1,0:1}
two={-8:1,0:1};three={-12:1,0:1}
for r in range(8):
    actual=mul(cap,x,power(dWh,r))
    expected=mul(power(tminus,r+2),cyclo3,power(two,r+1),power(three,r+1))
    shift=max(actual)-max(expected)
    sign=actual[max(actual)]//expected[max(expected)]
    assert actual==sh(scale(expected,sign),shift),(r,actual,expected)
print('PASS: exact trefoil defect, preferred 1/2 cap, and tower factorization.')
