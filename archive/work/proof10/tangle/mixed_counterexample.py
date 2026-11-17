"""Actual mixed pretzel knot with zero order-two and order-three Jones jets."""
from pathlib import Path
import sys,json
WORK=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WORK/'braid_classification/packages'))
sys.path.insert(0,str(WORK/'generic'))
from tangle_unit_check import *
from spherogram.links.tangles import RationalTangle
import regina
out=[]
for params in[(8,-3,-3,1),(40,-15,-13,3)]:
 t=RationalTangle(1,params[0]);v=power_b(-params[0])[::-1]
 for p in params[1:]:t=t+RationalTangle(1,p);v=pairmul(v,power_b(-p)[::-1])
 l=t.numerator_closure();pd=l.PD_code();w=l.writhe()
 rr=regina.Link.fromPD([[x+1 for x in c]for c in pd]);V=rr.jones()
 coeff={e//2:int(str(V[e]))for e in range(V.minExp(),V.maxExp()+1)if int(str(V[e]))}
 assert all(e%2==0 for e in range(V.minExp(),V.maxExp()+1)if int(str(V[e])))
 logmom=[sum(c*e**k for e,c in coeff.items())for k in range(6)]
 deriv=[sum(c*__import__('math').prod(e-j for j in range(k))for e,c in coeff.items())for k in range(6)]
 assert logmom[:4]==[1,0,0,0] and deriv[:4]==[1,0,0,0]
 B=add(mul(DELTA,v[0]),v[1])
 # Standard TL-A normalized from actual writhe or its inverse convention.
 expected={3*w-4*e:c*(-1)**w for e,c in coeff.items()}
 assert B==expected or B=={-e:c for e,c in expected.items()}
 det=abs(sum(c*(1 if e%2==0 else -1) for e,c in coeff.items()))
 assert det>1 and len(coeff)>1
 if params[0]==8:
  l.simplify('global');simplified=l.PD_code()
 else:simplified=None
 out.append({'parameters':params,'PD_original':pd,'writhe_original':w,'Regina_Jones_in_sqrt_t':str(V),'Jones_t':coeff,'log_moments':logmom,'ordinary_derivatives':deriv,'determinant':det,'Jones_span':max(coeff)-min(coeff),'PD_after_simplification':simplified})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out:print({k:v for k,v in r.items()if k not in['PD_original','PD_after_simplification']})
