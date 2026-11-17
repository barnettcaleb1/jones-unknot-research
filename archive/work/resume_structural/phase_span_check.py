from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
pairs=list(combinations(range(1,7),2));N=len(pairs)
Q20=[[20*(i==j)-5*len(set(a)&set(b))+2 for j,b in enumerate(pairs)]for i,a in enumerate(pairs)]
w=[{(1,3):1,(1,4):-1,(2,3):-1,(2,4):1}.get(a,0)for a in pairs]
P4=[[x*y for y in w]for x in w]
ops=[Q20]
for a,b in pairs:
 def perm(p):return tuple(sorted(b if v==a else a if v==b else v for v in p))
 ops.append([[row[pairs.index(perm(p))]for p in pairs]for row in Q20])
pivots={}; certificate=None
for i in range(N):
 for j in range(N):
  coeff=[F(m[i][j])for m in ops];rhs=F(P4[i][j]);source={(i,j):F(1)}
  for k,(p,b,t)in sorted(pivots.items()):
   a=coeff[k]
   if not a:continue
   coeff=[x-a*y for x,y in zip(coeff,p)];rhs-=a*b
   for pos,v in t.items():source[pos]=source.get(pos,F(0))-a*v
   source={pos:v for pos,v in source.items()if v}
  if not any(coeff):
   if rhs and certificate is None:certificate=(source,rhs)
  else:
   k=next(k for k,a in enumerate(coeff)if a);a=coeff[k]
   pivots[k]=([x/a for x in coeff],rhs/a,{pos:v/a for pos,v in source.items()})
assert certificate
source,rhs=certificate
for m in ops:assert sum(v*m[i][j]for(i,j),v in source.items())==0
assert sum(v*P4[i][j]for(i,j),v in source.items())==rhs!=0
out={'basis_pairs':pairs,'span_rank':len(pivots),'scaling':'Q20=20Q, P4=4P','w':w,
'certificate':[{'row':pairs[i],'column':pairs[j],'coefficient':str(v)}for(i,j),v in source.items()],
'certificate_on_P4':str(rhs),'verified_on_identity_and_all_15_transpositions':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
