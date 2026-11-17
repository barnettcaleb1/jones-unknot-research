from pathlib import Path
import json,sys
from fractions import Fraction as F
from collections import defaultdict
import math,time
ROOT=Path(__file__).resolve().parent
# Import only reusable exact arithmetic and affine-locus routines, not examples.
ns={};exec((ROOT/'kt_partial_filter.py').read_text().split('f={-4:')[0],ns)
add,mul,divide=ns['add'],ns['mul'],ns['divide']
rows=json.loads((ROOT/'kt_double_cuts.json').read_text())['rows']
Q=[]
for row in rows:
 p={int(e):v for e,v in row['jones_coefficients'].items()}
 d={0:1}
 for _ in row['cut_bands']:d=mul(d,{1:-1,-1:-1})
 q,r=divide(p,d);assert not r and all(e%2==0 and v.denominator==1 for e,v in q.items())
 Q.append({e//2:int(v) for e,v in q.items()})
assert Q[3]=={0:1}
kt={int(e):v for e,v in json.loads((ROOT/'kt_partial_filter.json').read_text())['V_KT'].items()}
assert Q[0]==mul(kt,{-e:v for e,v in kt.items()})
A=add(Q[0],{e:-c for e,c in Q[1].items()},{e:-c for e,c in Q[2].items()},{0:1})
B=add(Q[2],{0:-1});C=add(Q[1],{0:-1})
poly={}
for p,b in [(A,(2,2)),(B,(2,0)),(C,(0,2))]:
 for e,c in p.items():poly[b+(e,)]=c
N=2
# Copied exact RREF branch mechanism, independent of bounds on twists.
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
go()
out={'normalization':'Regina x=t^(1/2), delta=-x-x^-1; x_i=t^(2n_i)', 'cut_Q':Q,'A':A,'B':B,'C':C,'equation':'A*t^(2n1+2n2)+B*t^(2n1)+C*t^(2n2)=0','affine_terms':[[*e,c] for e,c in poly.items()],'stats':dict(counts),'solution_loci':[[[str(x) for x in r] for r in leaf] for leaf in leaves]}
(ROOT/'kt_double_locus.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ['affine_terms']},indent=2))
