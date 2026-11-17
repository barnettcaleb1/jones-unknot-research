"""E1: single-child root closures of library boxes: horizontal X^mu Y^N (general special regions) and vertical (Theorem V).
All candidate (mu,N) / (a,N) from the exact end-coincidence sets (complete for units)."""
import sys, time, json, collections, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, scan
from vc import top, bot, shift, mul, add, span
def run(boxes, label, out, do_vert=True, log=None):
    t0=time.time(); units=[]; best={}; stats=collections.Counter()
    two_end=[]   # (min(rt,rb), rt, rb, ...) best two-ended cancellations
    for ib,(k,v,T,tag) in enumerate(boxes):
        if ib%20000==0: print('  box',ib,'units',len(units),'time',round(time.time()-t0,1),flush=True)
        A,B=v
        for mu,N,J in eng.hclosures(v):
            stats['h']+=1
            if mu=='all': continue
            a1,a3=eng.W(mu); S1=mul(a1,A); S2=shift(mul(a3,B),-3*N); F=add(S1,S2)
            rt,rb,gs,fs=scan.depths(S1,S2,F)
            if len(J)==1:
                units.append(('H',mu,N,T,tag)); continue
            sJ=span(J)
            key=('H',tag)
            rec=(sJ, sJ-span(A), rt, rb, mu, N, T)
            if key not in best or rec[:2]<best[key][:2]: best[key]=rec
            if min(rt,rb)>=3: two_end.append((min(rt,rb),rt,rb,'H',mu,N,sJ,span(A),T))
        if do_vert:
            for a,N,J in eng.vclosures(v):
                stats['v']+=1
                a1,aV=eng.WV(a); S1=mul(a1,A); S2=shift(mul(aV,B),-3*N); F=add(S1,S2)
                rt,rb,gs,fs=scan.depths(S1,S2,F)
                if len(J)==1:
                    units.append(('V',a,N,T,tag)); continue
                sJ=span(J)
                key=('V',tag)
                rec=(sJ, sJ-span(A), rt, rb, a, N, T)
                if key not in best or rec[:2]<best[key][:2]: best[key]=rec
                if min(rt,rb)>=3: two_end.append((min(rt,rb),rt,rb,'V',a,N,sJ,span(A),T))
    two_end.sort(key=lambda r:(-r[0],r[6]))
    res=dict(label=label,n=len(boxes),stats=dict(stats),units=units,best=best,two_end=two_end[:200],time=time.time()-t0)
    pickle.dump(res,open(out,'wb'))
    return res
if __name__=='__main__':
    which=sys.argv[1]
    if which=='L0':
        R=lib.rational(8)
        r=run(R,'rational<=8','e1_L0.pkl')
    elif which=='G':
        G=lib.general(); R=lib.rational(6)
        boxes=list(G)
        seen=set(b[0] for b in boxes)
        for g in G:
            for m in (1,-1,2,-2,3,-3):
                for N in range(-3,4):
                    b=lib.node(m,N,[g])
                    if b and b[0] not in seen: seen.add(b[0]); boxes.append(b)
        for g in G:
            for u in R:
                for m in (1,-1,2,-2,3,-3):
                    for N in range(-3,4):
                        b=lib.node(m,N,[g,u])
                        if b and b[0] not in seen: seen.add(b[0]); boxes.append(b)
        print('G-library',len(boxes),flush=True)
        r=run(boxes,'general bodies + F_m(Y^N g) + F_m(Y^N g*u), u rational<=6, |m|<=3, |N|<=3','e1_G.pkl')
    elif which=='L1':
        R=lib.rational(int(sys.argv[2]) if len(sys.argv)>2 else 6)
        boxes=[]; seen=set()
        for i in range(len(R)):
            for j in range(i,len(R)):
                for m in (1,-1,2,-2,3,-3):
                    for N in range(-3,4):
                        b=lib.node(m,N,[R[i],R[j]])
                        if b and b[0] not in seen: seen.add(b[0]); boxes.append(b)
        print('L1-library',len(boxes),flush=True)
        r=run(boxes,'F_m(Y^N u_i*u_j), u rational<=%s, |m|<=3, |N|<=3'%(sys.argv[2] if len(sys.argv)>2 else 6),'e1_L1.pkl')
    print(r['label'],'boxes',r['n'],'stats',r['stats'],'units',len(r['units']),'time',round(r['time'],1))
    for u in r['units'][:20]: print('UNIT',u[:3],u[4],vc.hw(u[3]) if u[0]=='H' else '')
    print('two-ended (min depth >=3):',len(r['two_end']))
    for x in r['two_end'][:10]: print(x[:8])
