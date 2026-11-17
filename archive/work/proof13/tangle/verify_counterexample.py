"""Recheck stored cut polynomials and test one full twist at each site."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]/"proof12"/"tangle"))
import kt_double_cuts as geom
from spherogram import Link
import regina
D=json.loads((ROOT/"sign_counterexample.json").read_text())
geom.L=Link(D["base_PD"]);geom.selected=D["selected_edges"]
Qs=[{int(e):c for e,c in p.items()} for p in D["cut_Q"]]
def add(*ps):
 out={}
 for p in ps:
  for e,c in p.items():out[e]=out.get(e,0)+c
 return {e:c for e,c in out.items() if c}
def sh(p,k):return {e+k:c for e,c in p.items()}
def jones(K):
 K=K.copy();K.simplify("global")
 R=regina.Link.fromPD([tuple(v+1 for v in row) for row in K.PD_code()]) if K.crossings else regina.Link(K.unlinked_unknot_components)
 if K.crossings:
  for _ in range(K.unlinked_unknot_components):R.insertLink(regina.Link(1))
 J=R.jones();out={e:int(str(J[e])) for e in range(J.minExp(),J.maxExp()+1) if int(str(J[e]))}
 assert all(e%2==0 for e in out)
 return {e//2:c for e,c in out.items()}
rows=[]
for site in [1,2]:
 K=geom.build([0],{site:2});PD=K.PD_code();v=jones(K)
 matches=[]
 for n in [-1,1]:
  expect=add(sh(Qs[0],2*n),Qs[site],{e:-c for e,c in sh(Qs[site],2*n).items()})
  if expect==v:matches.append(n)
 assert len(matches)==1,(site,matches,v)
 rows.append({"site":site,"inserted_crossings":[1,1],"n":matches[0],"PD":PD,"Jones_t":v})
 print("single-site recurrence passed",site,matches[0])
K=geom.build([0],{1:2,2:2});PD=K.PD_code();v=jones(K)
n,m=(r["n"] for r in rows)
A,B,C=({int(e):c for e,c in D[k].items()} for k in ["A","B","C"])
assert v==add({0:1},sh(A,2*(n+m)),sh(B,2*n),sh(C,2*m))
rows.append({"both_sites":True,"n":n,"m":m,"PD":PD,"Jones_t":v})
print("both-site recurrence passed",n,m)
(ROOT/"twist_checks.json").write_text(json.dumps(rows,indent=2))
