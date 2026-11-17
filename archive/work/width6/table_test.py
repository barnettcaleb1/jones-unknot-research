"""Exact crossing-change Jones test on one minimal HT census diagram per prime knot.

Uses the installed Spherogram/SnapPy-manifolds census for diagrams and Regina
for exact Laurent polynomials. Names are HT-style throughout, avoiding the
historical duplicate Perko labels in the Rolfsen 10-crossing table.
"""
from pathlib import Path
import json
import sys
import time

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/braid_classification/packages'))
import regina
from spherogram import Link

COUNTS={3:(1,0),4:(1,0),5:(2,0),6:(3,0),7:(7,0),8:(18,3),
        9:(41,8),10:(123,42),11:(367,185),12:(1288,888)}

def poly(j):
    return {str(e):int(str(j[e])) for e in range(j.minExp(),j.maxExp()+1) if j[e]}

def names():
    for n,(a,b) in COUNTS.items():
        for kind,count in [('a',a),('n',b)]:
            for k in range(1,count+1):yield n,f'{n}{kind}{k}'

def main():
    start=time.monotonic();hits=[];errors=[];summary={};done=0;changed=0
    for n,name in names():
        try:
            l=Link(name);pd=l.PD_code()
            assert len(pd)==n,(name,len(pd),n)
            r=regina.Link.fromPD([[v+1 for v in row] for row in pd])
            assert r.countComponents()==1
            j=r.jones()
            for i in range(n):
                rr=regina.Link(r);rr.change(rr.crossing(i));jj=rr.jones()
                changed+=1
                if jj==j:
                    row={'name':name,'crossing_index_zero_based':i,'crossings':n,
                         'original_PD_zero_based':pd,'changed_PD_one_based':rr.pdData(),
                         'Jones_Regina_x':poly(j),'original_signature':r.sig(),
                         'changed_signature':rr.sig(),'identification':'unresolved'}
                    hits.append(row)
                    print('HIT',name,i,flush=True)
            done+=1
            s=summary.setdefault(str(n),{'knots':0,'crossing_changes':0,'hits':0})
            s['knots']+=1;s['crossing_changes']+=n
            s['hits']=sum(h['crossings']==n for h in hits)
        except Exception as ex:
            errors.append({'name':name,'error':repr(ex)})
            print('ERROR',name,repr(ex),flush=True)
    out={'status':'completed','elapsed_seconds':time.monotonic()-start,
         'scope':'One minimal HT census PD per unoriented prime knot through 12 crossings; mirror choices represented by the table orientation. All crossings switched once.',
         'polynomial_variable':'Regina x is a square-root Jones variable; comparisons use exact Laurent integer polynomials within the same convention.',
         'counts':summary,'knots_tested':done,'crossing_changes_tested':changed,
         'hits':hits,'errors':errors,'census_counts':COUNTS}
    (Path(__file__).parent/'table_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['elapsed_seconds','knots_tested','crossing_changes_tested','counts','errors']},indent=2))
    print('TOTAL HITS',len(hits),flush=True)

if __name__=='__main__':main()
