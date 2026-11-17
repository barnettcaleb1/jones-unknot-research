from itertools import permutations
from pathlib import Path
import json, runpy, contextlib, io
out=Path(__file__).parent
same_edges=[(i,j) for i in range(7) for j in range(i+1,7) if (i<4)==(j<4)]
opp_edges=[(i,j) for i in range(4) for j in range(4,7)]
edge_index={e:k for k,e in enumerate(same_edges)}
actions=[]
for p in permutations(range(4)):
 for q in permutations(range(4,7)):
  perm=p+q
  actions.append(tuple(edge_index[tuple(sorted((perm[i],perm[j])))] for i,j in same_edges))
seen=set();reps=[]
for positions in permutations(range(9),5):
 v=[0]*9
 for pos,val in zip(positions,(2,5,6,9,11)):v[pos]=val
 v=tuple(v)
 if v in seen:continue
 orbit={tuple(v[k] for k in action) for action in actions}
 assert len(orbit)<=144
 seen.update(orbit);reps.append(min(orbit))
assert len(seen)==15120
with contextlib.redirect_stdout(io.StringIO()):f=runpy.run_path('work/bio7/quiver_candidate.py')
E=f['add']({0:1},f['shift'](f['habiro_factor'](4,2),3))
D={0:1}
for n in (1,2,3,5,6,7):D=f['mul'](D,{0:1,n:-1})
(out/'config.json').write_text(json.dumps({'reps':reps,'same_edges':same_edges,'opp_edges':opp_edges,'expected_H4':E,'divisor':D},indent=2)+'\n')
arr=lambda a:'{'+','.join(str(v) for v in a)+'}'
lines=['const int NR='+str(len(reps))+';', 'int reps[NR][9]={'+','.join(arr(r) for r in reps)+'};', 'int se[9][2]={'+','.join(arr(e) for e in same_edges)+'};','int oe[12][2]={'+','.join(arr(e) for e in opp_edges)+'};', 'long long expect[40]='+arr([E.get(i-2,0) for i in range(40)])+';', 'long long divisor[25]='+arr([D.get(i,0) for i in range(25)])+';']
(out/'config.h').write_text('\n'.join(lines)+'\n')
print({'same_representatives':len(reps),'same_orbit_total':len(seen),'total_assignments':len(reps)*166320,'expected_derivatives':[sum(c*__import__('math').prod(range(e-k+1,e+1)) for e,c in E.items()) for k in range(6)]})
