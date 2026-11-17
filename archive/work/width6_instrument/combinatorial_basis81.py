"""Exact rational geometry AND exact winding check of all 81 Gram entries."""
from pathlib import Path
from fractions import Fraction as F
import json,time
from combinatorial_exact_pairing import exact_model

HERE=Path(__file__).resolve().parent

def run():
    source=json.loads((HERE/'full_gram_calibration.json').read_text())
    results=[]
    begun=time.monotonic()
    for k,row in enumerate(source):
        r=exact_model(row['word'],keep_records=False,progress=0)
        u=row['deck_unit']
        expected=sorted([[a+u['q'],b+u['t'],c*u['sign']]for a,b,c in row['expected_Phi']])
        assert r['polynomial']==expected,(k,r['polynomial'],expected)
        assert r['polynomial']==row['polynomial'],k
        assert r['TL_line_specialization']==row['TL_line_specialization'],k
        results.append({'label':row['label'],'i':row['i'],'j':row['j'],'word':row['word'],
                        'polynomial':r['polynomial'],'TL_line_specialization':r['TL_line_specialization'],
                        'deck_unit':u,'configuration_count':r['configuration_count'],
                        'exact_generic_Phi_match':True,'float_aggregate_match':True,
                        'seconds':r['seconds']})
        out={'status':'RUNNING' if k<80 else'PASS_ALL_81',
             'arithmetic':'Fraction geometry and exact integer signed crossing winding',
             'complete':len(results),'seconds':round(time.monotonic()-begun,3),'entries':results}
        (HERE/'combinatorial_exact_basis81.json').write_text(json.dumps(out,indent=2)+'\n')
        print('BASIS',k+1,'/81',row['i'],row['j'],r['configuration_count'],out['seconds'],flush=True)
    return out

if __name__=='__main__':run()
