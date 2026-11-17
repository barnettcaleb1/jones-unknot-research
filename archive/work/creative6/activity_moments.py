"""Exact activity interaction degree and signed transfer-current moment tests."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,contextlib,io
import tree_probe as t
with contextlib.redirect_stdout(io.StringIO()):
    import statmech_bridge as base

def represent(E,terms,energies,degree):
    features=[S for d in range(degree+1)for S in combinations(range(len(E)),d)]
    rows={}
    for tt,j in zip(terms,energies):
        T=set(tt[3]);v={i:F(1)for i,S in enumerate(features)if set(S)<=T}
        v[len(features)]=F(j)
        for pivot,row in rows.items():
            if pivot in v:
                c=v[pivot]
                for k,a in row.items():
                    v[k]=v.get(k,F(0))-c*a
                    if not v[k]:v.pop(k,None)
        pivot=next((k for k in sorted(v)if k<len(features)),None)
        if pivot is None:
            if v.get(len(features),0):return None,len(rows)
        else:
            c=v[pivot];rows[pivot]={k:a/c for k,a in v.items()}
    coeff={}
    for pivot,row in reversed(list(rows.items())):
        coeff[pivot]=row.get(len(features),0)-sum(a*coeff.get(k,0)for k,a in row.items()if k!=pivot and k<len(features))
    out={features[k]:c for k,c in coeff.items()if c}
    assert all(sum(c for S,c in out.items()if set(S)<=set(tt[3]))==j for tt,j in zip(terms,energies))
    return out,len(rows)

def signed_kernel(n,E):
    B=[]
    for a,b,s in E:
        col=[0]*(n-1)
        if a<n-1:col[a]+=1
        if b<n-1:col[b]-=1
        B.append(col)
    L=[[sum(s*col[i]*col[j]for col,(_,_,s)in zip(B,E))for j in range(n-1)]for i in range(n-1)]
    Li=base.inverse(L)
    K=[[E[i][2]*sum(a[k]*Li[k][l]*b[l]for k in range(n-1)for l in range(n-1))for b in B]for i,a in enumerate(B)]
    return K

def moment(K,coeff):
    return sum(c*base.det([[K[i][j]for j in S]for i in S])for S,c in coeff.items())

results=[]
for name in ['8_19','10_124','11n42','hard_unknot']:
    L=t.Link(braid_closure=[1,2,1,-2,-1,-2,1,2])if name=='hard_unknot'else t.Link(name)
    n,E=t.graph(L);_,terms=t.tree_terms(L)
    energies=[(p+3*L.writhe())//4 for p,s,k,T in terms]
    checks=[]
    for degree in range(1,n):
        coeff,rank=represent(E,terms,energies,degree)
        checks.append({'degree':degree,'rank':rank,'representable':coeff is not None})
        if coeff is not None:break
    K=signed_kernel(n,E)
    first=moment(K,coeff)
    squared={}
    for S,c in coeff.items():
        for T,d in coeff.items():
            U=tuple(sorted(set(S)|set(T)))
            squared[U]=squared.get(U,F(0))+c*d
    second=moment(K,squared)
    signed_weights=[-1 if k%2 else 1 for p,s,k,T in terms]
    Z=sum(signed_weights)
    assert first==F(sum(w*j for w,j in zip(signed_weights,energies)),Z)
    assert second==F(sum(w*j*j for w,j in zip(signed_weights,energies)),Z)
    row={'name':name,'minimum_degree_for_this_diagram_and_edge_order':degree,
         'exact_linear_system_checks':checks,'nonzero_interaction_terms':len(coeff),
         'activity_polynomial':[[S,str(c)]for S,c in coeff.items()],
         'signed_expectation_j_via_Green_function_minors':str(first),
         'signed_expectation_j_squared_via_Green_function_minors':str(second),
         'direct_enumeration_agrees':True}
    results.append(row)
    print(name,'minimum degree',degree,'terms',len(coeff),'signed moments',first,second)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2))
