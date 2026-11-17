"""validate OWN automaton (K=3 and K=4) against EXACT Laurent computation on all normal forms u(m_0..m_{k-1}) with
sum|m_i| <= SMAX: top log-jets of a (order K), q (deg, lc, log-jet order K); bottom data of u == top data of the mirror
u'' = u(-m0-1, -m1, ..) (log-jets of a and q; deg q_bot = 3 - deg q_top(u''))."""
import sys, time, itertools, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rauto, rlaurent as RL
from fractions import Fraction as Fr
SMAX=int(sys.argv[1]) if __name__=="__main__" else 0
def exact_vec(ms):
    v1={0:1}; v2={}
    for m in ms:
        for _ in range(abs(m)):
            if m>0: v1,v2=v1,RL.pshift(RL.padd(v1,v2),-3)
            else: v1,v2=v1,RL.padd(RL.pneg(v1),RL.pshift(v2,3))
        v1,v2=RL.padd(v1,RL.pmul({0:1,4:-1},v2)),RL.pneg(RL.padd(v1,v2))
    a=v1; b=RL.padd(v1,RL.pmul({0:1,3:-1},v2))
    return a,b
def data(a,b,end,K):
    da,ca,xa=RL.enddata(a,end,K); db,cb,xb=RL.enddata(b,end,K)
    la=RL.logjet(xa); lb=RL.logjet(xb)
    return dict(la=la,lq=tuple(y-x for x,y in zip(la,lb)),dq=db-da,cq=Fr(cb,ca))
def forms(S):
    out=[]
    def rec(pre,rem):
        if pre: out.append(tuple(pre))
        for m in range(-rem,rem+1):
            if m==0: continue
            if not pre and m==-1: continue
            rec(pre+[m],rem-abs(m))
    rec([],S); return out
if __name__!="__main__": raise ImportError("skip")
t0=time.time()
NF=forms(SMAX); print('normal forms with sum|m| <=',SMAX,':',len(NF),flush=True)
for K in (3,4):
    order,trans=rauto.build(K); M=K+3
    fin={k:rauto.qdata(k,K) for k in order if k!='init'}
    def walk(ms):
        key='init'; la=[Fr(0)]*K
        for m in ms:
            mc=max(-M,min(M,m)); d,lc,l,nk=trans[(key,mc)]
            la=[x+y for x,y in zip(la,l)]; key=nk
        return key,tuple(la)
    bad=0; badb=0; cnt=0; maxk=0
    for ms in NF:
        a,b=exact_vec(ms)
        if len(a)==1: continue      # integral (should not happen)
        cnt+=1
        key,la=walk(ms); dq,cq,lq=fin[key]
        e=data(a,b,'top',K)
        if not (e['la']==la and e['lq']==lq and e['dq']==dq and e['cq']==cq): bad+=1
        mir=(-ms[0]-1,)+tuple(-m for m in ms[1:])
        key2,la2=walk(mir); dq2,cq2,lq2=fin[key2]
        eb=data(a,b,'bot',K)
        if not (eb['la']==la2 and eb['lq']==lq2 and eb['dq']==3-dq2): badb+=1
    print('K=%d: %d boxes, top mismatches %d, bottom(mirror) mismatches %d   (%.1fs)'%(K,cnt,bad,badb,time.time()-t0),flush=True)
