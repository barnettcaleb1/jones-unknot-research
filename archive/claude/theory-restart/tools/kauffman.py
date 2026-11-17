#!/usr/bin/env python3
"""Kauffman bracket of the completed (symmetrized) knot diagram of a kht++ half-diagram word, by sweeping the Morse word.
bracket(word) -> dict {A-exponent: coeff} for <D>/delta  (so the unknot gives a monomial)."""
import sys
import alex
def padd(p,q,c=1):
    for e,v in q.items():
        nv=p.get(e,0)+c*v
        if nv: p[e]=nv
        elif e in p: del p[e]
def pshift(p,k,c=1): return {e+k:c*v for e,v in p.items()}
def pdelta(p):
    r={}
    padd(r,pshift(p,2,-1)); padd(r,pshift(p,-2,-1)); return r
def cap(m,i):
    # insert matched pair at positions i,i+1
    m2=[(x+2 if x>=i else x) for x in m]
    m2[i:i]=[i+1,i]
    return tuple(m2)
def cup(m,i):
    """returns (new matching, closed_loop?)"""
    p,q=m[i],m[i+1]
    m=list(m)
    loop=False
    if p==i+1: loop=True
    else:
        m[p]=q; m[q]=p
    del m[i:i+2]
    m=[(x-2 if x>i+1 else x) for x in m]
    return tuple(m),loop
def bracket(word):
    full=alex.symmetrize(alex.parse(word))
    if full is None: return None
    state={(1,0):{0:1}}
    for c,i in full:
        new={}
        for m,p in state.items():
            if c in 'lr':
                if i>len(m): return None
                padd(new.setdefault(cap(m,i),{}),p)
            elif c=='u':
                if i+1>=len(m): return None
                m2,loop=cup(m,i)
                padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                if i+1>=len(m): return None
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=cup(m,i)
                q=pdelta(p) if loop else p
                padd(new.setdefault(cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    if set(state)-{()}: return None
    p=state.get((),{})
    # divide by delta = -A^2 - A^-2
    r={}; p=dict(p)
    while p:
        e=max(p); v=p[e]
        r[e-2]=-v
        padd(p,{e:-v,e-4:-v})
    return r
def normal(p):
    """shift so min exponent 0; fix sign of lowest coeff positive -> tuple key (mirror not identified)"""
    if not p: return ()
    lo=min(p); s=1 if p[lo]>0 else -1
    return tuple(sorted((e-lo,s*v) for e,v in p.items()))
def key(p):
    a=normal(p); hi=max(e for e,_ in a) if a else 0
    b=tuple(sorted((hi-e,v) for e,v in a))
    if b and b[0][1]<0: b=tuple((e,-v) for e,v in b)
    return min(a,b)
if __name__=='__main__':
    for w in sys.argv[1:]:
        p=bracket(w); print(w,len(p),sorted(p.items()))
