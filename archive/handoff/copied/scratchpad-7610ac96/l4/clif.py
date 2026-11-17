import json, cmath, sys
import numpy as np
from fractions import Fraction
from collections import Counter
data=json.load(open(sys.argv[1]))
def P(d): return {int(Fraction(k)):v for k,v in d.items()}
data=[(w,P(J),P(V)) for w,J,V in data]
def ev(Pd,z): return sum(c*z**e for e,c in Pd.items())
def norm(Pd,n):
    from math import gcd
    pr=1
    for k in range(1,n):
        if gcd(k,n)==1: pr*=ev(Pd,cmath.exp(2j*cmath.pi*k/n))
    return pr
def a2V(V): return -sum(c*e*(e-1) for e,c in V.items())/6.0
def a2J(J): return -sum(c*e*(e-1)*(-1)**(e-2) for e,c in J.items())/24.0
for n in [3,5,8,12,16,20,24]:
    rows=[]
    for w,J,V in data:
        det=abs(round(ev(V,-1).real)); arf=0 if round(ev(V,1j).real)==1 else 1
        NJ=norm(J,n)
        rows.append((round(NJ.real,4), det, arf, round(a2V(V),3), round(a2J(J),3)))
    c=Counter(r[0] for r in rows)
    print('n=%d'%n,'distinct norms of J(z):',len(c),'most common',c.most_common(8))
    # is norm a function of det? of (det,arf)?
    f={}
    bad=0
    for r in rows:
        k=(r[1],r[2]); 
        if k in f and f[k]!=r[0]: bad+=1
        f.setdefault(k,r[0])
    print('   norm determined by (det,arf)? conflicts=',bad)
