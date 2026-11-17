from pathlib import Path
import sys,json,contextlib,io,time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'width6_targeted'))
sys.path.insert(0,str(ROOT/'width6_lift'))
import geometric_intersections as g
import lift_pairing as l
from lp_completions import divide_one_minus_t

def expected(w):
 p=l.shift(divide_one_minus_t(l.pairing(w,7,7)),-4)
 assert all(a%2==0 for a,b in p)
 return {(a//2,b):c for (a,b),c in p.items()}
def monomial_equal(p,q):
 if not p or not q:return {} if p==q else None
 ap,bp=min(p);aq,bq=min(q);da,db=ap-aq,bp-bq
 if abs(p[ap,bp])!=abs(q[aq,bq]):return None
 sg=p[ap,bp]//q[aq,bq]
 return {'a':da,'b':db,'sign':sg} if p=={(a+da,b+db):c*sg for(a,b),c in q.items()}else None
cases=[[],[1],[2],[3],[4],[5],[2,1],[1,2],[2,3],[3,2],[2,4],[4,2],[2,1,3],[2,1,-3,-2],[2,1,2],[1,2,1],[2,3,2],[3,2,3],[2,1,-2], [2,3,-2]]
rows=[]
for w in cases:
 t=time.monotonic()
 with contextlib.redirect_stdout(io.StringIO()):r=g.model([-z for z in w],32,.01)
 p={(a,b):c for a,b,c in r['polynomial']}
 ex=expected(w)
 unit=monomial_equal(p,ex)
 transforms={}
 if unit is None:
  for name,ww in [('reverse',w[::-1]),('mirror',[-z for z in w]),('inverse',[-z for z in w[::-1]])]:
   z=monomial_equal(p,expected(ww))
   if z is not None:transforms[name]=z
 row={'word':w,'geometric':r['polynomial'],'expected':l.encode(ex),'unit':unit,'alternative_matches':transforms,'configuration_count':len(r['configurations']),'seconds':time.monotonic()-t}
 rows.append(row)
 print(w,'match',unit,'alternatives',transforms,'count',len(r['configurations']),'sec',round(row['seconds'],2),flush=True)
 (Path(__file__).parent/'conventions_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
