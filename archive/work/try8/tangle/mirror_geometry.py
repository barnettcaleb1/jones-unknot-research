"""Certify actual knot types in a proposed mirrored framing repair."""
from pathlib import Path
import sys,json
WORK=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WORK/'braid_classification/packages'))
from spherogram.links.tangles import RationalTangle
from spherogram import Link
import regina
X=RationalTangle(-1)+RationalTangle(1,2)+RationalTangle(1,3)
R=RationalTangle(1,4)
records=[]
for name,t in [('X',X),('R',R)]:
    s=t*(-t)
    for j in [0,1]:
        l=(s+RationalTangle(j)).numerator_closure()
        original=l.PD_code();wr=l.writhe()
        rr=regina.Link.fromPD([[v+1 for v in c] for c in original])
        jones=str(rr.jones())
        l.simplify('global')
        records.append({'tangle':name,'operation':'vertical product with mirror','probe':j,'PD_original':original,'writhe_original':wr,'Jones_Regina':jones,'PD_simplified':l.PD_code(),'remaining_crossings':len(l.crossings),'components':len(l.link_components)+l.unlinked_unknot_components})
assert [r['remaining_crossings'] for r in records]==[0,10,0,0]
assert all(r['components']==1 for r in records)
table=Link('10_153').PD_code()
assert set(map(tuple,records[1]['PD_simplified']))==set(map(tuple,table))
records[1]['knot']='10_153'
records[1]['identification']='Exact equality of reduced PD crossing sets with the standard table diagram; not identification from Jones alone.'
records[1]['table_PD']=table
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
print('Actual closures: X-mirror product gives U and 10_153; rational-mirror product gives U and U.')
