"""refV3: random exact sample for n = 3, 4 (R(6), odd a in [-9,9], |N| <= 12): exact J, J_* loophole test, spans."""
import sys, time, pickle, random, multiprocessing as mp
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import vc, lib
from jstar import jstar_hit
R6=lib.rational(6)
OUT='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/'
def work(args):
    cmb,a,N=args
    J=vc.J_vert(a,vc.Ypow(N,vc.starall([R6[i][1] for i in cmb])))
    if J is None: return (cmb,a,N,'NONE')
    return (cmb,a,N,vc.span(J),vc.a2(J),jstar_hit(J) if J!={0:1} else None)
if __name__=='__main__':
    NS=int(sys.argv[1]) if len(sys.argv)>1 else 100000
    rnd=random.Random(17); jobs=[]
    for i in range(NS):
        n=3+i%2
        jobs.append((tuple(sorted(rnd.randrange(len(R6)) for _ in range(n))),rnd.choice(list(range(-9,10,2))),rnd.randint(-12,12)))
    t0=time.time(); res=[]
    with mp.Pool(4) as pool:
        for r in pool.imap_unordered(work,jobs,chunksize=256): res.append(r)
    hits=[r for r in res if r[3]!='NONE' and r[5] is not None]
    print('n=3,4 random exact closures:',len(res),' None:',sum(1 for r in res if r[3]=='NONE'),' units:',sum(1 for r in res if r[3]==0),
          ' J_* loophole/anomalies:',len(hits),hits[:5],' min span:',min(r[3] for r in res if r[3]!='NONE'),' %.0fs'%(time.time()-t0))
    pickle.dump(res,open(OUT+'jstar34.pkl','wb'))
