from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'braid_classification/packages'))
from spherogram import Link
import regina
out=[]
for a,b in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    word=[a,-1,b,1,1]
    L=Link(braid_closure=word)
    pd=L.PD_code()
    R=regina.Link.fromPD([[v+1 for v in c]for c in pd])
    V=R.jones()
    p={e:int(str(V[e])) for e in range(V.minExp(),V.maxExp()+1) if V[e]!=0}
    L.simplify('global')
    row={'virtual_signs':[a,b],'braid_word':word,'exponent':sum(word),'PD':pd,'Jones_Regina_x':p,'simplified_PD':L.PD_code(),'simplified_components':len(L.link_components)+L.unlinked_unknot_components}
    assert sum(word) in [-1,1,3]
    if sum(word) in [-1,1]:assert not L.crossings and row['simplified_components']==1 and p=={0:1}
    else:assert p!={0:1}
    out.append(row)
(HERE/'virtual_resolutions.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
