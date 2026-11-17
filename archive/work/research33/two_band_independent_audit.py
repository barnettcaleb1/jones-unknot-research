"""Independent full bracket + fresh unknot simplification for all saved hits."""
import json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE),str(HERE.parent/'cancellation19')]
from lll_candidates import *
from spherogram import Link
from spherogram.links.bands.core import Band,add_one_band,normalize_crossing_labels
from spherogram.links.links_base import CrossingStrand
from independent_pd_bracket import evaluate
p=json.load(open(HERE/'two_band_test.json'));out=[]
for i,h in enumerate(p['hits']):
 source=lll(1);normalize_crossing_labels(source);assert [list(r)for r in source.PD_code()]==p['original_pd']
 for bandkey in ['first_band','second_band']:
  if bandkey=='second_band':
   source.simplify('basic');normalize_crossing_labels(source)
   assert [list(r)for r in source.PD_code()]==h['intermediate_pd'],i
   bm,_=evaluate(source.PD_code());wm=source.writhe();Vm={e-3*wm:n*(-1 if wm%2 else 1)for e,n in bm.items()}
   assert Vm!={2:-1,-2:-1},i
  b=Band(h[bandkey]);assert len(b.cs_along_top)==2 and not b.arc_is_under
  X,Z=[CrossingStrand(source.crossings[c],j)for c,j in b.cs_along_top]
  assert any(X in f and Z.opposite() in f for f in source.faces()),(i,bandkey)
  assert X.crossing.strand_components[X.strand_index]!=Z.crossing.strand_components[Z.strand_index]
  before=len(source.link_components);source=add_one_band(source,b)
  assert len(source.link_components)==before-1
 source.simplify('basic');assert [list(r)for r in source.PD_code()]==h['pd'],i
 L=Link(h['pd']);assert len(L.link_components)==1
 raw,stats=evaluate(L.PD_code());w=L.writhe()
 V={e-3*w:n*(-1 if w%2 else 1)for e,n in raw.items()}
 assert V=={0:1},(i,V)
 L.simplify('global')
 assert len(L.crossings)==0 and L.unlinked_unknot_components==1,(i,len(L.crossings),L.unlinked_unknot_components)
 assert h['simplified_pd']==[] and h['unlinked_unknot_components']==1
 out.append({'hit':i,'raw_bracket':raw,'writhe':w,'normalized_A':V,'crossings_before':len(h['pd']),'fresh_simplification_crossings':0,'fresh_unknot_components':1,**stats})
result={'count':len(out),'all_intermediate_jones_nonunlink':True,'all_saved_band_paths_replayed':True,'all_face_endpoint_conventions_checked':True,'all_full_brackets_one':True,'all_fresh_simplifications_unknot':True,'checks':out,'scope':'Checks saved successful candidates, not completeness of the generation search.'}
(HERE/'two_band_independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items()if k!='checks'})
