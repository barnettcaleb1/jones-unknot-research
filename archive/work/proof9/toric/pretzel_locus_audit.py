from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,product
import json,runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):s=runpy.run_path(str(Path(__file__).with_name('pretzel_unit_locus.py')))
data=json.loads(Path(__file__).with_name('pretzel_unit_locus.json').read_text())
exceptions=set(permutations((1,0,1)))|set(permutations((-1,0,-1)))|set(permutations((1,-2,-3)))|set(permutations((-1,2,3)))
uncovered=[];counts={'line':0,'exception':0}
for row in data['results']:
 p=row['parity']
 for raw in row['loci']:
  rows=tuple(tuple(F(x) for x in r) for r in raw)
  def forces(i,value):
   eq=[0]*5;eq[i]=2;eq[-1]=p[i]-value
   return s['extend'](rows,eq)==rows
  if any(forces(i,1) and forces(j,-1) for i in range(3) for j in range(3) if i!=j):counts['line']+=1
  elif any(all(forces(i,v) for i,v in enumerate(E)) for E in exceptions):counts['exception']+=1
  else:uncovered.append({'parity':p,'locus':raw})
assert not uncovered,uncovered
print('Every exact locus lies in the expected unknot families.',counts)
# Independently verify sufficiency at polynomial level; free-family all-p
# cancellation follows from x1*x2=1 and x1+x2=-(y+y^-1).
# At the all-odd parity sign is minus; with one even it is plus.
def poly(p,q,r):
 d={-1:1,0:2,1:1}
 def add(a,b):
  out=a.copy()
  for e,c in b.items():out[e]=out.get(e,0)+c
  return {e:c for e,c in out.items() if c}
 def mul(a,b):
  out={}
  for e,c in a.items():
   for f,v in b.items():out[e+f]=out.get(e+f,0)+c*v
  return {e:c for e,c in out.items() if c}
 xyz={-(p+q+r):(-1)**(p+q+r)}
 sumx={}
 for z in [p,q,r]:sumx=add(sumx,{-z:(-1)**z})
 dm1=add(d,{0:-1});dm2=add(d,{0:-2})
 return add(add(xyz,mul(dm1,sumx)),mul(dm1,dm2))
for p in range(-20,21):
 assert poly(p,1,-1)=={-p-1:(-1)**p,-p:2*(-1)**p,-p+1:(-1)**p}
for t in exceptions:
 E=poly(*t);assert len(E)==3
 lo=min(E);sgn=E[lo]
 assert abs(sgn)==1 and E=={lo:sgn,lo+1:2*sgn,lo+2:sgn}
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'All integer parameters, no twist bound; all solution loci contained in geometrically unknotted families','covered_loci':counts,'exceptional_triples':sorted(exceptions)},indent=2)+'\n')
