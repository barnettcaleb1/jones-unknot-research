"""The preselected long controls, using only certified local source isotopies."""
from pathlib import Path
import sys,json,time,traceback
from intersection_instrument import run
HERE=Path(__file__).resolve().parent
label=sys.argv[1]
rows=json.loads((HERE.parent/'width6_lift/c3_samples.json').read_text())
case=next(r for r in rows if r['label']==label)
start=time.monotonic()
try:
    result=run(case['word'],case['i'],case['j'],keep_records=True,simplify=True)
    result.update(label=label,status='CALIBRATED',total_seconds=time.monotonic()-start)
except Exception as ex:
    result={'label':label,'status':'FAILED_OR_BUDGET_LIMIT','error':str(ex),
            'total_seconds':time.monotonic()-start,'traceback':traceback.format_exc()}
    traceback.print_exc()
(HERE/(label+'_simplified.json')).write_text(json.dumps(result,separators=(',',':'))+'\n')
print('FINAL',label,result['status'],round(result['total_seconds'],2),flush=True)
