#!/usr/bin/env python3
"""Independent frontier state-sum, no Regina Jones computation.
At each crossing resolve (01)(23) with A, (03)(12) with A^-1.
Processed paths are stored as pairings of frontier edge labels.
"""
from collections import defaultdict
from pathlib import Path
import json,sys

def evaluate(pd,verbose=False):
 pending=list(map(tuple,pd));front=set();order=[];width=0
 while pending:
  c=min(pending,key=lambda c:(len(front.symmetric_difference(set(c))),-len(front.intersection(c))))
  pending.remove(c);order.append(c)
  # Every external PD edge occurs twice; a self-loop appears twice at one crossing.
  for v in c:
   if v in front:front.remove(v)
   else:front.add(v)
  width=max(width,len(front))
 states={():{0:1}};front=set();stats=[]
 for step,c in enumerate(order):
  newfront=set(front)
  for v in c:
   if v in newfront:newfront.remove(v)
   else:newfront.add(v)
  out={}
  for matching,pol in states.items():
   for pairs,shift in [([(c[0],c[1]),(c[2],c[3])],1), ([(c[0],c[3]),(c[1],c[2])],-1)]:
    labels=set(c)|front;parent={v:v for v in labels}
    def find(v):
     while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
     return v
    for a,b in list(matching)+pairs:
     a,b=find(a),find(b)
     if a!=b:parent[a]=b
    groups={}
    for v in labels:groups.setdefault(find(v),[])
    for v in newfront:groups[find(v)].append(v)
    loops=sum(not vs for vs in groups.values())
    assert all(len(vs) in (0,2) for vs in groups.values())
    dest=tuple(sorted(tuple(sorted(vs)) for vs in groups.values() if vs))
    p={e+shift:v for e,v in pol.items()}
    # One loop is normalized to 1, so remove its delta at the final step.
    if step==len(order)-1:loops-=1
    assert loops>=0
    for _ in range(loops):
     nxt=defaultdict(int)
     for e,v in p.items():nxt[e+2]-=v;nxt[e-2]-=v
     p={e:v for e,v in nxt.items() if v}
    q=out.setdefault(dest,defaultdict(int))
    for e,v in p.items():q[e]+=v
  states={s:{e:v for e,v in p.items() if v}for s,p in out.items()}
  states={s:p for s,p in states.items() if p};front=newfront
  stats.append(len(states))
  if verbose:print(step+1,'frontier',len(front),'states',len(states),flush=True)
 assert set(states)=={()}
 return states[()],{'max_frontier':width,'max_pairing_states':max(stats)}

if __name__=='__main__':
 sys.path.insert(0,str(Path('work/braid_classification/packages').resolve()))
 from spherogram import Link
 rows=json.load(open('work/cancellation19/stoimenow_k3.json'))
 L=Link(rows[0]['simplified_PD']);w=L.writhe()
 b,stats=evaluate(L.PD_code(),True)
 # Establish convention on a known trefoil before interpreting target.
 T=Link(braid_closure=[1,1,1]);bt,_=evaluate(T.PD_code())
 want={-4:1,-12:1,-16:-1}
 options=[]
 for mirror in (1,-1):
  vt={mirror*e-3*T.writhe():v*(-1 if T.writhe()%2 else 1) for e,v in bt.items()}
  if vt==want:options.append(mirror)
 assert len(options)==1,options
 mirror=options[0]
 vA={mirror*e-3*w:v*(-1 if w%2 else 1)for e,v in b.items()}
 assert all(e%4==0 for e in vA)
 vt={-e//4:v for e,v in vA.items()}
 expected={int(e)//2:v for e,v in rows[0]['coefficients'].items()}
 assert vt==expected,(vt,expected)
 result={'algorithm':'frontier Kauffman state sum, with known-trefoil convention check','PD_crossings':len(L.crossings),'writhe':w,**stats,'A_smoothing_sign':mirror,'Jones_t':dict(sorted(vt.items())),'matches_Regina_exactly':True}
 Path('work/cancellation19/independent_pd_bracket.json').write_text(json.dumps(result,indent=2))
 print(json.dumps(result,indent=2))
