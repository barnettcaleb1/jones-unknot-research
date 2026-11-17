"""Exact W(6,2) probes. No search on import.

beta acts on columns right-to-left. sigma_i=A I + A^-1 e_i.
I is top cap state, J bottom cup state. Return the TL2 id coefficient.
Zero coefficients and bare endpoint connectivity NEVER certify splitness.
"""
from collections import defaultdict
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'pass4'))
import braid_ren_cable as rc
STATES=rc.basis(6,2)
INDEX={s:i for i,s in enumerate(STATES)}
assert len(STATES)==9
TRANS=[[(INDEX[t] if t is not None else None,l) for t,l in
        (rc.transition(s,i) for s in STATES)] for i in range(5)]
def caps(s): return [(i,j) for i,j in enumerate(s) if i<j]
GRAM=[[rc.cap_weight(s,caps(t)) for s in STATES] for t in STATES]
def clean(p): return {e:c for e,c in p.items() if c}
def addto(p,q,k=0,m=1):
    for e,c in q.items():p[e+k]+=m*c
def delta(p):
    q=defaultdict(int);addto(q,p,2,-1);addto(q,p,-2,-1)
    return clean(q)
def action(word,j):
    vec=[{} for _ in STATES];vec[j]={0:1}
    for letter in reversed(word):
        sign=1 if letter>0 else -1
        nxt=[defaultdict(int) for _ in STATES]
        for k,p in enumerate(vec):
            if not p:continue
            addto(nxt[k],p,sign)
            dest,loops=TRANS[abs(letter)-1][k]
            if dest is not None:addto(nxt[dest],delta(p) if loops else p,-sign)
        vec=[clean(p) for p in nxt]
    return vec
def pair(vec,i):
    out=defaultdict(int)
    for p,loops in zip(vec,GRAM[i]):
        if loops is None:continue
        for _ in range(loops):p=delta(p)
        addto(out,p)
    return clean(out)
def coefficient(word,i,j):return pair(action(word,j),i)
def coefficient_matrix(word):
    columns=[action(word,j) for j in range(9)]
    return [[pair(v,i) for v in columns] for i in range(9)]
def geometry(word,i,j):
    """Bare incidence ONLY. Top endpoints precede bottom in boundary_pairs."""
    perm=list(range(6))
    for x in word:
        k=abs(x)-1;perm[k],perm[k+1]=perm[k+1],perm[k]
    edges=[(top,6+bottom) for bottom,top in enumerate(perm)]
    edges+=caps(STATES[i])+[(6+a,6+b) for a,b in caps(STATES[j])]
    cc=rc.bk.search.components(edges,12)
    ends=[x for x in range(6) if STATES[i][x]==-1]
    ends += [6+x for x in range(6) if STATES[j][x]==-1]
    groups=defaultdict(list)
    for k,v in enumerate(cc):groups[v].append(k)
    closed=[g for g in groups.values() if not set(g)&set(ends)]
    pairs=[[ends.index(x) for x in g if x in ends] for g in groups.values() if set(g)&set(ends)]
    assert all(len(p)==2 for p in pairs)
    return {'closed_components':len(closed),'boundary_pairs':pairs}
def tangle(word,i,j):
    sys.path.insert(0,str(ROOT.parent/'braid_classification/packages'))
    from spherogram.links.tangles import BraidTangle,Tangle,join_strands
    t=BraidTangle(word,6).copy();ends=t.adjacent.copy()
    # Spherogram orders bottom then top, with first braid letter on top.
    for a,b in caps(STATES[j]):join_strands(ends[a],ends[b])
    for a,b in caps(STATES[i]):join_strands(ends[6+a],ends[6+b])
    remain=[ends[k] for k in range(6) if STATES[j][k]==-1]
    remain += [ends[6+k] for k in range(6) if STATES[i][k]==-1]
    return Tangle((2,2),t.crossings,remain)
def closure_checks(word,i,j):
    sys.path.insert(0,str(ROOT.parent/'braid_classification/packages'))
    import regina
    out={}
    for name in ('numerator_closure','denominator_closure'):
        L=getattr(tangle(word,i,j),name)();pd=L.PD_code()
        R=regina.Link.fromPD([[x+1 for x in row] for row in pd])
        # PD codes omit crossing-free unknot components. Preserve them before
        # computing Jones or treating a closure as an actual unknot.
        omitted=int(L.unlinked_unknot_components)
        if omitted:R.insertLink(regina.Link(omitted))
        assert R.countComponents()==len(L.link_components)+omitted
        before=R.countComponents();J=str(R.jones());R.simplify()
        out[name]={'PD':pd,'Jones':J,'components':before,'simplified_crossings':R.size(),
                   'simplified_components':R.countComponents(),
                   'restored_crossing_free_components':omitted,
                   'unknot_certified':R.size()==0 and R.countComponents()==1}
    return out
def inv(w):return [-x for x in reversed(w)]
def reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def comm(a,b):return reduce(a+b+inv(a)+inv(b))
def validate():
    rc.verify_relations(6,2)
    for j in range(9):
        ident=action([],j)
        for i in range(1,6):assert action([i,-i],j)==ident
        for i in range(1,5):assert action([i,i+1,i],j)==action([i+1,i,i+1],j)
    for i in range(9):
        assert coefficient([],i,i)=={4:1,0:2,-4:1}
        for j in range(9):assert coefficient([],i,j)==coefficient([],j,i)
    return {'dimension':9,'checks':'TL, inverse and braid relations; Gram symmetry and diagonal delta^2'}
if __name__=='__main__':
    print(json.dumps(validate()))
    print(json.dumps({'states':STATES,'adjacent_cap_state_indices':[i for i,s in enumerate(STATES) if all(b==a+1 for a,b in caps(s))]}))
