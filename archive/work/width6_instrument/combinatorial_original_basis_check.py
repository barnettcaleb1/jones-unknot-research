"""Check effective transported seed entries against the ORIGINAL nine cap lifts.
This algebraic identification is independent of the rational geometry run.
"""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_lift'))
sys.path.insert(0,str(HERE.parent/'width6_targeted'))
import lift_pairing as lp
from lp_completions import divide_one_minus_t


def run():
    source=json.loads((HERE/'full_gram_calibration.json').read_text())
    ks={r['target']:int(next(iter(r['unit'])))for r in lp.TRANSPORT}
    out=[]
    for x in source:
        i,j=x['i'],x['j']
        orig=lp.shift(divide_one_minus_t(lp.pairing([],i,j)),-4)
        seed={(2*a,b):c for a,b,c in x['expected_Phi']}
        assert orig==lp.shift(seed,ks[j]-ks[i]),(i,j)
        u=x['deck_unit']
        actual={(2*a,b):c for a,b,c in x['polynomial']}
        sshift=2*u.get('q',0)+ks[i]-ks[j]
        assert actual==lp.shift(orig,sshift,u.get('t',0),u.get('sign',1)), (i,j)
        out.append({'i':i,'j':j,'original_Phi':lp.encode(orig),
                    'transport_unit_i':ks[i],'transport_unit_j':ks[j],
                    'original_equals_s_shift_times_effective_seed':ks[j]-ks[i],
                    'geometry_unit_relative_to_original':{'s':sshift,'t':u.get('t',0),'sign':u.get('sign',1)},
                    'exact_original_Gram_identification':True})
    result={'status':'PASS_ALL_81','formula':'Phi_original(i,j)=s^(k_j-k_i) Phi_effective_seed',
            'entries':out}
    (HERE/'combinatorial_original_basis81.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS all 81 original cap identifications')
    exactpath=HERE/'combinatorial_exact_basis81.json'
    if exactpath.exists():
        exact=json.loads(exactpath.read_text())
        for e in exact['entries']:
            x=out[9*e['i']+e['j']]
            e['exact_original_Gram_identification']=True
            e['unit_relative_to_original_cap_Phi']=x['geometry_unit_relative_to_original']
        # Only amend after the running geometry process has completed.
        if exact['status']=='PASS_ALL_81':
            exact['original_cap_identification']='All 81 directly checked against lp.pairing([],i,j)'
            exactpath.write_text(json.dumps(exact,indent=2)+'\n')
    return result

if __name__=='__main__':run()
