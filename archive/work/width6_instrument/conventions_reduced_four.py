from pathlib import Path
from fractions import Fraction as F
import json
from transport_exact_intersections import figure8
import combinatorial_winding as cw
HERE=Path(__file__).resolve().parent
x=json.loads((HERE/'transport_simplified_pairing_14.json').read_text())
source=[[tuple(F(v)for v in p)for p in c]for c in x['source_curves']]
target=[figure8(1,2),figure8(3,4)]
ints=x['one_point_intersections']
recs=x['records']
def at(c,t):
 k=min(int(t),len(c)-2);u=t-k
 return tuple(c[k][j]+u*(c[k+1][j]-c[k][j])for j in(0,1))
def path(c,start,end):
 if start>end:return list(reversed(path(c,end,start)))
 return [at(c,start)]+[c[k]for k in range(int(start)+1,int(end)+1)if start<k<end]+[at(c,end)]
def info(i):
 m,xi,yi,*_=recs[i];p=[ints[0][m][xi],ints[1][1-m][yi]]
 return m,p

def pairloop(i,j):
 sm,sp=info(i);em,ep=info(j)
 starts=[None,None];ends=[None,None]
 for k in(0,1):
  starts[sm if k==0 else 1-sm]=F(sp[k]['target_parameter'])
  ends[em if k==0 else 1-em]=F(ep[k]['target_parameter'])
 current=[at(target[k],starts[k])for k in(0,1)];out=[tuple(current)]
 for k in(0,1):
  for z in path(target[k],starts[k],ends[k])[1:]:
   current[k]=z;out.append(tuple(current))
 for k in(0,1):
  label=em if k==0 else 1-em
  for z in path(source[k],F(ep[k]['source_parameter']),F(sp[k]['source_parameter']))[1:]:
   current[label]=z;out.append(tuple(current))
 assert sorted(out[0])==sorted(out[-1])
 mon=cw.configuration_monodromy(out)
 winds=[sum(cw.ray_segment_count(previous[k],current[k],(F(p),F(0)))for previous,current in zip(out,out[1:])for k in(0,1))for p in range(1,7)]
 return {'record_pair':[i,j],'monodromy':list(mon),'puncture_windings_1_to_6':winds,'swaps_point_labels':out[0]!=out[-1],
         'path_vertices':[[[str(v)for v in p]for p in conf]for conf in out]}
out={'records':recs,'h_partners':[pairloop(0,2),pairloop(1,3)],
 'same_matching_pairs':[pairloop(0,1),pairloop(2,3)],
 'interpretation':'Actual reduced point involution is0<->2,1<->3: each pair has equal raw sign and monodromy(1,1). Pair0<->1 uses two traversals of the same physical target1 connector point, but differs by one clockwise circuit of puncture4, so it does not itself cancel. Pair2<->3 uses two source0 crossings of target1 puncture4 lobe and has the same puncture4 monodromy. This describes the actual paths and local-system monodromy, not a separating-disk-induced map.'}
(HERE/'conventions_reduced_four.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:[{kk:vv for kk,vv in r.items()if kk!='path_vertices'}for r in v] if k in('h_partners','same_matching_pairs')else v for k,v in out.items()},indent=2))
