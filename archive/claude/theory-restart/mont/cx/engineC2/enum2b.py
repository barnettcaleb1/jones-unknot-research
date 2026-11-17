import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import plat2, enum2, constit, sym, lp, fastS
NAME={'a':'s1p','A':'s1m','b':'s2p','B':'s2m','c':'tlp','C':'tlm','d':'trp','D':'trm'}
if __name__=='__main__':
    first=sys.argv[1]; Lmax=int(sys.argv[2])
    t0=time.time(); res={}; n=0; units=[]; cert={'K1knotted':0,'K1unknot':0}
    for w in enum2.words(first,Lmax):
        if not plat2.is_arc(w): continue
        J=plat2.J(w); n+=1
        if J is None: print('NONE',w); continue
        key=tuple(sorted(J.items()))
        if len(J)==1:
            ev=sym.symmetric(plat2.top_events(w))
            triv=constit.trivial_constituent(ev)
            cert['K1unknot' if triv else 'K1knotted']+=1
            units.append((w,triv))
            if not triv: print('UNIT WITH KNOTTED CONSTITUENT',w,flush=True)
            continue
        if key in res: continue
        tp,bt=enum2.tropical(w)
        res[key]=(w,lp.span(J)/2.0,(tp-bt)/8.0)+fastS.gates(J)
    pickle.dump((res,units,n),open('enum2_%s_%d.pkl'%(NAME[first],Lmax),'wb'))
    print(first,Lmax,'words',n,'distinct nonunit J',len(res),'unit words',len(units),cert,'time %.0f'%(time.time()-t0))
