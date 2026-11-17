"""Independent TL2 and geometric audit of the parent's complete 3-pretzel locus."""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
import sys,json
WORK=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WORK/'generic'))
from tangle_unit_check import add,mul,shift,pairmul,power_b,DELTA,ONE,ZERO
D=mul(DELTA,DELTA);D1=add(D,{0:-1});D2=add(D,{0:-2})
def bracket(params):
 v=(ONE,ZERO)
 for p in params:v=pairmul(v,power_b(-p)[::-1])
 return add(mul(DELTA,v[0]),v[1])
def formula_numerator(params):
 xyz=shift(ONE,-4*sum(params),(-1)**sum(params))
 sm=ZERO
 for p in params:sm=add(sm,shift(ONE,-4*p,(-1)**p))
 return shift(add(add(xyz,mul(D1,sm)),mul(D1,D2)),sum(params))
def expected(p):
 return (1 in p and -1 in p) or sorted(p) in [sorted(z) for z in[(0,1,1),(0,-1,-1),(1,-2,-3),(-1,2,3)]]
count=0;monomial=[]
for p in product(range(-6,7),repeat=3):
 b=bracket(p);assert mul(D,b)==formula_numerator(p)
 unit=len(b)==1 and abs(next(iter(b.values())))==1
 assert unit==expected(p),(p,b)
 count+=1
 if unit:monomial.append(p)
# Audit EVERY solver leaf, including its free integer parameter.
raw=json.loads((WORK/'proof9/toric/pretzel_unit_locus.json').read_text())
points=set();families=0
for item in raw['results']:
 parity=item['parity']
 for rows0 in item['loci']:
  rows=[list(map(Q,r)) for r in rows0]
  if len(rows)==4:
   vals=[None]*4
   for r in rows:
    pivot=next(i for i in range(4) if r[i]);assert r[pivot]==1
    assert all(not r[i] for i in range(4) if i!=pivot)
    vals[pivot]=-r[-1]
   assert all(v.denominator==1 for v in vals)
   p=tuple(parity[i]+2*int(vals[i]) for i in range(3));assert expected(p)
   points.add(p)
  elif len(rows)==3:
   # The sole free variable is m; express p,q,r as affine functions of m.
   aff=[None]*3
   for r in rows:
    pivot=next(i for i in range(4) if r[i]);assert pivot<3
    assert r[pivot]==1 and all(not r[i] for i in range(3) if i!=pivot)
    aff[pivot]=(-2*r[3],parity[pivot]-2*r[4])
   assert sorted(aff)==sorted([(Q(-1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1))])
   # The half-integral coordinate simply restricts m to the required parity;
   # the resulting free pretzel parameter ranges over that parity class.
   families+=1
  else:raise AssertionError(rows)
sys.path.insert(0,str(WORK/'braid_classification/packages'))
from spherogram.links.tangles import RationalTangle
geometric=[]
for p in [(1,-2,-3),(-1,2,3),(0,1,1),(0,-1,-1)]+[(k,1,-1) for k in[-5,-2,0,3,8]]:
 t=RationalTangle(1,p[0])+RationalTangle(1,p[1])+RationalTangle(1,p[2])
 l=t.numerator_closure();original=l.PD_code();l.simplify('global')
 assert len(l.crossings)==0 and len(l.link_components)+l.unlinked_unknot_components==1
 geometric.append({'parameters':p,'PD_original':original,'crossings_after_Reidemeister_simplification':0,'components':1})
out={'formula_checks':count,'grid_unit_count':len(monomial),'all_solver_leaves_audited':sum(len(r['loci']) for r in raw['results']),'rank_three_families':families,'distinct_point_triples':sorted(points),'actual_unknot_geometry':geometric}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['distinct_point_triples','actual_unknot_geometry']}))
