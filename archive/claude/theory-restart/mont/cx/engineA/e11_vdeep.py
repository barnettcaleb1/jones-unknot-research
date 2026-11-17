"""E11: COMPLETE search for unit J among vertical closures V_a(Y^N u_1...u_n) of rational products (sub-products of size <= S
from R(L), so n <= 2S), every odd |a| >= 3 in the block-separation window, every N.
Completeness: Theorem V2 (PROVED) gives min(r_top, r_bot) <= 1, hence r >= Tot - 1 >= 4n + 1 >= 5 at the other end, so a
one-ended key with Kd = 4 terms (agreement >= 5 orders) at top or bottom catches every unit."""
import sys, time, json, collections, pickle, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, scan
from vc import top, bot, mul, add, span
spec=json.loads(sys.argv[1]); out=sys.argv[2]; t0=time.time()
pool=lib.rational(spec['R']); S=spec['S']; Kd=spec['Kd']; AM=spec['Amax']
if spec.get('nested'):
    import jets
    Ra=lib.rational(spec['nested']['Ra']); seenb=set(b[0] for b in pool); ext=[]
    for i in range(len(Ra)):
        for j in range(i,len(Ra)):
            for m in spec['nested']['M']:
                for N in range(-spec['nested']['NN'],spec['nested']['NN']+1):
                    b=lib.node(m,N,[Ra[i],Ra[j]])
                    if b and b[0] not in seenb:
                        J=jets.jet(b[1],1)
                        if (J['dt']-J['db'],J['Lt'][0]+J['Lb'][0])!=(-1,0): seenb.add(b[0]); ext.append(b)
    for g in lib.general():
        if g[0] not in seenb: seenb.add(g[0]); ext.append(g)
    pool=pool+ext
P=len(pool)
subs=[()]
for k in range(1,S+1): subs+=list(itertools.combinations_with_replacement(range(P),k))
vecs={}
def vprod(s):
    if s not in vecs: vecs[s]=vc.star(vprod(s[:-1]),pool[s[-1]][1]) if s else vc.E1
    return vecs[s]
print('pool',P,'subs',len(subs),flush=True)
res=dict(units=[],near=[]); nc=collections.Counter(); seen=set()
avals=[a for a in range(-AM,AM+1) if a%2 and abs(a)>=3]
for end in ('top','bot'):
    sl=[ser.slope(vprod(s),end,Kd) if s else (0,1,tuple([0]*Kd)) for s in subs]
    H=collections.defaultdict(list)
    for x in range(len(subs)): H[(sl[x][1],sl[x][2])].append(x)
    groups=collections.defaultdict(list)
    for a in avals:
        a1,aV=eng.WV(a)
        T=ser.divD(ser.pdata(a1,end,Kd),ser.pdata(aV,end,Kd))
        groups[(-T[1],T[2])].append((a,T[0]))
    print(end,'hashed',len(H),'target groups',len(groups),round(time.time()-t0,1),flush=True)
    for (lcT,sT),alist in groups.items():
        for x in range(len(subs)):
            need=(lcT/sl[x][1], ser.sdiv(sT,sl[x][2]))
            for y in H.get(need,()):
                if y<x: continue
                full=tuple(sorted(subs[x]+subs[y]))
                if not full: continue
                p0=None
                for (a,dT) in alist:
                    z=sl[x][0]+sl[y][0]-dT
                    if z%3: continue
                    N=z//3; key=(full,a,N)
                    if key in seen: continue
                    if p0 is None:
                        p0=vc.star(vprod(subs[x]),vprod(subs[y]))
                        win=max(span(p0[0]),span(p0[1]))+8
                    if abs(a)>win: continue
                    seen.add(key); nc[end]+=1
                    p=vc.Ypow(N,p0); A,B=p
                    a1,aV=eng.WV(a); S1=mul(a1,A); S2=mul(aV,B); F=add(S1,S2)
                    J=vc.divexact(F,vc.PHI3)
                    rt,rb,g,f=scan.depths(S1,S2,F)
                    if len(J)==1: res['units'].append((a,N,full)); continue
                    res['near'].append((max(rt,rb),rt,rb,span(J),span(A),a,N,full))
        print(' ',end,'group of',len(alist),'a-values; checks',dict(nc),'units',len(res['units']),round(time.time()-t0,1),flush=True)
near=sorted(res['near'],key=lambda r:(-r[0]+r[3]))
hist=collections.Counter(min(r[0],40) for r in near)
pickle.dump(dict(spec=spec,checks=dict(nc),units=res['units'],near=[(r[:7],[pool[i][2] for i in r[7]]) for r in near[:200]],hist=dict(hist)),open(out,'wb'))
print('DONE checks',dict(nc),'units',len(res['units']),'one-ended depth hist',sorted(hist.items())[-12:],round(time.time()-t0,1))
for r in near[:6]: print(r[:7])
