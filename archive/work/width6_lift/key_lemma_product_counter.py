"""Product-cycle zero without disjoint arc systems, with no closed component."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
import lift_pairing as lp
sys.path.insert(0,str(HERE.parent/'width6'))
import probe
from central_arc_artin import action,inv
beta=[2,1,1,1,1,-2]
a=beta+[2]+inv(beta);b=[1]
left=action(a+b+a);right=action(b+a+b)
p=lp.pairing(beta,7,2)
assert not p and not probe.coefficient(beta,7,2)
assert probe.geometry(beta,7,2)['closed_components']==0
assert left!=right
out={'word':beta,'top_state':7,'bottom_state':2,'Lreg':lp.encode(p),
 'Jones_coefficient':probe.coefficient(beta,7,2),'geometry':probe.geometry(beta,7,2),
 'arc_half_twist':a,'test_half_twist':b,'aba_images':left,'bab_images':right,
 'braid_relation_holds':False,
 'reason':'If alpha=beta(arc23) and arc12 had disjoint interiors, their half twists sharing endpoint2 would satisfy the braid relation. The Artin images differ.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Product pairing zero; no closed components; arc-disjointness test fails.')
