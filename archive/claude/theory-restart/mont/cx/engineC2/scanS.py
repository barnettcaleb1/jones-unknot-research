"""E1: S-necklace scan.  For every box vector v (canonical mod Y), integral part N (all N with a top tie), even m != 0:
R = v_N^T G(m) v_N~ (palindromic); rho = (naive_top - actual_top)/naive_top (1 <=> unit).  Gates on near misses."""
import sys, pickle, time, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import fastS, lp, vc, lib
from lp import top, bot, span, shift
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
def scan_box(key,v,tag,ms,stats,best,units):
    a,b=v
    for m in ms:
        G=tab[m]
        T1=top(G[0][0])+span(a); T4=top(G[1][1])+span(b)
        T20=top(G[0][1])+top(a)-bot(b); T30=top(G[1][0])+top(b)-bot(a)
        lo=-((abs(T20)+abs(T30)+abs(T1)+abs(T4))//3+3); hi=-lo
        for N in range(lo,hi+1):
            T2=T20+3*N; T3=T30-3*N
            Ts=sorted([T1,T2,T3,T4],reverse=True)
            if Ts[0]>4 and Ts[0]!=Ts[1]: continue
            vN=(a,shift(b,-3*N))
            R=fastS.R_of(G,vN)
            stats['cand']+=1
            naive=Ts[0]-4; act=top(R)
            if len(R)==1:
                units.append((tag,key,m,N,R)); continue
            if naive<=0: continue
            rho=(naive-act)/naive
            J=lp.normalize(R)
            a2,z10=fastS.gates(J)
            rec=(rho,naive-act,naive,span(J),m,N,tag,key,a2,z10)
            if rho>best.get('rho',(0,))[0]: best['rho']=rec
            if naive-act>best.get('depth',(0,0))[1]: best['depth']=rec
            if a2==0 and z10:
                best.setdefault('gated',[]).append(rec)
            if rho>=0.5: best.setdefault('hi',[]).append(rec)
if __name__=='__main__':
    which=sys.argv[1]
    ms=[m for m in sorted(tab) if m!=0]
    t0=time.time()
    if which=='R7':
        lib_=[(k,v,'R:'+str(T)) for k,v,T,tag in lib.rational(7)]
    elif which=='G':
        lib_=[(k,v,'G:'+str(T)) for k,v,T,tag in lib.general()]
    elif which=='P5':
        R5=lib.rational(5); lib_=[]; seen=set()
        for i in range(len(R5)):
            for j in range(i,len(R5)):
                v=vc.starall([R5[i][1],R5[j][1]]); v2,T=lib.canonY(v,('p',[R5[i][2],R5[j][2]]))
                k=lib.vkey(v2)
                if k in seen: continue
                seen.add(k); lib_.append((k,v2,'P:'+str(T)))
    elif which=='N5':
        R5=lib.rational(5)+lib.general(); lib_=[]; seen=set()
        for u in R5:
            for kk in [-4,-3,-2,-1,1,2,3,4]:
                for NN in [-2,-1,0,1,2]:
                    try: nd=lib.node(kk,NN,[u])
                    except AssertionError: continue
                    if nd is None or nd[0] in seen: continue
                    seen.add(nd[0]); lib_.append((nd[0],nd[1],'N:'+str(nd[2])))
    stats={'cand':0}; best={}; units=[]
    for k,v,tag in lib_:
        scan_box(k,v,tag,ms,stats,best,units)
    print(which,'boxes',len(lib_),'candidates',stats['cand'],'units',len(units),'time %.1f'%(time.time()-t0))
    print(' best rho  :',best.get('rho'))
    print(' best depth:',best.get('depth'))
    g=sorted(best.get('gated',[]),key=lambda r:r[3])[:5]
    print(' doubly gated (a2=0 & zeta10):',len(best.get('gated',[])),'smallest spans:',[(r[3],r[4],r[5],r[6][:60]) for r in g])
    hi=sorted(best.get('hi',[]),reverse=True)[:8]
    print(' rho>=0.5:',len(best.get('hi',[])),[(round(r[0],3),r[1],r[2],r[4],r[5],r[6][:50]) for r in hi])
    for u in units[:10]: print(' UNIT',u)
    pickle.dump((stats,best,units),open('scanS_%s.pkl'%which,'wb'))
