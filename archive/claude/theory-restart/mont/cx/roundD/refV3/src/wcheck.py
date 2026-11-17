"""refV3: Lemma-W cross-check of the brute force.  For every multiset of R(6) boxes with n <= NMAX (n = 4: random sample), run
engineA's Lemma-W candidate generator eng.vclosures (FULL a-window |a| <= max(span A, span B)+8, N in {N_top, N_bot}) and
collect exact units.  Compare with brute.py (all a in [-9,9], |N| <= 12, no Lemma W)."""
import sys, time, pickle, itertools, random, multiprocessing as mp
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import vc, lib, eng
R6=lib.rational(6)
OUT='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/'
def work(cmb):
    p=vc.starall([R6[i][1] for i in cmb])
    out=[]; ncand=0; maxa=0
    for (a,N,Jr) in eng.vclosures(p):
        ncand+=1
        if Jr is not None and len(Jr)==1: out.append((cmb,a,N))
    return out,ncand
if __name__=='__main__':
    NMAX=int(sys.argv[1]) if len(sys.argv)>1 else 3
    NS4=int(sys.argv[2]) if len(sys.argv)>2 else 20000
    jobs=[]
    for n in range(1,NMAX+1):
        jobs+=list(itertools.combinations_with_replacement(range(len(R6)),n))
    rnd=random.Random(11)
    if NS4: jobs+=[tuple(sorted(rnd.randrange(len(R6)) for _ in range(4))) for _ in range(NS4)]
    print('multisets',len(jobs),flush=True)
    t0=time.time(); units=[]; nc=0
    with mp.Pool(8) as pool:
        for i,(u,c) in enumerate(pool.imap_unordered(work,jobs,chunksize=64)):
            units+=u; nc+=c
            if i%20000==0: print(i,len(units),nc,round(time.time()-t0),flush=True)
    print('Lemma-W candidates',nc,'units',len(units),round(time.time()-t0),flush=True)
    byk={}
    for (cmb,a,N) in units: byk[(len(cmb),a)]=byk.get((len(cmb),a),0)+1
    print('units by (n,a):',byk)
    print('units with |a|<=9 and |N|<=12:',sum(1 for (c,a,N) in units if abs(a)<=9 and abs(N)<=12))
    print('units outside that box:',[(c,a,N) for (c,a,N) in units if not (abs(a)<=9 and abs(N)<=12)])
    b=pickle.load(open(OUT+'brute_n4.pkl','rb'))
    bu=set((tuple(c),a,N) for (n,c,a,N,J) in b['exact_units'])
    wu=set((tuple(c),a,N) for (c,a,N) in units if abs(a)<=9 and abs(N)<=12)
    print('brute units == Lemma-W units in the box:',bu==wu, len(bu), len(wu))
    pickle.dump(units,open(OUT+'wcheck.pkl','wb'))
