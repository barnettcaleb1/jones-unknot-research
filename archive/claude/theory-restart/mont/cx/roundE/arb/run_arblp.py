"""Uniform LP over S = top-300 + D36 + the ELIGIBLE depth-one signatures from gen1 pickles given on the command line
(multisets of n rational boxes, |m| <= 7, |N| <= 4).  Output arblp_<tag>.pkl / log: per case closed/open (+ LP support)."""
import sys, pickle, time, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import arblp, d2two, lpg
from fractions import Fraction as Fr
from multiprocessing import Pool
SS=None
def init(S):
    global SS; SS=S
def one(job): return arblp.decide_job(SS,job)
def load(tag_files):
    base=d2two.S; keys=set(c.key for c in base); S=list(base); reps={}
    for f in tag_files:
        tot=pickle.load(open(f,'rb'))
        for k,(cnt,el,rep) in tot.items():
            if not el or k in keys: continue
            keys.add(k); c=lpg.Cls(k,cnt,'g1_%d'%len(S)); S.append(c); reps[c.label]=(f,rep)
    return S,reps
if __name__=='__main__':
    tag=sys.argv[1]; files=sys.argv[2:]; t0=time.time()
    S,reps=load(files)
    jobs=arblp.jobs_for(S)
    print('S: %d classes (%d new depth-one signatures); jobs %d'%(len(S),len(S)-len(d2two.S),len(jobs)),flush=True)
    res=[]
    with Pool(3,initializer=init,initargs=(S,)) as P:
        for r in P.imap_unordered(one,jobs,chunksize=4):
            res.append(r)
            if r[1]!='closed': print('  ',r[0],r[1],str(r[2])[:400],flush=True)
            if len(res)%200==0: print('progress',len(res),round(time.time()-t0,1),flush=True)
    pickle.dump(dict(res=res,labels=[c.label for c in S],keys=[c.key for c in S],reps=reps),open('arblp_%s.pkl'%tag,'wb'))
    print('DONE',len(res),dict(collections.Counter(r[1] for r in res)),'time',round(time.time()-t0,1),flush=True)
