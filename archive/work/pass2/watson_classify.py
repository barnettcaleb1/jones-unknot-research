from watson_model import *
from pathlib import Path
import json,time
p=Path(__file__).with_name('watson_search.json');data=json.loads(p.read_text());start=time.monotonic()
for i,row in enumerate(data['rows']):
    if not row['final_crossings']:continue
    l=watson(row['alpha'],RationalTangle(row['n']),RationalTangle(-row['n']))
    l.simplify('global')
    row['spherogram_final_crossings']=len(l.crossings)
    row['spherogram_final_components']=len(l.link_components)+l.unlinked_unknot_components
    print(i,'->',len(l.crossings),'components',row['spherogram_final_components'],round(time.monotonic()-start,1),flush=True)
    p.write_text(json.dumps(data,indent=2))
