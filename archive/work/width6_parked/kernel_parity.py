"""Exact matching-parity extraction and parked-weight zero orders."""
from pathlib import Path
from collections import defaultdict
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_targeted'))
from lp_completions import divide_one_minus_t

def certify(row):
    phi={(x,y):c for x,y,c in row['Phi_in_s_t']}
    pieces=[];orders=[];quotients=[]
    for m in(0,1):
        f={(x,(y-m)//2):c for(x,y),c in phi.items()if y%2==m}
        if not f:
            pieces.append({});orders.append('identically_zero');quotients.append([]);continue
        count=0
        while True:
            ev=defaultdict(int)
            for(x,y),c in f.items():ev[x]+=c
            ev={x:c for x,c in ev.items()if c}
            if count==0:pieces.append(ev)
            if ev:break
            f=divide_one_minus_t(f);count+=1
        orders.append(count);quotients.append([[x,y,c]for(x,y),c in sorted(f.items())])
    assert all(not e for e in pieces)
    degree=max(int(x)for x in row['Phi_TL_in_s'])
    row.update(Phi_even_odd_at_t1=pieces,
        Phi_matching_vanishing_orders_at_u1=orders,
        Phi_matching_quotients_variable_u_equals_t2=quotients,
        Phi_matching_L1_bounds=[sum(abs(c)for(x,y),c in phi.items()if y%2==m)for m in(0,1)],
        Phi_top_surviving_s_degree=degree,
        Phi_top_line_terms=[[x,y,c,int(c*(-1)**y)]for(x,y),c in phi.items()if x-2*y==degree])
    return row

if __name__=='__main__':
    path=HERE/'kernel_specific.json';data=json.loads(path.read_text())
    for row in data['cases']:certify(row)
    path.write_text(json.dumps(data,indent=2)+'\n')
