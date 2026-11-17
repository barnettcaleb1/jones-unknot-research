"""J0 sanity for THEOREM M300: random multisets of 2-4 boxes from the top-300 classes x 0-2 rational boxes (R(5)); exact closures
(all mu, all odd a, Lemma W windows).  The theorem predicts 0 units; any unit would expose an unsound step."""
import sys, random, time, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact, classes, lib
from multiprocessing import Pool
if __name__=='__main__':
    t0=time.time(); random.seed(17); NP=int(sys.argv[1])
    items=exact.load_items(); R=lib.rational(5)
    pool=[x for c in classes.top(300) for x in classes.SIGS[c.key]]
    jobs=[]
    for i in range(NP):
        k=random.choice([2,2,3,3,4]); n=random.choice([0,1,2])
        xs=[random.choice(pool) for _ in range(k)]; rr=[random.randrange(len(R)) for _ in range(n)]
        jobs.append((('J0',tuple(xs),tuple(rr)),[items[x][2] for x in xs]+[R[i][1] for i in rr]))
    units=[]; nc=0; ms=[]
    with Pool(3) as P:
        for o in P.imap_unordered(exact.check,jobs,chunksize=16):
            nc+=o['n']
            if o['units']: units.append((o['tag'],o['units'])); print('UNIT',o['tag'],o['units'],flush=True)
            if o['minspan']: ms.append(o['minspan'][0])
    print('J0 products %d candidates %d UNITS %d min span %s time %.1f'%(len(jobs),nc,len(units),min(ms) if ms else None,time.time()-t0),flush=True)
