from pathlib import Path
import json,sys
sys.path.insert(0,str(Path('work/braid_classification/packages').resolve()))
from spherogram import Link,Crossing
from spherogram.links.tangles import BraidTangle,join_strands
import regina
BRIDGE=json.loads(Path('work/proof12/tangle/kt_bridge_data.json').read_text())
L=Link(BRIDGE['PD'])
from spherogram.links.links_base import CrossingStrand
edge_pass={}
for i,path in enumerate(L.overstrands()):
 for x in path:
  for j in [x.strand_index,(x.strand_index+2)%4]:
   cs=CrossingStrand(x.crossing,j);edge_pass[cs]=edge_pass[cs.opposite()]=i
selected=None
for face in L.faces():
 if len({edge_pass[c] for c in face if c in edge_pass})==3:
  selected=[];seen=set()
  for c in face:
   if c in edge_pass and edge_pass[c] not in seen:
    selected.append((c.crossing.label,c.strand_index));seen.add(edge_pass[c])
  break
assert selected is not None

def build(join_ids,twists={},perm=(2,1,0,3)):
 a=[Crossing(('A',i)) for i in range(len(L.crossings))]
 b=[Crossing(('B',i)) for i in range(len(L.crossings))]
 idx={c:i for i,c in enumerate(L.crossings)}
 for c in L.crossings:
  i=idx[c]
  for j in range(4):
   d,k=c.adjacent[j];h=idx[d]
   a[i][j]=a[h][k]
   # Reflection of planar cyclic order; crossing over/under parity is unchanged.
   b[i][-j%4]=b[h][-k%4]
 for s in join_ids:
  lab,j=selected[s];c=next(c for c in L.crossings if c.label==lab);i=idx[c]
  d,k=c.adjacent[j];h=idx[d]
  a[i][j]=b[i][-j%4];a[h][k]=b[h][-k%4]
 extra=[]
 for site,num in twists.items():
  assert site not in join_ids
  lab,j=selected[site];c=next(c for c in L.crossings if c.label==lab);i=idx[c]
  d,k=c.adjacent[j];h=idx[d]
  T=BraidTangle([1 if num>0 else -1]*abs(num),2)
  ports=[(a[i],j),(b[h],-k%4),(a[h],k),(b[i],-j%4)]
  for u,v in zip([ports[k] for k in perm],T.adjacent):join_strands(u,v)
  extra.extend(T.crossings)
 return Link(a+b+extra)
if __name__=="__main__":
 rows=[]
 
 for cut in [[],[1],[2],[1,2]]:
  Q=build([0]+cut)
  before=Q.PD_code();comps=len(Q.link_components)
  assert all(x==0 for row in Q.linking_matrix() for x in row)
  Q.simplify('global')
  print('cut',cut,'components',comps,'simplified',len(Q.crossings),'free',Q.unlinked_unknot_components)
  R=regina.Link.fromPD([tuple(v+1 for v in x) for x in Q.PD_code()]) if Q.crossings else regina.Link(Q.unlinked_unknot_components)
  # Spherogram may remove unlinked unknots alongside a nonempty diagram.
  for i in range(Q.unlinked_unknot_components if Q.crossings else 0):R.insertLink(regina.Link(1))
  print('Jones',R.jones())
  rows.append({'cut_bands':cut,'initial_PD':before,'components':comps,'simplified_PD':Q.PD_code(),'free_unknot_components':Q.unlinked_unknot_components,'jones':str(R.jones()),'jones_coefficients':{e:int(str(R.jones()[e])) for e in range(R.jones().minExp(),R.jones().maxExp()+1) if R.jones()[e]}})
 Path(__file__).with_suffix('.json').write_text(json.dumps({'selected_edges':selected,'rows':rows},indent=2))
