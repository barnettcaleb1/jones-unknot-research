"""CLOSURE STEP 1 (depth one): signatures of F_m(Y^N u_1...u_n) over ALL multisets of n rational boxes from a pool, |N| <= 4,
1 <= |m| <= 7.  Records per n: distinct signatures (all / eligible), new ones vs smaller n, clipping test (m = +-7 vs +-6 and
N = +-4 vs +-3 give the same signature for the same multiset), low-precision count.  Output gen1_<pool>_<n>.pkl."""
import sys, itertools, pickle, time, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import jbox, lib
from multiprocessing import Pool
MS=[m for m in range(-7,8) if m]; NS=list(range(-4,5))
POOL=None
def init(L):
    global POOL
    R=lib.rational(L); POOL=[jbox.from_vec(r[1]) for r in R]
def work(ms):
    out={}; low=0; clipm=0; clipm_bad=0; clipN=0; clipN_bad=0; scal=0
    for idx in ms:
        x=POOL[idx[0]]
        for i in idx[1:]: x=jbox.star(x,POOL[i])
        for N in NS:
            y=jbox.ypow(N,x)
            sig={}
            for m in MS:
                try: key,el,info=jbox.signature(jbox.nest(m,y))
                except AssertionError: key=None
                if key is None: low+=1; continue
                sig[m]=key
                if key not in out: out[key]=[0,el,(idx,N,m)]
                out[key][0]+=1
            for a,b in ((7,6),(-7,-6)):
                if a in sig and b in sig:
                    clipm+=1; clipm_bad+=(sig[a]!=sig[b])
    return out,low,clipm,clipm_bad
if __name__=='__main__':
    L=int(sys.argv[1]); n=int(sys.argv[2]); t0=time.time()
    R=lib.rational(L); idxs=list(itertools.combinations_with_replacement(range(len(R)),n))
    chunks=[idxs[i::64] for i in range(64)]
    tot={}; low=cm=cmb=0
    with Pool(4,initializer=init,initargs=(L,)) as P:
        for out,l,a,b in P.imap_unordered(work,chunks):
            low+=l; cm+=a; cmb+=b
            for k,v in out.items():
                if k not in tot: tot[k]=v
                else: tot[k][0]+=v[0]
    el=sum(1 for v in tot.values() if v[1])
    print('pool R(%d) n=%d: multisets %d, boxes %d, distinct signatures %d (eligible %d), lowprec %d, clip m=+-7 vs +-6: %d/%d differ, time %.1f'
          %(L,n,len(idxs),len(idxs)*len(MS)*len(NS),len(tot),el,low,cmb,cm,time.time()-t0),flush=True)
    pickle.dump(tot,open('gen1_R%d_n%d.pkl'%(L,n),'wb'))
