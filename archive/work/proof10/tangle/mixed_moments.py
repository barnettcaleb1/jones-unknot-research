from fractions import Fraction as F
from itertools import product
from math import factorial
from collections import defaultdict
from pathlib import Path
import json
# Truncated exponential series with polynomial coefficients in p0,...,pn-1.
def padd(a,b):
 c=defaultdict(F,a)
 for e,v in b.items():c[e]+=v
 return {e:v for e,v in c.items()if v}
def pmul(a,b):
 c=defaultdict(F)
 for e,v in a.items():
  for f,w in b.items():c[tuple(x+y for x,y in zip(e,f))]+=v*w
 return {e:v for e,v in c.items()if v}
def scale(a,c):return {e:v*c for e,v in a.items()if v*c}
def sadd(a,b):return [padd(x,y)for x,y in zip(a,b)]
def smul(a,b):
 c=[{}for _ in range(4)]
 for i in range(4):
  for j in range(4-i):c[i+j]=padd(c[i+j],pmul(a[i],b[j]))
 return c
out={}
for n in[3,4,5,6]:
 z=(0,)*n;one={z:F(1)}
 C=[scale(one,3),{},one,{}]
 N1=[one,{},{},{}];N2=C
 for i in range(n):
  u=tuple(int(j==i)for j in range(n));exp=[{tuple(k*v for v in u):F((-1)**k,factorial(k))}for k in range(4)]
  eps=1 if i==0 else-1
  N1=smul(N1,sadd(C,[scale(p,eps)for p in exp]))
  N2=smul(N2,sadd([scale(one,-1),{},{},{}],[scale(p,eps)for p in exp]))
 N=sadd(N1,N2)
 a=[F(-(1+3*(-1)**(n-1)),4)]+[F(1,2)]*(n-1)
 linear={tuple(int(i==j)for j in range(n)):-v for i,v in enumerate(a)}
 exp=[one,linear,scale(pmul(linear,linear),F(1,2)),scale(pmul(pmul(linear,linear),linear),F(1,6))]
 V=smul(smul(N,exp),[scale(one,F(1,2**(n+1))),{},scale(one,-F(n+1,8*2**(n+1))),{}])
 assert V[0]==one and not V[1]
 rows={}
 for k in[2,3]:
  p=scale(V[k],factorial(k));rows[str(k)]={' '.join(map(str,e)):str(v)for e,v in sorted(p.items())}
  print('n',n,'moment',k,rows[str(k)])
 out[n]=rows
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
