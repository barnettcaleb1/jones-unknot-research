"""Exact Goeritz linking-form gate for actual EKT LLL diagrams, no CAS."""
from lll_candidates import *
from spherogram.links.links_base import CrossingStrand
import networkx as nx
from fractions import Fraction as F
from math import gcd,lcm

def rref(A):
 A=[[F(x)for x in r]for r in A];piv=[];i=0
 for j in range(len(A[0])):
  k=next((k for k in range(i,len(A))if A[k][j]),None)
  if k is None:continue
  A[i],A[k]=A[k],A[i];a=A[i][j];A[i]=[x/a for x in A[i]]
  for k in range(len(A)):
   if k!=i:
    a=A[k][j];A[k]=[x-a*y for x,y in zip(A[k],A[i])]
  piv.append(j);i+=1
  if i==len(A):break
 return A,piv

def det(A):
 A=[[F(x)for x in r]for r in A];v=F(1)
 for i in range(len(A)):
  k=next((k for k in range(i,len(A))if A[k][i]),None)
  if k is None:return F(0)
  if k!=i:A[i],A[k]=A[k],A[i];v=-v
  a=A[i][i];v*=a
  for k in range(i+1,len(A)):
   b=A[k][i]/a
   for j in range(i,len(A)):A[k][j]-=b*A[i][j]
 return v

def inv(A):
 n=len(A);B,p=rref([list(r)+[int(i==j)for j in range(n)]for i,r in enumerate(A)])
 assert p==list(range(n));return [r[n:]for r in B]

def goeritz(L):
 fs={corner:i for i,face in enumerate(L.faces())for corner in face}
 edges=[];g=nx.Graph()
 for c in L.crossings:
  for k,sign in [(0,1),(1,-1)]:
   a,b=fs[CrossingStrand(c,k)],fs[CrossingStrand(c,k+2)]
   edges.append((a,b,sign));g.add_edge(a,b)
 comps=list(nx.connected_components(g));assert len(comps)==2
 comp=sorted(comps,key=lambda x:(len(x),min(x)))[0]
 vs=sorted(comp);index={v:i for i,v in enumerate(vs)};M=[[0]*len(vs)for _ in vs]
 for a,b,sign in edges:
  if a in comp and a!=b:
   i,j=index[a],index[b];M[i][j]+=sign;M[j][i]+=sign;M[i][i]-=sign;M[j][j]-=sign
 return [r[1:]for r in M[1:]]

if __name__=='__main__':
 out=[]
 for n in range(4):
  G=goeritz(lll(n));rr,p=rref(G);free=[i for i in range(len(G))if i not in p];assert len(free)==1
  k=[F(0)]*len(G);k[free[0]]=1
  for i,j in enumerate(p):k[j]=-rr[i][free[0]]
  den=lcm(*[x.denominator for x in k]);k=[int(x*den)for x in k];d=gcd(*k);k=[x//d for x in k]
  piv=next(i for i,x in enumerate(k)if abs(x)==1)
  ids=[i for i in range(len(G))if i!=piv];B=[[G[i][j]for j in ids]for i in ids];N=abs(int(det(B)));Bi=inv(B)
  vectors=[[int(i==j)for i in range(len(B))]for j in range(len(B))]
  vectors += [[int(i==j)+int(i==k)for i in range(len(B))]for j in range(len(B))for k in range(j+1,len(B))]
  vec=next(v for v in vectors if lcm(*[sum(row[i]*v[i]for i in range(len(B))).denominator for row in Bi])==N)
  val=sum(vec[i]*Bi[i][j]*vec[j]for i in range(len(B))for j in range(len(B)));assert (val*N).denominator==1;a=int(val*N)%N
  squares={j*j%N for j in range(N)if gcd(j,N)==1}
  good=a in squares or (-a)%N in squares
  row={'n':n,'Goeritz':G,'primitive_kernel':k,'kernel_pivot':piv,'nonsingular_block':B,'torsion_order':N,'generator_vector':vec,'signed_determinant':int(det(B)),'linking_numerator':a,'is_plus_or_minus_unit_square':good}
  out.append(row);print({k:v for k,v in row.items()if k not in ['Goeritz','nonsingular_block']},flush=True)
 (ROOT/'work/research33/lll_linking_form.json').write_text(json.dumps(out,indent=2)+'\n')
