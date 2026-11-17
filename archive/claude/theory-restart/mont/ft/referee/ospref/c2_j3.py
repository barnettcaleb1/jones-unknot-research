# Claim 2: J_3(K)(-1) = 1 and J_3(-e^h) = 1 + 0 h - 24 a2 h^2 - 144 v3 h^3 + O(h^4), KL convention, own code.
from rlib import *
KN={'3_1':(2,[1,1,1]),'3_1 (3-braid s1s2s1s2)':(3,[1,2,1,2]),'3_1 mirror':(2,[-1,-1,-1]),'4_1':(3,[1,-2,1,-2]),
    '5_1':(2,[1]*5),'5_2':(3,[1,1,1,2,-1,2]),'6_1':(4,[1,1,2,-1,-3,2,-3]),'6_2':(3,[1,1,1,-2,1,-2]),'6_3':(3,[1,1,-2,1,-2,-2]),
    '7_1':(2,[1]*7),'3_1#4_1':(4,[1,1,1,2,-3,2,-3]),'T(3,4)':(3,[1,2]*4),'4_1 alt diag (stab)':(4,[1,-2,1,-2,3])}
for name,(n,w) in KN.items():
    ops=braid_ops(n,w); V=jones(ops); J=J3(ops); ex=ev_h(J,4)
    a2=a2_of(V); v3=v3_of(V)
    ok2 = ex[0]==1 and ex[1]==0 and ex[2]==-24*a2 and ex[3]==-144*v3
    print('%-26s a2=%s v3=%s  J3(-e^h): %s  claim2 %s'%(name,a2,v3,[str(x) for x in ex],'OK' if ok2 else 'FAIL'))
