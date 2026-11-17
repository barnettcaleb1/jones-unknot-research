"""Exact Laurent filter for one-axis symmetric union partial knots of KT.
Our twist exponent m is opposite to Tanaka2022's m. Identity:
  (1+(-t)^m) F(t)=V_KT(t)+(-t)^m V_KT(t^-1), F=V_J V_J^*.
Tanaka's congruence 8|m| divides V'_KT(-1) gives m=+-1,+-2,+-3,+-6.
"""
from fractions import Fraction
from pathlib import Path
import json

def clean(p):return {e:c for e,c in p.items() if c}
def add(*ps):
 r={}
 for p in ps:
  for e,c in p.items():r[e]=r.get(e,0)+c
 return clean(r)
def mul(p,q):
 r={}
 for e,c in p.items():
  for f,d in q.items():r[e+f]=r.get(e+f,0)+c*d
 return clean(r)
def star(p):return {-e:c for e,c in p.items()}
def evaluate(p,t):return sum(Fraction(c)*Fraction(t)**e for e,c in p.items())
def divide(a,b):
 # independent shift numerator and denominator to ordinary polynomials.
 a0=min(a);b0=min(b)
 a={e-a0:Fraction(c) for e,c in a.items()};b={e-b0:Fraction(c) for e,c in b.items()};q={}
 while a and max(a)>=max(b):
  k=max(a)-max(b);v=a[max(a)]/b[max(b)];q[k]=v
  a=add(a,{k+e:-v*c for e,c in b.items()})
 return {e+a0-b0:c for e,c in q.items()},a
f={-4:1,-3:-2,-2:3,-1:-4,0:4,1:-4,2:3,3:-2,4:1}
V=add({0:1},mul({2:1,0:-1},f))
assert evaluate(V,1)==1 and sum(e*c for e,c in V.items())==0
assert sum(e*c*Fraction(-1)**(e-1) for e,c in V.items())==-48
rows=[]
for m in [-6,-3,-2,-1,1,2,3,6]:
 x={m:1 if m%2==0 else -1}; den=add({0:1},x);num=add(V,mul(x,star(V)))
 q,r=divide(num,den)
 row={'m':m,'Laurent':not r,'remainder':{e:str(c) for e,c in r.items()}}
 if not r:
  assert q==star(q)
  row['F']={e:str(c) for e,c in sorted(q.items())}
  # Constant coefficient of norm P P* is sum of integer coefficient squares.
  row['constant_coefficient']=str(q.get(0,0))
  row['F_minus1']=str(evaluate(q,-1))
  omega=[sum(c for e,c in q.items() if e%3==i) for i in range(3)]
  omega_reduced=[omega[0]-omega[2],omega[1]-omega[2]]
  row['F_omega']=list(map(str,omega_reduced))
  if omega_reduced!=[1,0]:row['excluded']='V_J(primitive cube root)=1, but this norm fails that identity'
  # If constant coefficient =1, only integer norm is 1, so nonconstant rules out.
  if q.get(0,0)==1 and q!={0:1}:row['excluded']='integer norm constant coefficient 1 forces monomial P, hence F=1'
  if q.get(0,0)<1:row['excluded']='integer norm has positive constant coefficient'
 rows.append(row)
assert [r['m'] for r in rows if r['Laurent'] and 'excluded' not in r]==[2]
print(json.dumps(rows,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps({'V_KT':V,'rows':rows},indent=2))
