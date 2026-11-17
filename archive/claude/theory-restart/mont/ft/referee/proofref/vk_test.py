# (a) own W_m vs exact for m=3,4 on more words; (b) W_2 = -12 Delta^2 a_2(K) with a_2 from V_K; (e) iota symbol vs v_3 from V_K.
import sys, random, time
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
from ss import *
import flat_search as fs, words, kauffman
def VK(word):
    kb=kauffman.bracket(word)
    if not kb: return None
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}; d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}
def der(V,k):
    tot=0
    for e,c in V.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f
    return tot
def a2(V): return Fr(-der(V,2),6)
def v3(V): return Fr(-(der(V,3)+3*der(V,2)),36)
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
seed=int(sys.argv[1]); N=int(sys.argv[2]); rnd=random.Random(seed)
agree={}; bad=[]; a2chk=[0,0,0]; iot={'int':[0,0],'vals':{}}; t0=time.time(); done=0
while done<N:
    r=rnd.random()
    if r<0.35: w=myword(rnd,rnd.randint(14,26))
    elif r<0.75: w=fs.gen(rnd,rnd.randint(12,22))
    else:
        mm=rnd.choice([-2,-1,1,2]); rows=[rnd.choice([-5,-3,3,5]) for _ in range(rnd.randint(2,3))]
        w=words.mont(mm,rows,tw=rnd.choice('xy'),ax=rnd.choice('xy'),off=rnd.choice('xy'))
    if not w or not valid(w) or lp.J(w) is None: continue
    fl=crossing_tokens(w); m=rnd.choice([2,3,3,4])
    if len(fl)<m: continue
    sites=rnd.sample(fl,m); Js=configs(w,sites)
    if Js is None: continue
    done+=1
    exact=(-1)**m*quot_at_m1(alt_sum(Js),m)
    recs,L,ax=chord_data(w,sites); mine,n=W_J(L,ax,recs)
    st=agree.setdefault(m,[0,0,0]); st[0 if mine==exact else 1]+=1; st[2]+=(exact!=0)
    if mine!=exact: bad.append((w,sites,mine,exact))
    eps=1
    for v in n: eps*=v//4
    if m==2:
        Vs={S:VK(flip(w,[s for s,b in zip(sites,S) if b])) for S in Js}
        if any(v is None for v in Vs.values()): continue
        d2=sum((-1)**sum(S)*a2(V) for S,V in Vs.items())
        a2chk[0 if exact==-12*d2 else 1]+=1; a2chk[2]+=(d2!=0)
    if m==3:
        Vs={S:VK(flip(w,[s for s,b in zip(sites,S) if b])) for S in Js}
        if any(v is None for v in Vs.values()): continue
        d3v=sum((-1)**sum(S)*v3(V) for S,V in Vs.items())
        d3M=sum((-1)**sum(S)*M(J,3) for S,J in Js.items())
        assert d3M==6*exact, (d3M,exact)
        io=(Fr(d3M,36)-7*d3v)/5
        iot['int'][0 if io.denominator==1 else 1]+=1
        key=eps*(io-d3v); iot['vals'][key]=iot['vals'].get(key,0)+1
print('own W vs exact by m [agree,disagree,nonzero]:',agree); print('bad:',bad[:3])
print('W_2 == -12 Delta^2 a_2(K) [ok,fail,nonzero]:',a2chk)
print('Delta^3 iota integral [yes,no]:',iot['int'],'  eps*Delta^3(iota-v3) values:',iot['vals'])
print('time %.1f'%(time.time()-t0))
