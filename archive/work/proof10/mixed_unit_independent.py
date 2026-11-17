"""Independent exact polynomial elimination for the mixed unit-box theorem."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json

def add(*args):
    out=defaultdict(F)
    for arg in args:
        for e,c in arg.items(): out[e]+=c
    return {e:c for e,c in out.items() if c}
def scale(k,arg): return {e:k*c for e,c in arg.items() if k*c}
def mul(a,b):
    out=defaultdict(F)
    for e,c in a.items():
        for f,d in b.items(): out[tuple(x+y for x,y in zip(e,f))]+=c*d
    return {e:c for e,c in out.items() if c}
def power(a,n):
    out={(0,0,0):F(1)}
    for _ in range(n): out=mul(out,a)
    return out
def subvar(poly,index,replacement):
    terms=[]
    for e,c in poly.items():
        f=list(e); n=f[index]; f[index]=0
        terms.append(mul({tuple(f):c},power(replacement,n)))
    return add(*terms)

one={(0,0,0):F(1)}
p={(1,0,0):F(1)}; a={(0,1,0):F(1)}; b={(0,0,1):F(1)}
T=add(scale(2,a),one)
Q3=add(scale(2,power(a,3)),scale(6,mul(a,power(b,2))),one)
F3=add(scale(2,Q3),scale(-2,T),p,scale(3,mul(p,power(T,2))),scale(-1,power(p,3)))
B2=add(one,scale(-1,power(a,2)),scale(F(-1,2),power(p,2)),scale(-1,mul(p,T)))
reduced=[]
for e,c in F3.items():
    assert e[2] in (0,2)
    reduced.append(mul({(e[0],e[1],0):c},B2 if e[2] else one))
c=add(p,scale(2,a))
assert add(*reduced)==add(scale(-1,power(c,3)),scale(4,c))
square=power(add(a,one),2)
for value in (0,-2,2):
    specialized=subvar(B2,0,add(scale(value,one),scale(-2,a)))
    assert specialized==add(square,scale(-4 if value==2 else 0,one))

# Independent checks of the exceptional Jones polynomial in t.
Q={i:c for i,c in enumerate([1,2,4,5,6,5,4,2,1])}
V=defaultdict(int,{0:1})
for i,c in Q.items():
    for j,d in enumerate([1,-4,6,-4,1]): V[i+j-8]+=c*d
V={e:c for e,c in V.items() if c}
def derivative(k):
    total=0
    for e,c in V.items():
        for j in range(k): c*=e-j
        total+=c
    return total
assert [derivative(k) for k in range(5)]==[1,0,0,0,720]
det=sum(c*((-1) if e%2 else 1) for e,c in V.items())
assert det==33
report={'elimination_identity':'F3=-(p+2a)^3+4(p+2a)',
        'all_three_specializations_verified':True,
        'exception_Jones':V,'derivatives_0_to_4':[derivative(k) for k in range(5)],
        'determinant':det}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: exact elimination, all branches, exceptional polynomial and determinant.')
