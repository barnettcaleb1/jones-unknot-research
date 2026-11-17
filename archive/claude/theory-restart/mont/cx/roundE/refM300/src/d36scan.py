"""vector-calculus unit scan for D36 configurations: one listed box of a D36 class + 0-4 top-300 boxes + 0-2 rational
boxes, EVERY Lemma-W candidate (H all mu, V all odd a)."""
import sys, random, time, pickle, collections
EA='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
sys.path.insert(0,EA); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import vc, eng, lib, spot_lib
from multiprocessing import Pool
items,pool=spot_lib.load()
CD=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','rb'))
OPEN24={'d2_457','d2_459','d2_460','d2_497','d2_536','d2_565','d2_895','d2_902','d2_1232','d2_1238','d2_1247','d2_1494','d2_2557','d2_2780','d2_3075','d2_3076','d2_3077','d2_3933','d2_4277','d2_4643','d2_5150','d2_5152','d2_5153','d2_5154'}
D36=[x for l,r in CD.items() if l.startswith('d2_') and l not in OPEN24 for x in r['xs']]
R6=lib.rational(6)
def job(seed):
    rng=random.Random(10**6+seed)
    xs=[rng.choice(D36)]+[rng.choice(pool[rng.randrange(300)]) for _ in range(rng.randint(0,4))]
    rr=[rng.randrange(len(R6)) for _ in range(rng.randint(0,2))]
    p=vc.starall([items[x][2] for x in xs]+[R6[i][1] for i in rr])
    cands=[c for c in eng.hclosures(p) if c[0]!='all']+eng.vclosures(p)
    return len(cands),sum(1 for c in cands if c[2] is not None and len(c[2])==1),len(xs)
if __name__=='__main__':
    t0=time.time(); NP=int(sys.argv[1]); nc=0; nu=0
    print('D36 listed boxes',len(D36),flush=True)
    with Pool(2) as P:
        for a,b,k in P.imap_unordered(job,range(NP),chunksize=10): nc+=a; nu+=b
    print('D36 scan: products %d, Lemma-W candidates %d, UNITS %d (%.0fs)'%(NP,nc,nu,time.time()-t0))
