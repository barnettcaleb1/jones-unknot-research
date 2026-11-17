"""Standard-library replay of the exact saved 16-record exclusion certificate."""
from pathlib import Path
import json
H=Path(__file__).resolve().parent

def p(c):return {int(e):int(a)for e,a in c.items()if a}
def add(a,b):
 r=dict(a)
 for e,c in b.items():r[e]=r.get(e,0)+c
 return {e:c for e,c in r.items()if c}
def mul(a,b):
 r={}
 for e,c in a.items():
  for f,d in b.items():r[e+f]=r.get(e+f,0)+c*d
 return {e:c for e,c in r.items()if c}
def order(a):
 for n in range(len(a)):
  moment=sum(c*e**n for e,c in a.items())
  if moment:return n,moment
 raise AssertionError('zero polynomial')
delta={1:-1,-1:-1};z={-4:1};one_minus_z={0:1,-4:-1}
j=json.loads((H/'marked_hits.json').read_text());cs={r['hit']:r for r in json.loads((H/'corner_verification.json').read_text())}
certified=[];unresolved=[]
for r in j['hits']:
 i=r['hit']
 if r['status']!='certified marked pair':unresolved.append(i);continue
 assert p(r['anchor']['coefficients'])=={0:1}
 assert p(r['cuts'][2]['coefficients'])==mul(delta,delta)
 orders=[]
 for k in range(2):
  S=p(r['cuts'][k]['coefficients']);P=add(S,{1:1,-1:1});n,m=order(P);orders.append(n)
  assert n==r['cuts'][k]['vanishing_order_at_1'] and m==r['cuts'][k]['leading_Euler_moment']
  V=p(cs[i]['corners'][k]['coefficients'])
  assert mul(delta,V)==add(mul(delta,z),mul(one_minus_z,S))
  assert cs[i]['corners'][k]['writhe']==r['anchor']['writhe']-2
 assert sorted(orders)==[2,3]
 certified.append(i)
assert certified==[1,3,5,6,7,8,9,10,11,12,13,14,15,16,19,20]
assert unresolved==[0,2,4,17,18,21]
print('PASS: 16 marked records, 48 cut polynomials, 32 twist checks, exact all-integer exclusion.')
print('Six unmarked records remain unresolved:',unresolved)
