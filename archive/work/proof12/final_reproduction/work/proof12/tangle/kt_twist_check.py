from pathlib import Path
import json
from kt_double_cuts import build,regina
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'kt_double_locus.json').read_text());Qs=[{int(e):c for e,c in q.items()}for q in D['cut_Q']]
def add(*ps):
 o={}
 for p in ps:
  for e,c in p.items():o[e]=o.get(e,0)+c
 return {e:c for e,c in o.items()if c}
def shift(p,k):return {e+k:c for e,c in p.items()}
rows=[]
for site in [1,2]:
 K=build([0],{site:2});K.simplify('global')
 R=regina.Link.fromPD([tuple(v+1 for v in x)for x in K.PD_code()]);J=R.jones()
 v={e//2:int(str(J[e])) for e in range(J.minExp(),J.maxExp()+1) if int(str(J[e]))};assert all(e%2==0 for e in range(J.minExp(),J.maxExp()+1)if int(str(J[e])))
 matches=[]
 for n in [-1,1]:
  p=add(shift(Qs[0],2*n),Qs[site],{e:-c for e,c in shift(Qs[site],2*n).items()})
  if p==v:matches.append(n)
 assert len(matches)==1,(site,v)
 row={'site':site,'inserted_braid':[1,1],'full_twist_parameter_n':matches[0],'PD':K.PD_code(),'Jones_t':v};rows.append(row)
 print('site',site,'passed, n=',matches[0],flush=True)
(ROOT/'kt_twist_check.json').write_text(json.dumps(rows,indent=2))
