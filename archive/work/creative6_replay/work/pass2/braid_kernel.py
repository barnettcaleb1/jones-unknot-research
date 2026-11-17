#!/usr/bin/env python3
"""Exact B5 Burau-kernel construction and full TL5 Jones evaluations.

Source: Bigelow, GT 3 (1999) 397--404, p403, for the two conjugated
factors. We use [x,y]=xyx^-1y^-1; Bigelow p399 uses x^-1y^-1xy.
Both belong to the all-integer exponent family studied here. Sage braid
documentation uses our convention. No numerical interpolation is used.
"""
import sys, pathlib, json, time, itertools
from collections import defaultdict
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'attack_search'))
import search
from functools import lru_cache
search.tables=lru_cache(None)(search.tables)

def inv(w): return [-s for s in reversed(w)]
def reduce(w):
    out=[]
    for s in w:
        if out and out[-1]==-s: out.pop()
        else: out.append(s)
    return out
def comm(a,b): return reduce(a+b+inv(a)+inv(b))
def power(w,k): return reduce((w if k>=0 else inv(w))*abs(k))
def conjugate(w,c): return reduce(inv(c)+w+c)
def shift(p,k,c=1): return {e+k:v*c for e,v in p.items()}
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for e,c in p.items():out[e]+=c
    return {e:c for e,c in out.items() if c}

PSI1=[-3,2,1,1,2,4,4,4,3,2]
PSI2=[-4,3,2,-1,-1,2,1,1,2,2,1,4,4,4,4,4]
HALF=conjugate([4],PSI1)
FULL=conjugate([4,3,2,1,1,2,3,4],PSI2)
KERNEL=comm(HALF,FULL)
ANCHOR=[1,2,3,4]

def burau(w,n=5):
    """Unreduced Burau, generators have block[[1-t,t],[1,0]]."""
    m=[[{0:1} if i==j else {} for j in range(n)] for i in range(n)]
    for s in w:
        i=abs(s)-1
        for row in m:
            a,b=row[i],row[i+1]
            if s>0: row[i],row[i+1]=add(a,shift(a,1,-1),b),shift(a,1)
            else: row[i],row[i+1]=shift(b,-1),add(a,b,shift(b,-1,-1))
    return m
def identity(m):
    return all(p==({0:1} if i==j else {}) for i,row in enumerate(m) for j,p in enumerate(row))

def permutation(w,n=5):
    p=list(range(n))
    for s in w:
        i=abs(s)-1;p[i],p[i+1]=p[i+1],p[i]
    return p

def summarize(label,w):
    started=time.monotonic();v=search.jones_a(w,5)
    assert all(e%4==0 for e in v),v
    vt={-e//4:c for e,c in v.items()}
    return dict(label=label,word=w,length=len(w),jones_one=vt=={0:1},
                jones_t=vt,min_degree=min(vt),max_degree=max(vt),
                max_coefficient=max(abs(c) for c in vt.values()),seconds=time.monotonic()-started)

def tl_vector(w,vec=None,n=5):
    ident,ts,loops=search.tables(n)
    if vec is None:
        vec=[{} for _ in loops];vec[ident]={0:1}
    for s in w:
        nxt=[defaultdict(int) for _ in loops]
        sign=1 if s>0 else -1
        for j,p in enumerate(vec):
            search.addto(nxt[j],p,sign)
            dest,lp=ts[abs(s)-1][j]
            q=p
            for _ in range(lp):q=search.loopmul(q)
            search.addto(nxt[dest],q,-sign)
        vec=[search.clean(p) for p in nxt]
    return vec

def close_vector(vec,writhe,n=5):
    _,_,loops=search.tables(n);out=defaultdict(int)
    for j,p in enumerate(vec):
        for _ in range(loops[j]-1):p=search.loopmul(p)
        search.addto(out,p)
    return {e-3*writhe:(-1 if writhe%2 else 1)*c for e,c in search.clean(out).items()}

def validate():
    assert identity(burau([1,-1]))
    assert burau([1,2,1])==burau([2,1,2])
    assert identity(burau(KERNEL))
    assert permutation(KERNEL)==list(range(5))
    assert sum(1 if s>0 else -1 for s in KERNEL)==0
    assert search.jones_a(ANCHOR,5)=={0:1}
    assert burau(KERNEL+ANCHOR)==burau(ANCHOR)

if __name__=='__main__':
    validate(); print('Kernel verified: freely reduced length',len(KERNEL),flush=True)
    row=summarize('Bigelow kernel times unknot anchor',KERNEL+ANCHOR)
    (ROOT/'braid_kernel_seed.json').write_text(json.dumps(dict(kernel=KERNEL,anchor=ANCHOR,result=row),indent=2))
    print({k:v for k,v in row.items() if k not in ('word','jones_t')},flush=True)
