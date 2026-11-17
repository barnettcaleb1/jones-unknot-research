"""Section 7 / Theorem O,N vs lp.J on necklaces s.r2.(y1)^m.B_1...B_n.u1 of NON-RATIONAL bodies.
Checks per necklace N:
 (i)   Norm(e1^T X^-m p) == lp.J(s.N)                          (Theorem N)
 (ii)  t^(2m(1-eps)) e1^T X^-m p == lp.J(s.N)  EXACTLY          (unit of (7.1), first coordinate)
 (iii) independent preferred vector of N (raw TL3 sandwich, normalised) == t^(2m(1-eps)) X^-m p  (both coords)
 (iv)  eps(v_N) == eps(p) == prod (-1)^n0(B_i)
 (v)   depth 2: s.r2.(y1)^m2.N.C.u1 == Norm(e1^T X^-m2 (v_N * v_C)) with v_N from (7.1)
p = product of preferred body vectors (bodies from general_boxes.json; vectors recomputed independently)."""
import json, random, sys
from tlib import *
L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
gen=[B for B,_ in L]
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 5)
NTR=int(sys.argv[2]) if len(sys.argv)>2 else 110
cache={}
def vec(B):
    if B not in cache:
        A0,B0=body_pref(B); cache[B]=v_from_ab(A0,B0)
    return cache[B]
def eps(v): return ev(add(v[0],mul(OMT3,v[1])),-1)
def n0(B): return sum(1 for tok in B.split('.') if tok in ('x0','y0'))
st={'N':0,'i':0,'ii':0,'iii':0,'iv':0,'v_tot':0,'v':0,'parity':0}
bad=[]
for trial in range(NTR):
    n=rnd.choice([1,1,2,2,3]); Bs=[rnd.choice(gen) for _ in range(n)]; m=rnd.choice([-3,-2,-1,1,2,3])
    N=neck_body(m,Bs); w='s.'+N
    Jw=lp.J(w)
    if Jw is None: continue
    st['N']+=1
    p=vec(Bs[0])
    for B in Bs[1:]: p=lp.star(p,vec(B))
    e=eps(p)
    q=Xpow_first_row_apply(-m,p)
    k=2*m*(1-e)
    vN_pred=[shift(q[0],k),shift(q[1],k)]
    ok1 = normalize(q[0])==Jw
    ok2 = vN_pred[0]==Jw
    vN=vec(N)
    ok3 = (vN[0]==vN_pred[0] and vN[1]==vN_pred[1])
    ok4 = (eps(vN)==e) and (e==eval('*'.join(str((-1)**n0(B)) for B in Bs)))
    st['parity']+= all(eps(vec(B))==(-1)**n0(B) for B in Bs)
    st['i']+=ok1; st['ii']+=ok2; st['iii']+=ok3; st['iv']+=ok4
    if not (ok1 and ok2 and ok3 and ok4): bad.append((w,ok1,ok2,ok3,ok4)); print('BAD',w,ok1,ok2,ok3,ok4)
    # depth 2
    C=rnd.choice(gen); m2=rnd.choice([-2,-1,1,2])
    w2='s.'+neck_body(m2,[N,C])
    J2=lp.J(w2)
    if J2 is not None:
        st['v_tot']+=1
        pp=lp.star(vN_pred,vec(C))
        q2=Xpow_first_row_apply(-m2,pp)
        if normalize(q2[0])==J2: st['v']+=1
        else: bad.append((w2,'depth2')); print('BAD depth2',w2)
print(st); print('bad',bad)
