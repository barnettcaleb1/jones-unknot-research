import sys,json,random,collections,time,pathlib
from classify import *

def apply2(L,op):
 if op[0]=='r1add':return L.r1(regina.StrandRef(L.crossing(op[1]),op[2]),op[3],op[4])
 return apply(L,op)

def greedy(L,ops):
 while True:
  op=None
  for i in range(L.size()):
   if L.hasR1(L.crossing(i)):op=['r1',i];break
   if L.hasR2(L.crossing(i)):op=['r2',i];break
  if op is None:return
  before=snap(L);assert apply(L,op);ops.append({'move':op,'before':before,'after':snap(L)})

def neighbors(L,maxn):
 for i in range(L.size()):
  c=L.crossing(i)
  if L.hasR1(c):yield ['r1',i]
  if L.hasR2(c):yield ['r2',i]
  for side in (0,1):
   if L.hasR3(c,side):yield ['r3',i,side]
 if L.size()<maxn:
  for i in range(L.size()):
   for st in (0,1):
    for side in (0,1):
     for sign in (-1,1):yield ['r1add',i,st,side,sign]

i=86;word=rows[i]['word'];pd=[[a+1 for a in x] for x in spherogram.Link(braid_closure=word).PD_code()]
L=regina.Link.fromPD(pd);pre=[];greedy(L,pre);rng=random.Random(0)
while L.size()>11:
 choices=[['r3',i,s] for i in range(L.size()) for s in (0,1) if L.hasR3(L.crossing(i),s)]
 op=rng.choice(choices);before=snap(L);assert apply(L,op);pre.append({'move':op,'before':before,'after':snap(L)});greedy(L,pre)
start=L;print('starting',L.size(),len(pre),flush=True)
q=collections.deque([(L,0)]);parents=[(None,None)];seen={L.sig(False,False,False):0};t=time.monotonic();goal=None
while q and len(seen)<100000:
 L,node=q.popleft()
 if L.size()<11:goal=node;print('escaped',L.size(),'states',len(seen),'elapsed',time.monotonic()-t,flush=True);break
 for op in neighbors(L,12):
  M=regina.Link(L);before=snap(M);assert apply2(M,op)
  sig=M.sig(False,False,False)
  if sig in seen:continue
  j=len(parents);seen[sig]=j;parents.append((node,{'move':op,'before':before,'after':snap(M)}));q.append((M,j))
 if len(seen)%1000<20:print('states',len(seen),'queue',len(q),'time',time.monotonic()-t,flush=True)
if goal is not None:
 chunks=[]
 while goal:
  parent,step=parents[goal];chunks.append(step);goal=parent
 ops=pre+chunks[::-1];greedy(L,ops)
 print('final',L.size(),'ops',len(ops),flush=True)
 result={'index':i,'word':word,'pd':pd,'steps':ops,'regina_version':regina.versionString(),'spherogram_version':spherogram.__version__}
 (ROOT/'certificate86.json').write_text(json.dumps(result,indent=2))
else:print('NO ESCAPE',len(seen),len(q),time.monotonic()-t)
