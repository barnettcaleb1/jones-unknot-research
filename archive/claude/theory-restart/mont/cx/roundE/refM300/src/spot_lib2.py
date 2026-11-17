"""spot-check (v2): random multisets of 2-5 top-300 boxes (nesting depth of the box half-word <= DMAX, to keep lp.J
tractable) + 0-2 rational companions; closure H or V at a FORCED Lemma-W coincidence:
  H: a candidate (mu, N) of eng.hclosures (degree coincidence at an end for N, mu at P/Q end alignment);
  V: a candidate (a, N) of eng.vclosures (degree coincidence + leading cancellation, or both ends coincide); if none
     exists, a forced DEGREE coincidence N = N_top(a) or N_bot(a) for a random odd 3 <= |a| <= 9.
Every Lemma-W candidate of the product (closure kind) is also scanned for units with the vector calculus."""
import sys, pickle, random, time
EA='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
sys.path.insert(0,EA); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import vc, eng
from vc import top, bot
import spot_lib
def depth(w):
    d=0; md=0
    for L in w.split('.'):
        if L[0] in 'rl': d+=1; md=max(md,d)
        elif L[0]=='u': d-=1
    return md
_sh=None
def shallow(DMAX):
    global _sh
    if _sh is None:
        items,pool=spot_lib.load()
        _sh=[[x for x in pool[c] if depth(vc.word(items[x][1]))<=DMAX] for c in range(300)]
    return _sh
def build(seed,DMAX=3):
    items,pool=spot_lib.load(); sh=shallow(DMAX); rng=random.Random(seed)
    cs=[c for c in range(300) if sh[c]]
    while True:
        k=rng.choice([2,2,3,3,4,5]); n=rng.choice([0,1,1,2])
        cls=[rng.choice(cs) for _ in range(k)]
        if rng.random()<0.3: cls[1]=cls[0]
        xs=[rng.choice(sh[c]) for c in cls]
        if rng.random()<0.15: xs[1]=xs[0]
        rats=[spot_lib.rand_rational(rng,rng.randint(2,5)) for _ in range(n)]
        kind=rng.choice(['H','V'])
        vecs=[items[x][2] for x in xs]+[v for w,v in rats]; trees=[items[x][1] for x in xs]+[('w',w) for w,v in rats]
        p=vc.starall(vecs)
        if kind=='H':
            cands=[c for c in eng.hclosures(p) if c[0]!='all']; how='lemmaW'
        else:
            cands=eng.vclosures(p); how='lemmaW'
        units=[c[:2] for c in cands if c[2] is not None and len(c[2])==1]
        if cands:
            x,N,Jraw=rng.choice(cands)
        elif kind=='V':
            A,B=p; got=None
            for _ in range(20):
                a=rng.choice([3,5,7,9])*rng.choice([1,-1]); a1,aV=eng.WV(a)
                nt=top(aV)+top(B)-top(a1)-top(A); nb=bot(aV)+bot(B)-bot(a1)-bot(A)
                Ns=[z//3 for z in (nt,nb) if z%3==0]
                if Ns: got=(a,rng.choice(Ns)); break
            if got is None: continue
            x,N=got; Jraw=eng.divexact(eng.add(eng.mul(a1,A),eng.shift(eng.mul(aV,B),-3*N)),eng.PHI3); how='degree-only'
        else: continue
        meta=dict(seed=seed,cls=cls,xs=xs,rats=[w for w,v in rats],kind=kind,x=x,N=N,how=how,ncand=len(cands),units_vc=units)
        body=('p',trees+([('w',('Y' if N>0 else 'y')*abs(N))] if N else []))
        bw=vc.word(body)
        if kind=='H': w='s.r2.'+spot_lib.tw(-x)+bw+'.u1'
        else: w='s.l1.'+bw+'.'+(('x2.' if x>0 else 'y2.')*abs(x))+'u1'
        meta['word']=w; meta['Jvc']=vc.norm(Jraw) if Jraw else None; meta['depth']=depth(w); meta['len']=len(w.split('.'))
        # coincidence depth (agreement orders at both ends of S1 and -S2) via the raw polynomial F = Phi3 * Jraw
        return meta
