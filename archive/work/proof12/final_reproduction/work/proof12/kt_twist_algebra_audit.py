from pathlib import Path
from fractions import Fraction
import json
rows=json.loads(Path('work/proof12/tangle/kt_double_cuts.json').read_text())['rows']
def clean(p): return {e:c for e,c in p.items() if c}
def add(*ps):
 r={}
 for p in ps:
  for e,c in p.items():r[e]=r.get(e,0)+c
 return clean(r)
def shift(p,k,s=1):return {e+k:s*c for e,c in p.items()}
def mul(p,q):
 r={}
 for e,c in p.items():
  for f,d in q.items():r[e+f]=r.get(e+f,0)+c*d
 return clean(r)
def div(p,q):
 p0,q0=min(p),min(q);r=shift(p,-p0);q=shift(q,-q0);ans={}
 while r and max(r)>=max(q):
  k=max(r)-max(q);v=Fraction(r[max(r)],q[max(q)]);ans[k]=v
  r=add(r,shift(q,k,-v))
 assert not r,r
 return {e+p0-q0:int(c) if c.denominator==1 else c for e,c in ans.items()}
ps=[clean({int(e):v for e,v in row['jones_coefficients'].items()}) for row in rows]
P=ps[0];Q1=div(ps[1],{1:-1,-1:-1});Q2=div(ps[2],{1:-1,-1:-1});Q12=div(ps[3],{2:1,0:2,-2:1});assert Q12=={0:1}
A=add(P,shift(Q1,0,-1),shift(Q2,0,-1),{0:1});B=add(Q2,{0:-1});C=add(Q1,{0:-1})
assert A and B and C
leading_certificate=[{'polynomial':name,'highest_x_exponent':max(p),'leading_coefficient':p[max(p)]} for name,p in [('A',A),('B',B),('C',C)]]
assert [r['highest_x_exponent'] for r in leading_certificate]==[20,16,18]
assert all(r['leading_coefficient']==-1 for r in leading_certificate)
# Solve A+x^u B+x^v C=0. A highest exponent must tie B or C,
# or B and C tie one another. This is exhaustive for three nonzero terms.
sol=[];tests=[]
def check(u,v,case):
 residual=add(A,shift(B,u),shift(C,v));good=not residual
 tests.append({'case':case,'u':u,'v':v,'identity':good,'u_mod4':u%4,'v_mod4':v%4,'residual_terms':len(residual)})
 if good and u%4==v%4==0:sol.append([u,v])
u=max(A)-max(B);D=add(A,shift(B,u))
if D:check(u,max(D)-max(C),'A-top=B-top')
else:tests.append({'case':'A-top=B-top','impossible':'remaining C nonzero'})
v=max(A)-max(C);D=add(A,shift(C,v))
if D:check(max(D)-max(B),v,'A-top=C-top')
else:tests.append({'case':'A-top=C-top','impossible':'remaining B nonzero'})
d=max(C)-max(B);D=add(shift(B,d),C)
if D:
 v=max(A)-max(D);check(v+d,v,'B-top=C-top')
else:tests.append({'case':'B-top=C-top','impossible':'remaining A nonzero'})
out={'Q1':Q1,'Q2':Q2,'A':A,'B':B,'C':C,'leading_coefficient_certificate':leading_certificate,'candidate_tests':tests,'integer_twist_solutions':sol,'status':'exact algebra conditional on the supplied cut-link template and its twist recurrence'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:out[k] for k in ('candidate_tests','integer_twist_solutions','status')},indent=2))
