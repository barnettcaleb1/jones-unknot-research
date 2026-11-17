"""Three-minute targeted shrink of one already certified cancellation witness."""
import sys,json,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
import lift_pairing as lp
sys.path.insert(0,str(HERE.parent/'width6'));import probe
seed=json.loads((HERE/'cancellation_standard.json').read_text());w=seed['word'];start=time.monotonic();log=[];tested=0
for block in [54,40,30,20,15,10,8,6,4,3,2,1]:
 changed=True
 while changed and time.monotonic()-start<160:
  changed=False
  for k in range(len(w)-block+1):
   if time.monotonic()-start>160:break
   v=probe.reduce(w[:k]+w[k+block:]);tested+=1
   if len(v)>=len(w)or probe.geometry(v,7,7)['closed_components']or probe.coefficient(v,7,7):continue
   p=lp.pairing(v,7,7)
   if not p:continue
   c=probe.closure_checks(v,7,7)
   n=c['numerator_closure'];d=c['denominator_closure']
   if not(d['simplified_crossings']==0 and d['simplified_components']==1 and n['simplified_crossings']==0 and n['simplified_components']==2):continue
   log.append({'old_length':len(w),'deleted_start':k,'block_size':block,'new_length':len(v)})
   w=v;changed=True;print('SHRINK',len(w),'tested',tested,'seconds',round(time.monotonic()-start,2),flush=True)
   out={'word':w,'length':len(w),'i':7,'j':7,'Lreg':lp.encode(p),'term_count':len(p),'J':{},'closures':c,'shrink_log':log,'tested':tested}
   (HERE/'cancellation_minimal.json').write_text(json.dumps(out,indent=2)+'\n')
   break
p=lp.pairing(w,7,7)
if not log:out=seed
out.update({'elapsed_seconds':time.monotonic()-start,'tested':tested,'final_word':w,'final_length':len(w)})
(HERE/'cancellation_minimal.json').write_text(json.dumps(out,indent=2)+'\n')
print('FINAL',len(w),len(p),'tested',tested,'seconds',round(time.monotonic()-start,2))
