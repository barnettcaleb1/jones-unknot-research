"""E2b: two-child root necklaces, COMPLETE design (no sampling).
A hit at (mu,N) has agreement orders r_top + r_bot = Tot := span(A) + span(w_1(mu)) - 2 (A = a1 a2).
 S1 (two-ended): key (delta, d_top mod 3, top lc + Kt terms, bottom lc + Kb terms) -> all hits with r_top > Kt and r_bot > Kb.
 S2/S3 (deep one-ended): key at one end with Kd terms -> all hits with r_end > Kd.
 Remaining hits have Tot <= Kt + Kd + 1 (or Kb + Kd + 1): pairs with span(a1)+span(a2) <= that bound are brute-forced (S4).
Children: A-side = non-rational boxes (nested / general), B-side = all boxes (non-rational + rational R(Lr)). """
import sys, time, pickle, collections, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, scan
from vc import top, bot, shift, mul, add, span
def build(spec):
    G=lib.general(); M=spec['M']; NN=range(-spec['NN'],spec['NN']+1)
    Ra=lib.rational(spec['Ra']); Rb=lib.rational(spec['Rb'])
    nested=[]; seen=set()
    def put(b):
        if b and b[0] not in seen: seen.add(b[0]); nested.append(b)
    for i in range(len(Ra)):
        for j in range(i,len(Ra)):
            for m in M:
                for N in NN: put(lib.node(m,N,[Ra[i],Ra[j]]))
    for g in G: put(g)
    for g in G:
        for m in M:
            for N in NN: put(lib.node(m,N,[g]))
    for g in G:
        for u in Ra:
            for m in M:
                for N in NN: put(lib.node(m,N,[g,u]))
    rat=[b for b in Rb if b[0] not in seen]
    return nested, rat
def tgt(mu,end,K):
    a1,a3=eng.W(mu)
    T=ser.divD(ser.pdata(a1,end,K),ser.pdata(a3,end,K)); return (T[0],-T[1],T[2])
def check_pair(allb,i,j,N,musok,res,tag):
    p=vc.Ypow(N,vc.star(allb[i][1],allb[j][1])); A,B=p
    P,Q=eng.PQ(A,B)
    if not Q: return 0
    cm=set(range(-eng.MUBF,eng.MUBF+1)) if len(P)<=1 else {top(P)-top(Q), bot(P)-bot(Q)}
    n=0
    for mu in cm:
        if mu==0 or not musok(mu): continue
        n+=1
        J=add(P,mul(vc.tmono(mu),Q))
        a1,a3=eng.W(mu); S1=mul(a1,A); S2=mul(a3,B); F=add(S1,S2)
        rt,rb,gs,fs=scan.depths(S1,S2,F)
        if len(J)==1: res['units'].append((mu,N,allb[i][2],allb[j][2],allb[i][3],allb[j][3],tag)); continue
        res['near'].append((min(rt,rb),rt,rb,span(J),span(A),mu,N,i,j,tag))
    return n
def run(spec,out):
    t0=time.time()
    nested,rat=build(spec)
    if spec.get('d2pos'):
        R4=lib.rational(4); L1=[]; sn=set(b[0] for b in nested)
        for i in range(len(R4)):
            for j in range(i,len(R4)):
                for m in (1,-1,2,-2):
                    for N in range(-2,3):
                        b=lib.node(m,N,[R4[i],R4[j]])
                        if b: L1.append(b)
        def l1(f,end): return ser.pdata(f,end,1)[2][0]
        d2=[]
        for c in L1+lib.general():
            for u in R4:
                for m in (1,-1,2,-2):
                    for N in range(-2,3):
                        b=lib.node(m,N,[c,u])
                        if b and b[0] not in sn and (l1(b[1][0],'top')>0 or l1(b[1][0],'bot')>0 or l1(b[1][1],'top')>0 or l1(b[1][1],'bot')>0):
                            sn.add(b[0]); d2.append(b)
        print('depth-2 positive-potential boxes:',len(d2),flush=True)
        import pickle as _pk; _pk.dump(d2,open('d2pos_boxes.pkl','wb'))
        nested=d2+nested; NSEL=len(d2)
    if spec.get('posb'):
        def l1(f,end): return ser.pdata(f,end,1)[2][0]
        sel=[b for b in nested if l1(b[1][1],'top')>0 or l1(b[1][1],'bot')>0 or l1(b[1][0],'top')>0 or l1(b[1][0],'bot')>0]
        ks=set(b[0] for b in sel); nested=sel+[b for b in nested if b[0] not in ks]
        spec['ichunk']=None; NSEL=len(sel)
        print('positive-potential boxes selected:',NSEL,[b[3] for b in sel],flush=True)
    allb=nested+rat; nN=len(nested)
    print('library nested',nN,'rational',len(rat),round(time.time()-t0,1),flush=True)
    Kt=spec['Kt']; Kd=spec['Kd']; MU=spec['MU']
    res=dict(units=[],near=[],ncand=collections.Counter(),nchk=collections.Counter())
    mus=[m for m in range(-MU,MU+1) if m]
    ck=spec.get('ichunk') or [0,1]; IR=[i for i in range(nN) if i%ck[1]==ck[0]]
    if spec.get('posb') or spec.get('d2pos'): IR=list(range(NSEL))
    # ---- S1 two-ended
    st=[ser.slope(b[1],'top',Kt) for b in allb]; sb=[ser.slope(b[1],'bot',Kt) for b in allb]
    H=collections.defaultdict(list)
    for x in range(len(allb)):
        H[(st[x][0]-sb[x][0], st[x][0]%3, st[x][1], st[x][2], sb[x][1], sb[x][2])].append(x)
    groups=collections.defaultdict(list)
    for mu in mus: groups[(tgt(mu,'top',Kt),tgt(mu,'bot',Kt))].append(mu)
    seenp=set()
    for (Tt,Tb),gm in ([] if spec.get('deep_only') else groups.items()):
        lo,hi=min(gm),max(gm); gs=set(gm)
        musok=lambda m,gs=gs,lo=lo,hi=hi: (m in gs) or (hi==MU and m>hi) or (lo==-MU and m<lo)
        dl=Tt[0]-Tb[0]
        for i in IR:
            need=(dl-(st[i][0]-sb[i][0]), (Tt[0]-st[i][0])%3, Tt[1]/st[i][1], ser.sdiv(Tt[2],st[i][2]), Tb[1]/sb[i][1], ser.sdiv(Tb[2],sb[i][2]))
            for j in H.get(need,()):
                if j<nN and j<i: continue
                x=st[i][0]+st[j][0]-Tt[0]
                if x%3: continue
                N=x//3
                if (i,j,N,lo) in seenp: continue
                seenp.add((i,j,N,lo)); res['ncand']['S1']+=1
                res['nchk']['S1']+=check_pair(allb,i,j,N,musok,res,'S1')
    print('S1 done cand',res['ncand']['S1'],'units',len(res['units']),round(time.time()-t0,1),flush=True)
    # ---- S2/S3 deep one-ended
    for end in (() if spec.get('only_S1') else ('top','bot')):
        sl=[ser.slope(b[1],end,Kd) for b in allb]
        H=collections.defaultdict(list)
        for x in range(len(allb)): H[(sl[x][0]%3,sl[x][1],sl[x][2])].append(x)
        groups=collections.defaultdict(list)
        for mu in mus: groups[tgt(mu,end,Kd)].append(mu)
        for T,gm in groups.items():
            lo,hi=min(gm),max(gm); gs=set(gm)
            musok=lambda m,gs=gs,lo=lo,hi=hi: (m in gs) or (hi==MU and m>hi) or (lo==-MU and m<lo)
            for i in IR:
                need=((T[0]-sl[i][0])%3, T[1]/sl[i][1], ser.sdiv(T[2],sl[i][2]))
                for j in H.get(need,()):
                    if j<nN and j<i: continue
                    x=sl[i][0]+sl[j][0]-T[0]
                    if x%3: continue
                    N=x//3
                    if (i,j,N,lo,end) in seenp: continue
                    seenp.add((i,j,N,lo,end)); res['ncand'][end]+=1
                    res['nchk'][end]+=check_pair(allb,i,j,N,musok,res,'deep-'+end)
        print('deep',end,'cand',res['ncand'][end],'units',len(res['units']),round(time.time()-t0,1),flush=True)
    # ---- S4 small pairs: brute force all (mu,N) candidates (eng.hclosures) when span a1 + span a2 <= Kt+Kd+1
    bound=Kt+Kd+2 if not (spec.get('only_S1') or spec.get('deep_only')) else -1
    small=[x for x in range(len(allb)) if span(allb[x][1][0])<=bound-4]
    IRs=set(IR)
    for ii,i in enumerate(small):
        if i>=nN or i not in IRs: continue
        for j in small:
            if j<nN and j<i: continue
            if span(allb[i][1][0])+span(allb[j][1][0])>bound: continue
            p=vc.star(allb[i][1],allb[j][1])
            for mu,N,J in eng.hclosures(p):
                res['ncand']['S4']+=1
                if mu=='all': continue
                if len(J)==1: res['units'].append((mu,N,allb[i][2],allb[j][2],allb[i][3],allb[j][3],'S4'))
    print('S4 small pairs (span sum <=%d) checks'%bound,res['ncand']['S4'],'units',len(res['units']),round(time.time()-t0,1),flush=True)
    near=res['near']; near.sort(key=lambda r:(-r[0],r[3]))
    hist=collections.Counter(min(r[0],15) for r in near)
    keep=[(r[:7],r[9],allb[r[7]][2],allb[r[8]][2],allb[r[7]][3],allb[r[8]][3]) for r in near[:400]]
    bysp=sorted(near,key=lambda r:(r[3]-r[4],r[3]))[:200]
    keep2=[(r[:7],r[9],allb[r[7]][2],allb[r[8]][2],allb[r[7]][3],allb[r[8]][3]) for r in bysp]
    mins=sorted(near,key=lambda r:r[3])[:200]
    keep3=[(r[:7],r[9],allb[r[7]][2],allb[r[8]][2],allb[r[7]][3],allb[r[8]][3]) for r in mins]
    outd=dict(spec=spec,ncand=dict(res['ncand']),nchk=dict(res['nchk']),units=res['units'],two_end=keep,rel_span=keep2,min_span=keep3,
              hist=dict(hist),nlib=(nN,len(rat)),time=time.time()-t0)
    pickle.dump(outd,open(out,'wb'))
    print('DONE',dict(res['ncand']),'units',len(res['units']),'time',round(time.time()-t0,1))
    print('two-ended depth hist',sorted(hist.items()))
    for r in keep[:10]: print(r[0],r[1],r[4],r[5])
if __name__=='__main__':
    spec=json.loads(sys.argv[1]); run(spec,sys.argv[2])
