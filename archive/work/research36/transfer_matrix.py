"""Exact TL2 vectors from the two source-grounded planar closure diagrams."""
from source_machine import make,regina
import json
from pathlib import Path

def clean(p):return {k:v for k,v in p.items()if v}
def add(p,q):
 r=dict(p)
 for k,v in q.items():r[k]=r.get(k,0)+v
 return clean(r)
def scale(p,a):return clean({k:a*v for k,v in p.items()})
def shift(p,a):return {k+a:v for k,v in p.items()}
def mul(p,q):
 r={}
 for i,a in p.items():
  for j,b in q.items():r[i+j]=r.get(i+j,0)+a*b
 return clean(r)
def div(p,q):
 offset=-min(p);r=shift(p,offset);ans={};lo=min(q);q=shift(q,-lo)
 while r and max(r)>=max(q):
  n=max(r)-max(q);a=r[max(r)]//q[max(q)];assert a*q[max(q)]==r[max(r)]
  ans[n]=ans.get(n,0)+a;r=add(r,scale(shift(q,n),-a))
 assert not r,r
 return shift(clean(ans),-offset-lo)
def bracket(fig,cl):
 K=make(fig=fig,closure=cl);v=regina.Link.fromPD([[x+1 for x in c]for c in K.PD_code()]).jones()
 return {3*K.writhe()-2*e:(1 if K.writhe()%2==0 else -1)*int(str(v[e]))for e in range(v.minExp(),v.maxExp()+1)if v[e]!=0}
d={2:-1,-2:-1};den=add(mul(d,d),{0:-1});out={}
for fig in ['omega1','omega5','claimed']:
 bv=bracket(fig,'vertical');bh=bracket(fig,'horizontal')
 f=div(add(mul(d,bv),scale(bh,-1)),den)
 g=div(add(mul(d,bh),scale(bv,-1)),den)
 assert add(mul(d,f),g)==bv and add(f,mul(d,g))==bh
 out[fig]={'I':f,'e':g};print(fig,out[fig])
Path(__file__).with_name('transfer_vectors.json').write_text(json.dumps(out,indent=2)+'\n')
