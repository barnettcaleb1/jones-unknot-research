from pathlib import Path
from collections import Counter,defaultdict
import json
import sys
import numpy as np
HERE=Path(__file__).resolve().parent
source=sys.argv[1] if len(sys.argv)>1 else 'transport_pairing_14.json'
tag='_exact' if 'exact_intersections' in source else ''
x=json.loads((HERE/source).read_text())
pts={};pointdata=[];rows=[]
for r in x['configurations']:
 ids=[]
 for k in (0,1):
  target=r['matching'] if k==0 else 1-r['matching']
  key=(k,target,r['source_parameters'][k],r['target_parameters'][k])
  if key not in pts:
   pts[key]=len(pts);pointdata.append({'source_arc':k,'target_loop':target,'source_parameter':key[2],'target_parameter':key[3],'position':r['positions'][k]})
  ids.append(pts[key])
 rows.append((r['index'],r['a'],r['b'],r['sign'],*ids))
arr=np.asarray(rows,dtype=np.int64)
np.savez_compressed(HERE/f'conventions_14{tag}_compact.npz',configuration_records=arr)
(HERE/f'conventions_14{tag}_points.json').write_text(json.dumps(pointdata,indent=2)+'\n')
del x
counts=Counter((a,b,sgn)for _,a,b,sgn,xi,yi in rows)
groups=defaultdict(Counter)
for(a,b,sgn),n in counts.items():groups[a-b,sgn][b]=n
fail=[];packets=0
for (d,sgn),bs in sorted(groups.items()):
 previous=0
 for b in range(min(bs),max(bs)+1):
  outgoing=bs.get(b,0)-previous
  if outgoing<0 or (b==max(bs)and outgoing):
   fail.append({'collapsed_degree':d,'polynomial_sign':sgn,'b':b,'count':bs.get(b,0),'incoming_required':previous,'outgoing':outgoing})
   break
  packets+=outgoing;previous=outgoing
# Necessary neighbor check for a partner preserving one of the two geometric intersections.
byx=defaultdict(list);byy=defaultdict(list)
for idx,a,b,sgn,xi,yi in rows:
 byx[a,b,sgn,xi].append(idx);byy[a,b,sgn,yi].append(idx)
missing=[]
for idx,a,b,sgn,xi,yi in rows:
 found=any(byx.get((a+k,b+k,sgn,xi))or byy.get((a+k,b+k,sgn,yi))for k in(-1,1))
 if not found:missing.append(idx)
# Pure opposite-sign equal-exponent cancellations, followed by h packets.
byex=defaultdict(lambda:{1:[],-1:[]})
for idx,a,b,sgn,xi,yi in rows:byex[a,b][sgn].append(idx)
ordinary=[];residual=[]
for(a,b),p in sorted(byex.items()):
 n=min(len(p[1]),len(p[-1]))
 ordinary.extend(zip(p[1][:n],p[-1][:n]))
 for sign in(1,-1):residual.extend((idx,a,b,sign)for idx in p[sign][n:])
residual.sort(key=lambda r:(r[3],r[1]-r[2],r[2]))
hpairs=[]
while residual:
 r=residual.pop(0)
 j=next((j for j,z in enumerate(residual)if z[3]==r[3] and abs(z[1]-r[1])==1 and z[1]-r[1]==z[2]-r[2]),None)
 if j is None:raise AssertionError(('unpaired residual',r,residual))
 z=residual.pop(j);hpairs.append([r,z])
D=[a-b for _,a,b,sgn,xi,yi in rows]
top_degree=max(D)
top=[r for r,d in zip(rows,D)if d==top_degree]
tops=Counter((r[2],r[3])for r in top)
summary={'configuration_count':len(rows),'unique_one_point_intersections':len(pts),'raw_collapsed_range':[min(D),max(D)],
 'raw_top_configuration_count':len(top),'raw_top_by_b_and_sign':[{'b':b,'sign':sgn,'count':n}for(b,sgn),n in sorted(tops.items())],
 'raw_top_specialized_sum':sum(r[3]*(-1)**r[2]for r in top),
 'all_points_direct_h_pairing_possible':not fail,'direct_h_pairing_failures':fail,
 'points_without_h_partner_sharing_one_intersection':len(missing),'first_missing_indices':missing[:20],
 'ordinary_equal_exponent_opposite_sign_pairs':len(ordinary),'remaining_h_packets':hpairs,
 'scope':'The algebraic pairing choices are NOT a geometric involution or separating-disk certificate. Failure of the simple h map is a genuine cardinality obstruction for this fixed representative. Compact NPZ rows are index,a,b,sign,source0intersectionID,source1intersectionID.'}
(HERE/f'conventions_partners{tag}.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
