import json

def clean(p): return {k:v for k,v in p.items() if v}
def add(a,b):
 r=dict(a)
 for k,v in b.items():r[k]=r.get(k,0)+v
 return clean(r)
def shift(a,e,c=1):return {k+e:c*v for k,v in a.items()}
def dim(j):return {2*j-4*l:(-1)**j for l in range(j+1)}
def divexact(n,d):
 n=dict(n);q={}; low=min(d); lc=d[low]
 while n:
  e=min(n)-low;c=n[min(n)]//lc
  assert c*lc==n[min(n)]
  q[e]=q.get(e,0)+c;n=add(n,shift(d,e,-c))
  assert len(q)<10000
 return clean(q)
def colored_trefoil(j):
 n={}
 for k in range(0,2*j+1,2):
  e=3*k*(k+2)//2-6*j*(j+2)
  n=add(n,shift(dim(k),e,(-1)**(k//2)))
 return divexact(n,dim(j))
rows=[]
for j in range(7):
 p=colored_trefoil(j)
 assert min(p)==-6*j*j-10*j
 assert max(p)==-4*j
 assert all(e%4==0 for e in p)
 rows.append({'label':j,'t_min':-max(p)//4,'t_max':-min(p)//4,'terms':len(p)})
assert colored_trefoil(1)=={-4:1,-12:1,-16:-1}
print(json.dumps({'status':'passed','rows':rows},indent=2))
