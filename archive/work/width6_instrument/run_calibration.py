"""Finite geometric calibration cases; never infer point data from matrices."""
from pathlib import Path
from collections import Counter
import sys,json,time,contextlib,io
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_lift'))
sys.path.insert(0,str(HERE.parent/'width6_targeted'))
import lift_pairing as lp
from lp_completions import divide_one_minus_t
import transport_exact_intersections as geom

def expected(word):
    p=lp.shift(divide_one_minus_t(lp.pairing(word,7,7)),-4)
    assert all(a%2==0 for a,b in p)
    return {(a//2,b):c for (a,b),c in p.items()}

def monomial_match(actual,wanted):
    if not actual or not wanted:return {} if actual==wanted else None
    a,b=min(actual);c,d=min(wanted)
    da,db=a-c,b-d
    if abs(actual[a,b])!=abs(wanted[c,d]):return None
    sign=actual[a,b]//wanted[c,d]
    return {'q':da,'t':db,'sign':sign} if actual=={(u+da,v+db):sign*k for (u,v),k in wanted.items()} else None

def summary(result):
    records=result['configurations'];lines={}
    for x in records:
        d=x['a']-x['b']
        z=lines.setdefault(d,{'point_pairs':0,'sum':0,'b_counts':Counter(),'signed_b':Counter()})
        z['point_pairs']+=1;z['sum']+=x['sign']*(-1)**x['b']
        z['b_counts'][x['b']]+=1;z['signed_b'][x['b']]+=x['sign']
    surviving=[d for d,z in lines.items() if z['sum']]
    out={'configuration_count':len(records),'intersection_counts':result['intersection_counts'],
         'polynomial':result['polynomial'],'TL_line_specialization':result['TL_line_specialization']}
    if lines:
        out['highest_geometric_line']={'degree':max(lines),**lines[max(lines)]}
    if surviving:
        for name,d in [('highest_surviving_line',max(surviving)),('lowest_surviving_line',min(surviving))]:
            out[name]={'degree':d,**lines[d]}
    return out

def run_case(label,word):
    start=time.monotonic()
    result=geom.float_angle_adapter(word)
    actual={(a,b):c for a,b,c in result['polynomial']}
    wanted=expected(word);unit=monomial_match(actual,wanted)
    row={'label':label,'word':word,'calibrated':unit is not None,'deck_unit':unit,
         'seconds':time.monotonic()-start,**summary(result),
         'expected_Phi':[[a,b,c]for (a,b),c in sorted(wanted.items())],
         'rational_geometry_checks':result['rational_geometry_checks'],
         'winding_status':result['winding']}
    print(label,'calibrated',unit,'pairs',row['configuration_count'],'seconds',round(row['seconds'],2),flush=True)
    return row,result

if __name__=='__main__':
    rows=[]
    for r in lp.TRANSPORT:
        # Move both classes to the standard target by the pairing isometry.
        # Here target=C0, source=the given transported cap class.
        label='cap_'+str(r['target'])+'_against_C0'
        row,_=run_case(label,r['word'][::-1]);rows.append(row)
        (HERE/'basis_calibration.json').write_text(json.dumps(rows,indent=2)+'\n')
    assert all(r['calibrated']for r in rows)
