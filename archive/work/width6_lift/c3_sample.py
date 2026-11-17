"""Bounded samples from prior zero list; no new braid sweep."""
import json,sys,time
from pathlib import Path
import lift_pairing as lp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6'))
import probe
from kernel_words import BIGELOW6_REN,LONG_PATON6

def expected(w,i,j):
 p=probe.coefficient(w,i,j);ex=sum(1 if a>0 else -1 for a in w);out={}
 for e,c in p.items():
  assert(e-ex)%2==0;n=-(e-ex)//2
  out[n]=out.get(n,0)+c;out[n+2]=out.get(n+2,0)+c
 return {n:c for n,c in out.items()if c}
def record(label,w,i,j):
 t=time.monotonic();p=lp.pairing(w,i,j);s=lp.specialize(p)
 assert s==expected(w,i,j),(label,s,expected(w,i,j))
 r={'label':label,'word':w,'i':i,'j':j,'J_zero':not s,'Lreg_zero':not p,'Lreg_terms':lp.encode(p),'term_count':len(p),'specialization':s,'seconds':time.monotonic()-t}
 if p:
  ab=max(p,key=lambda ab:(ab[1],ab[0]));d=ab[0]-2*ab[1]
  r['extremal']={'max_t_then_s':ab,'coefficient':p[ab],'collapsed_exponent':d,'collapsed_coefficient':s.get(d,0),'survives':bool(s.get(d,0)),'collision_terms':[(a,b,c)for(a,b),c in p.items()if a-2*b==d]}
 return r
rows=[];seen=set()
old=json.loads((HERE.parent/'width6/probe_candidates.json').read_text())
for r in old:
 if r['geometry']['closed_components'] or r['family'] in seen:continue
 seen.add(r['family'])
 rows.append(record('prior_zero_'+r['family'],r['word'],r['i'],r['j']))
 print(rows[-1]['label'],rows[-1]['term_count'],round(rows[-1]['seconds'],2),flush=True)
 (HERE/'c3_samples.json').write_text(json.dumps(rows,indent=2)+'\n')
for label,w,i,j in [('Bigelow_nonzero',BIGELOW6_REN,7,7),('LP_nonzero',LONG_PATON6,7,7),('simple_nonzero',[2],7,7),('arc_noncancellation',[2,1,-2,3,2,-3],3,7)]:
 rows.append(record(label,w,i,j));print(label,rows[-1]['term_count'],round(rows[-1]['seconds'],2),flush=True)
 (HERE/'c3_samples.json').write_text(json.dumps(rows,indent=2)+'\n')
print('counts',len(rows),'Jzeros',sum(r['J_zero']for r in rows),'JonesCancellation',sum(r['J_zero']and not r['Lreg_zero']for r in rows),'extremal_killed',sum(bool(r.get('extremal'))and not r['extremal']['survives']for r in rows))
