import random, json, time
from pathlib import Path
rng=random.Random(192371)
s=[1]*4+[-1]*3
same_edges=[(i,j) for i in range(7) for j in range(i+1,7) if s[i]==s[j]]
opp_edges=[(i,j) for i in range(7) for j in range(i+1,7) if s[i]!=s[j]]
same=[0,0,0,0,2,5,6,9,11]
opp=[0,0,0,0,0,0,1,1,4,7,10,10]
found=[];best=10**9
for k in range(300000):
 rng.shuffle(same);rng.shuffle(opp)
 C=[[0]*7 for _ in range(7)]
 z=[0]*7
 for edges,values in ((same_edges,same),(opp_edges,opp)):
  for (i,j),v in zip(edges,values):
   C[i][j]=C[j][i]=v;z[i]+=v*s[j];z[j]+=v*s[i]
 score=sum(si*zi*zi for si,zi in zip(s,z))
 if abs(score)<best:best=abs(score)
 if not score:
  for i in range(4,7):C[i][i]=1
  found.append({'C':C,'z':z,'trial':k})
  if len(found)>=100:break
Path(__file__).with_suffix('.json').write_text(json.dumps({'trials':k+1,'best':best,'candidates':found},indent=2)+'\n')
print({'trials':k+1,'best':best,'candidates':len(found),'first':found[:1]})
