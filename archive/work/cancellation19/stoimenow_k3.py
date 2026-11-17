#!/usr/bin/env python3
"""Direct reconstruction of Stoimenow2005 Eq(10), p476, for n=3.
Crossing ports counterclockwise; ports0,2 are under,1,3 over.
Top horizontal bridge passes OVER each odd vertical strand and UNDER
 each even vertical strand. Encircled crossings are the even strands.
The latter convention was visually read from the original PDF pixels.
"""
import sys, json
from pathlib import Path
sys.path.insert(0,str(Path('work/braid_classification/packages').resolve()))
from spherogram import Link, Crossing
from spherogram.links.tangles import BraidTangle,join_strands
import regina
import spherogram

def build(flips=()):
 beta=[1,1,2,2,-1,-1,-2,-2]
 doubled=[]
 for j in beta:
  i=abs(j);s=1 if j>0 else -1
  doubled += [s*k for k in (2*i,2*i-1,2*i+1,2*i)]
 T=BraidTangle(doubled,6)
 B=T.adjacent[:6]; U=T.adjacent[6:]
 X=[];ports=[]
 for i in range(6):
  c=Crossing('clasp'+str(i));X.append(c)
  # geometrically: odd vertical strand under, even vertical over
  vert_over=(i%2==1)
  if i%2==1 and i//2 in flips:vert_over=not vert_over
  # ports S,E,N,W in counterclockwise order
  z=(1,2,3,0) if vert_over else (0,1,2,3)
  p={a:(c,b)for a,b in zip('SENW',z)};ports.append(p)
  join_strands(U[i],p['S'])
 for i in range(3):join_strands(ports[2*i]['N'],ports[2*i+1]['N'])
 for i in range(5):join_strands(ports[i]['E'],ports[i+1]['W'])
 join_strands(B[0],ports[0]['W']);join_strands(B[5],ports[5]['E'])
 for i in (1,3):join_strands(B[i],B[i+1])
 return Link(T.crossings+X)

def compute(flips):
 L=build(flips);pd=L.PD_code();comps=len(L.link_components);w=L.writhe()
 print('flips',flips,'crossings',len(pd),'components',comps,'writhe',w,flush=True)
 L.simplify(mode='global')
 R=regina.Link.fromPD([tuple(z+1 for z in c)for c in L.PD_code()]) if L.crossings else regina.Link(L.unlinked_unknot_components)
 if L.crossings:
  for _ in range(L.unlinked_unknot_components):R.insertLink(regina.Link(1))
 j=R.jones();coeff={e:int(str(j[e]))for e in range(j.minExp(),j.maxExp()+1)if int(str(j[e]))}
 out={'flips':flips,'initial_PD':pd,'components':comps,'writhe':w,'simplified_PD':L.PD_code(),'free_unknots':L.unlinked_unknot_components,'Jones_sqrt_t':str(j),'coefficients':coeff}
 print('simplified',len(L.crossings),'+free',L.unlinked_unknot_components,'Jones',j,flush=True)
 return out
if __name__=='__main__':
 rows=[compute([i for i in range(3)if m>>i&1])for m in range(8)]
 assert all(r['components']==1 for r in rows)
 assert all(r['simplified_PD']==[] and r['free_unknots']==1 for r in rows[1:])
 assert rows[0]['coefficients'] != {0:1}
 Path('work/cancellation19/stoimenow_versions.json').write_text(json.dumps({'python':sys.version,'spherogram':spherogram.__version__,'regina':regina.versionString()},indent=2))
 Path('work/cancellation19/stoimenow_k3.json').write_text(json.dumps(rows,indent=2))
