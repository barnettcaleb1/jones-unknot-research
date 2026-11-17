import sys, itertools, time
sys.path.insert(0,'nest')
from nlib import *
import alex, sympy as sp
def realize(w):
    """half-diagram body realising the box vector rho(w) e_1 (up to unit) by nested necklaces"""
    body=''
    for ch in reversed(w):
        if ch=='Y': body=('y0.'+body) if body else 'y0'
        elif ch=='y': body=('x0.'+body) if body else 'x0'
        elif ch=='X': body='r2.x1.'+(body+'.' if body else '')+'u1'
        elif ch=='x': body='r2.y1.'+(body+'.' if body else '')+'u1'
    return body
def reduced(w):
    return all(not (w[i]+w[i+1] in ('Xx','xX','Yy','yY')) for i in range(len(w)-1))
T=sp.symbols('t')
groups={}; ok=bad=0; t0=time.time()
for n in range(1,7):
    for w in itertools.product('XxYy',repeat=n):
        w=''.join(w)
        if not reduced(w) or w[-1] in 'Xx' : continue   # X e1 = e1: trailing X is trivial
        B=realize(w); word='s.'+B
        Jw=J(word)
        if Jw is None: continue
        pred=normalize(apply(w)[0])
        if pred==Jw: ok+=1
        else: bad+=1; print('MISMATCH',w,word)
        if span(Jw)==0: continue
        Al=alex.alex_poly(word)
        Al=sp.Poly(sp.expand(Al*T**60),T)
        cs=[c for c in Al.all_coeffs()]
        while cs and cs[-1]==0: cs.pop()
        while cs and cs[0]==0: cs.pop(0)
        if cs[0]<0: cs=[-c for c in cs]
        key=tuple(cs)
        groups.setdefault(key,set()).add(tuple(sorted(Jw.items())))
print('realisation check (J of nested-necklace word = e1^T rho(w) e1): ok',ok,'bad',bad,'time',round(time.time()-t0,1))
def mirror(Jt): return tuple(sorted(normalize({-e:c for e,c in dict(Jt).items()}).items()))
print('Alexander polynomial -> number of distinct J up to mirror (t->1/t):')
for key in sorted(groups,key=lambda k:(sum(abs(c) for c in k),k)):
    Js=groups[key]
    classes=set()
    for Jt in Js:
        classes.add(min(Jt,mirror(Jt)))
    det=sum(abs(c) for c in key) if all((c>0)==(i%2==0) for i,c in enumerate(key)) else None
    print('  alex',key,' det',abs(sum(c*(-1)**i for i,c in enumerate(key))),' #J',len(Js),' #classes mod mirror',len(classes))
