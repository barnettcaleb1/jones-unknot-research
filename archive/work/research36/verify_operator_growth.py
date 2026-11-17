#!/usr/bin/env python3
"""Exact Laurent/JVP part of the literal clasp-machine audit, standard library."""
from pathlib import Path
import runpy,json
ROOT=Path(__file__).resolve().parents[2]
lib=runpy.run_path(str(ROOT/'outputs/verify_twist_obstruction.py'))
add,mul,scale,shift,jvp=(lib[k]for k in ['add','mul','scale','shift','jvp'])
p={1:1,-1:-1}; p2=mul(p,p); H={1:-1,5:-1}
D={0:-1,2:1,6:1,8:-1}
assert add({4:1,0:-1},shift(mul(p,H),2))==D
rows=[]
for m in range(1,9):
 R=add({0:1},mul(D,{4*j:1 for j in range(m)}))
 a,b=jvp(R); assert max(set(a)|set(b))==4*m+3
 growth=scale(mul(p2,R),-1)
 ga,gb=jvp(growth); top=max(set(ga)|set(gb))
 assert top==4*m+5 and gb[top]==1
 rows.append({'m':m,'L':2*m-1,'residual_JVP_degree':4*m+3,
              'minus_p_squared_residual_JVP_degree':top,'leading_b':gb[top],
              'literal_locked_degree_if_L_at_least_7':top if m>=4 else None})
R=add({0:1},mul(D,{4*j:1 for j in range(4)}))
result={'host':'three-crossing trefoil diagram with its seed unknotting crossing switched',
        'host_Jones':{0:1},'smoothing_H':H,'residual_defect_D':D,
        'host_crossings':3,'paper_Bhat':20,'three_controlled_term_combination_degree_cap':18,
        'L7_residual_polynomial':R,'L7_locked_b21':1,'checks':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Verified exact residual recurrence and JVP degrees; L=7 forces literal locked b_21=1 above claimed cap20.')
