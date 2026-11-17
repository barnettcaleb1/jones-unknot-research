# (a) checks: J = 1 + D7*Q exactly; Q(1) = J'(1)/8 (= sigma(L_odd)/8 by 1.3), Q(-1) = a2(K);
# core: D8 | J-1 ; distribution of Q(1) in the core; moment congruences M3 mod 36 / 72.
import sys, random, collections
import clib, lp
from fractions import Fraction as F
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
D7=clib.D(2); D8=clib.D(3)
stats=collections.Counter(); core_Q1=collections.Counter(); allQ1=collections.Counter()
m3mod=collections.Counter(); m3core=collections.Counter(); ex_core_sig=[]
seen=set(); n=0
while n<N:
    w,J=clib.randJ(rnd)
    if w in seen: continue
    seen.add(w); n+=1
    Jm1=lp.sub(J,lp.ONE)
    q,r=clib.pdiv(Jm1,D7)
    stats['D7 divides' if not r else 'D7 FAILS']+=1
    Q1=lp.ev(q,1); Qm1=lp.ev(q,-1)
    Jp1=clib.der(J,1,1)
    stats['Jp1==8Q1' if Jp1==8*Q1 else 'Jp1!=8Q1']+=1
    a2=F(-clib.M(J,2),24)
    stats['Q(-1)==a2' if Qm1==a2 else 'Q(-1)!=a2']+=1
    allQ1[(int(a2)%2, Q1)]+=1
    M3=clib.M(J,3)
    m3mod[M3%36]+=1
    if a2==0 and Jm1:
        q8,r8=clib.pdiv(Jm1,D8)
        stats['core: D8 divides' if not r8 else 'core: D8 FAILS']+=1
        core_Q1[Q1]+=1
        m3core[M3%72]+=1
        if Q1!=0 and len(ex_core_sig)<5: ex_core_sig.append((w,Q1,M3))
print('samples',n); print(dict(stats))
print('Q(1) by (a2 mod 2, Q1):',sorted(allQ1.items())[:40])
print('core Q(1)=sigma(L_odd)/8 distribution:',dict(core_Q1))
print('M3 mod 36 (all):',dict(m3mod)); print('M3 mod 72 (core):',dict(m3core))
print('core examples with sigma(L_odd)!=0:',ex_core_sig)
