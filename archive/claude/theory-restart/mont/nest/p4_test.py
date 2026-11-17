import sys, time, random
sys.path.insert(0,'nest'); sys.path.insert(0,'.')
from nlib import *
from words import mont
Phi3=P((1,0),(1,1),(1,2)); Phi5=P((1,0),(1,1),(1,2),(1,3),(1,4)); Q2=P((1,0),(1,2))
def mt(a): return mono(a,(-1)**(a%2))   # (-t)^a
def vert_formula(a,v):
    """J(s.l1.B.(x2)^a.u1)*Phi3 = t A + (-t)^a ((1+t^2) A + t B) + t^(3a-1) Phi5 B ; returns normalized J"""
    A=a_of(v); B=b_of(v)
    num=add(mul(mono(1),A), mul(mt(a),add(mul(Q2,A),mul(mono(1),B))), mul(mono(3*a-1),mul(Phi5,B)))
    q=divexact(num,Phi3)
    if q is None: return 'NOTDIV'
    return normalize(q)
def Ta(a): return '.'.join((['x2'] if a>0 else ['y2'])*abs(a))
def Vword(B,a): return 's.l1.'+(B+'.' if B else '')+Ta(a)+'.u1'
def VP(p,q):
    mid=['x0' if q>0 else 'y0']*abs(q)
    return '.'.join(['s','l1']+mid+[Ta(p)]+['u1'])
t0=time.time()
# (i) pretzel family P(p,q,p) vertical
ok=bad=skip=0
for p in (-9,-7,-5,-3,-1,1,3,5,7,9):
    for q in range(-7,8):
        w=VP(p,q); Jw=J(w)
        if Jw is None: skip+=1; continue
        v=[ONE,{}] if q==0 else apply(('y'*q) if q>0 else ('Y'*(-q)))
        F=vert_formula(p,v)
        if F==Jw: ok+=1
        else: bad+=1; print('MISMATCH P(p,q,p)',p,q,w)
print('P(p,q,p) vertical family: ok',ok,'bad',bad,'skip',skip,'time',round(time.time()-t0,1),flush=True)
# (ii) random non-rational boxes at new a values
boxes=load_boxes()
rnd=random.Random(1)
ok=bad=0
for a in (9,-7,-9,11):
    for B,v in rnd.sample(boxes,10):
        Jw=J(Vword(B,a))
        if Jw is None: continue
        if vert_formula(a,v)==Jw: ok+=1
        else: bad+=1; print('MISMATCH box',a,B)
print('random boxes, a in {9,-7,-9,11}: ok',ok,'bad',bad,'time',round(time.time()-t0,1),flush=True)
# (iii) rational row boxes and products of boxes (Montesinos boxes) inside the vertical closure
from words import row
def rowbox(r):
    j=(abs(r)-1)//2
    return '.'.join(row(r)), apply(('X'*j+'Y') if r>0 else ('x'*j+'y'))
ok=bad=0
for a in (-3,-1,1,3,5):
    for rs in ([3],[5],[-3],[3,3],[3,-5],[1,3]):
        Bs=[rowbox(r) for r in rs]
        Bw='.'.join(b for b,_ in Bs); v=Bs[0][1]
        for _,u in Bs[1:]: v=star(v,u)
        Jw=J(Vword(Bw,a))
        if Jw is None: continue
        if vert_formula(a,v)==Jw: ok+=1
        else: bad+=1; print('MISMATCH rows',a,rs)
print('row boxes / products in vertical closure: ok',ok,'bad',bad,'time',round(time.time()-t0,1),flush=True)
# (iv) compare the two inversions of P(p,q,p), q even: horizontal = mont(-q/2,[p,p]) vs vertical
print('two inversions of P(p,q,p), q even (horizontal necklace vs vertical):')
for p in (3,5,-3,7):
    for q in (-6,-4,-2,2,4):
        Jh=J(mont(-q//2,[p,p])); Jv=J(VP(p,q))
        if Jh is None or Jv is None: continue
        print('  P(%d,%d,%d): same J? %s   span_h %d span_v %d  a2 %s %s'%(p,q,p,Jh==Jv,span(Jh),span(Jv),a2(Jh),a2(Jv)))
