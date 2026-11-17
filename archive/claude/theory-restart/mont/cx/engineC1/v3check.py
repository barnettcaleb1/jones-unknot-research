"""Independent numerical check of the V3 proof skeleton on random vertical closures of rational products:
 (i) whenever one end has r >= 2, the other end's slope mismatch l1(Q) - l1(q*) is exactly +1 (sigma-law);
 (ii) the weak end never shows the Phi_3 pattern; (iii) no unit."""
import sys, random, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, jets
R=lib.rational(7); rnd=random.Random(11)
stats=collections.Counter()
for it in range(4000):
    n=rnd.choice([2,2,3,3,4])
    bx=[R[rnd.randrange(len(R))][1] for _ in range(n)]
    p=vc.starall(bx); A,B=p
    a=rnd.choice([3,5,7,-3,-5,-7])
    a1,aV=eng.WV(a)
    # choose N to force a first-order coincidence at a random end
    end=rnd.choice(['top','bot'])
    if end=='top': x=max(aV)+max(B)-max(a1)-max(A)
    else: x=min(aV)+min(B)-min(a1)-min(A)
    if x%3: stats['skip']+=1; continue
    N=x//3
    S1=vc.mul(a1,A); S2=vc.mul(aV,vc.shift(B,-3*N)); F=vc.add(S1,S2)
    rt=max(max(S1),max(S2))-max(F); rb=min(F)-min(min(S1),min(S2))
    Q=(A,vc.shift(B,-3*N))
    qs={e:ser.slope(Q,e,2) for e in ('top','bot')}
    qt={e:ser.divD(ser.pdata(a1,e,2),ser.pdata(aV,e,2)) for e in ('top','bot')}
    for strong,weak,rs in (('top','bot',rt),('bot','top',rb)):
        if rs>=2:
            mm=jets.logs(qs[weak][2])[0]-jets.logs(qt[weak][2])[0]
            stats[('mismatch at weak end',str(mm))]+=1
    J=vc.divexact(F,vc.PHI3)
    stats[('depths',min(rt,rb)>=2)]+=1
    if J is not None and len(J)==1: stats['UNIT']+=1
print(sorted(stats.items(),key=str))
