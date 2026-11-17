"""Referee's own Kauffman-bracket (Temperley-Lieb) calculus for 'cap + braid' pictures.
A state is a linear combination of crossingless matchings of the points {'T'} u {0..n-1} (T = the single top end, 0..n-1 = bottom points,
read left to right), coefficients Laurent polynomials in A (dict exponent -> int).
Crossing between bottom positions i,i+1:   type 'y' :  A * id + A^-1 * U_i ,   type 'x' :  A^-1 * id + A * U_i   (mutually inverse).
Loop value delta = -A^2 - A^-2."""
from lp import add, mul, mon, clean, ONE, ZERO
DELTA={2:-1,-2:-1}
def norm(pairs): return frozenset(frozenset(p) for p in pairs)
def partner(m,pt):
    for p in m:
        if pt in p:
            (o,)=p-{pt}; return o
    raise KeyError(pt)
def U(state,i):
    """apply cup-cap at bottom positions i,i+1"""
    out={}
    for m,c in state.items():
        p=partner(m,i); q=partner(m,i+1)
        if p==i+1:
            mm=m; cc=mul(c,DELTA)
        else:
            mm=frozenset(x for x in m if i not in x and (i+1) not in x)|{frozenset((p,q)),frozenset((i,i+1))}; cc=c
        out[mm]=add(out.get(mm,{}),cc)
    return {m:c for m,c in out.items() if c}
def scale(state,p): return {m:mul(c,p) for m,c in state.items() if mul(c,p)}
def sadd(s1,s2):
    out=dict(s1)
    for m,c in s2.items():
        out[m]=add(out.get(m,{}),c)
    return {m:c for m,c in out.items() if c}
def crossing(state,kind,i):
    a,b=(1,-1) if kind=='y' else (-1,1)
    return sadd(scale(state,mon(a)),scale(U(state,i),mon(b)))
def apply_word(state,word):
    """word like 'y0.y1.y1.y0' """
    for tok in word.split('.'):
        if not tok: continue
        state=crossing(state,tok[0],int(tok[1:]))
    return state
def close_bottom(state,i,n):
    """join bottom positions i,i+1 by an arc below; relabel remaining bottom points 0..n-3"""
    out={}
    def rel(pt):
        if pt=='T': return 'T'
        return pt if pt<i else pt-2
    for m,c in state.items():
        p=partner(m,i); q=partner(m,i+1)
        rest=[x for x in m if i not in x and (i+1) not in x]
        if p==i+1: cc=mul(c,DELTA)
        else: rest.append(frozenset((p,q))); cc=c
        mm=frozenset(frozenset(rel(pt) for pt in x) for x in rest)
        out[mm]=add(out.get(mm,{}),cc)
    return {m:c for m,c in out.items() if c}
LETTER={'Y':'y0.y1.y1.y0','y':'x0.x1.x1.x0','X':'x2.x1.x3.x2','x':'y2.y1.y3.y2'}
E1=norm([('T',0),(1,4),(2,3)])
E0=norm([('T',0),(1,2),(3,4)])
E2=norm([('T',4),(0,1),(2,3)])
B4=norm([('T',2),(0,1)])   # after closing (0,1): points T,0,1,2 = c_2, m_1^+, m_2^-, m_2^+ ;  b = (T m_2^+)(m_1^+ m_2^-)
C4=norm([('T',0),(1,2)])   #                                                              c = (T m_1^+)(m_2^- m_2^+)
def tangle_vector(word):
    """bracket vector (coefficient of b, coefficient of c) of T_w, w = string in YXyx, L_1 first (nearest the cap)"""
    s={E1:ONE}
    for L in word: s=apply_word(s,LETTER[L])
    s=close_bottom(s,0,5)
    assert set(s)<= {B4,C4}, s
    return s.get(B4,{}), s.get(C4,{})
