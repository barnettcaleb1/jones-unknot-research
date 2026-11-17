from pathlib import Path
import sys,json,math,argparse
from fractions import Fraction
parser=argparse.ArgumentParser();parser.add_argument("--matrix",nargs=4,type=int,default=[1,0,0,1]);parser.add_argument("--samples",type=int,default=21);parser.add_argument("--out",default="torus_embedding.json");args=parser.parse_args()
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'braid_classification/packages'))
import numpy as np
from spherogram import Link
import regina
j=json.loads((HERE/'virtual_surface_states.json').read_text())[0]; PD=j['PD']; n=3
occ={e:[]for e in range(6)}
for i,row in enumerate(PD):
 for p,e in enumerate(row):occ[e].append(4*i+p)
alpha={a:b for ds in occ.values()for a,b in [ds,ds[::-1]]}
cs=[{int(k):v for k,v in c.items()}for c in j['cohomology_basis']]
vol={e:np.array([c[e]for c in cs],dtype=float)for e in occ}
sgn=lambda d:1 if d<alpha[d] else -1
edge=lambda d:PD[d//4][d%4]
# Barycentric triangulation: original V=0..2, edge midpoint=3..8, face center=9..11.
es=[]
for e,(d,D)in occ.items():es.extend([(d//4,3+e,np.zeros(2)),(3+e,D//4,vol[e])])
tri=[]
for f,path in enumerate(j['faces']):
 g=np.zeros(2)
 for d in path:
  e=edge(d);midg=g+(np.zeros(2) if sgn(d)>0 else -vol[e]);endg=g+sgn(d)*vol[e]
  es.extend([(9+f,d//4,g.copy()),(9+f,3+e,midg.copy())])
  tri.extend([(9+f,d//4,3+e,np.zeros(2),g.copy(),midg.copy()),(9+f,3+e,alpha[d]//4,np.zeros(2),midg.copy(),endg.copy())])
  g=endg
 assert np.max(np.abs(g))==0
N=12;mat=np.zeros((N,N));rhs=np.zeros((N,2))
for a,b,v in es:mat[a,a]+=1;mat[b,b]+=1;mat[a,b]-=1;mat[b,a]-=1;rhs[a]+=v;rhs[b]-=v
mat[0]=0;mat[0,0]=1;rhs[0]=0
pos=np.linalg.solve(mat,rhs)
areas=[]
for a,b,c,x,y,z in tri:
 u=pos[b]+y-pos[a]-x;v=pos[c]+z-pos[a]-x;areas.append(float(np.linalg.det(np.array([u,v])))/2)
print('triangle signed areas',min(areas),max(areas),sum(areas),flush=True)
assert min(areas)>1e-8 or max(areas)<-1e-8
# Finite straight triangulation realizes torus graph. Verify crossing rotations.
for k in range(3):
 ang=[]
 for p in range(4):
  d=4*k+p;e=edge(d);v=pos[3+e]-(vol[e] if sgn(d)<0 else 0)-pos[k]
  ang.append(math.atan2(v[1],v[0]))
 order=sorted(range(4),key=lambda p:ang[p]);print('rotation',k,order,flush=True)
 assert order in [[(s+r)%4 for r in range(4)]for s in range(4)]
# Knot traversal using opposite ports; each vertex crossing has under ports0,2.
path=[];d=0;g=np.zeros(2);start=d
while True:
 e=edge(d);mid=pos[3+e]+g-(vol[e] if sgn(d)<0 else 0);beg=pos[d//4]+g
 g2=g+sgn(d)*vol[e];D=alpha[d];end=pos[D//4]+g2
 # Trim crossing neighborhoods, retain edge midpoint.
 nearbeg=beg+.12*(mid-beg);nearend=end+.12*(mid-end)
 h=.08 if d%2 else -.08
 if not path:path.append((beg,h))
 path.extend([(nearbeg,0),(mid,0),(nearend,0),(end,.08 if D%2 else -.08)])
 d=4*(D//4)+(D%4+2)%4;g=g2
 if d==start:break
print('knot homology',g,flush=True)
# Smooth sampling of piecewise-linear UV arcs and small normal-height ramps.
verts=[]
for (a,h),(b,k)in zip(path,path[1:]):
 for t in np.linspace(0,1,args.samples)[:-1]:
  uv=(a*(1-t)+b*t)@np.array(args.matrix).reshape(2,2).T;z=h*(1-t)+k*t;u,v=2*np.pi*uv
  # u meridian, v longitude; surface normal equals radial tube normal.
  rr=1+z;verts.append([(3+rr*np.cos(u))*np.cos(v),(3+rr*np.cos(u))*np.sin(v),rr*np.sin(u)])
# periodic path ends at same point after integral g.
V=np.array(verts);theta=.391;phi=.237
Rz=np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
Ry=np.array([[np.cos(phi),0,np.sin(phi)],[0,1,0],[-np.sin(phi),0,np.cos(phi)]])
V=V@Rz@Ry;M=len(V);hits=[]
for i in range(M):
 a=V[i];u=V[(i+1)%M]-a
 for k in range(i+2,M):
  if i==0 and k==M-1:continue
  b=V[k];v=V[(k+1)%M]-b
  det=u[0]*v[1]-u[1]*v[0]
  if abs(det)<1e-12:continue
  q=b-a;t=(q[0]*v[1]-q[1]*v[0])/det;s=(q[0]*u[1]-q[1]*u[0])/det
  if 1e-9<t<1-1e-9 and 1e-9<s<1-1e-9:
   z1=a[2]+t*u[2];z2=b[2]+s*v[2];assert abs(z1-z2)>1e-7
   hits.append((i+t,k+s,z1>z2,det))
events=sorted((p,c,a)for c,h in enumerate(hits)for a,p in enumerate(h[:2]));idx={(c,a):i for i,(_,c,a)in enumerate(events)};out=[];L=2*len(hits)
for c,(p,q,firstover,det)in enumerate(hits):
 ui=idx[c,1 if firstover else 0];oi=idx[c,0 if firstover else 1]
 di=-det if firstover else det
 out.append([ui,oi,(ui+1)%L,(oi+1)%L]if di>0 else[ui,(oi+1)%L,(ui+1)%L,oi])
print('projected crossings',len(hits),flush=True)
K=Link(out);assert K.is_planar();Reg=regina.Link.fromPD([[x+1 for x in c]for c in out]);print('Jones',Reg.jones(),flush=True)
K.simplify('global');print('simplified',len(K.crossings),len(K.link_components)+K.unlinked_unknot_components,flush=True)
(HERE/args.out).write_text(json.dumps({'matrix':args.matrix,'samples':args.samples,'coordinates_rational':[[str(Fraction(float(x)).limit_denominator(10000))for x in row]for row in pos],'coordinates':pos.tolist(),'triangle_areas':areas,'homology':g.tolist(),'PD':out,'Jones':str(Reg.jones()),'simplified_PD':K.PD_code(),'simplified_components':len(K.link_components)+K.unlinked_unknot_components},indent=2)+'\n')
