"""Controls and side checks.
 (1) preferred stacking law: v_pref(B1.B2) == v_pref(B1) * v_pref(B2) exactly (independent raw TL3 vectors)
 (2) eps(v_B) == (-1)^n0(B) for all 50 general boxes (independent vectors)
 (3) dictionary in the vertical marking: Delta2 * y_flat(V_a(B)) == <Theta_a(B)> (my evaluator), odd a
 (4) negative controls: perturbed vertical formulas / X^{+m} / wrong unit must FAIL against lp.J"""
import json, random
from tlib import *
import r2lib
from r2lib import fs, alex
L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
gen=[B for B,_ in L]
rnd=random.Random(11)
def vec(B):
    A0,B0=body_pref(B); return v_from_ab(A0,B0)
def eps(v): return ev(add(v[0],mul(OMT3,v[1])),-1)
def n0(B): return sum(1 for tok in B.split('.') if tok in ('x0','y0'))
# (1)
ok=0; N=25
for _ in range(N):
    B1,B2=rnd.choice(gen),rnd.choice(gen)
    v12=vec(B1+'.'+B2); p=lp.star(vec(B1),vec(B2))
    ok+= (v12[0]==p[0] and v12[1]==p[1])
print('(1) stacking preferred law exact:',ok,'/',N)
# (2)
par=sum(1 for B in gen if eps(vec(B))==(-1)**n0(B)); print('(2) eps parity:',par,'/',len(gen),
   ' eps=-1 count:',sum(1 for B in gen if n0(B)%2))
# (3)
ok=0; tot=0
for B in gen[:15]:
    for a in (-3,-1,1,3):
        w=vword(B,a)
        y,x=fs.bracket_vector(alex.parse(w))
        v,k=r2lib.theta_eval(w)            # delta*<Theta>
        tot+=1; ok+= (r2lib.pmul(r2lib.pmul(r2lib.DELTA,r2lib.DELTA2),y)==v)
print('(3) Delta2*y_flat == <Theta> on vertical closures:',ok,'/',tot)
# (4)
def vert_bad(A,B,a,variant):
    l2=mono(a,(-1)**(a%2))
    if variant=='K2B=1': num=add(mul(mono(1),A), mul(l2, add(mul(P((1,0),(1,2)),A), B)), mul(mono(3*a-1), mul(PHI5,B)))
    if variant=='lam4=t^-3': num=add(mul(mono(1),A), mul(l2, add(mul(P((1,0),(1,2)),A), mul(mono(1),B))), mul(mono(-3*a-1), mul(PHI5,B)))
    if variant=='swapAB': num=add(mul(mono(1),B), mul(l2, add(mul(P((1,0),(1,2)),B), mul(mono(1),A))), mul(mono(3*a-1), mul(PHI5,A)))
    q=divexact(num,PHI3)
    return None if q is None else normalize(q)
for variant in ('K2B=1','lam4=t^-3','swapAB'):
    hit=0; tot=0
    for B in gen[:20]:
        A0,B0=body_pref(B)
        for a in (-3,1,3):
            tot+=1; hit+= (vert_bad(A0,B0,a,variant)==lp.J(vword(B,a)))
    print('(4) vertical variant',variant,'matches lp.J:',hit,'/',tot)
hitX=0; hitU=0; tot=0
for _ in range(20):
    B=rnd.choice(gen); m=rnd.choice([-2,-1,1,2]); w='s.'+neck_body(m,[B]); Jw=lp.J(w); v=vec(B); e=eps(v)
    q=Xpow_first_row_apply(m,v)   # wrong sign
    hitX+= (normalize(q[0])==Jw)
    q=Xpow_first_row_apply(-m,v); hitU+= (shift(q[0],2*m*(1+e))==Jw); tot+=1
print('(4) necklace with X^{+m} matches:',hitX,'/',tot,' wrong unit t^{2m(1+eps)} matches:',hitU,'/',tot)
