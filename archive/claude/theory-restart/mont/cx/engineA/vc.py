"""ENGINE A vector calculus (channel coordinates).  All exact, Laurent polys as {exp:coeff} dicts (lp.py conventions).
A box vector is stored in CHANNEL coordinates v = (a, b):  a = v_1,  b = v_1 + (1-t^3) v_2   (TH-2BR (v_1,v_2) -> (a,b)).
  star product          : (a,b)*(a',b') = (a a', b b')
  Y^k                   : (a,b) -> (a, t^-3k b)            [= star with integral box (y0)^k]
  X^mu                  : (A,B) = alpha (1,1) + beta (1+t^2, -t),  alpha = (tA+(1+t^2)B)/Phi3, beta = (A-B)/Phi3,
                          X^mu (A,B) = alpha (1,1) + (-t)^mu beta (1+t^2,-t)
  necklace body r2.(y1)^m.B1..Bn.u1 : F_m(p) = unit * X^-m p   (Theorem O; unit fixed by normalising a)
  closure s.N           : J = norm(a(v_N));  twisted closure s.r2.(y1)^m.N.u1 = closure of the body F_m(N)
  vertical (Theorem V)  : J(s.l1.N.(x2)^a.u1) Phi3 =. t A + (-t)^a ((1+t^2) A + t B) + t^(3a-1) Phi5 B
Every vector is kept NORMALISED: a(v) = 1 mod (t+1)^2 (then v is the pinned vector of the body, exactly).
Trees: ('w', word)        rational leaf, word in X,x,Y,y (x=X^-1, y=Y^-1), vector rho(word) e_1 (last letter acts first)
       ('g', i)           general body i of general_boxes.json
       ('b', bodyword, v) arbitrary body with known normalised vector v
       ('n', m, [children])  necklace body r2.(y1)^m.<children>.u1   (m=0 allowed: plain stack, then it is a product)
       ('p', [children])  plain stack (product) B1.B2...Bn
Halfword dictionary (PROVED in mont/proof, Cor 3.8 / Prop 3.2 / Theorem O):
       B(Y w)=y0.B(w), B(y w)=x0.B(w), B(X w)=r2.x1.B(w).u1, B(x w)=r2.y1.B(w).u1;  node -> r2.(y1)^m.B1...Bn.u1 (x1 if m<0).
"""
import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp
from lp import clean, add, neg, sub, mul, mono, ONE, shift, top, bot, span, ev

PHI3={0:1,1:1,2:1}; PHI5={0:1,1:1,2:1,3:1,4:1}; T2P1={0:1,2:1}; ONEMT3={0:1,3:-1}

def divexact(p,d):
    p=dict(p); q={}
    if not p: return {}
    lo=bot(p)-bot(d); dt=top(d); dc=d[dt]
    while p:
        e=top(p); c=p[e]; k=e-dt
        if k<lo or c%dc: return None
        q[k]=c//dc
        for f,g in d.items():
            ee=k+f; nv=p.get(ee,0)-g*(c//dc)
            if nv: p[ee]=nv
            else: p.pop(ee,None)
    return q

def nunit(p):
    """(sgn,k) with sgn*t^k*p = 1 mod (t+1)^2, or None"""
    s=0; d=0
    for e,c in p.items():
        if e%2: s-=c; d+=e*c
        else:   s+=c; d-=e*c
    if s not in (1,-1) or d%s: return None
    k=d//s
    return (s*(-1)**(k%2), k)
def norm(p):
    u=nunit(p)
    if u is None: return None
    sg,k=u
    return {e+k:sg*c for e,c in p.items()}
def scal(v,sg,k):
    return ({e+k:sg*c for e,c in v[0].items()},{e+k:sg*c for e,c in v[1].items()})
def nv(v):
    u=nunit(v[0])
    if u is None: return None
    return scal(v,*u)

def from_th(v):   # TH-2BR (v1,v2) -> (a,b)
    return (clean(dict(v[0])), add(v[0], mul(ONEMT3, v[1])))
def to_th(v):
    q=divexact(sub(v[1],v[0]),ONEMT3)
    return (v[0],q)

def star(v,w): return (mul(v[0],w[0]), mul(v[1],w[1]))
def starall(vs):
    a=ONE; b=ONE
    for v in vs: a=mul(a,v[0]); b=mul(b,v[1])
    return (a,b)
def Ypow(k,v): return (v[0], shift(v[1],-3*k))
def tmono(mu): return {mu:(-1)**(mu%2)}      # (-t)^mu
def Xpow(mu,v):
    A,B=v
    al=add(shift(A,1),mul(T2P1,B)); be=sub(A,B)
    tm=tmono(mu)
    a2=add(al,mul(mul(tm,T2P1),be)); b2=sub(al,shift(mul(tm,be),1))
    a2=divexact(a2,PHI3); b2=divexact(b2,PHI3)
    assert a2 is not None and b2 is not None
    return (a2,b2)
def eps(v): return ev(v[1],-1)
def F(m,p):
    """normalised vector of the necklace body r2.(y1)^m.<p>.u1 (Theorem O)"""
    w=Xpow(-m,p)
    u=nunit(w[0])
    assert u==(1,2*m*(1-eps(p))), (u,m,eps(p))   # Theorem O unit (CHECKED in every call)
    return scal(w,*u)

E1=(ONE,ONE)
def rat(word):
    """normalised channel vector of rational body B(word) (rho(word) e_1)"""
    v=E1
    for ch in reversed(word):
        if ch=='Y': v=Ypow(1,v)
        elif ch=='y': v=Ypow(-1,v)
        elif ch=='X': v=Xpow(1,v)
        elif ch=='x': v=Xpow(-1,v)
    return nv(v)
def ratbody(word):
    if not word: return ''
    ch=word[0]; rest=ratbody(word[1:])
    if ch=='Y': return 'y0'+('.'+rest if rest else '')
    if ch=='y': return 'x0'+('.'+rest if rest else '')
    if ch=='X': return 'r2.x1.'+(rest+'.' if rest else '')+'u1'
    if ch=='x': return 'r2.y1.'+(rest+'.' if rest else '')+'u1'

GB=None
def gboxes():
    global GB
    if GB is None:
        L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
        GB=[]
        for B,v in L:
            th=(dict((e,c) for e,c in v[0]),dict((e,c) for e,c in v[1]))
            GB.append((B,nv(from_th(th))))
    return GB

def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def vec(T):
    k=T[0]
    if k=='w': return rat(T[1])
    if k=='g': return gboxes()[T[1]][1]
    if k=='b': return T[2]
    if k=='p': return starall([vec(c) for c in T[1]])
    if k=='n':
        p=starall([vec(c) for c in T[2]])
        return F(T[1],p) if T[1] else p
    raise ValueError(k)
def word(T):
    k=T[0]
    if k=='w': return ratbody(T[1])
    if k=='g': return gboxes()[T[1]][0]
    if k=='b': return T[1]
    if k=='p': return '.'.join(x for x in (word(c) for c in T[1]) if x)
    if k=='n':
        inner='.'.join(x for x in (word(c) for c in T[2]) if x)
        return 'r2.'+tw(T[1])+(inner+'.' if inner else '')+'u1'
    raise ValueError(k)
def Jtree(T):
    """normalised J of the closure s.<T>"""
    return norm(vec(T)[0])
def hw(T): return 's.'+word(T)

# ---- closures as functionals on a product vector p=(A,B)
def J_neck(mu,p):
    """J of the necklace closure with special twist X^mu (mu=-m) applied to product p (normalised)"""
    return norm(Xpow(mu,p)[0])
def raw_vert(a,p):
    A,B=p
    tm=tmono(a)
    num=add(shift(A,1), mul(tm, add(mul(T2P1,A), shift(B,1))), shift(mul(PHI5,B),3*a-1))
    q=divexact(num,PHI3)
    assert q is not None
    return q
def J_vert(a,p): return norm(raw_vert(a,p))
def vert_word(a,bodyword):
    return 's.l1.'+(bodyword+'.' if bodyword else '')+(('x2.' if a>0 else 'y2.')*abs(a))+'u1'

def isunit(p): return p is not None and len(p)==1
def is_one(J): return J is not None and J=={0:1}
def a2(Jn): return lp.a2(Jn)
