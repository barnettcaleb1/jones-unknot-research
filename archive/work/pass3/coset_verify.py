"""Exact Laurent checks of every modular survivor, plus filter cross-checks."""
from pathlib import Path
from functools import lru_cache
import sys,json,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'attack_search'))
import search
search.tables=lru_cache(None)(search.tables)
def evaluate(poly,A,P):return sum(c*pow(A,e,P) for e,c in poly.items())%P
search.validate()
for line in (ROOT/'coset_modular_checks.txt').read_text().splitlines():
    nums=list(map(int,line.split()))
    assert evaluate(search.bracket(nums[1:]),2,1000003)==nums[0]
rows=[];start=time.monotonic()
for line in (ROOT/'coset_modular_hits.txt').read_text().splitlines():
    desc,word=line.split('|');w=list(map(int,word.split()))
    assert search.knot(w,4) and sum(1 if s>0 else -1 for s in w)==5
    p=search.jones_a(w,4)
    assert evaluate(p,2,1000003)==1
    rows.append(dict(description=desc.strip(),word=w,jones_one=p=={0:1},
                     degrees=[min(p),max(p)],terms=len(p),jones_A=p))
report=dict(modular_survivors=len(rows),jones_one=sum(r['jones_one'] for r in rows),
            exact=True,seconds=time.monotonic()-start,rows=rows)
(ROOT/'coset_exact_hits.json').write_text(json.dumps(report,indent=2))
print('Exact full Laurent verification:',report['modular_survivors'],'survivors,',report['jones_one'],'Jones-one;',round(report['seconds'],2),'seconds')
