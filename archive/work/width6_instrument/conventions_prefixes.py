from pathlib import Path
import sys,json,time,io,contextlib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'width6_targeted'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'width6_lift'))
import geometric_intersections as g
import lift_pairing as l
from lp_completions import divide_one_minus_t

def expected(w):return {(a//2,b):c for(a,b),c in l.shift(divide_one_minus_t(l.pairing(w,7,7)),-4).items()}
def eq(p,q):
 if not p or not q:return p==q
 ap,bp=min(p);aq,bq=min(q);da,db=ap-aq,bp-bq
 if abs(p[ap,bp])!=abs(q[aq,bq]):return False
 sg=p[ap,bp]//q[aq,bq]
 return p=={(a+da,b+db):c*sg for(a,b),c in q.items()}
w=[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]
rows=[]
for k in range(1,len(w)+1):
 t=time.monotonic()
 with contextlib.redirect_stdout(io.StringIO()):r=g.model([-x for x in w[:k]],64,.006)
 p={(a,b):c for a,b,c in r['polynomial']};ex=expected(w[:k]);ok=eq(p,ex)
 rows.append({'prefix':k,'word':w[:k],'match':ok,'actual':r['polynomial'],'expected':l.encode(ex),'configurations':len(r['configurations']),'intersection_counts':r['intersection_counts'],'seconds':time.monotonic()-t})
 print(k,ok,r['intersection_counts'],len(r['configurations']),round(rows[-1]['seconds'],2),flush=True)
 (Path(__file__).parent/'conventions_prefixes.json').write_text(json.dumps(rows,indent=2)+'\n')
