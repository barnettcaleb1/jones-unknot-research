"""Generic Z[s,s^-1] 15x9 embedding W(6,2) into specialized fork module.

q=s^2, t=-s^-2, normalized Jones generator=I+s e_i.
"""
from pathlib import Path
from collections import defaultdict
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6'))
import probe as tl
P=[(j,k)for j in range(1,7)for k in range(j+1,7)];IX={p:i for i,p in enumerate(P)}
def clean(p):return {e:c for e,c in p.items()if c}
def add(a,b,scale=1):
 c=defaultdict(int,a)
 for e,x in b.items():c[e]+=scale*x
 return clean(c)
def shift(a,n,c=1):return {e+n:x*c for e,x in a.items()if x*c}
def mul(a,b):
 c=defaultdict(int)
 for e,x in a.items():
  for f,y in b.items():c[e+f]+=x*y
 return clean(c)
def mv(A,v):
 return [sum_poly(mul(x,y)for x,y in zip(r,v))for r in A]
def sum_poly(ps):
 out={}
 for p in ps:out=add(out,p)
 return out
def mm(A,B):return [[sum_poly(mul(x,y)for x,y in zip(r,c))for c in zip(*B)]for r in A]
def eye(d):return [[{0:1}if i==j else{}for j in range(d)]for i in range(d)]
def fork_special():
 out=[]
 for i in range(1,6):
  M=[[{}for _ in P]for _ in P]
  for col,(j,k)in enumerate(P):
   if i not in (j-1,j,k-1,k):terms=[((j,k),{0:1})]
   elif i==j-1:terms=[((i,k),{2:1}),((i,j),{4:1,2:-1}),((j,k),{0:1,2:-1})]
   elif i==j and j!=k-1:terms=[((j+1,k),{0:1})]
   elif i==k-1 and i!=j:terms=[((j,i),{2:1}),((j,k),{0:1,2:-1}),((i,k),{2:1,0:-1})]
   elif i==k:terms=[((j,k+1),{0:1})]
   else:terms=[((j,k),{2:1})]
   for p,c in terms:M[IX[p]][col]=add(M[IX[p]][col],c)
  out.append(M)
 return out
def tlgen(i):
 M=eye(9)
 for col,(dest,loop)in enumerate(tl.TRANS[i]):
  if dest is not None:M[dest][col]=add(M[dest][col],{2:-1,0:-1}if loop else{1:1})
 return M
def run():
 gs=fork_special();I=eye(15)
 for i in range(4):assert mm(mm(gs[i],gs[i+1]),gs[i])==mm(mm(gs[i+1],gs[i]),gs[i+1])
 seed=[{}for _ in P]
 for pair,c in [((1,3),1),((1,4),-1),((2,3),-1),((2,4),1)]:seed[IX[pair]]={0:c}
 start=tl.STATES.index((1,0,3,2,-1,-1));vs={start:seed};paths={start:[]};queue=[start]
 while queue:
  j=queue.pop(0)
  for i in range(5):
   dest,loops=tl.TRANS[i][j]
   if dest is not None and dest not in vs:
    assert not loops
    vs[dest]=[shift(add(x,y,-1),-1)for x,y in zip(mv(gs[i],vs[j]),vs[j])]
    paths[dest]=paths[j]+[i+1];queue.append(dest)
 B=list(map(list,zip(*(vs[j]for j in range(9)))))
 for i in range(5):assert mm(gs[i],B)==mm(B,tlgen(i))
 # All columns are in the kernel of incidence B(q): columnFij=e_i+q e_j.
 incidence=[[{0:1}if k==i else{2:1}if k==j else{}for i,j in P]for k in range(1,7)]
 incidence_zero=all(not x for r in mm(incidence,B)for x in r)
 out={'variable':'s','q':'s^2','t':'-s^-2','normalized_TL_generator':'I+s e_i',
      'fork_basis':P,'W62_basis':tl.STATES,'embedding_15_by9':B,'generator_matrices':gs,
      'cell_seed_index':start,'e_paths':paths,'generic_intertwining_all5':True,
      'image_in_Budney_incidence_kernel_without_basis_change':incidence_zero,'independence':'follows from exact q=4 rank9 certificate',
      'seed':'F13-F14-F23+F24'}
 (HERE/'generic_intertwiner.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in ('embedding_15_by9','generator_matrices','W62_basis','fork_basis')}))
 return out
if __name__=='__main__':run()
