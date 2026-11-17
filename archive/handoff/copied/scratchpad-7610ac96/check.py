# Verify V~ = q^s + (1-q^-2) chi_q(Tors) and chi_1(Tors) = -s/2, chi'(1) = -6 a2 - s(s+2)/4
# Input: reduced Khovanov ranks (h,q):rank (KnotInfo khovanov_reduced_rational_polynomial), s, Jones in t (KnotInfo), a2
from collections import Counter
data = {
 '3_1':   dict(kh={(0,2):1,(2,6):1,(3,8):1}, s=2, jones={1:1,3:1,4:-1}, a2=1),
 '4_1':   dict(kh={(-2,-4):1,(-1,-2):1,(0,0):1,(1,2):1,(2,4):1}, s=0, jones={-2:1,-1:-1,0:1,1:-1,2:1}, a2=-1),
 '8_19':  dict(kh={(0,6):1,(2,10):1,(3,12):1,(4,12):1,(5,16):1}, s=6, jones={3:1,5:1,8:-1}, a2=5),
 '10_124':dict(kh={(0,8):1,(2,12):1,(3,14):1,(4,14):1,(5,18):1,(6,18):1,(7,20):1}, s=8, jones={4:1,6:1,10:-1}, a2=None),
 '9_42':  dict(kh={(-2,-6):1,(-1,-4):1,(0,-2):1,(0,0):1,(1,0):2,(2,2):1,(3,4):1,(4,6):1}, s=0, jones={-3:1,-2:-1,-1:1,0:-1,1:1,2:-1,3:1}, a2=None),
}
def knights(kh, s):
    """all decompositions pawn(0,s) + knights (b,a)->(b+1,a+2c), c>=1 consistent with ranks"""
    gens = []
    for (h,q),r in sorted(kh.items()): gens += [(h,q)]*r
    assert (0,s) in gens; gens.remove((0,s))
    sols=set()
    def rec(rem, acc):
        if not rem: sols.add(tuple(sorted(acc))); return
        g = rem[0]  # lowest h remaining must be a knight source
        b,a = g
        for i,t in enumerate(rem[1:],1):
            if t[0]==b+1 and t[1]>a and (t[1]-a)%2==0:
                c=(t[1]-a)//2
                rec(rem[1:i]+rem[i+1:], acc+[(b,a,c)])
    rec(sorted(gens), [])
    return sols
for name,d in data.items():
    sols = knights(d['kh'], d['s'])
    print(name, 's=',d['s'], '#decompositions consistent with ranks:', len(sols))
    for sol in sols:
        tors = Counter()   # q-degree -> signed dim
        for (b,a,c) in sol:
            for k in range(c): tors[a+2*c-2*k] += (-1)**(b+1)
        rhs = Counter({d['s']:1})
        for j,v in tors.items():
            rhs[j]+=v; rhs[j-2]-=v
        lhs = Counter()
        for (h,q),r in d['kh'].items(): lhs[q]+=(-1)**h*r
        jones_q = Counter({2*k:v for k,v in d['jones'].items()})
        clean=lambda C:{k:v for k,v in C.items() if v}
        chi1=sum(tors.values()); m1=sum(j*v for j,v in tors.items())
        print('  knights (b,a,c):',sol)
        print('  chi_q(Tors)=',dict(sorted(clean(tors).items())),' identity holds:',clean(lhs)==clean(rhs),' chi(Kh~)=Jones(t=q^2):',clean(lhs)==clean(jones_q))
        print('  chi_1(Tors)=',chi1,' -s/2=',-d['s']//2, ' sum(-1)^b c =',sum((-1)**b*c for b,a,c in sol), ' max c=',max(c for b,a,c in sol))
        if d['a2'] is not None: print('  first moment sum(-1)^h j =',m1,' predicted -6a2 - s(s+2)/4 =',-6*d['a2']-d['s']*(d['s']+2)//4)
        else: print('  first moment =',m1,' => a2 = ',(-m1 - d['s']*(d['s']+2)//4)/6)
