"""Actual diagram checks for the two top-twist sites; sole Jones-one closure."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
from spherogram.links.tangles import BraidTangle,Tangle,join_strands
import regina
BASE=[-2,1,1,1,-2,4,-5,-5,-5,4]
def diagram(p,q):
    word=BASE+[1 if p>0 else -1]*abs(p)+[5 if q>0 else -5]*abs(q)
    t=BraidTangle(word,6).copy();ends=t.adjacent.copy()
    join_strands(ends[2],ends[3]);join_strands(ends[8],ends[9])
    return Tangle((4,4),t.crossings,[ends[i]for i in [0,1,4,5,6,7,10,11]]).braid_closure()
rows=[]
for p,q in [(1,1),(3,1),(1,3),(-1,1),(3,-1),(-3,-5)]:
    L=diagram(p,q);pd=L.PD_code()
    R=regina.Link.fromPD([[x+1 for x in row]for row in pd])
    J=R.jones()
    signed_det=sum(int(str(J[e]))*(-1 if(e//2)%2 else 1)for e in range(J.minExp(),J.maxExp()+1)if e%2==0)
    expected=(-1 if((p+q)//2)%2 else 1)*(36+30*p-30*q-25*p*q)
    assert signed_det==expected and L.writhe()==p+q and R.countComponents()==1
    row={'p':p,'q':q,'PD_zero_based':pd,'Jones':str(J),'writhe':L.writhe(),
         'signed_Jones_at_minus_one':signed_det,'determinant_formula_matches':True}
    if(p,q)==(-1,1):
        R.simplify()
        row['Regina_final_crossings']=R.size();row['Regina_final_components']=R.countComponents()
        L.simplify('global')
        row['Spherogram_final_crossings']=len(L.crossings)
        row['Spherogram_final_components']=len(L.link_components)+L.unlinked_unknot_components
        assert R.size()==0 and R.countComponents()==1
        assert row['Spherogram_final_crossings']==0 and row['Spherogram_final_components']==1
    rows.append(row)
out={'diagram':'partial closure of BASE with top sigma1^p sigma5^q','rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps([{k:v for k,v in r.items()if k!='PD_zero_based'}for r in rows],indent=2))
