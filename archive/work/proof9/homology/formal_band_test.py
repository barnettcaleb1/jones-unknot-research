"""A formal stress test only. No knot or tangle realization is asserted."""
from collections import defaultdict
from pathlib import Path
import json

def mul(P,Q):
 R=defaultdict(int)
 for (h,q),v in P.items():
  for (i,j),w in Q.items():R[(h+i,q+j)]+=v*w
 return dict(R)
def add(P,Q):
 R=defaultdict(int,P)
 for k,v in Q.items():R[k]+=v
 return {k:v for k,v in R.items() if v}
def shift(P,h,q):return {(i+h,j+q):v for (i,j),v in P.items()}
def euler(P):
 R=defaultdict(int)
 for (h,q),v in P.items():R[q]+=(-1)**h*v
 return {q:int(v) for q,v in R.items() if v}
# Four length-one X-bars, paired at each source quantum grade with
# opposite homological parity. Free Lee generator has s=0.
a,b=4,10
source=mul({(0,0):1,(1,0):1},{(0,a):1,(2,b):1})
extra=mul(source,{(0,0):1,(1,2):1})
extra_unred=shift(mul(source,{(0,0):1,(1,4):1}),0,-1)
rows=[]
for n in range(-3,4):
 red=add({(0,0):1},shift(extra,2*n,4*n))
 unred=add({(0,-1):1,(0,1):1},shift(extra_unred,2*n,4*n))
 assert euler(red)=={0:1} and euler(unred)=={-1:1,1:1}
 assert sum(red.values())==9 and sum(unred.values())==10
 rows.append({'n':n,'reduced_rank':9,'unreduced_rank':10,'reduced_Euler':euler(red),'unreduced_Euler':euler(unred),'extra_support':sorted(shift(extra,2*n,4*n))})
report={'warning':'Abstract complexes only, not realized knots. This disproves an inference from the listed algebraic constraints, not a knot theorem.',
 'source_bars':[{'h':h,'q':q,'length':1} for h,q in source],
 'formula':'P_red(n)=1+t^(2n)q^(4n)(1+t)(1+t*q^2)(q^a+t^2*q^b)',
 'passes':['Euler Jones1','s=0','all Lee bars length1','free summand inclusion/retraction','Wang full-twist grading law'],
 'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('Verified formal rank9/rank10 stress test for seven twists; general identities are polynomial factorizations.')
