"""Exact rational calibration of Bigelow (2003) section5.2 fork matrices.

This is a specialization certificate at q=4, t=-1/4, not a symbolic
generic isomorphism claim. The published theorem supplies generic scope.
"""
from fractions import Fraction as F
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6'))
import probe as tl

def eye(n):return [[F(i==j) for j in range(n)]for i in range(n)]
def add(A,B,c=1):return [[x+c*y for x,y in zip(r,s)]for r,s in zip(A,B)]
def scale(A,c):return [[c*x for x in r]for r in A]
def mm(A,B):return [[sum(a*b for a,b in zip(r,c))for c in zip(*B)]for r in A]
def mv(A,v):return [sum(a*b for a,b in zip(r,v))for r in A]
def transpose(A):return list(map(list,zip(*A)))
def rref(A):
 A=[list(map(F,r))for r in A];piv=[];r=0
 for c in range(len(A[0])):
  z=next((i for i in range(r,len(A))if A[i][c]),None)
  if z is None:continue
  A[r],A[z]=A[z],A[r];a=A[r][c];A[r]=[x/a for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:
    a=A[i][c];A[i]=[x-a*y for x,y in zip(A[i],A[r])]
  piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv
def null(A):
 R,P=rref(A);d=len(A[0]);out=[]
 for c in range(d):
  if c in P:continue
  v=[F(0)]*d;v[c]=1
  for i,p in enumerate(P):v[p]=-R[i][c]
  out.append(v)
 return out
def fork(n,q,t):
 pairs=[(j,k)for j in range(1,n+1)for k in range(j+1,n+1)];ix={p:i for i,p in enumerate(pairs)};out=[]
 for i in range(1,n):
  M=[[F(0)for _ in pairs]for _ in pairs]
  for col,(j,k)in enumerate(pairs):
   if i not in (j-1,j,k-1,k):terms=[((j,k),1)]
   elif i==j-1:terms=[((i,k),q),((i,j),q*q-q),((j,k),1-q)]
   elif i==j and j!=k-1:terms=[((j+1,k),1)]
   elif i==k-1 and i!=j:terms=[((j,i),q),((j,k),1-q),((i,k),(1-q)*q*t)]
   elif i==k:terms=[((j,k+1),1)]
   else:terms=[((j,k),-t*q*q)]
   for p,c in terms:M[ix[p]][col]+=c
  out.append(M)
 return pairs,out
def controls(gs):
 for i in range(len(gs)-1):assert mm(mm(gs[i],gs[i+1]),gs[i])==mm(mm(gs[i+1],gs[i]),gs[i+1])
 for i in range(len(gs)):
  for j in range(i+2,len(gs)):assert mm(gs[i],gs[j])==mm(gs[j],gs[i])
def tlmat(sq):
 out=[];d=len(tl.STATES);delta=-(sq+1/sq)
 for i in range(5):
  M=eye(d)
  for j,(dest,loop)in enumerate(tl.TRANS[i]):
   if dest is not None:M[dest][j]+=sq*(delta if loop else 1)
  out.append(M)
 return out
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,list):return [encode(y)for y in x]
 if isinstance(x,dict):return {k:encode(v)for k,v in x.items()}
 return x
def run():
 controls(fork(6,F(2),F(3))[1])
 q=F(4);t=-1/q;sq=F(2);pairs,gs=fork(6,q,t);controls(gs)
 d=15;I=eye(d);defects=[mm(add(g,I,-1),add(g,scale(I,q)))for g in gs]
 rows=[r for P in defects for r in P];R,_=rref(rows);ranks=[len(R)]
 # Close the Hecke-relation annihilator under the dual braid action.
 while True:
  rows=R+[r for g in gs for r in mm(R,g)]
  new,_=rref(rows);ranks.append(len(new))
  if len(new)==len(R):break
  R=new
 H=null(R)
 # e1e3 cell generator has g1,g3 eigenvalue -q, g5 eigenvalue1.
 constraints=R+add(gs[0],scale(I,q))+add(gs[2],scale(I,q))+add(gs[4],I,-1)
 seeds=null(constraints);assert len(seeds)==1
 seed=seeds[0];C0=(1,0,3,2,-1,-1);start=tl.STATES.index(C0)
 vs={start:seed};paths={start:[]};queue=[start]
 while queue:
  j=queue.pop(0)
  for i in range(5):
   dest,loops=tl.TRANS[i][j]
   if dest is not None and dest not in vs:
    v=mv(add(gs[i],I,-1),vs[j]);fac=sq*((-(sq+1/sq))if loops else 1)
    vs[dest]=[x/fac for x in v];paths[dest]=paths[j]+[i+1];queue.append(dest)
 assert len(vs)==9
 B=transpose([vs[j]for j in range(9)]);T=tlmat(sq)
 assert all(mm(g,B)==mm(B,s)for g,s in zip(gs,T))
 assert len(rref(B)[1])==9
 out={'q':q,'t':t,'sqrt_q':sq,'fork_basis':pairs,'fork_generators':gs,
      'hecke_defect_generator_ranks':[len(rref(P)[1])for P in defects],
      'dual_relation_closure_ranks':ranks,'maximal_Hecke_submodule_dimension':len(H),
      'W62_basis':tl.STATES,'intertwiner_15_by9':B,'cell_seed_index':start,
      'e_paths_from_cell_seed':paths,'intertwining_all5_exact':True,
      'generic_scope':'Only q=4 checked here; Bigelow2003 Theorem6.1 supplies generic image theorem. Full fork specialization is not Hecke.'}
 (HERE/'lkb_calibration.json').write_text(json.dumps(encode(out),indent=2)+'\n')
 print(json.dumps({k:encode(out[k])for k in ['q','t','hecke_defect_generator_ranks','dual_relation_closure_ranks','maximal_Hecke_submodule_dimension','intertwining_all5_exact']}))
if __name__=='__main__':run()
