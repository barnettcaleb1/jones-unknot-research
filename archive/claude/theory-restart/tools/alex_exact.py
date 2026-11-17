#!/usr/bin/env python3
"""Exact Alexander polynomial of the strongly invertible knot of a half-diagram word, by exact integer evaluation at many points
and Lagrange interpolation (degree bound = number of crossings). Prints the polynomial up to units +-t^k."""
import sys
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
def raw_det(word,t):
    full=alex.symmetrize(alex.parse(word)); cr=alex.diagram(full)
    if cr is None: return None,None
    if not cr: return 1,0
    M,w=alex.alex_matrix(cr,t)
    m=[r[:-1] for r in M[:-1]]
    return alex.bareiss(m),len(cr)
def interpolate(xs,ys):
    # returns coefficient list (lowest degree first) of the unique polynomial of degree < len(xs)
    n=len(xs); coeffs=[Fr(0)]*n
    for i in range(n):
        # basis polynomial
        num=[Fr(1)]; den=Fr(1)
        for j in range(n):
            if j==i: continue
            num=[Fr(0)]+num
            for k in range(len(num)-1): num[k]-=xs[j]*num[k+1]
            den*=(xs[i]-xs[j])
        for k in range(len(num)): coeffs[k]+=ys[i]*num[k]/den
    return coeffs
def exact(word):
    d0,n=raw_det(word,2)
    if d0 is None: return None
    xs=list(range(2,2+n+3)); ys=[]
    for x in xs:
        d,_=raw_det(word,x); ys.append(Fr(d))
    c=interpolate([Fr(x) for x in xs],ys)
    assert all(v.denominator==1 for v in c)
    c=[int(v) for v in c]
    while c and c[-1]==0: c.pop()
    lo=0
    while lo<len(c) and c[lo]==0: lo+=1
    c=c[lo:]
    if c and c[0]<0: c=[-v for v in c]
    return c
if __name__=='__main__':
    for w in sys.argv[1:]:
        print(w,'  Alexander polynomial coefficients (up to units):',exact(w))
