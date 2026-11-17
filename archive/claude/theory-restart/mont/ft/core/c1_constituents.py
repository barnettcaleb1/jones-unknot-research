# Constituent knots of the quotient theta-curve of a half-word.
# Quotient picture: axis at position 0, half-strand k at position k+1 (everything lies right of the axis).
# K_in  = arc u A_in  (A_in = axis segment between the two vertices): y0/x0 -> full twist (c,0),(c,0) of arc around A_in.
# K_out = arc u A_out (A_out = rest of the axis, isotopic to a strand at position 0 meeting nothing): y0/x0 deleted.
# Start: implicit cap (0,1) (vertex v_top joins axis and arc); end: cup ('u',0) (vertex v_bot).
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex, kauffman
from kauffman import padd, pshift, pdelta, cap, cup
import clib, lp
def raw_bracket(full):
    state={(1,0):{0:1}}
    for c,i in full:
        new={}
        for m,p in state.items():
            if c in 'lr':
                if i>len(m): return None
                padd(new.setdefault(cap(m,i),{}),p)
            elif c=='u':
                if i+1>=len(m): return None
                m2,loop=cup(m,i); padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                if i+1>=len(m): return None
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=cup(m,i); q=pdelta(p) if loop else p
                padd(new.setdefault(cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    if set(state)-{()}: return None
    p=dict(state.get((),{})); r={}
    while p:
        e=max(p); v=p[e]; r[e-2]=-v; padd(p,{e:-v,e-4:-v})
    return r
def constituent_words(word):
    half=alex.parse(word)
    kin=[]; kout=[]
    for c,s in half:
        if c in 'xy' and s==0:
            kin+=[(c,0),(c,0)]
        elif c in 'xy':
            kin.append((c,s)); kout.append((c,s))
        elif c in 'lr':
            kin.append((c,s)); kout.append((c,s))
        elif c=='u':
            kin.append(('u',s)); kout.append(('u',s))
    kin.append(('u',0)); kout.append(('u',0))
    return kin,kout
def V_of_bracket(kb):
    if not kb: return None
    kb={e:c for e,c in kb.items() if c}
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}
    d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}
def constituents(word):
    kin,kout=constituent_words(word)
    Vi=V_of_bracket(raw_bracket(kin)); Vo=V_of_bracket(raw_bracket(kout))
    return Vi,Vo
if __name__=='__main__':
    for w in ('s.l1.u2','s.l1.y0.x1.u2','s.l1.x0.y1.u2','s.l1.y0.y0.x1.u2','s.l1.x0.x0.y1.u2','s.l1.y0.x1.y0.x1.u2','s.l1.x0.x0.x0.x1.x1.u2'):
        Vi,Vo=constituents(w)
        print(w,' K_in V=',sorted(Vi.items()) if Vi else Vi,' K_out V=',sorted(Vo.items()) if Vo else Vo)
