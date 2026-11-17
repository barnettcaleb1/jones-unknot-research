from itertools import combinations_with_replacement
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'generic'))
from tangle_unit_check import *
def bracket(p):
 v=(ONE,ZERO)
 for q in p:v=pairmul(v,power_b(-q)[::-1])
 return add(mul(DELTA,v[0]),v[1])
results=[]
for n in[4,5]:
 for q in combinations_with_replacement(range(-31,32,2),n-1):
  T=sum(q);Q2=sum(x*x for x in q);Q3=sum(x**3 for x in q);m=n-1
  if n%2:
   if T==0:
    if Q2!=m:continue
    candidates=range(-20,21,2)
   else:
    if (Q2-m)%(2*T):continue
    p=(Q2-m)//(2*T)
    if p%2:continue
    candidates=[p]
  else:
   # p²+2Tp+Q2-m=0
   d=T*T-Q2+m
   if d<0:continue
   from math import isqrt
   s=isqrt(d)
   if s*s!=d:continue
   candidates=set([-T-s,-T+s])
  for p in candidates:
   if p%2:continue
   eq=2*Q3-T*(2+3*p*T+3*p*p)if n%2 else 2*Q3-2*T+p+3*p*T*T-p**3
   if eq:continue
   b=bracket((p,)+q)
   monomial=len(b)==1 and abs(next(iter(b.values())))==1
   row={'parameters':(p,)+q,'monomial_bracket':monomial,'bracket_A':b}
   results.append(row)
   if not monomial:print('NONTRIVIAL',row,flush=True)
print('total',len(results),'nontrivial',sum(not r['monomial_bracket']for r in results))
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n')
