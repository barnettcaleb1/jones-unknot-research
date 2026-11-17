"""Exact Laurent checks for the all-markings virtualized-trefoil reduction.

The finite loop below checks the surviving markings only. Completeness follows
from the integer inequalities in all_markings.txt, not from a parameter search.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import json

def clean(p):return {e:c for e,c in p.items() if c}
def add(*ps):
    c=Counter()
    for p in ps:
        for e,v in p.items():c[e]+=v
    return clean(c)
def scale(p,k):return clean({e:k*c for e,c in p.items()})
def shift(p,k):return {e+k:c for e,c in p.items()}
def mul(p,q):
    c=Counter()
    for i,a in p.items():
        for j,b in q.items():c[i+j]+=a*b
    return clean(c)
def odd_quantum_integer(n):
    assert n%2
    sign=1 if n>0 else -1;n=abs(n)
    return {e:sign for e in range(-(n-1)//2,(n-1)//2+1)}
def E(p,q):
    return add({0:2},shift(odd_quantum_integer(2*p+1),q*(p+1)),
               scale(shift(odd_quantum_integer(2*p-1),q*(p-1)),-1))
def G(p,q,r,s):
    return add({0:1,2:-2,3:-1},mul({2:1,1:-1},E(p,q)),
               shift(E(r,s),2),{2+3*r*s:-1,3+3*r*s:-1})
def jet(poly,k):return sum(Fraction(c*e**k,factorial(k)) for e,c in poly.items())

if __name__=='__main__':
    survivors=[]
    for p,q,r,s in product(range(-1,2),repeat=4):
        if p*s-q*r!=1 or p*p+q*q!=1 or p*q!=0 or r*s not in (0,-1):continue
        assert not G(p,q,r,s)
        survivors.append({'matrix_columns':[[p,q],[r,s]],'G_x':G(p,q,r,s)})
    assert len(survivors)==8
    # Independent finite algebra sanity checks of the general jet derivation.
    # These support the symbolic derivation, not completeness over all markings.
    checked=0
    for p,q,r,s in product(range(-3,4),repeat=4):
        if abs(p*s-q*r)!=1:continue
        a=p*q;b=r*s;U=p*p+q*q;T=r*r+s*s
        poly=G(p,q,r,s)
        eq2=T-4*b*b-3*b+6*a-1
        eq3=Fraction(30*a*a+54*a+6*U+12*T+10*b*T-40*b**3-75*b*b-43*b-18,6)
        assert jet(poly,0)==jet(poly,1)==0
        assert jet(poly,2)==eq2
        assert jet(poly,3)==eq3
        if eq2==0:
            assert eq3==Fraction(10*a*a-6*a+2*U+b*b+b-2-20*a*b,2)
        checked+=1
    result={'exact_unit_markings':survivors,'jet_sanity_checks':checked,
            'completeness_method':'Analytic integer inequalities, not a finite search.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
