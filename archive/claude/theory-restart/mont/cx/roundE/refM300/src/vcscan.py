"""broad vector-calculus scan (complements the lp.J sample, ANY nesting depth): random products of 2-6 listed top-300 boxes
+ 0-2 rational boxes; EVERY Lemma-W candidate (H all mu, V all odd a): units; and the sigma-law / P0 logic on actual
closures: X_end := l1(s2) - l1(s1) at each end; X_top + X_bot == mB (= sigma.k - sigma*) always; when one end has r >= 2,
the other end's mismatch == mB."""
import sys, random, time, pickle, collections
EA='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
sys.path.insert(0,EA); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import vc, eng, lib, spot_lib
import rlaurent as RL
from fractions import Fraction as Fr
from multiprocessing import Pool
items,pool=spot_lib.load()
CD=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','rb'))
W=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/wdata.pkl','rb'))
R6=lib.rational(6)
def l1(f,end): return RL.logdata(f,end,1)[2][0]
def ragree(S1,S2,end):
    F=RL.padd(S1,S2)
    if not F: return 99
    if end=='top':
        if max(S1)!=max(S2): return 0
        return max(S1)-max(F)
    if min(S1)!=min(S2): return 0
    return min(F)-min(S1)
def job(seed):
    rng=random.Random(seed)
    k=rng.randint(2,6); n=rng.randint(0,2)
    cls=[rng.randrange(300) for _ in range(k)]
    xs=[rng.choice(pool[c]) for c in cls]; rr=[rng.randrange(len(R6)) for _ in range(n)]
    vecs=[items[x][2] for x in xs]+[R6[i][1] for i in rr]
    sig=sum(CD['top%d'%c]['key'][2] for c in cls)
    A,B=vc.starall(vecs)
    out=dict(nc=0,units=0,lawfail=0,strong=0,weakok=0)
    cands=[('H',)+c for c in eng.hclosures((A,B)) if c[0]!='all']+[('V',)+c for c in eng.vclosures((A,B))]
    for kind,x,N,J in cands:
        out['nc']+=1
        if J is not None and len(J)==1: out['units']+=1
        if kind=='H': w1,w2=eng.W(x); sgs=W['H'][x][1] if x in W['H'] else W['H'][4 if x>0 else -4][1]
        else:
            if abs(x)<3: continue
            w1,w2=eng.WV(x); sgs=Fr(-1)
        S1=RL.pmul(w1,A); S2=RL.pshift(RL.pmul(w2,B),-3*N)
        X={e:l1(S2,e)-l1(S1,e) for e in ('top','bot')}
        mB=sig-sgs
        if X['top']+X['bot']!=mB: out['lawfail']+=1
        rt,rb=ragree(S1,RL.pneg(RL.pneg(S2)),'top'),ragree(S1,S2,'bot')
        for se,we in (('top','bot'),('bot','top')):
            r=ragree(S1,S2,se)
            if r>=2:
                out['strong']+=1
                if X[we]==mB: out['weakok']+=1
    return out
if __name__=='__main__':
    t0=time.time(); NP=int(sys.argv[1])
    tot=collections.Counter()
    with Pool(2) as P:
        for o in P.imap_unordered(job,range(NP),chunksize=10):
            for kk,v in o.items(): tot[kk]+=v
    print('products %d: Lemma-W candidates %d, UNITS %d; sigma-law X_top + X_bot == mB failures %d; ends with r >= 2: %d, opposite-end mismatch == mB in %d  (%.0fs)'%(NP,tot['nc'],tot['units'],tot['lawfail'],tot['strong'],tot['weakok'],time.time()-t0))
