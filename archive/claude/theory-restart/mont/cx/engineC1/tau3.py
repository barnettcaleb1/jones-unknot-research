import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, ser, jets, scan
from fractions import Fraction as Fr
D=pickle.load(open('libA_jets.pkl','rb')); Bx=D['boxes']; V=D['vecs']
res=pickle.load(open('tau2.pkl','rb'))
C,ex=res[-2]
def depths(S1,S2):
    F=vc.add(S1,S2)
    rt=max(max(S1),max(S2))-max(F) if F else None
    rb=min(F)-min(min(S1),min(S2)) if F else None
    return rt,rb,F
for key,(i,j) in sorted(ex.items()):
    p=vc.star(V[i],V[j]); A,B=p
    tq=ser.slope(p,'top',3); bq=ser.slope(p,'bot',3)
    a1,a3=eng.W(-2)
    tt=ser.divD(ser.pdata(a1,'top',3),ser.pdata(a3,'top',3)); tb=ser.divD(ser.pdata(a1,'bot',3),ser.pdata(a3,'bot',3))
    # N from degree matching at top: tq[0]-3N = tt[0]
    N=(tq[0]-tt[0])//3
    S1=vc.mul(a1,A); S2=vc.mul(a3,vc.shift(B,-3*N))
    rt,rb,F=depths(S1,S2)
    J=vc.divexact(F,vc.PHI3)
    print(key,'N',N,'tie depths (top,bot)=',(rt,rb),'span J',vc.span(J) if J else None,'boxes',Bx[i][1],'|',Bx[j][1])
    print('   top slope',tq[0],tq[1],[str(x) for x in jets.logs(tq[2])],' target',tt[0],-tt[1],[str(x) for x in jets.logs(tt[2])])
    print('   bot slope',bq[0],bq[1],[str(x) for x in jets.logs(bq[2])],' target',tb[0],-tb[1],[str(x) for x in jets.logs(tb[2])])
