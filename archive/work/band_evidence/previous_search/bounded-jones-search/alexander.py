#!/usr/bin/env python3
"""Independent Alexander polynomial via the reduced Burau representation."""
import itertools,json
from collections import defaultdict
from search import ROOT

def plus(*ps):
 r=defaultdict(int)
 for p in ps:
  for k,v in p.items():r[k]+=v
 return {k:v for k,v in r.items() if v}
def mult(a,b):
 r=defaultdict(int)
 for k,v in a.items():
  for l,w in b.items():r[k+l]+=v*w
 return {k:v for k,v in r.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def matmul(a,b):
 return [[plus(*(mult(a[i][k],b[k][j]) for k in range(3))) for j in range(3)] for i in range(3)]
def ident():return [[{0:1} if i==j else {} for j in range(3)] for i in range(3)]
def alexander(w):
 b=ident()
 for s in w:
  m=ident();i=abs(s)-1
  m[i][i]={1:-1} if s>0 else {-1:-1}
  if i>0:m[i][i-1]={1:1} if s>0 else {0:1}
  if i<2:m[i][i+1]={0:1} if s>0 else {-1:1}
  b=matmul(b,m)
 m=[[plus({0:1} if i==j else {},neg(b[i][j])) for j in range(3)] for i in range(3)]
 det={}
 for p in itertools.permutations(range(3)):
  v={0:1}
  for i in range(3):v=mult(v,m[i][p[i]])
  parity=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
  det=plus(det,neg(v) if parity else v)
 if not det:return {}
 off=min(det);det={k-off:v for k,v in det.items()};q={}
 while det and max(det)>=3:
  k=max(det)-3;v=det[k+3];q[k]=v
  det=plus(det,{k+j:-v for j in range(4)})
 assert not det,det
 if q[max(q)]<0:q=neg(q)
 return q
if __name__=='__main__':
 assert alexander([1,2,3])=={0:1}
 assert alexander([1,1,1,2,3])=={0:1,1:-1,2:1}
 assert alexander([1,-2,1,-2,3])=={0:1,1:-3,2:1}
 rows=json.loads((ROOT/'exact_hits.json').read_text())
 values=[alexander(x['word']) for x in rows if x['jones_one']]
 assert all(x=={0:1} for x in values)
 print('Independent Alexander polynomial checks: all',len(values),'exact Jones-one knots have Alexander polynomial 1.')
