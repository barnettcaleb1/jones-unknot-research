from pathlib import Path
import numpy as np,json
from collections import defaultdict
HERE=Path(__file__).resolve().parent
rows=np.load(HERE/'conventions_14_exact_compact.npz')['configuration_records']
points=json.loads((HERE/'conventions_14_exact_points.json').read_text())
top=rows[rows[:,1]-rows[:,2]==1]
# Pair one moving source coordinate, with the other configuration point fixed.
lookup=defaultdict(list)
for r in top:
 for k in(0,1):lookup[k,int(r[5-k]),int(r[1]),int(r[2]),int(r[3])].append(r)
# Adjacent points along target among BOTH source arcs: this excludes intrusion
# from the fixed source arc through the proposed target edge.
by_target=defaultdict(list)
for i,p in enumerate(points):by_target[p['target_loop']].append((p['target_parameter'],i))
tadj=set()
for target,ps in by_target.items():
 ps.sort()
 for (_,i),(_,j) in zip(ps,ps[1:]):tadj.add(frozenset((i,j)))
candidates=[]
for r in top:
 if r[3]!=1:continue
 for k in(0,1):
  i=int(r[4+k]);p=points[i]
  for s in lookup[k,int(r[5-k]),int(r[1]),int(r[2]),-1]:
   j=int(s[4+k]);q=points[j]
   if frozenset((i,j))not in tadj:continue
   if int(p['target_parameter'])==int(q['target_parameter']):
    candidates.append({'positive':r.tolist(),'negative':s.tolist(),'moving_source':k,'point_ids':[i,j],
     'target_loop':p['target_loop'],'target_segment':int(p['target_parameter']),
     'source_span':abs(q['source_parameter']-p['source_parameter']),
     'target_span':abs(q['target_parameter']-p['target_parameter']),
     'point_data':[p,q]})
candidates.sort(key=lambda c:(c['source_span'],c['target_span']))
(HERE/'conventions_local_bigon_candidates.json').write_text(json.dumps(candidates[:20],indent=2)+'\n')
print('candidates',len(candidates));print(json.dumps(candidates[:2],indent=2))
