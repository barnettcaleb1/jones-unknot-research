"""order-3 subclasses of the UNSAFE n=3/n=4 classes only (certtest2), for the per-class order-3 extension."""
import sys, itertools, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import jbox, lib, gen1k3
from multiprocessing import Pool
U=None
def init(L,keys):
    global U
    gen1k3.init(L); U=keys
def work(ms):
    out=gen1k3.work(ms)
    return {k:v for k,v in out.items() if k in U}
if __name__=='__main__':
    L=int(sys.argv[1]); n=int(sys.argv[2]); t0=time.time()
    C=pickle.load(open('certtest2.pkl','rb'))
    keys=set(k for l,k,c in C['unsafe'] if l.startswith('n%d'%n))
    R=lib.rational(L); idxs=list(itertools.combinations_with_replacement(range(len(R)),n))
    chunks=[idxs[i::48] for i in range(48)]
    tot={}
    with Pool(3,initializer=init,initargs=(L,keys)) as P:
        for out in P.imap_unordered(work,chunks):
            for k,d in out.items():
                for d3,rep in d.items(): tot.setdefault(k,{}).setdefault(d3,rep)
    print('R(%d) n=%d unsafe classes %d found %d, order-3 subclasses %d, time %.1f'%(L,n,len(keys),len(tot),sum(len(v) for v in tot.values()),time.time()-t0),flush=True)
    pickle.dump(tot,open('gen1k3u_R%d_n%d.pkl'%(L,n),'wb'))
