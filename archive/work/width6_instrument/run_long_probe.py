"""Budgeted attempts on the three preselected archived long words."""
from pathlib import Path
import sys,json,time
import transport_pl as pl
import transport_exact_intersections as gi
from run_calibration import lp,run_case
HERE=Path(__file__).resolve().parent

def main(label):
    cases=json.loads((HERE.parent/'width6_lift/c3_samples.json').read_text())
    row=next(r for r in cases if r['label']==label)
    words={r['target']:r['word']for r in lp.TRANSPORT}
    effective=words[row['i']][::-1]+row['word']+[-a for a in words[row['j']]]
    curves=[[pl.point(1),pl.point(2)],[pl.point(3),pl.point(4)]]
    start=time.monotonic();trace=[]
    result={'label':label,'i':row['i'],'j':row['j'],'original_word':row['word'],
            'effective_matrix_word':effective,'status':'RUNNING','trace':trace,
            'limits':{'transport_seconds':150,'vertices_per_curve':15000,'configuration_pairs':2000000}}
    dest=HERE/(label+'_attempt.json')
    for k,g in enumerate(effective):
        curves=[pl.braid_curve(c,[-g],limit=100000)for c in curves]
        entry={'prefix':k+1,'matrix_generator':g,'vertices':[len(c)for c in curves],
               'seconds':time.monotonic()-start}
        trace.append(entry);dest.write_text(json.dumps(result,indent=2)+'\n')
        print(label,k+1,entry['vertices'],round(entry['seconds'],2),flush=True)
        if max(entry['vertices'])>15000 or entry['seconds']>150:
            result['status']='STOPPED_AT_TRANSPORT_BUDGET';break
    else:
        targets=[gi.figure8(1,2),gi.figure8(3,4)]
        allints=[[gi.intersection_records(c,t)[0]for t in targets]for c in curves]
        counts=[[len(x)for x in r]for r in allints]
        pairs=counts[0][0]*counts[1][1]+counts[0][1]*counts[1][0]
        result.update(intersection_counts=counts,configuration_count=pairs)
        if pairs>2000000:
            result['status']='STOPPED_AT_PAIR_COUNT_BUDGET'
        else:
            # Recompute from the standard seed, avoiding any change in conventions.
            answer,_=run_case(label,effective)
            result['status']='CALIBRATED' if answer['calibrated'] else 'FAILED_CALIBRATION'
            result['answer']=answer
    result['seconds']=time.monotonic()-start
    dest.write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main(sys.argv[1])
