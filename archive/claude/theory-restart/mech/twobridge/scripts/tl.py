"""Kauffman bracket of kht++ Morse words by a Temperley-Lieb transfer computation, and the quotient-tangle word of a half diagram
(transcription of Tangle::quotient() in khtpp/sources/modules/Tangles.cpp, WITHOUT the framing twists, which only rescale).
State: dict {matching -> Laurent polynomial in A}; a matching is a tuple pairing the boundary points
('t',i) top ends and ('b',i) current bottom ends. Crossing 'x': A*id + A^-1*cupcap; 'y': A^-1*id + A*cupcap. (Which is which is
immaterial up to the mirror A <-> A^-1; calibrated against the data below.)
"""
import sympy as sp
A=sp.symbols('A')
d=-A**2-A**-2
def norm(pairs): return tuple(sorted(tuple(sorted(p)) for p in pairs))
def start(ntop):
    return {norm([(('t',i),('b',i)) for i in range(ntop)]):sp.Integer(1)}, ntop
def partner(m,pt):
    for p in m:
        if p[0]==pt: return p[1]
        if p[1]==pt: return p[0]
    raise KeyError(pt)
def relabel(m,f):
    return norm([tuple(f(x) for x in p) for p in m])
def cap(state,n,i):
    # insert new bottom points i,i+1 joined by an arc
    def f(x):
        return ('b',x[1]+2) if x[0]=='b' and x[1]>=i else x
    out={}
    for m,c in state.items():
        m2=norm(list(relabel(m,f))+[(('b',i),('b',i+1))])
        out[m2]=out.get(m2,0)+c
    return out,n+2
def cup(state,n,i):
    out={}
    for m,c in state.items():
        a=partner(m,('b',i)); b=partner(m,('b',i+1))
        rest=[p for p in m if ('b',i) not in p and ('b',i+1) not in p]
        if a==('b',i+1):
            c=c*d
        else:
            rest.append((a,b))
        def f(x):
            return ('b',x[1]-2) if x[0]=='b' and x[1]>i+1 else x
        m2=relabel(rest,f)
        out[m2]=sp.expand(out.get(m2,0)+c)
    return out,n-2
def cupcap(state,n,i):
    s,n2=cup(state,n,i); return cap(s,n2,i)
def crossing(state,n,i,kind):
    ca,cb=(A,A**-1) if kind=='x' else (A**-1,A)
    out={m:sp.expand(ca*c) for m,c in state.items()}
    s2,_=cupcap(state,n,i)
    for m,c in s2.items(): out[m]=sp.expand(out.get(m,0)+cb*c)
    return out,n
def run(word,ntop=1,state=None):
    if state is None: st,n=start(ntop)
    else: st,n=state
    for t in word.split('.'):
        if not t: continue
        k=t[0]; i=int(t[1:])
        if k in 'lr': st,n=cap(st,n,i)
        elif k=='u': st,n=cup(st,n,i)
        else: st,n=crossing(st,n,i,k)
    return st,n
def quotient_word(half):
    toks=half.split('.')
    assert toks[0]=='s'
    out=['r1','r2']
    for t in toks[1:]:
        k=t[0]; s=int(t[1:])
        if k in 'xy':
            if s==0: out+=[k+'0',k+'1',k+'1',k+'0']
            else: out+=[k+str(2*s),k+str(2*s-1),k+str(2*s+1),k+str(2*s)]
        elif k in 'lr': out+=[k+str(2*s-1),k+str(2*s)]
        elif k=='u': out+=[k+str(2*s),k+str(2*s-1)]
    out.append('u0')
    return '.'.join(out)
Q0=norm([(('t',0),('b',2)),(('b',0),('b',1))])     # kht++ 'l0': top-b3, cap b1-b2  (horizontal, slope 0)
Qinf=norm([(('t',0),('b',0)),(('b',1),('b',2))])   # kht++ 'l1': top-b1, cap b2-b3  (vertical, slope infinity)
def J_of_half(half):
    st,n=run(quotient_word(half))
    assert n==3
    y=st.get(Q0,0); z=st.get(Qinf,0)
    return sp.factor(sp.cancel(y/(y+d*z)))
if __name__=='__main__':
    for h in ['s.l1.y0.x1.u2','s.l1.y0.y0.x1.u2','s.l1.y0.x1.x1.u2','s.l1.y0.x1.y0.x1.u2']:
        print(h, J_of_half(h))
