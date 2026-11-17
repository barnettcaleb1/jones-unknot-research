"""Explicit nonrational point on the width-six actual-unknot-closure locus."""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6'))
sys.path.insert(0,str(HERE.parent/'braid_classification/packages'))
import probe as p
import regina
SEED_SHORT=[-2,-2,4,4,4]
CAP_TRANSPORT=[2,3,4,5,1,2,3,4]
BETA=p.reduce(list(reversed(CAP_TRANSPORT))+SEED_SHORT)
def main():
    closures=p.closure_checks(SEED_SHORT,0,7)
    standard=p.closure_checks(BETA,7,7)
    assert closures['denominator_closure']['unknot_certified']
    assert standard['denominator_closure']['unknot_certified']
    f=p.coefficient(BETA,7,7)
    assert f=={5:-1,1:2,-3:-2,-7:1}
    L=p.tangle(SEED_SHORT,0,7).numerator_closure()
    factors=[]
    for factor in L.deconnect_sum():
        pd=factor.PD_code();R=regina.Link.fromPD([[x+1 for x in row]for row in pd])
        if factor.unlinked_unknot_components:R.insertLink(regina.Link(factor.unlinked_unknot_components))
        factors.append({'PD':pd,'components':R.countComponents(),'crossings':R.size(),'Jones':str(R.jones())})
    assert sorted((f['crossings'],f['components'])for f in factors)==[(2,2),(3,1)]
    out={'status':'TRUSTED','short_braid':SEED_SHORT,'short_cap_states':[0,7],
         'cap_transport':CAP_TRANSPORT,'standard_C0_braid':BETA,'coefficient':f,
         'short_closures':closures,'standard_closures':standard,'N_connected_sum_factors':factors,
         'geometry':'N is the component-connected sum of a trefoil and Hopf link. Its branched cover is a nontrivial lens-space connected sum, so N is not2bridge. Thus X is nonrational and has minimal width6 in the cap/cup ladder; D is nevertheless the actualunknot.'}
    (HERE/'hilden_anchor.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k]for k in ['standard_C0_braid','coefficient','N_connected_sum_factors']},indent=2))
if __name__=='__main__':main()
