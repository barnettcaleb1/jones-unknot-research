"""Stdlib exact longitudinal-monotonicity certificate for marked virtual trefoil."""
from fractions import Fraction as Q
import json
from pathlib import Path
H=Path(__file__).resolve().parent
j=json.loads((H/'virtual_surface_states.json').read_text())[0]
PD=j['PD'];pos=[(Q(0),Q(0)),(Q(-1,2),Q(-19,30)),(Q(-1,2),Q(-11,30)),(Q(-5,8),Q(-1,2)),(Q(-1,4),Q(-13,60)),(Q(1,4),Q(13,60)),(Q(-3,8),Q(-1,2)),(Q(1,4),Q(-13,60)),(Q(-1,4),Q(13,60))]
occ={e:[]for e in range(6)}
for k,row in enumerate(PD):
 for p,e in enumerate(row):occ[e].append(4*k+p)
al={a:b for ds in occ.values()for a,b in [ds,ds[::-1]]}
cs=[{int(k):v for k,v in c.items()}for c in j['cohomology_basis']];vol={e:tuple(Q(c[e])for c in cs)for e in range(6)}
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
mul=lambda a,t:tuple(x*t for x in a)
d=0;g=(Q(0),Q(0));out=[]
while True:
 e=PD[d//4][d%4];sgn=1 if d<al[d]else-1
 a=add(pos[d//4],g);m=add(pos[3+e],g if sgn>0 else add(g,mul(vol[e],-1)))
 g=add(g,mul(vol[e],sgn));D=al[d];b=add(pos[D//4],g)
 assert a[1]>m[1]>b[1]
 out.append(tuple(str(z[1])for z in [a,m,b]));d=4*(D//4)+(D%4+2)%4
 if d==0:break
assert g==(0,-2)
print('Exact descending longitude waypoints:',out)
print('Total homology (0,-2); every meridional-axis embedding is a closed two-braid.')
# Exact degree-one orientation certificate for the flat marked torus embedding.
pos.extend([(Q(-1,2),Q(0)),(Q(0),Q(-1,2)),(Q(-1,2),Q(-1,2))])
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
det=lambda a,b:a[0]*b[1]-a[1]*b[0]
areas=[]
for f,face in enumerate(j['faces']):
 g=(Q(0),Q(0));F=pos[9+f]
 for d in face:
  e=PD[d//4][d%4];sgn=1 if d<al[d]else-1
  a=add(pos[d//4],g);m=add(pos[3+e],g if sgn>0 else add(g,mul(vol[e],-1)))
  g=add(g,mul(vol[e],sgn));b=add(pos[al[d]//4],g)
  areas.extend([det(sub(a,F),sub(m,F))/2,det(sub(m,F),sub(b,F))/2])
 assert g==(0,0)
assert len(areas)==24 and all(a<0 for a in areas) and sum(areas)==-1
print('Exact triangulation:24 nondegenerate, consistently oriented triangles; degree -1.')
