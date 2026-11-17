from collections import defaultdict
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path('work/attack_search').resolve()))
from search import matchings,canonical,components,addto,clean,loopmul
n=int(sys.argv[1]) if len(sys.argv)>1 else 3
N=2*n+2
BASIS=[canonical(p,N//2) for p in matchings(list(range(N)))];IX={x:i for i,x in enumerate(BASIS)}
ID=IX[canonical([(i,i+1)for i in range(0,N,2)],N//2)]
def e_action(v,i):
 out=[defaultdict(int)for _ in BASIS]
 for p,a in zip(v,BASIS):
  if not p:continue
  if a[i]==i+1:q=loopmul(p);dest=IX[a]
  else:
   b=list(a);l,r=a[i],a[i+1];b[i]=i+1;b[i+1]=i;b[l]=r;b[r]=l;dest=IX[tuple(b)];q=p
  addto(out[dest],q)
 return [clean(x)for x in out]
def braid(v,j):
 s=1 if j>0 else -1;e=e_action(v,abs(j)-1)
 out=[defaultdict(int)for _ in BASIS]
 for q,p,r in zip(out,v,e):addto(q,p,s);addto(q,r,-s)
 return [clean(x)for x in out]
def P(v):
 for i in range(1,2*n,2):
  ev=e_action(v,i);v=[clean({k:loopmul(a).get(k,0)-b.get(k,0) for k in loopmul(a).keys()|b.keys()})for a,b in zip(v,ev)]
 return v

def top_vector():
 # clasp points S,E,N,W; port0 under, port1 over.
 edges=[];ports=[]
 for i in range(2*n):
  z=(1,2,3,0)if i%2 else(0,1,2,3)
  p={a:N+4*i+b for a,b in zip('SENW',z)};ports.append(p);edges.append((i+1,p['S']))
 for i in range(n):edges.append((ports[2*i]['N'],ports[2*i+1]['N']))
 for i in range(2*n-1):edges.append((ports[i]['E'],ports[i+1]['W']))
 edges.extend([(0,ports[0]['W']),(N-1,ports[2*n-1]['E'])])
 v=[defaultdict(int)for _ in BASIS]
 for bits in range(1<<(2*n)):
  ed=list(edges)
  for i in range(2*n):
   p=[N+4*i+j for j in range(4)]
   ed.extend([(p[0],p[3]),(p[1],p[2])]if bits>>i&1 else[(p[0],p[1]),(p[2],p[3])])
  cc=components(ed,N+8*n);groups={}
  for j in range(N):groups.setdefault(cc[j],[]).append(j)
  assert all(len(g)==2 for g in groups.values())
  loops=len(set(cc))-len(groups)
  p={2*n-2*bits.bit_count():1}
  for _ in range(loops):p=loopmul(p)
  addto(v[IX[canonical(groups.values(),N//2)]],p)
 return [clean(x)for x in v]
def mul(a,b):
 c=defaultdict(int)
 for i,x in a.items():
  for j,y in b.items():c[i+j]+=x*y
 return clean(c)
def sub(a,b):return clean({k:a.get(k,0)-b.get(k,0)for k in a.keys()|b.keys()})
def proportional(a,b):
 pivot=next((i for i,p in enumerate(b)if p),None)
 if pivot is None:return None
 return all(not sub(mul(p,b[pivot]),mul(q,a[pivot]))for p,q in zip(a,b)),pivot
v=[{}for _ in BASIS];v[ID]={0:1}
t=top_vector();s=[{-e:c for e,c in p.items()}for p in t]
pv,ps=P(v),P(s)
alpha={0:1}
for _ in range(n):alpha=mul(alpha,{0:1,4:-1})
assert all(a==mul(alpha,b)for a,b in zip(ps,pv))
print('n',n,'dim',len(BASIS),'exact alpha=(1-A4)^n verified')
Path(f'work/research20/projected_clasp_n{n}.json').write_text(json.dumps({'basis':BASIS,'bottom':v,'top':t,'Pbottom':pv,'Ptop_adjoint':ps,'proportional':proportional(ps,pv)},indent=2))
