"""E2: two-child root necklaces J Phi3 = w1(mu) A1 A2 + w3(mu) t^-3N B1 B2 by meet-in-the-middle on slope series.
A hit has r_end >= K+1 at one end (or span A + span w1 - 2 <= 2K: small cases, brute-forced separately), so hashing the
truncated slope series at one end with K terms is COMPLETE for hits with deep agreement at that end."""
import sys, time, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, scan
from vc import top, bot, shift, mul, add, span
def build_libs(spec):
    R5=lib.rational(5); R8=lib.rational(int(spec.get('Rb',8)))
    G=lib.general()
    nested=[]; seen=set()
    def put(b):
        if b and b[0] not in seen: seen.add(b[0]); nested.append(b)
    Ra=lib.rational(int(spec.get('Ra',5)))
    M=spec.get('M',(1,-1,2,-2,3,-3)); NN=range(-spec.get('NN',3),spec.get('NN',3)+1)
    for i in range(len(Ra)):
        for j in range(i,len(Ra)):
            for m in M:
                for N in NN: put(lib.node(m,N,[Ra[i],Ra[j]]))
    for g in G: put(g)
    for g in G:
        for m in M:
            for N in NN: put(lib.node(m,N,[g]))
    if spec.get('Gu',True):
        for g in G:
            for u in Ra:
                for m in M:
                    for N in NN: put(lib.node(m,N,[g,u]))
    rat=[b for b in R8 if b[0] not in seen]
    return nested, rat
def targets(end,K,MU):
    groups=collections.defaultdict(list)
    for mu in range(-MU,MU+1):
        if mu==0: continue
        a1,a3=eng.W(mu)
        T=ser.divD(ser.pdata(a1,end,K),ser.pdata(a3,end,K)); T=(T[0],-T[1],T[2])
        groups[T].append(mu)
    return groups
def run(spec,K,end,MU,out):
    t0=time.time()
    nested,rat=build_libs(spec)
    allb=nested+rat; nN=len(nested)
    print('library nested',len(nested),'rational',len(rat),'built',round(time.time()-t0,1),flush=True)
    sl=[ser.slope(b[1],end,K) for b in allb]
    H=collections.defaultdict(list)
    for idx,(d,lc,s) in enumerate(sl): H[(d%3,lc,s)].append(idx)
    print('hashed',len(H),'keys',round(time.time()-t0,1),flush=True)
    groups=targets(end,K,MU)
    ncand=0; nchk=0; units=[]; best=[]; stats=collections.Counter()
    seenpair=set()
    for T,mus in groups.items():
        musset=set(mus); lo=min(mus); hi=max(mus)
        extend_hi = hi==MU; extend_lo = lo==-MU   # constant class continues beyond the range
        for i in range(nN):          # A-side: nested boxes only (at least one child non-rational)
            d1,lc1,s1=sl[i]
            need=((T[0]-d1)%3, T[1]/lc1, ser.sdiv(T[2],s1))
            for j in H.get(need,()):
                if j<nN and j<i: continue          # unordered nested-nested
                d2=sl[j][0]
                x=d1+d2-T[0]
                if x%3: continue
                N=x//3
                key=(i,j,N,lo)
                if key in seenpair: continue
                seenpair.add(key); ncand+=1
                p=vc.Ypow(N,vc.star(allb[i][1],allb[j][1]))
                A,B=p
                BN=B
                P,Q=eng.PQ(A,BN)
                if not Q: stats['scalar']+=1; continue
                if len(P)<=1: cm=set(range(-eng.MUBF,eng.MUBF+1))
                else: cm={top(P)-top(Q), bot(P)-bot(Q)}
                for mu in cm:
                    if mu==0: continue
                    ok = mu in musset or (extend_hi and mu>hi) or (extend_lo and mu<lo)
                    if not ok: continue
                    nchk+=1
                    J=add(P,mul(vc.tmono(mu),Q))
                    a1,a3=eng.W(mu); S1=mul(a1,A); S2=mul(a3,B); F=add(S1,S2)
                    rt,rb,gs,fs=scan.depths(S1,S2,F)
                    if len(J)==1:
                        units.append((mu,N,allb[i][2],allb[j][2],allb[i][3],allb[j][3])); continue
                    best.append((min(rt,rb),rt,rb,span(J),span(A),mu,N,i,j))
        print('group',mus[:3],'...',len(mus),'cand so far',ncand,'checks',nchk,'units',len(units),round(time.time()-t0,1),flush=True)
    best.sort(key=lambda r:(-r[0],r[3]))
    keep=[(r[:7],allb[r[7]][2],allb[r[8]][2],allb[r[7]][3],allb[r[8]][3]) for r in best[:300]]
    bysp=sorted(best,key=lambda r:(r[3]-r[4],r[3]))[:100]
    keep2=[(r[:7],allb[r[7]][2],allb[r[8]][2],allb[r[7]][3],allb[r[8]][3]) for r in bysp]
    hist=collections.Counter((min(r[0],12)) for r in best)
    res=dict(spec=spec,K=K,end=end,MU=MU,ncand=ncand,nchk=nchk,units=units,two_end=keep,small_span=keep2,hist=dict(hist),
             nlib=(len(nested),len(rat)),time=time.time()-t0)
    pickle.dump(res,open(out,'wb'))
    print('DONE cand',ncand,'checks',nchk,'units',len(units),'time',round(time.time()-t0,1))
    print('two-ended depth histogram (min(rt,rb)):',sorted(hist.items()))
    for r in keep[:8]: print(r[0],r[3],r[4])
    return res
if __name__=='__main__':
    import json
    spec=json.loads(sys.argv[1]); K=int(sys.argv[2]); end=sys.argv[3]; MU=int(sys.argv[4]); out=sys.argv[5]
    run(spec,K,end,MU,out)
