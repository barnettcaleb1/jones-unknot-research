"""E9: vertical closures V_a(c1*c2) (and single c) with c from a pool containing DEPTH-2 boxes of non-generic jet, keyed at
order Kt+1 at both ends (two-ended); records two-ended depths."""
import sys, time, json, collections, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, scan, jets, e4_vert
from vc import top, bot, mul, add, span
spec=json.loads(sys.argv[1]); out=sys.argv[2]; t0=time.time()
R4=lib.rational(4); R=lib.rational(spec['R'])
L1=[]; seen=set()
for i in range(len(R4)):
    for j in range(i,len(R4)):
        for m in (1,-1,2,-2):
            for N in range(-2,3):
                b=lib.node(m,N,[R4[i],R4[j]])
                if b and b[0] not in seen: seen.add(b[0]); L1.append(b)
G=lib.general()
def jt(b):
    J=jets.jet(b[1],1); return (J['dt']-J['db'], J['Lt'][0]+J['Lb'][0])
seeds=[b for b in L1 if jt(b)!=(-1,0)]+G
L2=[]
for c in seeds:
    for u in R4:
        for m in (1,-1,2,-2):
            for N in range(-2,3):
                b=lib.node(m,N,[c,u])
                if b and b[0] not in seen and jt(b)!=(-1,0): seen.add(b[0]); L2.append(b)
pool=[b for b in R if b[0] not in seen]+[b for b in L1 if jt(b)!=(-1,0)]+G+L2
P=len(pool); print('pool',P,'(depth-2 non-generic',len(L2),')',round(time.time()-t0,1),flush=True)
Kt=spec['Kt']
st=[ser.slope(b[1],'top',Kt) for b in pool]; sb=[ser.slope(b[1],'bot',Kt) for b in pool]
one=(0,1,tuple([0]*Kt))
H=collections.defaultdict(list)
for x in range(-1,P):
    a=st[x] if x>=0 else one; b=sb[x] if x>=0 else one
    H[(a[0]-b[0],a[0]%3,a[1],a[2],b[1],b[2])].append(x)
res=dict(units=[],near=[]); nc=0; seenc=set()
for a in spec['a']:
    a1,aV=eng.WV(a)
    Tt=e4_vert.tgtV(a,'top',Kt); Tb=e4_vert.tgtV(a,'bot',Kt); dl=Tt[0]-Tb[0]
    for x in range(P):
        need=(dl-(st[x][0]-sb[x][0]),(Tt[0]-st[x][0])%3,Tt[1]/st[x][1],ser.sdiv(Tt[2],st[x][2]),Tb[1]/sb[x][1],ser.sdiv(Tb[2],sb[x][2]))
        for y in H.get(need,()):
            if y>=0 and y<x: continue
            dy=st[y][0] if y>=0 else 0
            z=st[x][0]+dy-Tt[0]
            if z%3: continue
            N=z//3; key=(x,y,a,N)
            if key in seenc: continue
            seenc.add(key); nc+=1
            v=pool[x][1] if y<0 else vc.star(pool[x][1],pool[y][1])
            p=vc.Ypow(N,v); A,B=p
            S1=mul(a1,A); S2=mul(aV,B); F=add(S1,S2); J=vc.divexact(F,vc.PHI3)
            rt,rb,g,f=scan.depths(S1,S2,F)
            if len(J)==1: res['units'].append((a,N,x,y)); continue
            res['near'].append((min(rt,rb),rt,rb,span(J),span(A),a,N,x,y))
    print(' a',a,'cand',nc,'units',len(res['units']),round(time.time()-t0,1),flush=True)
near=sorted(res['near'],key=lambda r:(-r[0],r[3]))
hist=collections.Counter(min(r[0],15) for r in near)
keep=[(r[:7],pool[r[7]][2],(pool[r[8]][2] if r[8]>=0 else None)) for r in near[:200]]
pickle.dump(dict(spec=spec,ncand=nc,units=res['units'],two_end=keep,hist=dict(hist)),open(out,'wb'))
print('DONE cand',nc,'units',len(res['units']),'hist',sorted(hist.items()),round(time.time()-t0,1))
for r in keep[:6]: print(r[0])
