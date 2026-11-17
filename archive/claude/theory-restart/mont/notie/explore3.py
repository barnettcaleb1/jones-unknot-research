from nt import *
import itertools, time
from collections import Counter, defaultdict
t0=time.time()
seqs=[s for s in normal_seqs(3,2)]
B={s:box(s) for s in seqs}
CH={s:chan(B[s]) for s in seqs}
def isR(s): # top state R iff last exponent positive
    return s[-1]>0
def Tgen(mu,N,ss):
    rho=sum(isR(s) for s in ss); d=2*rho-3*N
    if mu>0: return mu+2+max(d,0)
    if mu<-1: return max(2+d,1)
    return max(2+d,-1)
res=[]
for ss in itertools.combinations_with_replacement(seqs,2):
    A=mul(CH[ss[0]][0],CH[ss[1]][0])
    for mu in [m for m in range(-4,5) if m]:
        for N in range(-3,5):
            Jv=neck(mu,N,[B[s] for s in ss])
            T=top(Jv)+2-top(A); Tb=2-bot(Jv)+bot(A)
            ssm=tuple(mirror_seq(s) for s in ss)
            res.append((span(Jv),mu,N,ss,span(A),T,Tgen(mu,N,ss),Tb,Tgen(-mu,2-N,ssm)))
print('time',round(time.time()-t0,1),'cases',len(res))
print(sorted(Counter(r[0] for r in res).items())[:10])
print('top deficit T-Tgen:',sorted(Counter(r[5]-r[6] for r in res).items()))
print('bot deficit:',sorted(Counter(r[7]-r[8] for r in res).items()))
res.sort()
for r in res[:30]: print(r)
