"""Actual knot check of the geometric a2 obstruction; no quotient diagrams assumed."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/braid_classification/packages'))
from spherogram import Link
import regina
out=[]
for name in ['3_1','4_1','6_1','8_20','9_42','9_46']:
    L=Link(name); pd=L.PD_code(); V=regina.Link.fromPD([[x+1 for x in c] for c in pd]).jones()
    coeff={e//2:int(str(V[e])) for e in range(V.minExp(),V.maxExp()+1) if int(str(V[e]))}
    assert all(e%2==0 for e in range(V.minExp(),V.maxExp()+1) if int(str(V[e])))
    second=sum(c*e*(e-1) for e,c in coeff.items())
    assert second%6==0
    out.append({'knot':name,'PD':pd,'Jones_t':coeff,'V_second_at_1':second,'a2':-second//6})
assert [r['a2'] for r in out[:2]]==[1,-1]
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out: print(r['knot'],'a2=',r['a2'],'Jones=',r['Jones_t'])
