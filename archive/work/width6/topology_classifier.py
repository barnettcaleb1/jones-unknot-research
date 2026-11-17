"""Cheap one-sided split certificates for cap-beta-cup tangles.

No braid search. No failure of simplification is called nonsplit.
Indices/word conventions come from probe.py. Tangles with closed components
are excluded before Reidemeister simplification.
"""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent))
import probe
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
from spherogram.links.links_base import Crossing,Strand,CrossingStrand
from spherogram.links.tangles import join_strands

def simplify_open(T):
    """Reidemeister I/II away from boundary; retain a move log."""
    for S in list(T.crossings):
        if isinstance(S,Strand):
            assert S.adjacent[0][0] is not S,'closed strand excluded'
            S.fuse();T.crossings.remove(S)
    if not getattr(T,'_unique_labels',False):
        for k,C in enumerate(T.crossings):C.label=k
        T._unique_labels=True
    moves=[]
    while True:
        hit=False
        # Exhaust all RI first: a proposed RII partner can itself carry
        # an RI loop, in which case the four-end RII splice degenerates.
        for C in list(T.crossings):
            for a in range(4):
                if C.adjacent[a]==(C,(a+1)%4):
                    p,q=C.adjacent[a+2],C.adjacent[a+3]
                    assert p[0] is not C and q[0] is not C
                    join_strands(p,q);T.crossings.remove(C)
                    moves.append(['R1',C.label,a]);hit=True;break
            if hit:break
        if hit:continue
        for C in list(T.crossings):
            for a in range(4):
                B,b=C.adjacent[a];D,d=C.adjacent[a+1]
                if isinstance(B,Crossing) and B is not C and B is D and (b-1)%4==d and (a+b)%2==0:
                    # Match Spherogram's local RII splice, but allow Tangle
                    # endpoints and never treat the boundary as a crossing.
                    W,w=C.adjacent[a+2];X,x=C.adjacent[a+3]
                    Y,y=B.adjacent[b+1];Z,z=B.adjacent[b+2]
                    if W is not B:join_strands((W,w),(Z,z))
                    if X is not B:join_strands((X,x),(Y,y))
                    T.crossings.remove(C);T.crossings.remove(B)
                    moves.append(['R2',C.label,B.label,a,b]);hit=True;break
            if hit:break
        if not hit:return moves

def components_and_mixed(T,with_over=False):
    seen={};pairs=[]
    for endpoint in range(4):
        if ('boundary',endpoint) in seen:continue
        ci=len(pairs);seen[('boundary',endpoint)]=ci
        C,k=T.adjacent[endpoint]
        while C is not T:
            assert isinstance(C,Crossing)
            assert (C,k) not in seen,'unexpected internal closed loop'
            seen[C,k]=seen[C,(k+2)%4]=ci
            C,k=C.adjacent[k+2]
        seen['boundary',k]=ci;pairs.append([endpoint,k])
    mixed=[]
    over=[]
    for C in T.crossings:
        assert all((C,k) in seen for k in range(4))
        if seen[C,0]!=seen[C,1]:mixed.append(C.label);over.append(seen[C,1])
    return (pairs,mixed,over) if with_over else (pairs,mixed)

def triangles(T):
    """Internal triangular faces only; boundary-adjacent regions excluded."""
    ans=[];seen=set()
    for C in T.crossings:
        for a in range(4):
            face=[];X,k=C,a
            for _ in range(3):
                if not isinstance(X,Crossing):break
                face.append(CrossingStrand(X,k));X,k=X.adjacent[k+1]
            if len(face)!=3 or X is not C or k!=a:continue
            key=frozenset((e.crossing.label,e.strand_index) for e in face)
            if key in seen:continue
            seen.add(key)
            if len({e.crossing for e in face})!=3:continue
            if sum(e.strand_index%2 for e in face) not in (1,2):continue
            while face[1][1]%2!=0 or face[2][1]%2!=1:face=face[1:]+face[:1]
            ans.append(face)
    return ans

def move_III(T,triple):
    """Spherogram's RIII local rewiring, using boundary-safe join_strands."""
    A,B,C=(t.crossing for t in triple);a,b,c=(t.strand_index for t in triple)
    border=[(C,c-1),(C,c-2),(A,a-1),(A,a-2),(B,b-1),(B,b-2)]
    strands=[]
    for X,x in border:
        x%=4;Y,y=X.adjacent[x];S=Strand()
        join_strands((S,0),(X,x));join_strands((S,1),(Y,y));strands.append(S)
    for S,(X,x) in zip(strands,[(A,a),(B,b+1),(B,b),(C,c+1),(C,c),(A,a+1)]):
        join_strands((X,x%4),(S,0))
    for p,q in [((A,a-1),(B,b+2)),((B,b-1),(C,c+2)),((C,c-1),(A,a+2))]:
        join_strands((p[0],p[1]%4),(q[0],q[1]%4))
    for S in strands:S.fuse()

def classify_with_III(word,i,j,seed=0,steps=1000):
    import random
    rng=random.Random(seed);T=probe.tangle(word,i,j);moves=simplify_open(T)
    for step in range(steps+1):
        pairs,mixed=components_and_mixed(T)
        if not mixed:
            return {'classification':'split_certified_RIII','seed':seed,'steps':step,
                    'remaining_crossings':len(T.crossings),'moves':moves,
                    'trivial_tangle_certified':len(T.crossings)==0}
        ts=triangles(T)
        if not ts:break
        t=rng.choice(ts);moves.append(['R3',[(e.crossing.label,e.strand_index) for e in t]])
        move_III(T,t);moves.extend(simplify_open(T))
    return {'classification':'unknown','seed':seed,'steps':step,'remaining_crossings':len(T.crossings),'mixed_crossings':len(mixed)}

def classify(word,i,j):
    geo=probe.geometry(word,i,j)
    out={'word':word,'i':i,'j':j,'geometry':geo}
    if geo['closed_components']:
        out['classification']='excluded_closed_components';return out
    T=probe.tangle(word,i,j);moves=simplify_open(T)
    pairs,mixed=components_and_mixed(T)
    out.update({'reidemeister_moves':moves,'remaining_crossings':len(T.crossings),
                'boundary_pairs_bottom_then_top':pairs,'mixed_crossings':mixed})
    if not mixed:
        out['classification']='split_certified'
        out['certificate']='After boundary-relative R1/R2, the two arc projections have no shared crossing.'
        out['trivial_tangle_certified']=len(T.crossings)==0
    else:out['classification']='unknown'
    return out

if __name__=='__main__':
    data=json.load(sys.stdin)
    if isinstance(data,dict):data=[data]
    print(json.dumps([classify(r['word'],r['i'],r['j']) for r in data],indent=2))
