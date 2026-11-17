"""Find short cap-state transport braids; no zero-coefficient search.

Candidate moves are two neighboring braid generators. Exact TL action
identifies their target state and unit. Generic fork lifts are retained.
"""
from pathlib import Path
import json,itertools
import generic_intertwiner as g
HERE=Path(__file__).resolve().parent
def inverse_tl(i):
 M=g.eye(9)
 for col,(dest,loop)in enumerate(g.tl.TRANS[i]):
  if dest is not None:M[dest][col]=g.add(M[dest][col],{0:-1,-2:-1}if loop else{-1:1})
 return M
def action(word,v,gs,ginv):
 for x in reversed(word):v=g.mv(gs[x-1]if x>0 else ginv[-x-1],v)
 return v
def run():
 gs=[g.tlgen(i)for i in range(5)];gi=[inverse_tl(i)for i in range(5)]
 candidates=[]
 for i in range(1,5):
  for a,b in [(i,i+1),(i+1,i)]:
   for s,t in itertools.product((1,-1),repeat=2):candidates.append([s*a,t*b])
 start=g.tl.STATES.index((1,0,3,2,-1,-1));paths={start:[]};units={start:{0:1}};queue=[start];moves=[]
 while queue:
  j=queue.pop(0);v=[{}for _ in range(9)];v[j]={0:1}
  for w in candidates:
   y=action(w,v,gs,gi);nz=[(i,p)for i,p in enumerate(y)if p]
   if len(nz)!=1:continue
   k,p=nz[0]
   if len(p)!=1 or abs(next(iter(p.values())))!=1:continue
   if k not in paths:
    paths[k]=w+paths[j];units[k]=g.mul(p,units[j]);queue.append(k)
    moves.append({'source':j,'target':k,'word':w,'unit':p})
 assert len(paths)==9,(len(paths),paths)
 for j,w in paths.items():
  v=[{}for _ in range(9)];v[start]={0:1};y=action(w,v,gs,gi)
  assert y[j]==units[j]and sum(bool(x)for x in y)==1
 out={'start_state':start,'states':g.tl.STATES,'normalized_generator':'I+s e_i',
      'word_action':'rho(word) acts rightmost first on columns',
      'transports':[{'target':j,'word':paths[j],'unit':units[j]}for j in range(9)],
      'elementary_moves':moves,
      'geometry_scope':'Two-adjacent-generator cap slides; TL transports checked exactly. Generic lift uses actual braid action on the cap-product seed.'}
 (HERE/'cap_braid_lifts.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
 return out
if __name__=='__main__':run()
