"""Only powers n=2,3,4 of the specified Bigelow6 word, two cap/cup pairs."""
import json,time,random
from pathlib import Path
import probe,topology_classifier as tc
HERE=Path(__file__).resolve().parent
rows=json.loads((HERE/'probe_candidates.json').read_text())
word=next(r['word'] for r in rows if r['family']=='Bigelow6')
results=[]
for n in (2,3,4):
    for i,j in ((4,5),(5,4)):
        w=probe.reduce(word*n);r={'n':n,'i':i,'j':j,'word':w}
        t=time.monotonic();r['direct']=tc.classify(w,i,j)
        if r['direct']['classification']=='unknown':
            r['RIII']=tc.classify_with_III(w,i,j,seed=100*n+10*i+j,steps=2000)
        r['closures']=probe.closure_checks(w,i,j)
        N=r['closures']['numerator_closure'];D=r['closures']['denominator_closure']
        r['property_R_trivial_tangle_certified']=(N['simplified_crossings']==0 and N['simplified_components']==2 and D['simplified_crossings']==0 and D['simplified_components']==1)
        r['seconds']=time.monotonic()-t;results.append(r)
        (HERE/'powers_topology.json').write_text(json.dumps(results,indent=2)+'\n')
        print(n,i,j,'direct',r['direct']['classification'],'RIII',r.get('RIII',{}).get('classification'), 'closure crossings',N['simplified_crossings'],D['simplified_crossings'],'PropertyR',r['property_R_trivial_tangle_certified'],'seconds',round(r['seconds'],2),flush=True)
