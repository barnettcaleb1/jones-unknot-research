"""order-3 refinement of gen1 classes: for each ELIGIBLE order-2 signature, the set of order-3 end data (l3a, l3b at top and
bottom) realised, with one representative each.  Same box family as gen1 (multisets of n rational boxes from R(L), |N|<=4, 1<=|m|<=7)."""
import sys, itertools, pickle, time, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import jbox, lib
from jauto import logs
from fractions import Fraction as Fr
from multiprocessing import Pool
MS=[m for m in range(-7,8) if m]; NS=list(range(-4,5))
POOL=None
def init(L):
    global POOL
    POOL=[jbox.from_vec(r[1]) for r in lib.rational(L)]
def l3data(x):
    out=[]
    for e in ('top','bot'):
        A,B=x[e]
        if jbox.relprec(A)<3 or jbox.relprec(B)<3: return None
        la=logs(jbox.endjet(A,3)[2]); lb=logs(jbox.endjet(B,3)[2]); out+= [la[2],lb[2]]
    return tuple(out)
def work(ms):
    out={}
    for idx in ms:
        x=POOL[idx[0]]
        for i in idx[1:]: x=jbox.star(x,POOL[i])
        for N in NS:
            y=jbox.ypow(N,x)
            for m in MS:
                z=jbox.nest(m,y)
                try: key,el,info=jbox.signature(z)
                except AssertionError: continue
                if key is None or not el: continue
                d3=l3data(z)
                if d3 is None: continue
                out.setdefault(key,{}).setdefault(d3,(idx,N,m))
    return out
if __name__=='__main__':
    L=int(sys.argv[1]); n=int(sys.argv[2]); t0=time.time()
    R=lib.rational(L); idxs=list(itertools.combinations_with_replacement(range(len(R)),n))
    chunks=[idxs[i::32] for i in range(32)]
    tot={}
    with Pool(3,initializer=init,initargs=(L,)) as P:
        for out in P.imap_unordered(work,chunks):
            for k,d in out.items():
                for d3,rep in d.items(): tot.setdefault(k,{}).setdefault(d3,rep)
    print('R(%d) n=%d: eligible order-2 classes %d, order-3 subclasses %d, time %.1f'%(L,n,len(tot),sum(len(v) for v in tot.values()),time.time()-t0))
    pickle.dump(tot,open('gen1k3_R%d_n%d.pkl'%(L,n),'wb'))
