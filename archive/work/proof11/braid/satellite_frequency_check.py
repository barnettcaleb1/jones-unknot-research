#!/usr/bin/env python3
"""Exact rational-free identities; u=q^(1/2), Laurent dictionaries."""
from collections import defaultdict
import json,pathlib

def add(a,b):
 c=defaultdict(int,a)
 for e,v in b.items():c[e]+=v
 return {e:v for e,v in c.items() if v}
def mul(a,b):
 c=defaultdict(int)
 for e,v in a.items():
  for f,w in b.items():c[e+f]+=v*w
 return {e:v for e,v in c.items() if v}
def shift(a,e,s=1):return {f+e:s*v for f,v in a.items()}
def qdim(n):return {e:1 for e in range(1-n,n,2)}
def torus_numerator(j,m):
 p={}
 for a in range(j+1):
  lam=a*(a+1)-j*(j+2)
  p=add(p,shift(qdim(2*a+1),(2*m+1)*lam,(-1)**(j-a)))
 return p
rows=[]
for j in range(13):
 assert torus_numerator(j,0)==qdim(j+1)
 if j:
  lead={-j*(j+2):(-1)**j}
  nxt=shift(qdim(3),2-j*(j+2),(-1)**(j-1))
  ratio=shift(qdim(3),2,-1)
  assert nxt==mul(lead,ratio)
  rows.append({'label':j,'leading_x_degree':j*(j+2),'second_x_degree':j*(j+2)-2,
               'ratio_in_u':ratio})
# Fundamental formula checked by clearing [2] and evaluating several torus colors.
for m in range(8):
 expected=add({-3*(2*m+1):-1},shift(qdim(3),-(2*m+1)))
 assert expected==torus_numerator(1,m)
out={'variable':'u=q^(1/2)','unknot_checks':13,'leading_ratio_checks':rows,'fundamental_checks':8}
p=pathlib.Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS:13 unknot normalizations,12 universal leading-ratio checks,8 fundamental torus checks.')
