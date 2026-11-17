#!/usr/bin/env python3
import json
from pathlib import Path
from fractions import Fraction
row=json.loads(Path('work/cancellation19/stoimenow_k3.json').read_text())[0]
p={int(k)//2:v for k,v in row['coefficients'].items() if v};assert all(int(k)%2==0 for k,v in row['coefficients'].items() if v)
p[0]-=1;p={k:v for k,v in p.items()if v}
lo=min(p);p={k-lo:Fraction(v)for k,v in p.items()}
def divide(p,q):
 r=dict(p);o={}
 while r and max(r)>=max(q):
  n=max(r)-max(q);c=r[max(r)]/q[max(q)];o[n]=o.get(n,0)+c
  for k,v in q.items():
   j=k+n;r[j]=r.get(j,0)-c*v
   if not r[j]:del r[j]
 return o,r
out={}
for name,q in [('t-1',{1:1,0:-1}),('t+1',{1:1,0:1}),('t2+1',{2:1,0:1}),('t2+t+1',{2:1,1:1,0:1}),('t2-t+1',{2:1,1:-1,0:1})]:
 count=0
 while True:
  a,r=divide(p,q)
  if r:break
  p=a;count+=1
 out[name]=count
print('V-1=t^',lo,'factors',out,'residual',p)
Path('work/cancellation19/stoimenow_factor.json').write_text(json.dumps({'t_shift':lo,'factors':out,'residual':{k:int(v)for k,v in p.items()}},indent=2))

assert lo==-12
assert out=={'t-1':7,'t+1':3,'t2+1':1,'t2+t+1':1,'t2-t+1':2}
assert p=={0:Fraction(-1)}
print('PASS: exact full factorization, not numerical evaluation.')
