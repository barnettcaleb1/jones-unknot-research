"""EXACT search of the order-3 survivors B^3 x u1 x u2 (B = box 50216 [d2_497] and its mirror 50139 [d2_460]), u_i in R(L)."""
import sys, itertools, time, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact, lib
from multiprocessing import Pool
if __name__=='__main__':
    t0=time.time(); L=int(sys.argv[1])
    items=exact.load_items(); R=lib.rational(L)
    jobs=[]
    for x in (50216,50139):
        v=items[x][2]
        for n in (1,2,3) if L<=5 else (2,):
            for rr in itertools.combinations_with_replacement(range(len(R)),n):
                jobs.append((('P3',x,L,rr),[v,v,v]+[R[i][1] for i in rr]))
    print('jobs',len(jobs),flush=True)
    units=[]; gates=[]; ncand=0; best=[]
    with Pool(4) as P:
        for o in P.imap_unordered(exact.check,jobs,chunksize=32):
            ncand+=o['n']
            if o['units']: units.append((o['tag'],o['units'])); print('UNIT',o['tag'],o['units'],flush=True)
            for g in o['gates']: gates.append((o['tag'],g))
            if o['minspan']: best.append((o['minspan'],o['tag']))
    best.sort()
    print('P3 L=%d products %d candidates %d UNITS %d gate-passers %d min span %s time %.1f'%(L,len(jobs),ncand,len(units),len(gates),best[0] if best else None,time.time()-t0),flush=True)
    for b in best[:5]: print('  ',b)
    pickle.dump(dict(units=units,gates=gates,best=best[:50],ncand=ncand),open('probe_exact_%d.pkl'%L,'wb'))
