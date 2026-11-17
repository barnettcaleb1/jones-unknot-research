"""State-sum extreme coefficients and their merger filtration, exact arithmetic."""
from pathlib import Path
from math import comb
from collections import defaultdict
import json,sys
from lando_probe import circles
WORK=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WORK/'braid_classification/packages'))
import regina
records=json.loads(Path(__file__).with_name('lando_probe.json').read_text())
summary=[]
for d in records:
 pd=d['PD'];c=len(pd);a=d['A']['state_circles'];b=d['B']['state_circles'];w=d['writhe']
 full=defaultdict(int)
 layerA=defaultdict(int);layerB=defaultdict(int)
 for mask in range(1<<c):
  n=mask.bit_count();s=circles(pd,mask);m=(a+n-s)//2;mb=(b+c-n-s)//2
  for r in range(s):
   coeff=(-1)**(s-1)*comb(s-1,r)
   full[c-2*n+2*(s-1)-4*r]+=coeff
   layerA[m+r]+=coeff;layerB[mb+r]+=coeff
 full={e:v for e,v in full.items() if v}
 rr=regina.Link.fromPD([[v+1 for v in cross]for cross in pd]);p=rr.jones()
 expected={3*w-2*e:int(str(p[e]))*(-1)**w for e in range(p.minExp(),p.maxExp()+1) if int(str(p[e]))}
 assert full==expected,(d['name'],full,expected)
 assert layerA[0]==(-1)**(a-1)*d['A']['I_minus_one']
 assert layerB[0]==(-1)**(b-1)*d['B']['I_minus_one']
 kA=min(k for k,v in layerA.items()if v);kB=min(k for k,v in layerB.items()if v)
 span=(max(full)-min(full))//4
 assert span==c-d['diagram_Turaev_genus']-kA-kB
 row={'name':d['name'],'crossings':c,'diagram_Turaev_genus':d['diagram_Turaev_genus'],'kA':kA,'kB':kB,'Jones_span':span,'first_three_A':[layerA[k]for k in range(3)],'first_three_B':[layerB[k]for k in range(3)],'Jones_Regina':str(p)}
 if d['name']in['8_19','10_133','11n118','11n95','8_crossing_actual_unknot']:summary.append(row)
Path(__file__).with_suffix('.json').write_text(json.dumps({'verified_diagrams':len(records),'examples':summary},indent=2)+'\n')
print('Verified complete state sums and both extreme graph coefficients against Regina on',len(records),'actual diagrams.')
for r in summary:print(r)
