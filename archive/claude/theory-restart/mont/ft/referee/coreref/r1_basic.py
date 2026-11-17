# Referee check of claims 1, 2, 7 on independent samples (own code; seeds/lengths differ from the builder's).
import sys, random, collections, math
import rlib, lp
from rlib import Fr
from math import comb
seed=int(sys.argv[1]); N=int(sys.argv[2]); Lmin=int(sys.argv[3]); Lmax=int(sys.argv[4])
rnd=random.Random(seed); st=collections.Counter(); seen=set(); n=0; core_ex=[]; fails=[]
while n<N:
    w,J=rlib.rand_word(rnd,Lmin,Lmax)
    if w in seen: continue
    seen.add(w)
    V=rlib.VK(w)
    if V is None: st['VK None']+=1; continue
    n+=1
    Jm1=rlib.psub(J,rlib.ONE)
    if not Jm1: st['J=1']+=1; continue
    Q=rlib.divmod_laurent(Jm1,rlib.D7)
    if Q is None: st['F1 FAIL']+=1; fails.append(('F1',w)); continue
    a2=rlib.a2V(V); v3=rlib.v3V(V)
    Jp1=rlib.deriv_at(J,1,1); Q1=sum(Q.values()); Qm1=rlib.mom(Q,0)
    st['Jp1==8Q1' if Jp1==8*Q1 else 'Jp1!=8Q1']+=1
    st['Q(-1)==a2(K)' if Qm1==a2 else 'Q(-1)!=a2(K)']+=1
    M=[rlib.mom(J,k) for k in range(9)]; q=[rlib.mom(Q,k) for k in range(9)]
    st['M2==-24a2' if M[2]==-24*a2 else 'M2 FAIL']+=1
    ok=all(M[k]==-sum(comb(k,i)*(7**i-4**i-3**i)*q[k-i] for i in range(2,k+1)) for k in range(2,9))
    st['moment formula k<=8 ok' if ok else 'moment formula FAIL']+=1
    st['M3=0 mod 36' if M[3]%36==0 else 'M3 mod36 FAIL']+=1
    st['M3/36=a2 mod2' if (M[3]//36-a2)%2==0 else 'M3/36 parity FAIL']+=1
    st['M4=-48a2 mod144' if (M[4]+48*a2)%144==0 else 'M4 mod144 FAIL']+=1
    # Conjecture D
    f=rlib.psub(rlib.subst_neg(J),rlib.subst_pow(V,2))
    if not f: st['D: f=0 (exact)']+=1; g1=0
    else:
        g=rlib.divmod_laurent(f,rlib.MODD)
        if g is None:
            st['ConjD FAIL']+=1; fails.append(('D',w)); g1=None
            # which factor fails?
            for nm,cp in (('Phi5',rlib.C5),('Phi3',rlib.C3),('t+1',rlib.T1)):
                if rlib.divmod_laurent(f,cp) is None: st['ConjD fails at '+nm]+=1
        else: st['ConjD ok']+=1; g1=sum(g.values())
    iota=(Fr(M[3],36)-7*v3)/5
    st['iota int' if iota.denominator==1 else 'iota NONINT']+=1
    if g1 is not None: st['iota==g(1)-3v3' if iota==g1-3*v3 else 'iota!=g(1)-3v3']+=1
    if a2==0:
        st['core']+=1
        Qp=rlib.divmod_laurent(Jm1,rlib.D8)
        st['core D8 ok' if Qp is not None else 'core D8 FAIL']+=1
        st['core M3=0 mod72' if M[3]%72==0 else 'core M3 mod72 FAIL']+=1
        st['core M4=16M3 mod288' if (M[4]-16*M[3])%288==0 else 'core M4 FAIL']+=1
        st['core Q1 even' if Q1%2==0 else 'core Q1 ODD']+=1
        if Q1!=0: st['core sigma!=0']+=1; core_ex.append((w,Q1))
print('seed',seed,'N',n,'L',Lmin,Lmax); 
for k,v in sorted(st.items()): print('  ',k,v)
print('core examples with Q(1)!=0:',core_ex[:5]); print('fails:',fails[:10])
