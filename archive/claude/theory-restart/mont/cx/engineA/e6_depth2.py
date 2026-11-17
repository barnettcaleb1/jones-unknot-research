"""E6: third-order two-ended search (Kt=2) for two-child roots whose children include DEPTH-2 nested boxes
F_m(Y^N c * u), c a depth-1 box with non-generic jet (delta != -1 or sigma != 0), u rational."""
import sys, time, json, collections, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, e2b, jets
spec=json.loads(sys.argv[1]); out=sys.argv[2]
t0=time.time()
R4=lib.rational(4); Rb=lib.rational(spec['Rb'])
L1=[]; seen=set()
for i in range(len(R4)):
    for j in range(i,len(R4)):
        for m in (1,-1,2,-2):
            for N in range(-2,3):
                b=lib.node(m,N,[R4[i],R4[j]])
                if b and b[0] not in seen: seen.add(b[0]); L1.append(b)
G=lib.general()
def nongeneric(b):
    J=jets.jet(b[1],1)
    return (J['dt']-J['db'])!=-1 or (J['Lt'][0]+J['Lb'][0])!=0
seeds=[b for b in L1 if nongeneric(b)]+G
print('L1',len(L1),'non-generic seeds',len(seeds),round(time.time()-t0,1),flush=True)
L2=[]
for c in seeds:
    for u in R4:
        for m in spec['M2']:
            for N in range(-spec['N2'],spec['N2']+1):
                b=lib.node(m,N,[c,u])
                if b and b[0] not in seen: seen.add(b[0]); L2.append(b)
    for m in spec['M2']:
        for N in range(-spec['N2'],spec['N2']+1):
            b=lib.node(m,N,[c])
            if b and b[0] not in seen: seen.add(b[0]); L2.append(b)
print('L2 (depth-2) boxes',len(L2),round(time.time()-t0,1),flush=True)
nested=L2+L1+G
rat=[b for b in Rb if b[0] not in seen]
allb=nested+rat; nN=len(nested)
Kt=spec['Kt']; MU=spec['MU']
res=dict(units=[],near=[],ncand=collections.Counter(),nchk=collections.Counter())
st=[ser.slope(b[1],'top',Kt) for b in allb]; sb=[ser.slope(b[1],'bot',Kt) for b in allb]
H=collections.defaultdict(list)
for x in range(len(allb)): H[(st[x][0]-sb[x][0], st[x][0]%3, st[x][1], st[x][2], sb[x][1], sb[x][2])].append(x)
print('hashed',len(H),round(time.time()-t0,1),flush=True)
groups=collections.defaultdict(list)
for mu in range(-MU,MU+1):
    if mu: groups[(e2b.tgt(mu,'top',Kt),e2b.tgt(mu,'bot',Kt))].append(mu)
seenp=set()
for (Tt,Tb),gm in groups.items():
    lo,hi=min(gm),max(gm); gs=set(gm)
    musok=lambda m,gs=gs,lo=lo,hi=hi: (m in gs) or (hi==MU and m>hi) or (lo==-MU and m<lo)
    dl=Tt[0]-Tb[0]
    for i in range(nN):
        need=(dl-(st[i][0]-sb[i][0]), (Tt[0]-st[i][0])%3, Tt[1]/st[i][1], ser.sdiv(Tt[2],st[i][2]), Tb[1]/sb[i][1], ser.sdiv(Tb[2],sb[i][2]))
        for j in H.get(need,()):
            if j<nN and j<i: continue
            x=st[i][0]+st[j][0]-Tt[0]
            if x%3: continue
            N=x//3
            if (i,j,N,lo) in seenp: continue
            seenp.add((i,j,N,lo)); res['ncand']['S1']+=1
            res['nchk']['S1']+=e2b.check_pair(allb,i,j,N,musok,res,'S1')
    print(' group',gm[:2],len(gm),'cand',res['ncand']['S1'],'units',len(res['units']),round(time.time()-t0,1),flush=True)
near=res['near']; near.sort(key=lambda r:(-r[0],r[3]))
hist=collections.Counter(min(r[0],15) for r in near)
keep=[(r[:7],r[9],allb[r[7]][2],allb[r[8]][2],allb[r[7]][3],allb[r[8]][3]) for r in near[:300]]
pickle.dump(dict(spec=spec,ncand=dict(res['ncand']),units=res['units'],two_end=keep,hist=dict(hist),nlib=(nN,len(rat),len(L2)),time=time.time()-t0),open(out,'wb'))
print('DONE',dict(res['ncand']),'units',len(res['units']),'hist',sorted(hist.items()),round(time.time()-t0,1))
for r in keep[:10]: print(r[0],r[4],r[5])
