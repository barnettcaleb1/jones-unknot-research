"""Exact Laurent certificate for the eight Jones-sign star patterns."""
from itertools import product
import json
from pathlib import Path

def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,0)+v
 return {k:v for k,v in d.items() if v}
def mul(p,q):
 d={}
 for i,a in p.items():
  for j,b in q.items():d[i+j]=d.get(i+j,0)+a*b
 return {k:v for k,v in d.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def power(p,n):
 r={0:1}
 for _ in range(n):r=mul(r,p)
 return r
u={0:-1,1:-1};v={0:-1,-1:-1};Q={1:1,0:2,-1:1}
assert mul(u,v)==Q
assert add(u,v)==neg(Q)
factor=mul(power({1:1,0:1},3),power({1:1,0:-1},2))
rows=[]
for signs in product([1,-1],repeat=3):
 a,b,c=[u if s==1 else v for s in signs]
 lam=add(Q,a,b,c)
 defect=add(mul(mul(a,b),c),neg(mul(Q,lam)))
 if len(set(signs))==2:assert not defect
 else:
  shift=-2 if signs[0]==1 else -3
  assert defect=={k+shift:-w for k,w in factor.items()}
 rows.append({'signs':signs,'defect':defect})
out={'mixed_cases_exact':6,'same_sign_cases_obstructed':2,'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Verified all 8 sign patterns: 6 exact Reidemeister cases, 2 nonzero defects.')
