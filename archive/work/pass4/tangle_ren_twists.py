"""Exact TL6 partial-closure model of Ren's two variable top twist sites."""
from pathlib import Path
import sys, json
from collections import defaultdict
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'attack_search'))
import search
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'generic'))
from tangle_unit_check import add, neg, mul, shift, ONE, ZERO, DELTA
n=6
order=list(range(n))+list(range(2*n-1,n-1,-1))
basis=[search.canonical(p,n)for p in search.matchings(order)]
ident,transitions,_=search.tables(n)
BASE=[-2,1,1,1,-2,4,-5,-5,-5,4]

def times_e(vec,i):
    out=[{}for _ in basis]
    for j,p in enumerate(vec):
        k,loops=transitions[i-1][j]
        for _ in range(loops):p=mul(p,DELTA)
        out[k]=add(out[k],p)
    return out
def times_crossing(vec,i):
    v=times_e(vec,abs(i));sgn=1 if i>0 else -1
    return [add(shift(p,sgn),shift(q,-sgn))for p,q in zip(vec,v)]
vec=[{}for _ in basis];vec[ident]=ONE
for i in BASE:vec=times_crossing(vec,i)

def closure_type(diagram):
    edges=[]
    for i,j in enumerate(diagram):
        if i<j:edges.append((i,j,0))
    edges += [(2,3,0),(8,9,0)]
    edges += [(i,i+6,1)for i in (0,1,4,5)]
    adj=defaultdict(list)
    for i,j,w in edges:adj[i].append((j,w));adj[j].append((i,-w))
    unused=set(range(12));essential=contractible=0
    while unused:
        first=min(unused);cur=first;prev=None;winding=0
        while True:
            unused.discard(cur)
            choices=adj[cur]
            nxt,w=choices[0] if choices[0][0]!=prev else choices[1]
            winding+=w;prev,cur=cur,nxt
            if cur==first:break
        assert abs(winding)<=1
        essential+=abs(winding);contractible+=int(winding==0)
    return contractible,essential
types=[closure_type(b)for b in basis]
def close(vec):
    out=defaultdict(dict)
    for p,(c,e)in zip(vec,types):
        for _ in range(c):p=mul(p,DELTA)
        out[e]=add(out[e],p)
    return {e:p for e,p in out.items()if p}
blocks=[close(vec),close(times_e(vec,1)),close(times_e(vec,5)),close(times_e(times_e(vec,1),5))]
def power_coeff(p):
    if p==0:return ONE,ZERO
    out=(ONE,ZERO)
    crossing=({1:1},{-1:1})if p>0 else({-1:1},{1:1})
    for _ in range(abs(p)):
        f,g=out;h,k=crossing
        out=mul(f,h),add(add(mul(f,k),mul(g,h)),mul(DELTA,mul(g,k)))
    return out
def annular(p,q):
    f,g=power_coeff(p);h,k=power_coeff(q)
    weights=[mul(f,h),mul(g,h),mul(f,k),mul(g,k)]
    out={}
    for degree in (0,2,4):
        value={}
        for weight,block in zip(weights,blocks):value=add(value,mul(weight,block.get(degree,{})))
        if value:out[degree]=value
    return out

prior=json.loads((Path(__file__).resolve().parents[1]/'pass3/tangle_ren_check.json').read_text())
expected={int(k):{int(e):c for e,c in p.items()}for k,p in prior['annular_bracket_coefficients'].items()}
assert annular(1,1)==expected,(annular(1,1),expected)
assert all(not b.get(4)for b in blocks)
a00,a10,a01,a11=[b.get(2,{})for b in blocks]
F=[a11,add(mul(DELTA,a10),neg(a11)),add(mul(DELTA,a01),neg(a11)),
   add(add(mul(mul(DELTA,DELTA),a00),neg(mul(DELTA,add(a10,a01)))),a11)]
assert not F[0]
PQR=[]
for poly,offset in zip(F[1:],[22,14,18]):
    assert all((e+offset)%4==0 for e in poly)
    p={(e+offset)//4:c for e,c in poly.items()}
    assert min(p)==0 and max(p)==9 and p[0]==1 and p[9]==1
    PQR.append(p)
def divide_exact(p,q):
    p=p.copy();out={};floor=min(p)-min(q)
    while p:
        degree=max(p)-max(q)
        assert degree>=floor
        assert p[max(p)]%q[max(q)]==0
        c=p[max(p)]//q[max(q)]
        out[degree]=c;p=add(p,neg(shift(q,degree,c)))
    return out
def root_factor(p):
    if not p:return [0,0]
    mod=next(iter(p))%4
    assert all(e%4==mod for e in p)
    return [mod,sum(c*(-1 if((e-mod)//4)%2 else 1)for e,c in p.items())]
a_roots=[root_factor(block.get(2,{}))for block in blocks]
b_over_delta=[divide_exact(block[0],DELTA)for block in blocks]
b_roots=[root_factor(p)for p in b_over_delta]
assert a_roots==[[2,0],[0,25],[0,25],[0,0]]
assert b_roots==[[0,36],[2,30],[2,-30],[0,25]]
out={'base_braid':BASE,'closure':'cap3-4 top/bottom; annular-close1,2,5,6',
     'basis_count':len(basis),'four_block_annular_brackets':blocks,
     'degree2_F_coefficients_rs_r_s_1':F,
     'formula':'delta² A^(-p-q) [z²] bracket = F_rs x^(p+q)+F_r x^p+F_s x^q+F_1, x=-A^-4',
     'original_1_1_matches_independent_PD':True,
     'P_Q_R_in_y':PQR,
     'degree_zero_equation':'(-1)^p P(y)y^(-p)+(-1)^q Q(y)y^(2-q)=-yR(y)',
     'degree_zero_integer_solutions':'none, by breadth and extreme coefficients',
     'a_root_values_as_A_power_times_integer':a_roots,
     'b_divided_by_delta_root_values':b_roots,
     'signed_Jones_minus_one_formula':'(-1)^((p+q)/2)*(36+30p-30q-25pq-50(p+q)n)',
     'determinant_one_necessary_equation':'(5p+10n+6)(5q+10n-6)=100n^2-1'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':
    print(json.dumps(out,indent=2))
