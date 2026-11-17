import sys,itertools
from pathlib import Path
from collections import Counter,defaultdict
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
from spherogram import Link
from spherogram.links.links_base import CrossingStrand
import regina

def graph(L):
 f={corner:n for n,face in enumerate(L.faces())for corner in face};edges=[]
 for c in L.crossings:
  for a,s in [(0,1),(1,-1)]:edges.append((f[CrossingStrand(c,a)],f[CrossingStrand(c,a+2)],s))
 vertices=set(v for e in edges for v in e[:2]);comps=[]
 while vertices:
  todo=[vertices.pop()];comp=set(todo)
  while todo:
   v=todo.pop()
   for a,b,s in edges:
    n=b if a==v else a if b==v else None
    if n in vertices:vertices.remove(n);comp.add(n);todo.append(n)
  comps.append(comp)
 V=min(comps,key=len);ix={v:i for i,v in enumerate(sorted(V))}
 return len(V),[(ix[a],ix[b],s)for a,b,s in edges if a in V]
def components(n,E,subset):
 p=list(range(n))
 def find(x):
  while p[x]!=x:x=p[x]
  return x
 for i in subset:
  a,b,s=E[i];p[find(a)]=find(b)
 return [find(x)for x in range(n)]
def tree_terms(L):
 n,E=graph(L);terms=[]
 for tt in itertools.combinations(range(len(E)),n-1):
  if len(set(components(n,E,tt)))!=1:continue
  T=set(tt);power=0;sgn=1
  for i,(a,b,s) in enumerate(E):
   if i in T:
    c=components(n,E,T-{i});active=all(j>i for j,(v,w,ss)in enumerate(E)if j not in T and c[v]!=c[w])
    power+=(-3*s if active else s)
   else:
    # e is externally active iff all tree edges on its fundamental cycle are later.
    active=True
    for j in T:
     c=components(n,E,T-{j})
     if c[a]!=c[b] and j<i:active=False
    power+=(3*s if active else -s)
   if active:sgn=-sgn
  terms.append((power,sgn,sum(E[i][2]<0 for i in T),tuple(sorted(T))))
 return E,terms
if __name__=='__main__':
 for name in ['3_1','8_19','8_20','11n34','11n42','hard_unknot']:
  L=Link(braid_closure=[1,2,1,-2,-1,-2,1,2])if name=='hard_unknot'else Link(name)
  E,terms=tree_terms(L);Q=Counter()
  for power,s,k,tt in terms:Q[power]+=s
  Q={e:c for e,c in Q.items()if c}
  R=regina.Link.fromPD([[x+1 for x in row]for row in L.PD_code()]);J=R.jones();V={-2*e:int(str(J[e]))for e in range(J.minExp(),J.maxExp()+1)if J[e]!=0}
  expect={e+3*L.writhe():c*(-1 if L.writhe()%2 else 1)for e,c in V.items()}
  print(name,'match',Q==expect,'mirror',{-e:c for e,c in Q.items()}==expect,'writhe',L.writhe(),'trees',len(terms))
