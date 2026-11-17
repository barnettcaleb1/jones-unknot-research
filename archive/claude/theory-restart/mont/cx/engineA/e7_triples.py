"""E7: three-child roots J Phi3 = w1(mu) a1a2a3 + w3(mu) t^-3N b1b2b3 with >= 1 non-generic child (jet (delta,sigma) != (-1,0)):
MITM pair-table x single, two-ended keys (Kt terms at both ends, delta forced). Finds every triple whose closure ties to order
Kt+1 at both ends; records exact two-ended depths (min(r_top,r_bot))."""
import sys, time, json, collections, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, scan, jets, e2b
from vc import top, bot, mul, add, span
spec=json.loads(sys.argv[1]); out=sys.argv[2]
t0=time.time()
Ra=lib.rational(spec['Ra']); R=lib.rational(spec['R'])
L1=[]; seen=set()
for i in range(len(Ra)):
    for j in range(i,len(Ra)):
        for m in spec['M']:
            for N in range(-spec['NN'],spec['NN']+1):
                b=lib.node(m,N,[Ra[i],Ra[j]])
                if b and b[0] not in seen: seen.add(b[0]); L1.append(b)
G=lib.general()
allb=L1+G+[b for b in R if b[0] not in seen]
def ng(b):
    J=jets.jet(b[1],1); return (J['dt']-J['db'])!=-1 or (J['Lt'][0]+J['Lb'][0])!=0
NG=[x for x in range(len(allb)) if (x<len(L1)+len(G)) and ng(allb[x])]
NGs=set(NG)
print('all',len(allb),'non-generic',len(NG),round(time.time()-t0,1),flush=True)
Kt=spec['Kt']; MU=spec['MU']
vec=[b[1] for b in allb]
st1=[ser.slope(v,'top',Kt) for v in vec]; sb1=[ser.slope(v,'bot',Kt) for v in vec]
H=collections.defaultdict(list); npairs=0
for x in NG:
    for y in range(len(allb)):
        if y in NGs and y<x: continue
        # series of product = product of series (exact for the truncated normalised series)
        a=ser.mulD(st1[x],st1[y]); b=ser.mulD(sb1[x],sb1[y])
        H[(a[0]-b[0],a[0]%3,a[1],a[2],b[1],b[2])].append((x,y,a[0])); npairs+=1
print('pair table',npairs,'keys',len(H),round(time.time()-t0,1),flush=True)
groups=collections.defaultdict(list)
for mu in range(-MU,MU+1):
    if mu: groups[(e2b.tgt(mu,'top',Kt),e2b.tgt(mu,'bot',Kt))].append(mu)
res=dict(units=[],near=[]); ncand=0; seenT=set()
for (Tt,Tb),gm in groups.items():
    lo,hi=min(gm),max(gm); gs=set(gm)
    musok=lambda m,gs=gs,lo=lo,hi=hi: (m in gs) or (hi==MU and m>hi) or (lo==-MU and m<lo)
    dl=Tt[0]-Tb[0]
    for z in range(len(allb)):
        need=(dl-(st1[z][0]-sb1[z][0]),(Tt[0]-st1[z][0])%3,Tt[1]/st1[z][1],ser.sdiv(Tt[2],st1[z][2]),Tb[1]/sb1[z][1],ser.sdiv(Tb[2],sb1[z][2]))
        for (x,y,dxy) in H.get(need,()):
            w=dxy+st1[z][0]-Tt[0]
            if w%3: continue
            N=w//3
            tr=tuple(sorted((x,y,z)))
            if (tr,N,lo) in seenT: continue
            seenT.add((tr,N,lo)); ncand+=1
            p=vc.Ypow(N,vc.starall([vec[x],vec[y],vec[z]])); A,B=p
            P,Q=eng.PQ(A,B)
            if not Q: continue
            cm=set(range(-eng.MUBF,eng.MUBF+1)) if len(P)<=1 else {top(P)-top(Q),bot(P)-bot(Q)}
            for mu in cm:
                if mu==0 or not musok(mu): continue
                J=add(P,mul(vc.tmono(mu),Q))
                a1,a3=eng.W(mu); S1=mul(a1,A); S2=mul(a3,B); F=add(S1,S2)
                rt,rb,gsp,fs=scan.depths(S1,S2,F)
                if len(J)==1: res['units'].append((mu,N,[allb[i][2] for i in tr])); continue
                res['near'].append((min(rt,rb),rt,rb,span(J),span(A),mu,N,tr))
    print(' group',gm[:2],len(gm),'cand',ncand,'units',len(res['units']),round(time.time()-t0,1),flush=True)
near=res['near']; near.sort(key=lambda r:(-r[0],r[3]))
hist=collections.Counter(min(r[0],15) for r in near)
keep=[(r[:7],[allb[i][2] for i in r[7]]) for r in near[:300]]
pickle.dump(dict(spec=spec,ncand=ncand,units=res['units'],two_end=keep,hist=dict(hist),time=time.time()-t0),open(out,'wb'))
print('DONE cand',ncand,'units',len(res['units']),'hist',sorted(hist.items()),round(time.time()-t0,1))
for r in keep[:8]: print(r[0])
