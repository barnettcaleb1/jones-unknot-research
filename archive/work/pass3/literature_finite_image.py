"""Exact finite-image tests at t primitive sixth root, reduced Burau B4."""
from collections import deque
from pathlib import Path
import json
Z=(0,0);O=(1,0);T=(0,1);IT=(1,-1)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def sm(xs):
 a=Z
 for x in xs:a=add(a,x)
 return a
def mm(a,b):return tuple(tuple(sm(mul(a[i][k],b[k][j]) for k in range(3)) for j in range(3)) for i in range(3))
I=((O,Z,Z),(Z,O,Z),(Z,Z,O))
B={1:((neg(T),O,Z),(Z,O,Z),(Z,Z,O)),
   -1:((neg(IT),IT,Z),(Z,O,Z),(Z,Z,O)),
   2:((O,Z,Z),(T,neg(T),O),(Z,Z,O)),
   -2:((O,Z,Z),(O,neg(IT),IT),(Z,Z,O)),
   3:((O,Z,Z),(Z,O,Z),(Z,T,neg(T))),
   -3:((O,Z,Z),(Z,O,Z),(Z,O,neg(IT)))}
def mat(word):
 a=I
 for g in word:a=mm(a,B[g])
 return a
def tr(a):return sm(a[i][i] for i in range(3))
for g in (1,2,3):assert mm(B[g],B[-g])==I
U=mat([1,-3]);Ui=mat([3,-1]);V=mat([2,1,-3,-2]);Vi=mat([2,3,-1,-2])
gens=[U,Ui,V,Vi]
found={I:[]};todo=deque([I])
while todo and len(found)<100000:
 a=todo.popleft()
 for k,g in enumerate(gens):
  b=mm(a,g)
  if b not in found:
   found[b]=found[a]+[k];todo.append(b)
assert not todo, len(found)
print('kernel image size',len(found))
def tp(n):
 a=O
 for _ in range(n%6):a=mul(a,T)
 return a
data=json.loads(Path(__file__).with_name('literature_trace_targets.json').read_text())
res=[]
for seed in data:
 gamma=mat(seed['quotient_word'])
 target=sm(mul((c,0),tp(-(int(e)-5)//2)) for e,c in seed['a31_target'].items())
 hits=[word for a,word in found.items() if tr(mm(a,gamma))==target]
 print(seed['quotient_tuple'],'target',target,'matching image elements',len(hits))
 res.append({'quotient_tuple':seed['quotient_tuple'],'target':target,'matching_image_elements':len(hits),'first_word':hits[:1]})
Path(__file__).with_suffix('.json').write_text(json.dumps({'kernel_image_order':len(found),'cosets':res},indent=2)+'\n')
