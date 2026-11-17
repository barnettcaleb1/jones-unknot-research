"""Five prespecified archived zero records; exact geometry, no minimization."""
from pathlib import Path
import json,sys,time,signal
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_instrument'))
from intersection_instrument import effective_word
from transport_exact_intersections import rational_model

LABELS=['prior_zero_identity','prior_zero_one_generator','prior_zero_Ren_standard',
        'prior_zero_arc_commutator','prior_zero_product_conjugates']
samples=json.loads((HERE.parent/'width6_lift/c3_samples.json').read_text())
candidates=json.loads((HERE.parent/'width6/probe_candidates.json').read_text())
topology=json.loads((HERE.parent/'width6/topology_results.json').read_text())

def limit(signum,frame):raise TimeoutError('60 second per-case bound')
signal.signal(signal.SIGALRM,limit)
out=[]
for label in LABELS:
    row=next(x for x in samples if x['label']==label)
    index=next(k for k,x in enumerate(candidates)if x['word']==row['word']and x['i']==row['i']and x['j']==row['j'])
    arc=candidates[index];top=topology[index]
    assert arc['geometry']['closed_components']==0 and arc['geometry']['boundary_pairs']==[[0,1],[2,3]]
    assert not arc['c_id']
    eff=effective_word(row['word'],row['i'],row['j'])
    ans={'label':label,'archive_index':index,'original_word':row['word'],'i':row['i'],'j':row['j'],
         'effective_matrix_word':eff,'original_geometry':arc['geometry'],
         'archived_split_classification':top['classification'],
         'representative':'Exact rational PL transport of stored cap lifts; no source simplification, cap slides, or minimization',
         'count_meaning':'Intersection incidences/preimages on parametrized figure-eight loops, whose return connectors retrace'}
    start=time.monotonic();signal.alarm(60)
    try:
        source,target,ints,checks=rational_model(eff)
        counts=[[len(v)for v in r]for r in ints]
        products=[counts[0][0]*counts[1][1],counts[0][1]*counts[1][0]]
        ans.update(status='EXACT_COUNT',source_vertices=[len(v)for v in source],
                   one_point_counts=counts,matching_products=products,total_pairs=sum(products),geometry_checks=checks)
    except Exception as ex:
        ans.update(status='NOT_COMPLETED',error=repr(ex))
    finally:signal.alarm(0)
    ans['seconds']=round(time.monotonic()-start,4);out.append(ans)
    print(label,ans['status'],ans.get('one_point_counts'),ans.get('matching_products'),ans['seconds'],flush=True)
    (HERE/'counts_saved.json').write_text(json.dumps(out,indent=2)+'\n')
