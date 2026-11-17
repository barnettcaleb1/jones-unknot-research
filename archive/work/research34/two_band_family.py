"""Two fixed disjoint face bands on the ORIGINAL EKT LLL(1) diagram.
No simplification, orientation rebuild, or relabelling occurs between bands.
Parameter m,n counts full twists, i.e. 2m,2n local half twists.
"""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'braid_classification/packages'))
from spherogram import Link,Crossing
from spherogram.links.tangles import join_strands
from spherogram.links.links_base import CrossingStrand
from spherogram.links.bands.core import normalize_crossing_labels
import regina
BASE_PD=[[30,36,31,35],[36,32,37,31],[34,21,35,22],[22,37,23,34],[20,30,21,29],[32,20,33,19],[18,23,19,24],[24,17,25,18],[16,13,17,0],[25,13,26,12],[15,6,16,7],[26,6,27,5],[4,28,5,27],[11,29,12,28],[3,14,4,15],[10,33,11,14],[9,2,10,3],[1,8,2,9],[7,0,8,1]]
SITES=[[(17,1),(5,3)],[(9,3),(3,3)]]

def base():
    L=Link(BASE_PD);normalize_crossing_labels(L);return L

def insert_face_band_unrebuilt(L,site,twists):
    (c,s),(d,t)=site
    X=(L.crossings[c],s); Z=(L.crossings[d],t)
    Y=L.crossings[c].adjacent[s];W=L.crossings[d].adjacent[t]
    upper,lower=X,Y
    E=[Crossing(len(L.crossings)+i) for i in range(abs(twists))]
    for C in E:
        if twists>=0:
            join_strands(upper,(C,3));join_strands(lower,(C,0))
            upper,lower=(C,2),(C,1)
        else:
            join_strands(upper,(C,2));join_strands(lower,(C,3))
            upper,lower=(C,1),(C,0)
    join_strands(upper,Z);join_strands(lower,W)
    L.crossings.extend(E)

def family(m=0,n=0,active=(True,True)):
    L=base()
    for site,k,on in zip(SITES,[m,n],active):
        if on:insert_face_band_unrebuilt(L,site,2*k)
    # Rebuild ONLY AFTER both original rectangles have been applied.
    L._rebuild();assert L.is_planar()
    return L

def record(L,**kw):
    pd=L.PD_code();R=regina.Link.fromPD([[x+1 for x in c]for c in pd]);V=R.jones()
    coefficients={e:int(str(V[e]))for e in range(V.minExp(),V.maxExp()+1)if V[e]!=0}
    data={**kw,'PD':pd,'Jones_Regina':str(V),'Jones_x_coefficients':coefficients,'writhe':L.writhe(),
          'components':len(L.link_components)+L.unlinked_unknot_components}
    L.simplify('global')
    data.update(simplified_PD=L.PD_code(),simplified_crossings=len(L.crossings),
                simplified_components=len(L.link_components)+L.unlinked_unknot_components)
    return data

def main():
    B=base();faces=B.faces();site_faces=[];edge_sets=[]
    for site in SITES:
        (c,s),(d,t)=site
        X=CrossingStrand(B.crossings[c],s);Z=CrossingStrand(B.crossings[d],t)
        f=[i for i,F in enumerate(faces)if X in F and Z.opposite()in F]
        assert len(f)==1;site_faces.append(f[0]);edge_sets.append({X.strand_label(),Z.strand_label()})
    assert site_faces==[2,10] and edge_sets[0].isdisjoint(edge_sets[1])
    corners=[record(family(m,n),m=m,n=n)for m,n in [(0,0),(1,0),(0,1),(1,1),(1,-1)]]
    cuts=[record(family(active=a),active_bands=a)for a in [(False,False),(True,False),(False,True)]]
    assert corners[0]['Jones_Regina']=='1' and corners[0]['simplified_crossings']==0 and corners[0]['simplified_components']==1
    assert all(r['components']==1 for r in corners)
    prior=json.loads((HERE.parent/'research33/two_band_test.json').read_text())
    assert [list(c)for c in corners[0]['PD']]==prior['hits'][5]['pd']
    out={'base_PD':BASE_PD,'original_band_sites':SITES,'original_face_indices':site_faces,
         'original_attaching_edge_labels':[sorted(a)for a in edge_sets],
         'twist_convention':'m,n full twists, inserted as 2m,2n half twists; no intermediate rebuild',
         'prior_unknot_hit':5,'corners':corners,'cuts':cuts}
    (HERE/'two_band_family.json').write_text(json.dumps(out,indent=2)+'\n')
    for r in corners:print(r['m'],r['n'],r['Jones_Regina'],'w=',r['writhe'],'simplified=',r['simplified_crossings'])
    for r in cuts:print('cut',r['active_bands'],r['Jones_Regina'],'w=',r['writhe'])
if __name__=='__main__':main()
