"""tau-law exploration: tau(q) = l2_top(q) + l2_bot(q) (slope log-jets); targets q* = -w_1/w_3 (horizontal mu)."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, ser, jets
from fractions import Fraction as Fr
K=3
D=pickle.load(open('libA_jets.pkl','rb')); B=D['boxes']; nN=D['nN']
def tgt(mu,end):
    a1,a3=eng.W(mu)
    T=ser.divD(ser.pdata(a1,end,K),ser.pdata(a3,end,K)); return (T[0],-T[1],jets.logs(T[2]))
for mu in (1,-1,2,-2,3,-3,4,-4,5):
    tt=tgt(mu,'top'); tb=tgt(mu,'bot')
    print('mu=%d q*: top d=%d lc=%s l=%s | bot d=%d lc=%s l=%s | sigma*=%s tau*=%s'%(mu,tt[0],tt[1],[str(x) for x in tt[2]],tb[0],tb[1],[str(x) for x in tb[2]],tt[2][0]+tb[2][0],tt[2][1]+tb[2][1]))
tau=collections.Counter(); sig=collections.Counter()
for k,T,tag,tp,bt in B:
    tau[(tag[0],tp[2][1]+bt[2][1])]+=1; sig[(tag[0],tp[2][0]+bt[2][0])]+=1
print('tau by family:',sorted((k[0],str(k[1]),v) for k,v in tau.items()))
print('sigma by family:',sorted((k[0],str(k[1]),v) for k,v in sig.items()))
