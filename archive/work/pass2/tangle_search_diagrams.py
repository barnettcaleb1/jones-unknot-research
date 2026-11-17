from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'braid_classification/packages'))
import regina
from spherogram.links.tangles import RationalTangle
p=Path(__file__).with_name('tangle_search_hits.json');data=json.loads(p.read_text())
T=RationalTangle(-1)+RationalTangle(1,2)+RationalTangle(1,3)
seeds=[T,T.rotate(1),-T,(-T).rotate(1)]
def build(ex):
    op=ex[0]
    if op=='s':return seeds[ex[1]].copy()
    if op=='b':return RationalTangle(ex[1])
    if op=='r':return build(ex[1]).rotate(1)
    return build(ex[1])+build(ex[2])
for h in data['hits']:
    t=build(h['expression'])
    L=t.numerator_closure() if h['closure']=='N' else t.denominator_closure()
    pd=L.PD_code();r=regina.Link.fromPD([[x+1 for x in row] for row in pd])
    h['PD_zero_based']=pd;h['components']=r.countComponents();h['crossings']=r.size();h['jones']=str(r.jones())
    r.simplify();h['simplified_crossings']=r.size();h['simplified_components']=r.countComponents()
    print(h['i'],h['seeds'],h['crossings'],h['jones'],'->',r.size(),flush=True)
p.write_text(json.dumps(data,indent=2))
