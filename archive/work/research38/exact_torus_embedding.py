"""Exact rational PL torus embedding of the three-crossing ribbon diagram.
All projection intersections and over/under comparisons use rational arithmetic.
The PL torus is the 4x4 triangulated boundary of a standard unknotted solid torus.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,argparse
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H.parent/'braid_classification/packages'))
from spherogram import Link
import regina
ap=argparse.ArgumentParser();ap.add_argument('--matrix',nargs=4,type=int,default=[1,0,0,1]);ap.add_argument('--out',default='exact_axes.json');arg=ap.parse_args();M=arg.matrix
j=json.loads((H/'virtual_surface_states.json').read_text())[0];pd=j['PD'];d=json.loads((H/'torus_embedding.json').read_text());pos=[tuple(Q(x).limit_denominator(10000)for x in r)for r in d['coordinates']]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def mat(a):return (M[0]*a[0]+M[1]*a[1]+Q(1,37),M[2]*a[0]+M[3]*a[1]+Q(1,41))
cs=[{int(k):v for k,v in c.items()}for c in j['cohomology_basis']];vol={e:tuple(Q(c[e])for c in cs)for e in range(6)}
occ={e:[]for e in range(6)}
for i,row in enumerate(pd):
 for p,e in enumerate(row):occ[e].append(4*i+p)
al={a:b for ds in occ.values()for a,b in [ds,ds[::-1]]}
sgn=lambda d:1 if d<al[d]else-1
edge=lambda d:pd[d//4][d%4]
CS=[(1,0),(0,1),(-1,0),(0,-1)]
def torvert(i,k):
 c,s=CS[i%4];a,b=CS[k%4];return tuple(map(Q,((3+c)*a,(3+c)*b,s)))
def face(uv):
 x,y=mul(uv,4);i=x.numerator//x.denominator;k=y.numerator//y.denominator;x-=i;y-=k
 if x>=y:ids=[(i,k),(i+1,k),(i+1,k+1)];w=[1-x,x-y,y]
 else:ids=[(i,k),(i+1,k+1),(i,k+1)];w=[1-y,x,y-x]
 vv=[torvert(*z)for z in ids];p=tuple(sum(t*z[a]for t,z in zip(w,vv))for a in range(3));normal=cross(sub(vv[1],vv[0]),sub(vv[2],vv[0]));return p,normal,ids
# Graph edges mapped piecewise-affinely to the PL torus. Exact breakpoints include
# every grid edge and diagonal of the chosen triangulation.
def mapped_segment(a,b):
 ts={Q(0),Q(1)}
 for x,y in [(a[0],b[0]),(a[1],b[1]),(a[0]-a[1],b[0]-b[1])]:
  if x==y:continue
  lo,hi=sorted([4*x,4*y]);L=lo.numerator//lo.denominator-1;U=hi.numerator//hi.denominator+2
  for k in range(L,U+1):
   t=(Q(k,4)-x)/(y-x)
   if 0<t<1:ts.add(t)
 return [face(add(a,mul(sub(b,a),t)))[0]for t in sorted(ts)]
path=[];dart=0;g=(Q(0),Q(0));patches=[]
while True:
 e=edge(dart);beg=add(pos[dart//4],g);mid=add(pos[3+e],g)
 if sgn(dart)<0:mid=sub(mid,vol[e])
 g2=add(g,mul(vol[e],sgn(dart)));D=al[dart];end=add(pos[D//4],g2)
 nb=add(beg,mul(sub(mid,beg),Q(1,1000)));ne=add(end,mul(sub(mid,end),Q(1,1000)))
 B,N,ids=face(mat(beg));E,NN,ids2=face(mat(end));assert face(mat(nb))[2]==ids and face(mat(ne))[2]==ids2
 raised=add(B,mul(N,Q(-1 if dart%2 else 1,1000000)))
 if not path:path.append(raised)
 path.extend(mapped_segment(mat(nb),mat(mid)));path.extend(mapped_segment(mat(mid),mat(ne))[1:]);path.append(add(E,mul(NN,Q(-1 if D%2 else 1,1000000))))
 patches.append({'crossing':dart//4,'dart':dart,'triangle':ids})
 dart=4*(D//4)+(D%4+2)%4;g=g2
 if dart==0:break
assert path[-1]==path[0];path.pop()
# Generic EXACT rational projection. Kernel direction is (1,2,31), all crossings
# have strict over/under and no event occurs at a segment endpoint.
proj=lambda p:(p[0]+Q(1,31)*p[2],p[1]+Q(2,31)*p[2],p[2])
V=list(map(proj,path));n=len(V);hits=[];mins=[]
for i in range(n):
 a=V[i];u=sub(V[(i+1)%n],a)
 for k in range(i+2,n):
  if i==0 and k==n-1:continue
  b=V[k];v=sub(V[(k+1)%n],b);D=det(u,v)
  if not D:continue
  q=sub(b,a);t=det(q,v)/D;s=det(q,u)/D
  if 0<=t<=1 and 0<=s<=1:
   assert 0<t<1 and 0<s<1,(i,k,t,s)
   z1=a[2]+t*u[2];z2=b[2]+s*v[2];assert z1!=z2
   hits.append((Q(i)+t,Q(k)+s,z1>z2,D));mins.append(abs(z1-z2))
events=sorted((p,c,a)for c,h in enumerate(hits)for a,p in enumerate(h[:2]));idx={(c,a):i for i,(_,c,a)in enumerate(events)};out=[];L=2*len(hits)
for c,(p,q,fo,D)in enumerate(hits):
 ui=idx[c,1 if fo else 0];oi=idx[c,0 if fo else 1];di=-D if fo else D
 out.append([ui,oi,(ui+1)%L,(oi+1)%L]if di>0 else[ui,(oi+1)%L,(ui+1)%L,oi])
K=Link(out);assert K.is_planar();R=regina.Link.fromPD([[x+1 for x in c]for c in out]);J=str(R.jones());K.simplify('global')
r={'matrix':M,'exact_polygon':[[str(x)for x in p]for p in path],'crossing_patches':patches,'minimum_crossing_height_gap':str(min(mins)),'PD':out,'Jones':J,'simplified_PD':K.PD_code(),'simplified_components':len(K.link_components)+K.unlinked_unknot_components}
(H/arg.out).write_text(json.dumps(r,indent=2)+'\n');print('matrix',M,'segments',n,'crossings',len(hits),'Jones',J,'simplified',len(K.crossings),r['simplified_components'])
