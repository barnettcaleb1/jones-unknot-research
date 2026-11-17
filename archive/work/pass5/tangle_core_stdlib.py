"""Rebuild Ren's capped TL4 core from its ten crossings, standard library only.

Uses search.py only for noncrossing matching enumeration and diagram product.
No saved coefficient data or knot-theory packages are read.
"""
from pathlib import Path
from collections import defaultdict
from types import SimpleNamespace
import sys
here=Path(__file__).resolve().parent
if not (here/'search.py').exists():
    sys.path.insert(0,str(here.parent/'attack_search'))
import search

def add(p,q):
    out=defaultdict(int,p)
    for e,c in q.items():out[e]+=c
    return {e:c for e,c in out.items() if c}
def mul(p,q):
    out=defaultdict(int)
    for e,c in p.items():
        for f,d in q.items():out[e+f]+=c*d
    return {e:c for e,c in out.items() if c}
def shift(p,e,s=1):return {k+e:c*s for k,c in p.items() if c*s}
DELTA={2:-1,-2:-1}
six=SimpleNamespace(add=add,mul=mul,shift=shift,DELTA=DELTA)

def make_basis(n):
    return [search.canonical(p,n) for p in search.matchings(list(range(n))+list(range(2*n-1,n-1,-1)))]
def cross(vec,g,transitions):
    out=[{} for _ in vec];sgn=1 if g>0 else -1
    for i,p in enumerate(vec):
        out[i]=add(out[i],shift(p,sgn))
        j,loops=transitions[abs(g)-1][i]
        for _ in range(loops):p=mul(p,DELTA)
        out[j]=add(out[j],shift(p,-sgn))
    return out

BASE=[-2,1,1,1,-2,4,-5,-5,-5,4]
basis6=make_basis(6);identity6,transitions6,_=search.tables(6)
vec6=[{} for _ in basis6];vec6[identity6]={0:1}
for crossing in BASE:vec6=cross(vec6,crossing,transitions6)

BASIS=make_basis(4);INDEX={b:i for i,b in enumerate(BASIS)}
IDENT,TRANSITIONS,_=search.tables(4)
SURVIVORS=[0,1,4,5,6,7,10,11]
def partial_cap(diagram):
    # Form the graph after adding the two caps. Outer components are paths;
    # any component missing all outer vertices contributes one delta loop.
    edges=[(i,j) for i,j in enumerate(diagram) if i<j]+[(2,3),(8,9)]
    components=search.components(edges,12)
    outer=defaultdict(list)
    for new,old in enumerate(SURVIVORS):outer[components[old]].append(new)
    assert all(len(v)==2 for v in outer.values())
    loops=len(set(components))-len(outer)
    return search.canonical(outer.values(),4),loops

CORE=[{} for _ in BASIS]
for p,diagram in zip(vec6,basis6):
    d,loops=partial_cap(diagram)
    for _ in range(loops):p=mul(p,DELTA)
    i=INDEX[d];CORE[i]=add(CORE[i],p)
assert CORE[IDENT]=={}

def closure_type(diagram):
    adj=defaultdict(list)
    for i,j in enumerate(diagram):
        if i<j:adj[i].append((j,0));adj[j].append((i,0))
    for i in range(4):adj[i].append((i+4,1));adj[i+4].append((i,-1))
    remaining=set(range(8));contractible=essential=0
    while remaining:
        first=next(iter(remaining));cur=first;prev=None;winding=0
        while True:
            remaining.remove(cur)
            options=adj[cur]
            nxt,w=options[0] if options[0][0]!=prev else options[1]
            winding+=w;prev,cur=cur,nxt
            if cur==first:break
        assert abs(winding)<=1
        essential+=abs(winding);contractible+=int(winding==0)
    return contractible,essential
TYPES=[closure_type(b) for b in BASIS]

def annular(word):
    vec=CORE
    for crossing in word:vec=cross(vec,crossing,TRANSITIONS)
    out=defaultdict(dict)
    for p,(c,e) in zip(vec,TYPES):
        for _ in range(c):p=mul(p,DELTA)
        out[e]=add(out[e],p)
    return {e:p for e,p in out.items() if p}

if __name__=='__main__':
    print('Rebuilt ten-crossing TL6 core, capped to TL4; identity coefficient zero.')
    print('TL6 basis:',len(basis6),'TL4 basis:',len(BASIS))
