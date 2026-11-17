"""Tracked cap-product lifts and regularized Budney two-variable pairings.
Variables s,t with q=s². Budney form is linear in first argument.
This is a fixed geometric braid-transport choice, not cap-slide invariance.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json,sys,time
HERE=Path(__file__).resolve().parent
P=list(combinations(range(1,7),2));IX={p:i for i,p in enumerate(P)}
ONE={(0,0):1};Q={(2,0):1};T={(0,1):1}
def add(a,b,c=1):
 d=defaultdict(int,a)
 for k,v in b.items():d[k]+=c*v
 return {k:v for k,v in d.items()if v}
def mul(a,b):
 d=defaultdict(int)
 for (i,j),v in a.items():
  for (k,l),w in b.items():d[i+k,j+l]+=v*w
 return {k:v for k,v in d.items()if v}
def shift(a,i=0,j=0,c=1):return {(k+i,l+j):v*c for (k,l),v in a.items()if v*c}
def bar(a):return {(-i,-j):c for (i,j),c in a.items()}
def summ(ps):
 d={}
 for p in ps:d=add(d,p)
 return d
def positive(v,i):
 out=[{}for _ in P]
 for col,(j,k)in enumerate(P):
  if i not in (j-1,j,k-1,k):terms=[((j,k),ONE)]
  elif i==j-1:terms=[((i,k),Q),((i,j),{(4,0):1,(2,0):-1}),((j,k),{(0,0):1,(2,0):-1})]
  elif i==j and j!=k-1:terms=[((j+1,k),ONE)]
  elif i==k-1 and i!=j:terms=[((j,i),Q),((j,k),{(0,0):1,(2,0):-1}),((i,k),{(2,1):1,(4,1):-1})]
  elif i==k:terms=[((j,k+1),ONE)]
  else:terms=[((j,k),{(4,1):-1})]
  for dest,c in terms:out[IX[dest]]=add(out[IX[dest]],mul(c,v[col]))
 return out
def action(w,v):
 for a in reversed(w):
  u=positive(v,abs(a))
  if a>0:v=u
  else:
   uu=positive(u,-a)
   c1={(2,0):1,(4,1):1,(0,0):-1};c0={(6,1):1,(2,0):-1,(4,1):-1}
   v=[shift(add(add(x,mul(c1,y)),mul(c0,z)),-6,-1)for x,y,z in zip(uu,u,v)]
 return v
def gnorm():
 out=[];qm1={(2,0):1,(0,0):-1};h={(0,0):1,(2,1):1}
 for i,j in P:
  row=[]
  for k,l in P:
   if (i==k and j<l)or(i<k and j==l):x=shift(qm1,4,2,-1)
   elif(k==i and l<j)or(k<i and j==l):x=shift(qm1,c=-1)
   elif i<j==k<l:x=shift(qm1,0,1)
   elif k<l==i<j:x=shift(qm1,4,1)
   elif i<k<j<l:x=shift(mul(mul(qm1,qm1),h),0,1,-1)
   elif k<i<l<j:x=mul(mul(qm1,qm1),h)
   elif i==k and j==l:x=mul({(0,0):1,(2,1):-1},{(0,0):1,(4,1):1})
   else:x={}
   row.append(x)
  out.append(row)
 return out
G=gnorm()
SEED=[{}for _ in P]
for pair,c in [((1,3),1),((1,4),-1),((2,3),-1),((2,4),1)]:SEED[IX[pair]]={(0,0):c}
TRANSPORT=json.loads((HERE/'cap_braid_lifts.json').read_text())['transports']
LIFTS=[None]*9
for r in TRANSPORT:
 k=int(next(iter(r['unit'])))
 LIFTS[r['target']]=[shift(p,-k)for p in action(r['word'],SEED)]
def specialize(p):
 out=defaultdict(int)
 for (a,b),c in p.items():out[a-2*b]+=c*((-1)**b)
 return {a:int(c)for a,c in out.items()if c}
def divide_h(p):
 groups=defaultdict(dict)
 for (a,b),c in p.items():groups[a-2*b][b]=c
 out={}
 for d,x in groups.items():
  lo=min(x);hi=max(x);prev=0
  for b in range(lo,hi+1):
   z=x.get(b,0)-prev
   if b==hi:assert z==0,(d,b,z)
   elif z:out[d+2*b,b]=z
   prev=z
 return out
def pairing(w,i,j):
 right=action([-a for a in w],LIFTS[j])
 vals=[bar(p)for p in right]
 gp=[summ(mul(g,v)for g,v in zip(row,vals))for row in G]
 raw=summ(mul(a,b)for a,b in zip(LIFTS[i],gp))
 assert not specialize(raw)
 return divide_h(raw)
def encode(p):return [[a,b,c]for (a,b),c in sorted(p.items())]
def run():
 sys.path.insert(0,str(HERE.parent/'width6'));import probe
 from kernel_words import BIGELOW6_REN
 # Essential local controls, including inverse cubic.
 for i in range(1,6):assert action([i,-i],SEED)==SEED
 samples=[('identity_zero',[],2,7),('identity_nonzero',[],3,7),('identity_self',[],7,7),
 ('handleslide_zero',[2,1,1,2],2,7),('handleslide_nestedzero',[2,1,1,2],1,7),
 ('handleslide_nonzero',[2,1,1,2],3,7),('Bigelow45',BIGELOW6_REN,4,5),('Bigelow54',BIGELOW6_REN,5,4)]
 rows=[]
 for label,w,i,j in samples:
  t=time.monotonic();p=pairing(w,i,j);spec=specialize(p)
  rawTL=probe.coefficient(w,i,j)
  # Convert A powers to s powers: s=A^-2 and normalized g=A^-1 rho.
  exp=sum(1 if a>0 else -1 for a in w)
  expected={}
  for e,c in rawTL.items():
   assert(e-exp)%2==0
   n=-(e-exp)//2
   expected[n]=expected.get(n,0)+c;expected[n+2]=expected.get(n+2,0)+c
  expected={n:c for n,c in expected.items()if c}
  assert spec==expected,(label,spec,expected)
  rec={'label':label,'i':i,'j':j,'word':w,'regularized_pairing':encode(p),'specialization':spec,'terms':len(p),'zero':not p,'seconds':time.monotonic()-t}
  if p:
   highest=max(p,key=lambda ab:(ab[1],ab[0]));d=highest[0]-2*highest[1]
   orbit=[(a,b,c)for(a,b),c in p.items()if a-2*b==d]
   rec['extremal']={'max_b_then_a':list(highest),'coefficient':p[highest],'collapsed_exponent':d,'collapsed_coefficient':spec.get(d,0),'same_line_terms':orbit,'survives':bool(spec.get(d,0))}
  rows.append(rec);print(label,'terms',len(p),'spec_terms',len(spec),'time',round(rec['seconds'],2),flush=True)
  (HERE/'lift_pairing_results.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':run()
