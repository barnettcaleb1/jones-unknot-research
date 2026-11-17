"""Generic chosen geometric cap lifts in Bigelow's Krammer fork basis.

Polynomial keys(s-exponent,t-exponent), q=s^2. No zero search here.
"""
from collections import defaultdict
from pathlib import Path
import json
import generic_intertwiner as uni
HERE=Path(__file__).resolve().parent
P=uni.P;IX=uni.IX
def clean(p):return {e:c for e,c in p.items()if c}
def add(a,b,c=1):
 out=defaultdict(int,a)
 for e,x in b.items():out[e]+=c*x
 return clean(out)
def shift(p,a=0,b=0,c=1):return {(e+a,f+b):v*c for(e,f),v in p.items()if v*c}
def mul(a,b):
 out=defaultdict(int)
 for(e,f),x in a.items():
  for(g,h),y in b.items():out[e+g,f+h]+=x*y
 return clean(out)
def bar(p):return {(-e,-f):v for(e,f),v in p.items()}
def sum_poly(ps):
 out={}
 for p in ps:out=add(out,p)
 return out
def pos(i,v):
 out=[{}for _ in P]
 for(j,k),p in zip(P,v):
  if not p:continue
  if i not in(j-1,j,k-1,k):terms=[((j,k),{(0,0):1})]
  elif i==j-1:terms=[((i,k),{(2,0):1}),((i,j),{(4,0):1,(2,0):-1}),((j,k),{(0,0):1,(2,0):-1})]
  elif i==j and j!=k-1:terms=[((j+1,k),{(0,0):1})]
  elif i==k-1 and i!=j:terms=[((j,i),{(2,0):1}),((j,k),{(0,0):1,(2,0):-1}),((i,k),{(2,1):1,(4,1):-1})]
  elif i==k:terms=[((j,k+1),{(0,0):1})]
  else:terms=[((j,k),{(4,1):-1})]
  for pair,c in terms:out[IX[pair]]=add(out[IX[pair]],mul(c,p))
 return out
def letter(i,v):
 if i>0:return pos(i,v)
 # g^-1=(g²+(q+tq²−1)g+(tq³−q−tq²)I)/(tq³).
 gv=pos(-i,v);ggv=pos(-i,gv)
 a={(2,0):1,(4,1):1,(0,0):-1};b={(6,1):1,(2,0):-1,(4,1):-1}
 return [shift(sum_poly((x,mul(a,y),mul(b,z))),-6,-1)for x,y,z in zip(ggv,gv,v)]
def action(w,v):
 for x in reversed(w):v=letter(x,v)
 return v
def seed():
 v=[{}for _ in P]
 for pair,c in [((1,3),1),((1,4),-1),((2,3),-1),((2,4),1)]:v[IX[pair]]={(0,0):c}
 return v
def specialize(p):
 out=defaultdict(int)
 for(a,b),c in p.items():out[a-2*b]+=c*((-1)**b)
 return {k:int(v)for k,v in out.items()if v}
def divide_epsilon(p):
 """Exact division by1+s²t; returnsquotient orraisesValueError."""
 groups=defaultdict(dict)
 for(a,b),c in p.items():groups[a-2*b][b]=c
 out={}
 for r,z in groups.items():
  lo=min(z);hi=max(z);arr=[z.get(k,0)for k in range(lo,hi+1)]
  quotient=[0]*(len(arr)-1)
  for k in range(len(arr)-1,0,-1):quotient[k-1]=arr[k];arr[k-1]-=arr[k]
  if arr[0]:raise ValueError('not divisible byepsilon')
  for k,c in enumerate(quotient):
   if c:out[r+2*(k+lo),k+lo]=c
 return out
def encode(p):return [[a,b,c]for(a,b),c in sorted(p.items())]
def decode(p):return {(a,b):c for a,b,c in p}
def lifts():
 rows=json.load(open(HERE/'cap_braid_lifts.json'))['transports'];v=seed();out=[]
 for row in rows:
  w=row['word'];power=len(w)//2;u=[shift(p,-power)for p in action(w,v)]
  out.append({'state':row['target'],'word':w,'normalizing_s_power':-power,'vector':u})
 return out
def run():
 v=seed()
 for i in range(1,6):assert letter(-i,letter(i,v))==v
 for i in [1,3]:assert letter(i,v)==[shift(p,2,c=-1)for p in v]
 assert letter(5,v)==v
 rows=lifts();B=json.load(open(HERE/'generic_intertwiner.json'))['embedding_15_by9']
 for row in rows:
  j=row['state']
  assert [specialize(p)for p in row['vector']]==[{int(k):v for k,v in r[j].items()}for r in B]
 out={'variables':'s,t; q=s²','fork_basis':P,'seed':'F13−F14−F23+F24',
      'lifts':[{**row,'vector':[encode(p)for p in row['vector']]}for row in rows],
      'all9_specializations_match_generic_intertwiner':True}
 (HERE/'bivariate_lifts.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'all9_lifts':len(rows),'total_monomials':sum(len(p)for r in rows for p in r['vector']),'specialization_checks':True}))
if __name__=='__main__':run()
