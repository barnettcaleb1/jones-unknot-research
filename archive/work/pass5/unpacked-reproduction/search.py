#!/usr/bin/env python3
"""Exact TL4 Jones checks, and tables for a reproducible finite-field search.

Conventions: sigma_i = A*1 + A^-1*e_i; loop value d=-A^2-A^-2.
The closure bracket has one loop normalized to 1; V=(-A)^(-3*w)*bracket.
Thus Jones=1 iff bracket={3*w: (-1)**w}. No floating-point arithmetic.
"""
from collections import defaultdict
import json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parent

def matchings(xs):
    if not xs:
        yield ()
        return
    for k in range(1,len(xs),2):
        for a in matchings(xs[1:k]):
            for b in matchings(xs[k+1:]):
                yield ((xs[0],xs[k]),)+a+b

def canonical(pairs,n):
    out=[0]*(2*n)
    for a,b in pairs: out[a]=b; out[b]=a
    return tuple(out)

def components(edges,nv):
    parent=list(range(nv))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    for a,b in edges:
        a,b=find(a),find(b)
        if a!=b: parent[a]=b
    return [find(a) for a in range(nv)]

def compose(a,b,n):
    # Three rows: input, glued row, output.
    edges=[(i,a[i]) for i in range(2*n) if i<a[i]]
    edges += [(i+n,b[i]+n) for i in range(2*n) if i<b[i]]
    cc=components(edges,3*n)
    outer=list(range(n))+list(range(2*n,3*n))
    groups=defaultdict(list)
    for j,k in enumerate(outer): groups[cc[k]].append(j)
    assert all(len(v)==2 for v in groups.values())
    loops=len(set(cc))-len(groups)
    return canonical(groups.values(),n),loops

def tables(n):
    order=list(range(n))+list(range(2*n-1,n-1,-1))
    basis=[canonical(p,n) for p in matchings(order)]
    ix={x:i for i,x in enumerate(basis)}
    ident=canonical([(j,n+j) for j in range(n)],n)
    transitions=[]
    for k in range(n-1):
        e=canonical([(k,k+1),(n+k,n+k+1)]+[(j,n+j) for j in range(n) if j not in (k,k+1)],n)
        transitions.append([(ix[c],l) for c,l in (compose(a,e,n) for a in basis)])
    loops=[]
    for a in basis:
        edges=[(j,a[j]) for j in range(2*n) if j<a[j]]+[(j,n+j) for j in range(n)]
        loops.append(len(set(components(edges,2*n))))
    return ix[ident],transitions,loops

def clean(p): return {k:v for k,v in p.items() if v}
def addto(target,p,shift=0,mult=1):
    for k,v in p.items(): target[k+shift]+=mult*v
def loopmul(p):
    out=defaultdict(int); addto(out,p,2,-1); addto(out,p,-2,-1)
    return clean(out)

def bracket(word,n=4):
    ident,ts,loops=tables(n)
    vec=[{} for _ in loops]; vec[ident]={0:1}
    for s in word:
        nxt=[defaultdict(int) for _ in loops]
        sign=1 if s>0 else -1
        for j,p in enumerate(vec):
            addto(nxt[j],p,sign)
            dest,lp=ts[abs(s)-1][j]
            q=p
            for _ in range(lp): q=loopmul(q)
            addto(nxt[dest],q,-sign)
        vec=[clean(p) for p in nxt]
    out=defaultdict(int)
    for j,p in enumerate(vec):
        for _ in range(loops[j]-1): p=loopmul(p)
        addto(out,p)
    return clean(out)

def jones_a(word,n=4):
    w=sum(1 if x>0 else -1 for x in word)
    sign=-1 if w%2 else 1
    return {e-3*w:c*sign for e,c in bracket(word,n).items()}

def knot(word,n=4):
    perm=list(range(n))
    for s in word:
        k=abs(s)-1; perm[k],perm[k+1]=perm[k+1],perm[k]
    seen={0}; q=perm[0]
    while q not in seen: seen.add(q); q=perm[q]
    return len(seen)==n

def validate():
    assert jones_a([1],2)=={0:1}
    assert jones_a([1,1,1],2)=={-4:1,-12:1,-16:-1}
    assert jones_a([1,-2,1,-2],3)=={-8:1,-4:-1,0:1,4:-1,8:1}
    tests=[[1,2,3],[1,1,1,2,3],[1,-2,1,-2,3],[1,-2,3,1,2,-3,2,-1,3]]
    for word in tests:
        v=jones_a(word)
        assert jones_a([-s for s in word])=={-k:c for k,c in v.items()}
        assert jones_a(word+[2,-2])==v
        assert jones_a(word+[1,2,1])==jones_a(word+[2,1,2])
        assert jones_a(word+[1,3])==jones_a(word+[3,1])
    assert jones_a([1,1,1,2,3])==jones_a([1,1,1],2)
    assert jones_a([1,1,1,2,-3])==jones_a([1,1,1],2)
    assert knot([1,2,3]) and not knot([1,2,3,3])
    print('Known trefoil, figure-eight, unknot, mirror, braid-relation and stabilization checks passed.')

def write_tables():
    ident,ts,loops=tables(4)
    (ROOT/'tables.json').write_text(json.dumps({'identity':ident,'transitions':ts,'loops':loops}))
    with (ROOT/'tables.h').open('w') as f:
        f.write('const int identity='+str(ident)+';\n')
        f.write('const int dest[3][14]={'+','.join('{'+','.join(str(d) for d,l in t)+'}' for t in ts)+'};\n')
        f.write('const int lp[3][14]={'+','.join('{'+','.join(str(l) for d,l in t)+'}' for t in ts)+'};\n')
        f.write('const int loops[14]={'+','.join(map(str,loops))+'};\n')

if __name__=='__main__':
    validate(); write_tables()
    if len(sys.argv)>1:
        src=pathlib.Path(sys.argv[1]); out=[]
        for line in src.read_text().splitlines():
            w=list(map(int,line.split()))
            v=jones_a(w)
            out.append({'word':w,'knot':knot(w),'jones_one':v=={0:1},'jones_A':v})
        (ROOT/'exact_hits.json').write_text(json.dumps(out,indent=2))
        print('Exact checks:',len(out),'Jones=1:',sum(r['jones_one'] for r in out))
