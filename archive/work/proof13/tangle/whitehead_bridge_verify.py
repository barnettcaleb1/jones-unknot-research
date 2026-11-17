"""Standard-library exact audit of clasp skein + color-three fusion.
Reads the actual Regina diagrams computed this pass and the independent
R-matrix color-three certificate from proof12. No approximate arithmetic.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'quotient_response_test.json').read_text())
colored=json.loads((ROOT.parents[1]/'proof12/braid/all_color_collision_check.json').read_text())
def clean(p):return {e:c for e,c in p.items() if c}
def add(*ps):
 d={}
 for p in ps:
  for e,c in p.items():d[e]=d.get(e,0)+c
 return clean(d)
def neg(p):return {e:-c for e,c in p.items()}
def mul(a,b):
 d={}
 for e,c in a.items():
  for f,v in b.items():d[e+f]=d.get(e+f,0)+c*v
 return clean(d)
def ints(p):return {int(e):c for e,c in p.items()}
delta={1:-1,-1:-1};dim3={2:1,0:1,-2:1}
for row in rows:
 P=ints(row['Seifert_parallel_Jones_x']);W=ints(row['Whitehead_Jones_x'])
 # The old certificate uses u, ordinary variable t=u^-2; here x=t^(1/2)=u^-1.
 J3={-int(e):c for e,c in colored['color3_unreduced_variable_u'][row['knot']].items()}
 assert mul(delta,P)==add(J3,{0:1})
 assert W==add({4:1},mul({3:1,1:-1},P))
 # Denominator-free form of W-1=(1-t^3)/(1+t)*(H3-1), H3=J3/dim3.
 assert mul(mul({2:1,0:1},dim3),add(W,{0:-1}))==mul({0:1,6:-1},add(J3,neg(dim3)))
 print(row['knot'],': exact zero-framed fusion and positive clasp identities passed')
assert rows[0]['Jones_x']==rows[1]['Jones_x']
assert rows[0]['Whitehead_Jones_x']!=rows[1]['Whitehead_Jones_x']
print('PASS: identical ordinary Jones does not determine the quotient Whitehead response.')
