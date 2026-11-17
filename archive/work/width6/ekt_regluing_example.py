"""One explicit independent-regluing calibration, not a candidate search."""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'ekt_model'))
import check_links as c
L=c.hopf(c.RationalTangle(3,1),c.RationalTangle(3,2))
pd=L.PD_code();r=c.regina.Link.fromPD([[x+1 for x in row] for row in pd])
result={'PD':pd,'crossings':len(pd),'components':r.countComponents(),
        'Jones_Regina':str(r.jones()),'H1_factors_free_rank':c.fox_factors(pd)}
(HERE/'ekt_regluing_example.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
