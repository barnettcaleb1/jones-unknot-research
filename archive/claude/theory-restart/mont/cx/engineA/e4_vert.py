"""E4: vertical (dihedral) closures V_a(N) of products N of up to 4 boxes, J Phi3 = w1(a) A + wV(a) t^-3N B (Theorem V),
by meet-in-the-middle on sub-products of size 0..2.  Keys: two-ended (Kt terms each end, delta forced) and deep one-ended (Kd).
A hit has r_top + r_bot = Tot = span A + span w1(a) - 2; for 4 non-integral rational boxes Tot >= 18, so Kt = 2, Kd = 15 is complete."""
import sys, time, pickle, collections, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, scan
from vc import top, bot, shift, mul, add, span
def tgtV(a,end,K):
    a1,aV=eng.WV(a)
    T=ser.divD(ser.pdata(a1,end,K),ser.pdata(aV,end,K)); return (T[0],-T[1],T[2])
def run(spec,out):
    t0=time.time()
    pool=lib.rational(spec['R'])
    if spec.get('nested'):
        Ra=lib.rational(spec['nested']['Ra']); seen=set(b[0] for b in pool); ext=[]
        for i in range(len(Ra)):
            for j in range(i,len(Ra)):
                for m in spec['nested']['M']:
                    for N in range(-spec['nested']['NN'],spec['nested']['NN']+1):
                        b=lib.node(m,N,[Ra[i],Ra[j]])
                        if b and b[0] not in seen and (span(b[1][1])-span(b[1][0]))!=-1: seen.add(b[0]); ext.append(b)
        if spec.get('general'):
            for g in lib.general():
                if g[0] not in seen: seen.add(g[0]); ext.append(g)
        pool=pool+ext
    P=len(pool)
    S=spec.get('S',2)
    subs=[()]
    for k in range(1,S+1): subs+=list(itertools.combinations_with_replacement(range(P),k))
    print('pool',P,'subproducts',len(subs),round(time.time()-t0,1),flush=True)
    vecs={}
    def vprod(s):
        if s not in vecs:
            vecs[s]=vc.star(vprod(s[:-1]),pool[s[-1]][1]) if s else vc.E1
        return vecs[s]
    Kt=spec['Kt']; Kd=spec['Kd']; avals=spec['a']
    res=dict(units=[],near=[],ncand=collections.Counter())
    seen=set()
    def check(s1,s2,a,N,tag):
        full=tuple(sorted(s1+s2))
        if len(full)==0: return
        key=(full,a,N)
        if key in seen: return
        seen.add(key); res['ncand'][tag]+=1
        p=vc.Ypow(N,vc.star(vprod(s1),vprod(s2))); A,B=p
        a1,aV=eng.WV(a); S1=mul(a1,A); S2=mul(aV,B); F=add(S1,S2)
        J=vc.divexact(F,vc.PHI3)
        rt,rb,gs,fs=scan.depths(S1,S2,F)
        if len(J)==1: res['units'].append((a,N,[pool[i][2] for i in full],tag)); return
        res['near'].append((min(rt,rb),rt,rb,span(J),span(A),a,N,full,tag))
    # two-ended
    ends=[('two',None)]+([] if spec.get('only_two') else [('deep',e) for e in ('top','bot')])
    for mode,end in ends:
        K=Kt if mode=='two' else Kd
        if mode=='two':
            st=[ser.slope(vprod(s),'top',K) if s else (0,1,tuple([0]*K)) for s in subs]
            sb=[ser.slope(vprod(s),'bot',K) if s else (0,1,tuple([0]*K)) for s in subs]
            H=collections.defaultdict(list)
            for x,s in enumerate(subs): H[(st[x][0]-sb[x][0],st[x][0]%3,st[x][1],st[x][2],sb[x][1],sb[x][2])].append(x)
        else:
            sl=[ser.slope(vprod(s),end,K) if s else (0,1,tuple([0]*K)) for s in subs]
            H=collections.defaultdict(list)
            for x,s in enumerate(subs): H[(sl[x][0]%3,sl[x][1],sl[x][2])].append(x)
        print(mode,end,'hashed',len(H),round(time.time()-t0,1),flush=True)
        for a in avals:
            if mode=='two':
                Tt=tgtV(a,'top',K); Tb=tgtV(a,'bot',K); dl=Tt[0]-Tb[0]
                for x,s in enumerate(subs):
                    need=(dl-(st[x][0]-sb[x][0]),(Tt[0]-st[x][0])%3,Tt[1]/st[x][1],ser.sdiv(Tt[2],st[x][2]),Tb[1]/sb[x][1],ser.sdiv(Tb[2],sb[x][2]))
                    for y in H.get(need,()):
                        if y<x: continue
                        z=st[x][0]+st[y][0]-Tt[0]
                        if z%3: continue
                        check(subs[x],subs[y],a,z//3,'two')
            else:
                T=tgtV(a,end,K)
                for x,s in enumerate(subs):
                    need=((T[0]-sl[x][0])%3,T[1]/sl[x][1],ser.sdiv(T[2],sl[x][2]))
                    for y in H.get(need,()):
                        if y<x: continue
                        z=sl[x][0]+sl[y][0]-T[0]
                        if z%3: continue
                        check(subs[x],subs[y],a,z//3,'deep-'+end)
            print(' a',a,mode,end,dict(res['ncand']),'units',len(res['units']),round(time.time()-t0,1),flush=True)
    near=res['near']; near.sort(key=lambda r:(-r[0],r[3]))
    hist=collections.Counter(min(r[0],20) for r in near)
    keep=[(r[:7],[pool[i][2] for i in r[7]],r[8]) for r in near[:300]]
    mins=sorted(near,key=lambda r:(r[3],-r[4]))[:200]
    keep3=[(r[:7],[pool[i][2] for i in r[7]],r[8]) for r in mins]
    outd=dict(spec=spec,ncand=dict(res['ncand']),units=res['units'],two_end=keep,min_span=keep3,hist=dict(hist),time=time.time()-t0)
    pickle.dump(outd,open(out,'wb'))
    print('DONE',dict(res['ncand']),'units',len(res['units']),'hist',sorted(hist.items()),'time',round(time.time()-t0,1))
    for r in keep[:8]: print(r[0],r[2])
    for r in keep3[:8]: print('minspan',r[0],r[2])
if __name__=='__main__':
    run(json.loads(sys.argv[1]),sys.argv[2])
