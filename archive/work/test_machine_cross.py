from itertools import product
from math import comb

def poly(L,flip=None,cross=False):
 names=['a','b','c','d']+[f'z{i}' for i in range(L)]
 names += ['e'] if cross else []
 N=len(names); index={n:i*4 for i,n in enumerate(names)}
 def v(n,i):return index[n]+i
 edges=[]
 def e(n,i,m,j):edges.append((v(n,i),v(m,j)))
 
 if cross:
  e('a',0,'e',0);e('b',2,'e',1);e('d',2,'e',2);e('c',0,'e',3)
 else:
  e('a',0,'b',2);e('c',0,'d',2)
 e('a',2,'b',0);e('a',3,'b',3)
 e('c',2,'d',0);e('c',1,'d',1)
 e('a',1,'z0',0);e('b',1,'z0',3)
 for i in range(L-1):e(f'z{i}',1,f'z{i+1}',0);e(f'z{i}',2,f'z{i+1}',3)
 e(f'z{L-1}',1,'c',3);e(f'z{L-1}',2,'d',3)
 # A smoothing=oriented for +; b,c differs rotationally.
 ori={n:0 for n in names};ori['b']=ori['c']=1
 if cross:ori['e']=1
 out={}
 for bits in product((0,1),repeat=N):
  parent=list(range(4*N))
  def find(a):
   while a!=parent[a]:a=parent[a]
   return a
  def union(a,b):parent[find(a)]=find(b)
  for a,b in edges:union(a,b)
  for n,bit in zip(names,bits):
   pairs=[(0,3),(1,2)] if bit==ori[n] else [(0,1),(2,3)]
   for a,b in pairs:union(v(n,a),v(n,b))
  loops=len({find(i) for i in range(4*N)})
  exponent=sum((1 if bit==0 else -1)*(-1 if n==flip else 1) for n,bit in zip(names,bits))
  for k in range(loops):
   exp=exponent+2*k-2*(loops-1-k)
   out[exp]=out.get(exp,0)+(-1)**(loops-1)*comb(loops-1,k)
 w=N-(2 if flip else 0)
 return {a-3*w:c*(-1)**w for a,c in out.items() if c}
for L,flip in [(1,None),(3,None),(3,'z0')]:
 print(L,flip,poly(L,flip,True))
