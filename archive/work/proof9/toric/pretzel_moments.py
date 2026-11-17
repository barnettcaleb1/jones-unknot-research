from fractions import Fraction as F
from collections import defaultdict
from math import factorial
from pathlib import Path
import json
# Variables p,a,b with q=a+b,r=a-b, p even and q,r odd.
def add(P,Q):
 out=defaultdict(F,P)
 for e,c in Q.items():out[e]+=c
 return {e:c for e,c in out.items() if c}
def mul(P,Q):
 out=defaultdict(F)
 for e,c in P.items():
  for f,v in Q.items():out[tuple(x+y for x,y in zip(e,f))]+=c*v
 return {e:c for e,c in out.items() if c}
def powerlinear(v,n):
 P={(0,0,0):F(1)};Q={(1,0,0):F(v[0]),(0,1,0):F(v[1]),(0,0,1):F(v[2]),(0,0,0):F(v[3])}
 for _ in range(n):P=mul(P,Q)
 return P
terms=[((-1,-2,0,0),1)]
for off in [-1,0,1]:
 terms += [((-1,0,0,off),1),((0,-1,-1,off),-1),((0,-1,1,off),-1)]
terms += [((0,0,0,k),v) for k,v in [(-2,1),(-1,1),(0,2),(1,1),(2,1)]]
terms += [((-1,1,0,k),-v) for k,v in [(-1,1),(0,2),(1,1)]]
res=[]
moments={}
for n in range(6):
 P={}
 for v,c in terms:P=add(P,{e:c*w for e,w in powerlinear(v,n).items()})
 moments[n]=P
 print(n,sorted((e,str(c)) for e,c in P.items()))
 res.append({'order':n,'coefficients':[[*e,str(c)]for e,c in sorted(P.items())]})
assert moments[0]==moments[1]=={}
assert moments[2]=={(0,0,0):6,(0,2,0):-6,(0,0,2):-6,(1,1,0):12}
assert moments[3]=={(0,1,0):6,(0,1,2):18,(0,3,0):-6,(2,1,0):-18}
# Eliminating b^2 gives M3/6 + a*M2/2 = a*(4-a^2-3*(p-a)^2).
lhs=add({e:c/6 for e,c in moments[3].items()},
        mul({(0,1,0):F(1,2)},moments[2]))
assert lhs=={(0,1,0):4,(0,3,0):-4,(1,2,0):6,(2,1,0):-3}
# Independent all-odd Q moments, now interpreting the variables as p,q,r.
qterms=[((-1,-1,-1,0),1),((-1,0,0,0),-1),
        ((0,-1,0,0),-1),((0,0,-1,0),-1),
        ((0,0,0,1),1),((0,0,0,-1),1)]
qm={}
for n in range(4):
 P={}
 for v,c in qterms:P=add(P,{e:c*w for e,w in powerlinear(v,n).items()})
 qm[n]=P
assert qm[0]==qm[1]=={}
assert qm[2]=={(0,0,0):2,(1,1,0):2,(1,0,1):2,(0,1,1):2}
factored=mul(mul({(1,0,0):-3,(0,1,0):-3},
                 {(0,1,0):1,(0,0,1):1}),{(1,0,0):1,(0,0,1):1})
assert qm[3]==factored
print('PASS: both parity cases, normalization moments, and ellipse elimination.')
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
