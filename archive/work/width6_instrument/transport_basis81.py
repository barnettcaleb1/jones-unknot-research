"""Exact-transport geometric calibration on every standard cap Gram pair."""
from pathlib import Path
import sys,json,time,contextlib,io
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_lift'))
sys.path.insert(0,str(HERE.parent/'width6_targeted'))
import lift_pairing as lp
from lp_completions import divide_one_minus_t
import transport_exact_intersections as geom

def compare_up_to_unit(actual,expected):
    if not actual or not expected:return {}if actual==expected else None
    a=min(actual);e=min(expected);shift=(a[0]-e[0],a[1]-e[1])
    ratio=actual[a]/expected[e]
    if ratio not in (-1,1):return None
    shifted={(x+shift[0],y+shift[1]):int(ratio)*c for(x,y),c in expected.items()}
    return {'s_exponent':shift[0],'t_exponent':shift[1],'sign':int(ratio)}if shifted==actual else None

def run():
    transports={r['target']:r['word']for r in lp.TRANSPORT}
    rows=[];start=time.monotonic()
    for i in range(9):
        for j in range(9):
            word=list(reversed(transports[i]))+[-x for x in transports[j]]
            p=lp.pairing([],i,j);expected=lp.shift(divide_one_minus_t(p),-4)if p else{}
            with contextlib.redirect_stdout(io.StringIO()):result=geom.float_angle_adapter(word)
            actual={(2*a,b):c for a,b,c in result['polynomial']}
            unit=compare_up_to_unit(actual,expected)
            row={'i':i,'j':j,'word':word,'configuration_pairs':len(result['configurations']),
                 'polynomial_terms':len(actual),'unit':unit,'pass':unit is not None,
                 'exact_geometry_checks':result['rational_geometry_checks']}
            rows.append(row)
            print(i,j,row['configuration_pairs'],row['pass'],round(time.monotonic()-start,2),flush=True)
            if unit is None:
                row.update(actual=lp.encode(actual),expected=lp.encode(expected))
                (HERE/'transport_basis81.json').write_text(json.dumps({'complete':False,'rows':rows},indent=2)+'\n')
                raise AssertionError(row)
    out={'complete':True,'all81_pass':all(r['pass']for r in rows),
         'transport':'Exact rational PL homeomorphism and exact target intersections',
         'winding':'Float angle to integer, independently calibrated for every pair',
         'seconds':time.monotonic()-start,'rows':rows}
    (HERE/'transport_basis81.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
