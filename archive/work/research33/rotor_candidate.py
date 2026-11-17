from pathlib import Path
import sys,json
W=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(W/'braid_classification/packages'))
from spherogram import Link, Crossing, Strand
from spherogram.links.tangles import RationalTangle,BraidTangle,Tangle,join_strands
import regina

def physical_flip(t):
    # 180-degree rotation about the in-plane radial axis: left/right reflection
    # AND over/under exchange. Reversing crossing cyclic order while swapping
    # its parity is i -> 1-i mod4. This is a spatial rotation, not a mirror.
    objects={c:(Crossing(c.label) if isinstance(c,Crossing) else Strand(c.label)) for c in t.crossings}
    def port(c,i): return (objects[c],(1-i)%(4 if isinstance(c,Crossing) else 2))
    for c in t.crossings:
        for i,(d,j) in enumerate(c.adjacent):
            if d is not t: join_strands(port(c,i),port(d,j))
    return Tangle(2,list(objects.values()),[port(*t.adjacent[i]) for i in [1,0,3,2]])

def seed(flip=False):
    t=RationalTangle(-1)+RationalTangle(1,2)+RationalTangle(1,3)
    return physical_flip(t) if flip else t

def diagram(flip=False,power=0):
    T=[seed(flip) for _ in range(4)]
    cs=sum([t.crossings for t in T],[])
    # In each radially oriented sector: 0,1 inward; 2,3 outward.
    # The inward pair connection goes clockwise around the central face.
    for i in range(4): join_strands(T[i].adjacent[1],T[(i+1)%4].adjacent[0])
    ports=sum([t.adjacent[2:] for t in T],[])
    if power:
        B=BraidTangle([2]*(power) if power>0 else [-2]*(-power),n=8)
        cs+=B.crossings
        for i in range(8):join_strands(ports[i],B.adjacent[i])
        ports=B.adjacent[8:]
    for i in range(0,8,2):join_strands(ports[i],ports[i+1])
    return Link(cs,check_planarity=True)

records=[]
for power in [0,2,-2]:
    for flip in [False,True]:
        L=diagram(flip,power)
        pd=L.PD_code()
        R=regina.Link.fromPD([[x+1 for x in c] for c in pd])
        result={'outside_braid_sigma2_power':power,'flipped':flip,'PD':pd,'crossings':len(L.crossings),'Jones_Regina':str(R.jones()),'components':len(L.link_components)+L.unlinked_unknot_components}
        L.simplify('global')
        result.update({'simplified_PD':L.PD_code(),'simplified_crossings':len(L.crossings),'simplified_components':len(L.link_components)+L.unlinked_unknot_components})
        records.append(result)
        print(power,flip,result['Jones_Regina'],result['simplified_crossings'],result['simplified_components'])
assert all(r['components']==r['simplified_components']==1 for r in records)
assert all(r['Jones_Regina']=='1' and r['simplified_crossings']==0 for r in records[:2])
for i in [0,2,4]: assert records[i]['Jones_Regina']==records[i+1]['Jones_Regina']
assert all(r['Jones_Regina']!='1' for r in records[2:])
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
