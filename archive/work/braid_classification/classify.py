#!/usr/bin/env python3
"""Find and record primitive Reidemeister reductions with Regina."""
import json,sys,random,pathlib,time,collections
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'packages'))
import spherogram,regina
rows=json.loads((ROOT.parent/'attack_search'/'exact_hits.json').read_text())

def snap(L): return {'crossings':L.size(),'components':L.countComponents(),'brief':L.brief()}
def apply(L,op):
 if op[0]=='r1': return L.r1(L.crossing(op[1]))
 if op[0]=='r2': return L.r2(L.crossing(op[1]))
 if op[0]=='r3': return L.r3(L.crossing(op[1]),op[2])
 raise ValueError(op)
def search(pd,seed,budget=5000):
 L=regina.Link.fromPD(pd); rng=random.Random(seed); ops=[]
 for _ in range(budget):
  chosen=None
  for i in range(L.size()):
   c=L.crossing(i)
   if L.hasR1(c):chosen=['r1',i];break
   if L.hasR2(c):chosen=['r2',i];break
  if chosen is None:
   choices=[['r3',i,s] for i in range(L.size()) for s in (0,1) if L.hasR3(L.crossing(i),s)]
   if not choices:break
   chosen=rng.choice(choices)
  before=snap(L);assert apply(L,chosen);ops.append({'move':chosen,'before':before,'after':snap(L)})
  assert L.countComponents()==1
  if L.size()==0:return ops
 return None

def verify(row):
 pd=[[a+1 for a in x] for x in spherogram.Link(braid_closure=row['word']).PD_code()]
 assert pd==row['pd']
 L=regina.Link.fromPD(pd)
 for step in row['steps']:
  assert snap(L)==step['before']; assert apply(L,step['move']); assert snap(L)==step['after']
 assert L.size()==0 and L.countComponents()==1

if __name__=='__main__':
 out=[];t=time.monotonic()
 for i in [82,86]:
  word=rows[i]['word'];pd=[[a+1 for a in x] for x in spherogram.Link(braid_closure=word).PD_code()]
  for seed in range(100):
   ops=search(pd,seed)
   if ops is not None:
    result={'index':i,'word':word,'pd':pd,'seed':seed,'steps':ops,'regina_version':regina.versionString(),'spherogram_version':spherogram.__version__};verify(result);out.append(result)
    print('Certified',i,'seed',seed,'moves',len(ops),'types',dict(collections.Counter(x['move'][0] for x in ops)),'elapsed',time.monotonic()-t,flush=True);break
  else: print('NOT FOUND',i,flush=True)
 (ROOT/'reidemeister_certificates.json').write_text(json.dumps(out,indent=2))
