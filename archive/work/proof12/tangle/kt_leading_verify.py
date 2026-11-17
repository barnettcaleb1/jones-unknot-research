"""Standard-library certificate from four stored, independently computed cut links.
Does not need Spherogram or Regina. Geometry is recorded in kt_double_cuts.py/json.
"""
from pathlib import Path
from fractions import Fraction
import json
ROOT=Path(__file__).resolve().parent
def clean(p):return {e:c for e,c in p.items()if c}
def add(*ps):
 r={}
 for p in ps:
  for e,c in p.items():r[e]=r.get(e,0)+c
 return clean(r)
def mul(a,b):
 r={}
 for e,c in a.items():
  for f,d in b.items():r[e+f]=r.get(e+f,0)+c*d
 return clean(r)
def divide(a,b):
 a=clean(a);b=clean(b);a0=min(a);b0=min(b)
 a={e-a0:Fraction(c)for e,c in a.items()};b={e-b0:Fraction(c)for e,c in b.items()};q={}
 while a and max(a)>=max(b):
  k=max(a)-max(b);v=a[max(a)]/b[max(b)];q[k]=v
  a=add(a,{k+e:-v*c for e,c in b.items()})
 assert not a
 return {e+a0-b0:c for e,c in q.items()if c}
rows=json.loads((ROOT/'kt_double_cuts.json').read_text())['rows'];Q=[]
for row in rows:
 p={int(e):c for e,c in row['jones_coefficients'].items()};d={0:1}
 for _ in row['cut_bands']:d=mul(d,{1:-1,-1:-1})
 q=divide(p,d)
 assert all(e%2==0 and c.denominator==1 for e,c in q.items())
 Q.append({e//2:int(c)for e,c in q.items()})
assert Q[3]=={0:1}
A=add(Q[0],{e:-c for e,c in Q[1].items()},{e:-c for e,c in Q[2].items()},{0:1})
B=add(Q[2],{0:-1});C=add(Q[1],{0:-1})
assert [(max(p),p[max(p)])for p in [A,B,C]]==[(10,-1),(8,-1),(9,-1)]
assert rows[3]['simplified_PD']==[] and rows[3]['free_unknot_components']==3
print('VERIFIED: A,B,C have leading coefficients -1 at t-degrees10,8,9.')
print('For every integer m,n, A*t^(2m+2n)+B*t^(2m)+C*t^(2n) is nonzero.')
print('Thus every knot in the specified full-band-twist family has Jones polynomial !=1.')
