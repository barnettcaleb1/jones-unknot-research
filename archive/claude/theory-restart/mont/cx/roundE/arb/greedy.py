"""Find a CERTIFIED family: S* = top-300 + D36 + (new eligible signatures minus a removed set D) such that EVERY case-LP is closed
(uniform over all multiplicities).  Iterate: run all case-LPs, put every new class in the support of an open LP into D, repeat.
Output greedy_<tag>.pkl: D (dangerous classes with keys/reps), rounds, final verdict."""
import sys, pickle, time, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import arblp, d2two, lpg, run_arblp
from multiprocessing import Pool
SS=None
def init(S):
    global SS; SS=S
def one(job): return arblp.decide_job(SS,job)
if __name__=='__main__':
    tag=sys.argv[1]; files=[f for f in sys.argv[2:] if f!='resume']; t0=time.time()
    Sall,reps=run_arblp.load(files)
    NB=len(d2two.S); newc=Sall[NB:]
    D=set(); rounds=[]; prev=None
    if len(sys.argv)>2 and sys.argv[2]=='resume':
        files=sys.argv[3:]; Sall,reps=run_arblp.load(files); NB=len(d2two.S); newc=Sall[NB:]
        G0=pickle.load(open('greedy_%s.pkl'%tag,'rb')); D=set(G0['D']); rounds=G0['rounds']
        prev=set(r[0] for r in G0['final_open'])
        sup=collections.Counter(l for r in G0['final_open'] if r[1]=='open' for l in r[2][0] if l.startswith('g1')); D|=set(sup)
    for rnd in range(len(rounds),40):
        S=d2two.S+[c for c in newc if c.label not in D]
        jobs=arblp.jobs_for(Sall)          # lattice from ALL classes (superset of slices)
        if prev is not None:
            jobs=[j for j in jobs if j in prev]   # only re-test jobs open last round (closed ones stay closed: S shrank)
        with Pool(3,initializer=init,initargs=(S,)) as P: res=P.map(one,jobs,chunksize=4)
        opn=[r for r in res if r[1]!='closed']
        sup=collections.Counter(l for r in opn if r[1]=='open' for l in r[2][0] if l.startswith('g1'))
        bad=[r for r in opn if r[1]=='open' and not any(l.startswith('g1') for l in r[2][0])]
        rounds.append(dict(n_jobs=len(jobs),n_open=len(opn),n_sup=len(sup),bad=len(bad)))
        print('round',rnd,'|S| =',len(S),'jobs',len(jobs),'open',len(opn),'new support classes',len(sup),'open w/o new class',len(bad),
              'time',round(time.time()-t0,1),flush=True)
        if not opn: break
        if not sup: print('  open cases not caused by new classes:',[r[0] for r in opn][:5]); break
        D|=set(sup); prev=set(r[0] for r in opn)
    Dk={l:(c.key,reps.get(l)) for c in newc for l in [c.label] if l in D}
    pickle.dump(dict(D=Dk,rounds=rounds,final_open=[r for r in res if r[1]!='closed'],nS=len(S)),open('greedy_%s.pkl'%tag,'wb'))
    print('FINAL: certified family = top-300 + D36 + %d new classes; removed (dangerous) %d; open cases left %d'%(len(S)-NB,len(D),len(opn)))
