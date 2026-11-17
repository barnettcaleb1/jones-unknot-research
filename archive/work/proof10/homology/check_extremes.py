"""Exact short-Lee-bar decomposition from KnotInfo's Q reduced Kh vectors.

For fusion-one ribbon knots, Sarkar's extortion bound gives P=1+(1+tq^2)S.
The division below also tests other knots with s=0, but does not certify their
fusion number or that a positive quotient alone is their Lee barcode.
"""
import ast,json
from collections import defaultdict
from pathlib import Path
root=Path(__file__).parent
data=json.load(open(root/'polys.json'))
meta={r['name']:r for r in json.load(open(root/'metadata.json'))}
out=[]
for row in data:
    vec=row.get('khovanov_reduced_rational_vector')
    if not isinstance(vec,str) or not vec.startswith('['): continue
    P=defaultdict(int)
    for mod,m,h,q in ast.literal_eval(vec):
        assert mod==1
        P[h,q]+=m
    R=P.copy();R[0,0]-=1
    S={}
    valid=True
    while any(R.values()):
        p=min(k for k,v in R.items() if v)
        v=R[p]
        if v<0: valid=False;break
        S[p]=v;R[p]=0
        dest=p[0]+1,p[1]+2
        R[dest]-=v
    if not valid or not S:continue
    qmin=min(q for h,q in S);qmax=max(q for h,q in S)
    extremes=[]
    for q in [qmin,qmax]:
        even=sum(v for (h,j),v in S.items() if j==q and h%2==0)
        odd=sum(v for (h,j),v in S.items() if j==q and h%2==1)
        extremes.append({'q':q,'even':even,'odd':odd,'imbalance':even-odd})
    entry={'name':row['name'],'rank':sum(P.values()),'extremes':extremes,
           'both_balanced':all(x['imbalance']==0 for x in extremes),
           'one_balanced':any(x['imbalance']==0 for x in extremes),
           'one_mixed':any(x['even'] and x['odd'] for x in extremes),
           'source':[[h,q,v] for (h,q),v in sorted(S.items())],
           'metadata':meta.get(row['name'].replace('*',''),{})}
    # Verify the full bigraded reconstruction, not just the Euler polynomial.
    reco=defaultdict(int);reco[0,0]=1
    for (h,q),v in S.items():reco[h,q]+=v;reco[h+1,q+2]+=v
    assert {k:v for k,v in reco.items() if v}=={k:v for k,v in P.items() if v}
    out.append(entry)
json.dump(out,open(root/'extreme_results.json','w'),indent=2)
print('all positive short-bar decompositions at s=0:',len(out))
for typ in ['both_balanced','one_balanced','one_mixed']:
    chosen=[x for x in out if x[typ]]
    print(typ,len(chosen))
    for x in chosen[:40]:print(x['name'],x['rank'],x['extremes'],x['metadata'])
