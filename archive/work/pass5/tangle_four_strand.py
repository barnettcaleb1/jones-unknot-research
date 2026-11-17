"""Exact TL4 element and actual topology for Ren's capped six-strand core.

No new searches: supplies a finite exact interface for arbitrary B4 top braids.
"""
from pathlib import Path
import sys,json
from collections import defaultdict
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pass4'))
import tangle_ren_twists as six
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'braid_classification/packages'))
from spherogram.links.tangles import BraidTangle,Tangle,join_strands

N=4
ORDER=list(range(N))+list(range(2*N-1,N-1,-1))
BASIS=[six.search.canonical(p,N) for p in six.search.matchings(ORDER)]
INDEX={b:i for i,b in enumerate(BASIS)}
IDENT,TRANSITIONS,_=six.search.tables(N)
SURVIVORS=[0,1,4,5,6,7,10,11]

def partial_cap(diagram):
    adj=defaultdict(list)
    for i,j in enumerate(diagram):
        if i<j:adj[i].append(j);adj[j].append(i)
    for i,j in [(2,3),(8,9)]:adj[i].append(j);adj[j].append(i)
    remaining=set(range(12));pairs=[];loops=0
    for start in SURVIVORS:
        if start not in remaining:continue
        prev=None;cur=start
        while True:
            remaining.remove(cur)
            nxt=next((x for x in adj[cur] if x!=prev),None)
            if nxt is None:
                pairs.append((SURVIVORS.index(start),SURVIVORS.index(cur)));break
            prev,cur=cur,nxt
    while remaining:
        loops+=1;first=next(iter(remaining));prev=None;cur=first
        while True:
            remaining.remove(cur)
            nxt=adj[cur][0] if adj[cur][0]!=prev else adj[cur][1]
            prev,cur=cur,nxt
            if cur==first:break
    return six.search.canonical(pairs,N),loops

CORE=[{} for _ in BASIS]
for coefficient,diagram in zip(six.vec,six.basis):
    result,loops=partial_cap(diagram)
    for _ in range(loops):coefficient=six.mul(coefficient,six.DELTA)
    i=INDEX[result];CORE[i]=six.add(CORE[i],coefficient)
assert not CORE[IDENT]

def closure_type(diagram):
    adj=defaultdict(list)
    for i,j in enumerate(diagram):
        if i<j:adj[i].append((j,0));adj[j].append((i,0))
    for i in range(N):adj[i].append((i+N,1));adj[i+N].append((i,-1))
    remaining=set(range(2*N));contractible=essential=0
    while remaining:
        first=next(iter(remaining));prev=None;cur=first;w=0
        while True:
            remaining.remove(cur)
            options=adj[cur];nxt,d=options[0] if options[0][0]!=prev else options[1]
            w+=d;prev,cur=cur,nxt
            if cur==first:break
        assert abs(w)<=1
        essential+=abs(w);contractible+=int(w==0)
    return contractible,essential

TYPES=[closure_type(b) for b in BASIS]
def times_e(vec,i):
    out=[{} for _ in BASIS]
    for j,p in enumerate(vec):
        k,loops=TRANSITIONS[i-1][j]
        for _ in range(loops):p=six.mul(p,six.DELTA)
        out[k]=six.add(out[k],p)
    return out

def times_crossing(vec,i):
    ev=times_e(vec,abs(i));sgn=1 if i>0 else -1
    return [six.add(six.shift(p,sgn),six.shift(q,-sgn)) for p,q in zip(vec,ev)]

def annular(word):
    vec=CORE
    for i in word:vec=times_crossing(vec,i)
    out=defaultdict(dict)
    for p,(c,e) in zip(vec,TYPES):
        for _ in range(c):p=six.mul(p,six.DELTA)
        out[e]=six.add(out[e],p)
    return {e:p for e,p in out.items() if p}

def core_tangle():
    tt=BraidTangle(six.BASE,6).copy();e=tt.adjacent.copy()
    join_strands(e[2],e[3]);join_strands(e[8],e[9])
    return Tangle((4,4),tt.crossings,[e[i] for i in SURVIVORS])

def diagram(word,with_axis=False):
    # BraidTangle([...]) multiplies the first listed crossing at the top.
    four=core_tangle()*BraidTangle(word,4)
    if not with_axis:return four.braid_closure()
    return ((four|BraidTangle([],1))*BraidTangle([4,3,2,1,1,2,3,4],5)).braid_closure()

CONNECTIVITY=(3,5,6,0,7,1,2,4)
def component_count(word):
    perm=list(range(4))
    for i in word:perm[abs(i)-1],perm[abs(i)]=perm[abs(i)],perm[abs(i)-1]
    adj=defaultdict(list)
    for i,j in enumerate(CONNECTIVITY):
        if i<j:adj[i].append(j);adj[j].append(i)
    for i in range(4):adj[i].append(4+perm[i]);adj[4+perm[i]].append(i)
    remaining=set(range(8));components=0
    while remaining:
        components+=1;todo=[remaining.pop()]
        while todo:
            for j in adj[todo.pop()]:
                if j in remaining:remaining.remove(j);todo.append(j)
    return components

assert annular([])==six.blocks[0]
assert annular([1,3])==six.annular(1,1)
assert annular([-1,3])==six.annular(-1,1)
for word in [[],[1,3],[-1,3],[2],[1,2,3],[1,-2,3,2]]:
    actual=diagram(word)
    assert component_count(word)==len(actual.link_components)+actual.unlinked_unknot_components

out={'convention':'sigma_i=A identity + A^-1 e_i; endpoints top0..3,bottom4..7; basis order follows noncrossing matching enumeration',
     'core_six_braid':six.BASE,'core_geometric_connectivity':CONNECTIVITY,
     'basis':[list(b) for b in BASIS],'identity_index':IDENT,
     'core_Laurent_coefficients':CORE,'generator_transitions':TRANSITIONS,
     'annular_closure_types_contractible_essential':TYPES,
     'identity_coefficient_zero':True,
     'all_B4_top_braids_have_annular_degree_at_most_two':True,
     'original_Ren_top_word':[1,3],'ordinary_unknot_top_word':[-1,3]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':
    print('TL4 basis',len(BASIS),'nonzero core coefficients',sum(bool(p) for p in CORE),'identity',IDENT,CORE[IDENT])
    print('Core connectivity',CONNECTIVITY,'components',component_count([]))
