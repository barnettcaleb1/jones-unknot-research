"""Actual fusion-two ribbon knot with short Lee bars and balanced extremes.

Input: KnotInfo rational reduced and integral unreduced Kh of 12n25.
Output: exact reduced Kh of K#mirror(K), via the connected-sum theorem.
No new knot invariant computation is assumed for the 24-crossing diagram.
"""
import ast,json
from collections import defaultdict
from pathlib import Path
p=Path(__file__).parent
k=next(x for x in json.load(open(p/'polys.json')) if x['name']=='12*n_25')
def plus(*ps):
    out=defaultdict(int)
    for x in ps:
        for a,v in x.items():out[a]+=v
    return {a:v for a,v in out.items() if v}
def mul(a,b):
    out=defaultdict(int)
    for (h,q),v in a.items():
        for (i,j),w in b.items():out[h+i,q+j]+=v*w
    return dict(out)
def shift(a,h,q):return {(i+h,j+q):v for (i,j),v in a.items()}
def clean(a):return {k:v for k,v in a.items() if v}
def divide(P):
    R=defaultdict(int,P);R[0,0]-=1;S={}
    while any(R.values()):
        h,q=min(k for k,v in R.items() if v);v=R[h,q]
        assert v>0
        S[h,q]=v;R[h,q]=0;R[h+1,q+2]-=v
    return S
P={(h,q):m for mod,m,h,q in ast.literal_eval(k['khovanov_reduced_rational_vector'])}
U={(h,q):m for mod,m,h,q in ast.literal_eval(k['khovanov_unreduced_integral_vector']) if mod==0}
assert sum(P.values())==21 and sum(U.values())==22
S=divide(P)
assert U==plus({(0,-1):1,(0,1):1},shift(S,0,-1),shift(S,1,3))
Pmirror={(-h,-q):v for (h,q),v in P.items()}
Smirror=shift({(-h,-q):v for (h,q),v in S.items()},-1,-2)
Pr=mul(P,Pmirror)
Sr=plus(S,Smirror,mul({(0,0):1,(1,2):1},mul(S,Smirror)))
assert Sr==divide(Pr)
assert Pr==plus({(0,0):1},mul({(0,0):1,(1,2):1},Sr))
Ur=plus({(0,-1):1,(0,1):1},shift(Sr,0,-1),shift(Sr,1,3))
ext=[]
for q in [min(j for h,j in Sr),max(j for h,j in Sr)]:
    block=[(h,v) for (h,j),v in sorted(Sr.items()) if j==q]
    imbalance=sum((-1)**h*v for h,v in block)
    assert imbalance==0
    ext.append({'q':q,'homological_multiplicities':block,'imbalance':imbalance})
def triples(P):return [[h,q,v] for (h,q),v in sorted(P.items())]
record={'base_name':'12n25','base_pd':ast.literal_eval(k['pd_notation']),
        'base_jones':k['jones_polynomial'],'base_source':triples(S),
        'base_reduced_rank':21,'base_unreduced_rank':22,
        'ribbon_knot':'12n25 # mirror(12n25)','fusion_number':2,
        'reduced_rank':sum(Pr.values()),'unreduced_rank':sum(Ur.values()),
        'source':triples(Sr),'extremes':ext,
        'note':'Fusion2 follows from bridge3 upper bound and Bleiler--Eudave-Munoz composite fusion1 theorem, not from the polynomial calculation.'}
json.dump(record,open(p/'composite_counterexample.json','w'),indent=2)
print(json.dumps({k:v for k,v in record.items() if k not in ['source','base_pd']},indent=2))
