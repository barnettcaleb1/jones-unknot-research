#!/usr/bin/env python3
from classify import *

def apply2(L,op):
 if op[0]=='r1add':return L.r1(regina.StrandRef(L.crossing(op[1]),op[2]),op[3],op[4])
 return apply(L,op)

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

def lower(start,extra=1):
 maxn=start.size()+extra;q=collections.deque([(regina.Link(start),0)]);parents=[(None,None)];seen={start.sig(False,False,False):0};t=time.monotonic();goal=None
 while q and len(seen)<100000:
  L,node=q.popleft()
  if L.size()<start.size():goal=node;print('escaped',start.size(),'to',L.size(),'states',len(seen),'elapsed',time.monotonic()-t,flush=True);break
  for op in neighbors(L,maxn):
   M=regina.Link(L);before=snap(M);assert apply2(M,op)
   sig=M.sig(False,False,False)
   if sig in seen:continue
   j=len(parents);seen[sig]=j;parents.append((node,{'move':op,'before':before,'after':snap(M)}));q.append((M,j))
 if goal is None:return None,None
 chunks=[]
 while goal:
  parent,step=parents[goal];chunks.append(step);goal=parent
 return L,chunks[::-1]

def verify2(row):
 pd=[[a+1 for a in x] for x in spherogram.Link(braid_closure=row['word']).PD_code()]
 assert pd==row['pd'];L=regina.Link.fromPD(pd)
 for step in row['steps']:
  assert snap(L)==step['before'];assert apply2(L,step['move']);assert snap(L)==step['after']
 assert L.size()==0 and L.countComponents()==1

if __name__=='__main__':
 row=json.loads((ROOT/'certificate86.json').read_text());L=regina.Link.fromPD(row['pd']);ops=row['steps']
 for st in ops:assert apply2(L,st['move'])
 while L.size():
  M,new=lower(L)
  if M is None:print('FAILED',L.size());break
  L=M;ops+=new
  row['steps']=ops;(ROOT/'certificate86.json').write_text(json.dumps(row,indent=2))
 if L.size()==0:
  verify2(row);print('CERTIFIED',len(ops),dict(collections.Counter(x['move'][0] for x in ops)))
