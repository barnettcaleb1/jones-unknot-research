#!/usr/bin/env python3
"""Independent exact Laurent R-matrix color3 certificate, no symbolic packages."""
from collections import defaultdict
from fractions import Fraction as F
from math import factorial
import itertools,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'attack_search'));from search import jones_a
ZERO={};ONE={0:1}
def add(a,b):
 c=defaultdict(int,a)
 for e,v in b.items():c[e]+=v
 return {e:v for e,v in c.items() if v}
def neg(a):return {e:-v for e,v in a.items()}
def shift(a,e,s=1):return {d+e:s*v for d,v in a.items() if s*v}
def mul(a,b):
 c=defaultdict(int)
 for e,v in a.items():
  for d,w in b.items():c[e+d]+=v*w
 return {e:v for e,v in c.items() if v}
def ident(n):return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def mm(a,b):
 n=len(a);out=[[ZERO for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for k in range(n):
   if not a[i][k]:continue
   for j in range(n):
    if b[k][j]:out[i][j]=add(out[i][j],mul(a[i][k],b[k][j]))
 return out

def inverse(a):
 n=len(a);m=[row[:]+eye for row,eye in zip(a,ident(n))]
 for i in range(n):
  j=next(j for j in range(i,n) if m[j][i]);m[i],m[j]=m[j],m[i]
  pivot=m[i][i];assert len(pivot)==1
  e,c=next(iter(pivot.items()));assert c in [-1,1]
  m[i]=[shift(x,-e,c) for x in m[i]]
  for j in range(n):
   if j==i:continue
   v=m[j][i]
   if v:m[j]=[add(x,neg(mul(v,y))) for x,y in zip(m[j],m[i])]
 return [row[n:] for row in m]
def local_R():
 r=[[ZERO for _ in range(9)] for _ in range(9)]
 for i,j in itertools.product(range(3),repeat=2):
  for k in range(min(i,2-j)+1):
   qb={1:1,-1:1} if k+j==2 and j==1 else ONE
   c=shift(qb,-2*(i+j)+2*(i-k)*(j+k)+k*(k-1)//2)
   for a in range(k):c=mul(c,{2-a-j:1,-2+a+j:-1})
   row=3*(j+k)+i-k;col=3*i+j;r[row][col]=add(r[row][col],c)
 return r
R=local_R();RI=inverse(R);assert mm(R,RI)==ident(9)
# Symbolic Yang--Baxter relation on the entire 27-dimensional tensor cube.
def action(vec,position,r):
 out={}
 for state,co in vec.items():
  a,b=state[position:position+2]
  for c,e in itertools.product(range(3),repeat=2):
   val=r[3*c+e][3*a+b]
   if val:
    dest=state[:position]+(c,e)+state[position+2:]
    out[dest]=add(out.get(dest,ZERO),mul(co,val))
 return {s:c for s,c in out.items() if c}
for state in itertools.product(range(3),repeat=3):
 v={state:ONE}
 left=action(action(action(v,0,R),1,R),0,R)
 right=action(action(action(v,1,R),0,R),1,R)
 assert left==right

def colored_unreduced(word,n):
 total=ZERO;allstates=list(itertools.product(range(3),repeat=n))
 for weight in range(2*n+1):
  states=[v for v in allstates if sum(v)==weight];index={v:i for i,v in enumerate(states)};d=len(states)
  M=ident(d)
  for letter in word:
   i=abs(letter)-1;r=R if letter>0 else RI;trans=[]
   for state in states:
    a,b=state[i:i+2];tr=[]
    for c,e in itertools.product(range(3),repeat=2):
     val=r[3*c+e][3*a+b]
     if val:
      dest=state[:i]+(c,e)+state[i+2:];tr.append((index[dest],val))
    trans.append(tr)
   out=[]
   for row in M:
    nr=[]
    for tr in trans:
     val=ZERO
     for k,v in tr:
      if row[k]:val=add(val,mul(row[k],v))
     nr.append(val)
    out.append(nr)
   M=out
  tr=ZERO
  for i in range(d):tr=add(tr,M[i][i])
  total=add(total,shift(tr,2*n-2*weight))
 writhe=sum(1 if s>0 else -1 for s in word)
 return shift(total,-2*writhe)

K=[-1]*5
L=[1,1,1,-2,-1,-1,-2,-3,2,-3,-3]
UK={40:1,32:-1,30:-1,28:-1,14:1,12:1,10:1,8:1,6:1}
UL={44:1,40:-1,30:-1,24:-1,16:1,14:1,10:1,6:1,0:2,-4:-1}
dim={2:1,0:1,-2:1}
assert colored_unreduced([],1)==dim
assert colored_unreduced([1],2)==colored_unreduced([-1],2)==dim
assert colored_unreduced([1,2],3)==colored_unreduced([1,-2],3)==dim
vK=jones_a(K,2);vL=jones_a(L,4);assert vK==vL
calcK=colored_unreduced(K,2);calcL=colored_unreduced(L,4)
assert calcK==UK,(calcK,UK)
assert calcL==UL,(calcL,UL)
D=add(UK,neg(UL))
# Exact Habiro coefficient difference; this is stronger than its first Taylor jet.
Dq={-e//2:c for e,c in D.items()};assert all(e%2==0 for e in D)
P32=mul({3:1,-3:1,1:-1,-1:-1},{3:1,-3:1,2:-1,-2:-1})
a2poly=shift(mul(mul({2:1,0:-1},{3:1,0:1}),{5:1,0:1}),-15)
assert mul(mul({1:1,0:1,-1:1},P32),a2poly)==Dq
assert sum(a2poly.values())==0 and sum(e*c for e,c in a2poly.items())==8
jet=[F(sum(c*e**k for e,c in D.items()),factorial(k)) for k in range(7)]
assert jet[:5]==[0]*5 and jet[5]==-30720
# u=e^s, ordinary Jones variable q=u^-2=e^h; divide quantum dimension3 at s=0.
ordinary_h5=jet[5]/3/F(-2)**5
assert ordinary_h5==320
# At N=3 the leading Habiro two-factor kernel is(9-1)(9-4)h^4=40h^4.
a2_first=ordinary_h5/40;assert a2_first==8
out={'braids':{'5_1':K,'10_132':L},'ordinary_Jones_A':vK,
     'color3_unreduced_variable_u':{'5_1':UK,'10_132':UL},
     'unreduced_difference_s_jet':[str(x) for x in jet],
     'normalization':'u=quantum-group variable; ordinary Jones q=u^-2; reduced color3=unreduced/(u²+1+u^-2)',
     'reduced_difference_h5':str(ordinary_h5),'Habiro_a2_difference_h1':str(a2_first),'Habiro_a2_difference_polynomial':a2poly,'Habiro_a2_factor':'q^-15(q²-1)(q³+1)(q⁵+1)',
     'all_N_formula':'H_N(5_1;e^h)-H_N(10_132;e^h)=8(N²-1)(N²-4)h^5+O(h^6), every N>=2',
     'primary_data':['https://katlas.org/wiki/5_1','https://katlas.org/wiki/10_132'],
     'R_matrix_source':'Jackson-Kerler arXiv0912.2114 eq23, s=u²; reproduced symbolically here'}
p=pathlib.Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact R-matrix reproduces both table polynomials; equal full Jones; first color3 difference coefficient320; uniform Habiro coefficient8.')
