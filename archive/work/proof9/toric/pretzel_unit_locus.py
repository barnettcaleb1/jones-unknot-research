"""Exact affine-exponent classification of monomial brackets for 3-pretzels.
No bound is imposed on parameters. Each branch adds a linear equation;
termination follows from the four-dimensional parameter space.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import math,json,time
N=4

def extend(rows,eq):
 v=list(map(F,eq))
 for row in rows:
  pivot=next(i for i in range(N) if row[i]);v=[a-v[pivot]*b for a,b in zip(v,row)]
 idx=[i for i in range(N) if v[i]]
 if not idx:return rows if not v[-1] else None
 p=idx[0];k=v[p];v=tuple(a/k for a in v)
 out=[tuple(a-row[p]*b for a,b in zip(row,v)) for row in rows]+[v]
 return tuple(sorted(out,key=lambda r:next(i for i in range(N) if r[i])))

def reduced(poly,rows):
 out=defaultdict(int)
 for e,c in poly.items():
  v=list(map(F,e))
  for row in rows:
   p=next(i for i in range(N) if row[i]);v=[a-v[p]*b for a,b in zip(v,row)]
  out[tuple(v)]+=c
 return {e:c for e,c in out.items() if c}

def int_possible(rows):
 for r in rows:
  den=math.lcm(*(v.denominator for v in r));ints=[int(v*den) for v in r];g=math.gcd(*ints[:-1])
  if ints[-1]%g:return False
 return True

def solve(poly):
 seen=set();leaves=[];counts=defaultdict(int)
 def go(rows=()):
  if rows in seen:return
  seen.add(rows);counts[len(rows)]+=1
  if not int_possible(rows):return
  red=reduced(poly,rows)
  if not red:leaves.append(rows);return
  if len(rows)==N:return
  opts=[]
  for e,c in red.items():
   opp=[f for f,d in red.items() if c*d<0 and e[:-1]!=f[:-1]]
   if not opp:return
   opts.append((len(opp),e,opp))
  _,e,opp=min(opts)
  for f in opp:
   nr=extend(rows,tuple(a-b for a,b in zip(e,f)))
   if nr is not None:go(nr)
 go();return leaves,dict(counts)

out=[];start=time.monotonic()
for parity in product([0,1],repeat=3):
 for sign in [-1,1]:
  P=defaultdict(int)
  P[(-2,-2,-2,0,-sum(parity))]+=(-1)**sum(parity)
  for i in range(3):
   for off in [-1,0,1]:
    e=[0]*5;e[i]=-2;e[-1]=off-parity[i];P[tuple(e)]+=(-1)**parity[i]
  for e,c in [(-2,1),(-1,1),(0,2),(1,1),(2,1)]:P[(0,0,0,0,e)]+=c
  for e,c in [(-1,1),(0,2),(1,1)]:P[(0,0,0,1,e)]-=sign*c
  P={e:c for e,c in P.items() if c}
  leaves,stats=solve(P)
  row={'parity':parity,'unit_sign':sign,'terms':len(P),'stats':stats,'loci':[[[str(x) for x in r] for r in rows] for rows in leaves]}
  out.append(row);print(parity,sign,len(leaves),stats,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'parameters':'p=parity[0]+2a,q=parity[1]+2b,r=parity[2]+2c; d=A^4+2+A^-4; E=sign*d*(A^4)^m','results':out,'seconds':time.monotonic()-start},indent=2)+'\n')
