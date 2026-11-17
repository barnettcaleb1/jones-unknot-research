"""Exact Laurent-polynomial and actual-data checks, not proof by testing."""
from pathlib import Path
from collections import defaultdict
import ast,json
ROOT=Path(__file__).resolve().parents[3]
def clean(d): return {k:v for k,v in d.items() if v}
def add(*ps):
    ans=defaultdict(int)
    for p in ps:
        for k,v in p.items(): ans[k]+=v
    return clean(ans)
def mul(p,q):
    ans=defaultdict(int)
    for a,b in p.items():
        for c,d in q.items(): ans[a+c]+=b*d
    return clean(ans)
def mon(e,c=1): return {e:c}
def qi(n): return {k:1 for k in range(n-1,-n,-2)}
def torus_num(j,m):
    return add(*(mul(mon((2*m+1)*(a*(a+1)-j*(j+2)),(-1)**(j-a)),qi(2*a+1)) for a in range(j+1)))
for j in range(9): assert torus_num(j,0)==qi(j+1)
assert torus_num(1,1)==mul(qi(2),{-2:1,-6:1,-8:-1})
rows=json.loads((ROOT/'work/proof10/homology/polys.json').read_text())
selected={r['name']:r for r in rows if r['name'] in ('5_1','10_132')}
data={}
for name,r in selected.items():
    eo=defaultdict(lambda:[0,0])
    for field,m,h,q in ast.literal_eval(r['khovanov_reduced_rational_vector']): eo[q][h%2]+=m
    e0=sum((e-o)**2 for e,o in eo.values());d0=sum((e+o)**2 for e,o in eo.values())
    rank=sum(sum(v) for v in eo.values())
    data[name]={'rank':rank,'E0':e0,'D0':d0,'quantum_even_odd':dict(sorted(eo.items())),'jones':r['jones_polynomial']}
assert data['5_1']['rank']==5 and data['10_132']['rank']==11
assert data['5_1']['E0']==data['10_132']['E0']==5
assert data['5_1']['D0']==5 and data['10_132']['D0']==21
def jones_vec(row):
    lo,hi,*coeff=ast.literal_eval(row['jones_polynomial_vector'].replace('{','[').replace('}',']'))
    assert len(coeff)==hi-lo+1
    return clean(dict(zip(range(lo,hi+1),coeff)))
assert jones_vec(selected['5_1'])=={-k:v for k,v in jones_vec(selected['10_132']).items()}
out={'exact_unknot_normalizations_checked':list(range(9)), 'mirror_trefoil_formula':'q^-1+q^-3-q^-4', 'slopes':{str(j):[a*(a+1)-j*(j+2) for a in range(j+1)] for j in range(9)},'actual_knot_norms':data}
(ROOT/'work/proof11/homology/verify_obstructions.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact normalization checks and actual-knot norm calculations passed.')
