"""A genuine unknot with silent single-site switches and a trefoil double switch."""
import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/attack_search'))
from search import jones_a
sys.path.insert(0,str(ROOT/'work/braid_classification/packages'))
from spherogram import Link
word=[1,2,1,-2,-1,-2,1,2]
records=[]
for switches in [[],[0],[2],[0,2]]:
    w=word[:]
    for i in switches:w[i]*=-1
    L=Link(braid_closure=w)
    original=L.PD_code()
    L.simplify('global')
    records.append({'switches':switches,'word':w,'Jones_A':jones_a(w,3),
                    'PD_original':original,'PD_simplified':L.PD_code(),
                    'remaining_crossings':len(L.crossings),
                    'components':len(L.link_components)+L.unlinked_unknot_components})
assert [r['remaining_crossings'] for r in records]==[0,0,0,3]
assert all(r['components']==1 for r in records)
assert [r['Jones_A'] for r in records[:3]]==[{0:1}]*3
assert records[3]['Jones_A']=={4:1,12:1,16:-1}
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
print('Verified actual unknot, unknot, unknot, trefoil under the four interventions.')
