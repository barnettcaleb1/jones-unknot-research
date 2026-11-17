"""Third-order mismatch at second-order two-ended ties (pairs): Delta_t = l2_top(Q) - l2_top(q*), Delta_b likewise (log-jets)."""
import sys, time, json, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, e2b, jets
from fractions import Fraction as Fr
spec=json.loads(sys.argv[1])
nested,rat=e2b.build(spec); allb=nested+rat; nN=len(nested)
K=2
st=[ser.slope(b[1],'top',K) for b in allb]; sb=[ser.slope(b[1],'bot',K) for b in allb]
H=collections.defaultdict(list)
for x in range(len(allb)): H[(st[x][0]-sb[x][0], st[x][0]%3, st[x][1], st[x][2][:1], sb[x][1], sb[x][2][:1])].append(x)
joint=collections.Counter(); bymu=collections.Counter(); ex={}
for mu in [m for m in range(-12,13) if m]:
    Tt=e2b.tgt(mu,'top',K); Tb=e2b.tgt(mu,'bot',K)
    for i in range(nN):
        nt=ser.sdiv(Tt[2],st[i][2]); nb=ser.sdiv(Tb[2],sb[i][2])
        need=((Tt[0]-Tb[0])-(st[i][0]-sb[i][0]),(Tt[0]-st[i][0])%3,Tt[1]/st[i][1],nt[:1],Tb[1]/sb[i][1],nb[:1])
        for j in H.get(need,()):
            if j<nN and j<i: continue
            if (st[i][0]+st[j][0]-Tt[0])%3: continue
            Qt=ser.mulD(st[i],st[j]); Qb=ser.mulD(sb[i],sb[j])
            lt=jets.logs(Qt[2]); lb=jets.logs(Qb[2]); tt=jets.logs(Tt[2]); tb=jets.logs(Tb[2])
            d=(lt[1]-tt[1], lb[1]-tb[1])
            joint[d]+=1; bymu[(mu,d[0]+d[1])]+=1; ex.setdefault(d,(mu,allb[i][2],allb[j][2]))
print('second-order two-ended pairs:',sum(joint.values()))
print('joint (Delta_t, Delta_b) distribution (top 20):')
for k,v in joint.most_common(20): print('   ',str(k[0]),str(k[1]),v)
print('Delta_t + Delta_b by mu:',sorted(((m,str(s)),v) for (m,s),v in bymu.items())[:40])
print('both zero:',joint.get((0,0),0))
