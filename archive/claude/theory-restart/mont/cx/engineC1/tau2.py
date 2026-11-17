"""Second-order two-ended ties of pairs (library A x (A u R8)) at mu = +-1, +-2: tau values and box types."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, ser, jets
from fractions import Fraction as Fr
K=3
D=pickle.load(open('libA_jets.pkl','rb')); Bx=D['boxes']; nN=D['nN']
def tgt(mu,end):
    a1,a3=eng.W(mu)
    T=ser.divD(ser.pdata(a1,end,K),ser.pdata(a3,end,K)); return (T[0],-T[1],jets.logs(T[2]))
H=collections.defaultdict(list)
for x,(k,T,tag,tp,bt) in enumerate(Bx):
    H[(tp[0]-bt[0], tp[0]%3, tp[1], tp[2][0], bt[1], bt[2][0])].append(x)
res={}
for mu in (1,-1,2,-2):
    tt=tgt(mu,'top'); tb=tgt(mu,'bot'); taus=tt[2][1]+tb[2][1]
    C=collections.Counter(); ex={}
    for i in range(nN):
        k,T,tag,tp,bt=Bx[i]
        need=((tt[0]-tb[0])-(tp[0]-bt[0]), (tt[0]-tp[0])%3, Fr(tt[1])/tp[1], tt[2][0]-tp[2][0], Fr(tb[1])/bt[1], tb[2][0]-bt[2][0])
        for j in H.get(need,()):
            if j<nN and j<i: continue
            k2,T2,tag2,tp2,bt2=Bx[j]
            ti=tp[2][1]+bt[2][1]; tj=tp2[2][1]+bt2[2][1]
            dsum=ti+tj-taus
            dt=tp[2][1]+tp2[2][1]-tt[2][1]; db=bt[2][1]+bt2[2][1]-tb[2][1]
            key=(dsum,dt,db)
            C[key]+=1; ex.setdefault(key,(i,j))
    res[mu]=(C,ex)
    print('mu=%d tau*=%s ties=%d  min(Dt+Db)=%s'%(mu,taus,sum(C.values()),min(k[0] for k in C)))
    for k,v in sorted(C.items())[:12]: print('    Dsum=%s (Dt,Db)=(%s,%s) x%d  ex %s | %s'%(k[0],k[1],k[2],v,Bx[ex[k][0]][2],Bx[ex[k][1]][2]))
pickle.dump(res,open('tau2.pkl','wb'))
