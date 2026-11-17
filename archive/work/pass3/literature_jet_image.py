"""Full image test over F2[t]/(t²+t+1)², with a strict size cap."""
from pathlib import Path
from collections import deque
import json
MOD=0b10101
def mul(a,b):
    s=0
    while b:
        if b&1:s^=a
        b>>=1;a<<=1
        if a&16:a^=MOD
    return s
M=[[mul(a,b) for b in range(16)] for a in range(16)]
def mm(a,b):
    return tuple(M[a[3*i]][b[j]]^M[a[3*i+1]][b[3+j]]^M[a[3*i+2]][b[6+j]] for i in range(3) for j in range(3))
T=2;IT=10;assert mul(T,IT)==1
I=(1,0,0,0,1,0,0,0,1)
B={1:(T,1,0,0,1,0,0,0,1),-1:(IT,IT,0,0,1,0,0,0,1),
2:(1,0,0,T,T,1,0,0,1),-2:(1,0,0,1,IT,IT,0,0,1),
3:(1,0,0,0,1,0,0,T,T),-3:(1,0,0,0,1,0,0,1,IT)}
def mat(word):
    a=I
    for g in word:a=mm(a,B[g])
    return a
for g in (1,2,3):assert mm(B[g],B[-g])==I
gens=[mat([1,-3]),mat([3,-1]),mat([2,1,-3,-2]),mat([2,3,-1,-2])]
found={I};todo=deque([I]);CAP=100000
while todo and len(found)<CAP:
    a=todo.popleft()
    for g in gens:
        b=mm(a,g)
        if b not in found:found.add(b);todo.append(b)
print('image size',len(found),'complete',not todo,flush=True)
def tp(n):
    z=1
    for _ in range(abs(n)):z=M[z][T if n>=0 else IT]
    return z
data=json.loads(Path(__file__).with_name('literature_trace_targets.json').read_text())
res=[]
if not todo:
    for seed in data:
        gamma=mat(seed['quotient_word']);target=0
        for e,c in seed['a31_target'].items():
            if c%2:target^=tp(-(int(e)-5)//2)
        traces={}
        for a in found:
            z=mm(a,gamma);tr=z[0]^z[4]^z[8]
            traces[tr]=traces.get(tr,0)+1
        print(seed['quotient_tuple'],'target',target,'hits',traces.get(target,0),flush=True)
        res.append({'seed':seed['quotient_tuple'],'target':target,'hit_count':traces.get(target,0),'trace_counts':traces})
Path(__file__).with_suffix('.json').write_text(json.dumps({'ring':'F2[t]/(t^2+t+1)^2','image_size':len(found),'image_complete':not todo,'cosets':res},indent=2)+'\n')
