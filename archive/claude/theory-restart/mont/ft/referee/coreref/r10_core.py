import random, collections, sys, time
import rlib, lp
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import words
w='s.l1.x1.y0.x1.x0.y1.y1.y1.y0.x2.y0.y1.x2.y0.y0.u1'; J=lp.J(w); V=rlib.VK(w)
print('k0=4 example: a2(K)=',rlib.a2V(V),' M1..M5=',[rlib.mom(J,k) for k in range(1,6)],' span J=',rlib.span(J),flush=True)
for k in (1,2):
    for rows in ([4*k-1,4*k+1],[-(4*k-1),-(4*k+1)]):
        for mm in (-k,k):
            w=words.mont(mm,rows); J=lp.J(w)
            if J is None: continue
            V=rlib.VK(w); f=rlib.psub(rlib.subst_neg(J),rlib.subst_pow(V,2))
            ok=(not f or rlib.divmod_laurent(f,rlib.MODD) is not None)
            print('mont(%d,%s): a2(K)=%s  J span %d  ConjD %s'%(mm,rows,rlib.a2V(V),rlib.span(J),ok),flush=True)
rnd=random.Random(9090); st=collections.Counter(); seen=set(); m4=collections.Counter(); t0=time.time()
while st['core']<80 and time.time()-t0<300:
    w,J=rlib.rand_word(rnd,8,18)
    if w in seen or J=={0:1}: continue
    seen.add(w)
    if rlib.mom(J,2)!=0: continue          # a2(K)=0 iff M2=0 (BRIEF 1.2); cheap prefilter before V_K
    V=rlib.VK(w)
    if V is None or rlib.a2V(V)!=0: st['prefilter mismatch']+=1; continue
    st['core']+=1
    f=rlib.psub(rlib.subst_neg(J),rlib.subst_pow(V,2))
    st['D ok' if (not f or rlib.divmod_laurent(f,rlib.MODD) is not None) else 'D FAIL']+=1
    st['V_K(zeta5)=1' if rlib.divmod_laurent(rlib.psub(V,rlib.ONE),rlib.C5) is not None else 'V_K(zeta5)!=1']+=1
    M4=rlib.mom(J,4); m4['+' if M4>0 else ('-' if M4<0 else '0')]+=1
print('core-targeted:',dict(st),' M_4 signs:',dict(m4),' time',round(time.time()-t0),flush=True)
