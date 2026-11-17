"""Exact independent TL2 verification of all-odd pretzel moment identities.
Standard library only. Optional --diagrams checks actual links with Regina.
"""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
from random import Random
import sys,json
WORK=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WORK/'generic'))
from tangle_unit_check import ONE,ZERO,DELTA,pairmul,power_b,add,mul,shift

def bracket(params):
    v=(ONE,ZERO)
    for p in params: v=pairmul(v,power_b(-p)[::-1])
    return add(mul(DELTA,v[0]),v[1])
def jones_y(params):
    S=sum(params);b=bracket(params)
    assert all((e+3*S)%4==0 for e in b)
    return {(e+3*S)//4:-c for e,c in b.items()}
def moments(params):
    v=jones_y(params);n=len(params);g=(n-1)//2;S=sum(params)
    e2=sum(a*b for a,b in combinations(params,2))
    e3=sum(a*b*c for a,b,c in combinations(params,3))
    ms=[sum(c*e**k for e,c in v.items()) for k in range(4)]
    expected=[1,0,-F(3,2)*(e2+g),-F(9,4)*(e3+S*(e2+2*g))]
    assert ms==expected,(params,ms,expected,v)
    if ms[2]==ms[3]==0:
        assert v=={0:1},(params,v)
        q=params if S>0 else tuple(-p for p in params);S=abs(S)
        assert all(abs(p)<=S for p in q)
        assert sum((S-p)*(p*p-1)for p in q)==0
        assert all(p in(-1,1,S)for p in q)
        if S>1:assert sum(p==S for p in q)==1
        assert sorted(q)==sorted([S]+[1]*g+[-1]*g)
    return ms
count=0;zero=[]
for n in[1,3,5,7]:
 for p in product((-3,-1,1,3),repeat=n):
    ms=moments(p);count+=1
    if ms[2]==ms[3]==0:zero.append(p)
rng=Random(20261031)
for _ in range(200):
 n=rng.choice([3,5,7,9,11]);p=tuple(rng.choice(range(-15,16,2))for i in range(n))
 moments(p);count+=1
examples=[]
for p in[(3,3,-3,-1,-1),(3,5,-3,-1,-1),(7,1,-1,1,-1),(9,-1,1,-1,1,-1,1),(-3,-3,-3,1,7)]:
 v=jones_y(p);ms=moments(p)
 examples.append({'parameters':p,'Jones_y':v,'log_moments_0_through_3':ms})
result={'full_Laurent_TL2_checks':count,'zero_jet_grid_cases':len(zero),'grid_by_strand_count':[1,3,5,7],'grid_parameter_values':[-3,-1,1,3],'random_tests':200,'examples':examples}
if '--diagrams' in sys.argv:
 sys.path.insert(0,str(WORK/'braid_classification/packages'))
 from spherogram.links.tangles import RationalTangle
 import regina
 checks=[]
 for p in[(3,3,-3,-1,-1),(3,5,-3,-1,-1),(7,1,-1,1,-1),(9,-1,1,-1,1,-1,1),(-3,-3,-3,1,7)]:
    t=RationalTangle(1,p[0])
    for q in p[1:]:t=t+RationalTangle(1,q)
    l=t.numerator_closure();pd=l.PD_code()
    rr=regina.Link.fromPD([[e+1 for e in c]for c in pd]);pol=rr.jones()
    actual={e:int(str(pol[e]))for e in range(pol.minExp(),pol.maxExp()+1)if int(str(pol[e]))}
    expected={2*e:c for e,c in jones_y(p).items()}
    assert actual==expected or actual=={-e:c for e,c in expected.items()},(p,actual,expected)
    if jones_y(p)=={0:1}:
      l.simplify('global');assert len(l.crossings)==0 and len(l.link_components)+l.unlinked_unknot_components==1
    checks.append({'parameters':p,'PD':pd,'Regina_Jones':str(pol),'components':len(rr.components()) if hasattr(rr,'components') else 1,'crossings_after_simplification':len(l.crossings)})
 result['independent_Regina_diagrams']=checks
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k not in['examples','independent_Regina_diagrams']}))
