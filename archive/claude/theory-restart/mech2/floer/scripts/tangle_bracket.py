#!/usr/bin/env python3
"""Kauffman bracket vector of a 4-ended tangle given by a kht++ Morse word with ONE top end (the special end T) and three bottom ends.
Independent check of J (no Khovanov homology involved). Polynomials: dict {A-exponent: coeff}."""
import sys
def padd(p,q,c=1):
    for e,v in q.items():
        nv=p.get(e,0)+c*v
        if nv: p[e]=nv
        elif e in p: del p[e]
def pshift(p,k,c=1): return {e+k:c*v for e,v in p.items()}
def pdelta(p):
    r={}; padd(r,pshift(p,2,-1)); padd(r,pshift(p,-2,-1)); return r
def cap(m,i):
    m2=[(x+2 if x>=i else x) for x in m]   # -1 stays -1
    m2[i:i]=[i+1,i]
    return tuple(m2)
def cup(m,i):
    p,q=m[i],m[i+1]; m=list(m); loop=False
    if p==i+1: loop=True
    else:
        if p==-1: m[q]=-1
        elif q==-1: m[p]=-1
        else: m[p]=q; m[q]=p
    del m[i:i+2]
    m=[(x-2 if x>i+1 else x) for x in m]
    return tuple(m),loop
def bracket_vec(word):
    toks=[(t[0],int(t[1:])) for t in word.split('.') if t]
    state={(-1,):{0:1}}
    for c,i in toks:
        new={}
        for m,p in state.items():
            if c in 'lr':
                padd(new.setdefault(cap(m,i),{}),p)
            elif c=='u':
                m2,loop=cup(m,i); padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=cup(m,i); q=pdelta(p) if loop else p
                padd(new.setdefault(cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    return state
def pmul(p,q):
    r={}
    for e,v in p.items():
        for f,w in q.items():
            r[e+f]=r.get(e+f,0)+v*w
    return {e:v for e,v in r.items() if v}
def pdivmono(p,q):
    """p / q when q is a monomial"""
    (e,v),=q.items()
    return {f-e:w*v for f,w in p.items()}   # v = +-1
if __name__=='__main__':
    w=sys.argv[1]
    st=bracket_vec(w)
    for m,p in st.items(): print(m,len(p),sorted(p.items()))
    D={2:-1,-2:-1}
    ms=list(st)
    if len(ms)==2:
        a,b=st[ms[0]],st[ms[1]]
        for (x,y,nm) in ((a,b,str(ms[0])+' is b'),(b,a,str(ms[1])+' is b')):
            u={}; padd(u,x); padd(u,pmul(D,y))
            print('assume',nm,': u = y + delta x has',len(u),'terms',sorted(u.items()) if len(u)<4 else '')
            if len(u)==1:
                J=pdivmono(x,u)
                print('  J = y/u in A:',sorted(J.items()))
