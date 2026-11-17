"""Exact top log-jets of rational boxes u(m_0..m_{k-1}) (normal form), for engine C1 lemma checks."""
import sys, itertools, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/notie')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
from nt import box, chan, normal_seqs
import auto2
from fractions import Fraction as Fr
import jets, ser
def logjet_top(p,K=4):
    D,c,s=ser.pdata(p,'top',K)
    return D,c,jets.logs(s)
def data(seq,K=4):
    u=box(seq); a,b=chan(u)
    Da,ca,la=logjet_top(a,K); Db,cb,lb=logjet_top(b,K)
    st,rho=auto2.run(seq)
    return dict(seq=seq,st=st,rho=rho,la=la,lb=lb,dq=Db-Da,lcq=Fr(cb,1)/ca)
if __name__=='__main__':
    K=int(sys.argv[1]); M=int(sys.argv[2])
    out=[]
    for s in normal_seqs(K,M):
        out.append(data(s))
    pickle.dump(out,open('jdata_%d_%d.pkl'%(K,M),'wb'))
    print(len(out))
