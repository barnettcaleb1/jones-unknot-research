from pathlib import Path
import json,time,traceback
import transport_simplify as ts
import transport_priority as tp
from intersection_instrument import run
# Same safe isotopy test; only candidate order is changed.
ts.simplify_joint=tp.simplify_joint
HERE=Path(__file__).resolve().parent
case=next(r for r in json.loads((HERE.parent/'width6_lift/c3_samples.json').read_text())if r['label']=='LP_nonzero')
start=time.monotonic()
try:
 result=run(case['word'],case['i'],case['j'],keep_records=True,simplify=True)
 result.update(label=case['label'],status='CALIBRATED',total_seconds=time.monotonic()-start)
except Exception as ex:
 result={'label':case['label'],'status':'FAILED_OR_BUDGET_LIMIT','error':str(ex),'total_seconds':time.monotonic()-start,'traceback':traceback.format_exc()}
 traceback.print_exc()
(HERE/'transport_priority_lp.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print('FINAL',result['status'],result['total_seconds'],flush=True)
