"""spot-check library: random closures of multisets of 2-5 top-300 boxes (+ 0-2 rational companions), Lemma-W forced
candidates (engineA eng.py logic, imported read-only), exact lp.J on the explicit half-word vs the vector calculus."""
import sys, pickle, random, time
EA='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
sys.path.insert(0,EA); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import vc, eng, lp
import rlaurent as RL
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
_items=None; _pool=None
def load():
    global _items,_pool
    if _items is None:
        L=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1/libA_jets.pkl','rb'))
        it=[(tag,T,v) for (k,T,tag,tp,bt),v in zip(L['boxes'],L['vecs']) if tag!='R']
        d2=pickle.load(open(EA+'/d2pos_boxes.pkl','rb')); it+=[('d2pos',b[2],b[1]) for b in d2]
        CD=pickle.load(open(HERE+'classdata.pkl','rb'))
        _items=it; _pool=[CD['top%d'%i]['xs'] for i in range(300)]
    return _items,_pool
INV={'X':'x','x':'X','Y':'y','y':'Y'}
def rand_rational(rng,L):
    while True:
        w=rng.choice('Xx')
        while len(w)<L:
            c=rng.choice('XxYy')
            if INV[c]==w[-1]: continue
            w+=c
        v=vc.rat(w)
        if v is not None and len(v[0])>1: return w,v
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def make(seed):
    items,pool=load(); rng=random.Random(seed)
    k=rng.choice([2,2,3,3,4,5]); n=rng.choice([0,1,1,2])
    cls=[rng.randrange(300) for _ in range(k)]
    if k>=2 and rng.random()<0.3: cls[1]=cls[0]            # force repeated classes sometimes
    xs=[rng.choice(pool[c]) for c in cls]
    if k>=2 and rng.random()<0.15: xs[1]=xs[0]              # literally the same box twice
    rats=[rand_rational(rng,rng.randint(2,6)) for _ in range(n)]
    kind=rng.choice(['H','V'])
    return dict(seed=seed,cls=cls,xs=xs,rats=[w for w,v in rats],kind=kind), [items[x][2] for x in xs]+[v for w,v in rats], [items[x][1] for x in xs]+[('w',w) for w,v in rats]
def run(seed):
    t0=time.time()
    meta,vecs,trees=make(seed); rng=random.Random(seed*7+1)
    p=vc.starall(vecs)
    if meta['kind']=='H':
        cands=[c for c in eng.hclosures(p) if c[0]!='all']
    else:
        cands=eng.vclosures(p)
    # unit scan of ALL Lemma-W candidates with the vector calculus (complete for units of this product & closure kind)
    allunits=[]
    for c in cands:
        J=c[2]
        if J is None: continue
        if len(J)==1: allunits.append(c[:2])
    meta['ncand']=len(cands); meta['units_vc']=allunits
    if not cands: meta['note']='no candidates'; return meta
    x,N,Jraw=rng.choice(cands)
    body=('p',trees+([('w',('Y' if N>0 else 'y')*abs(N))] if N else []))
    bw=vc.word(body)
    if meta['kind']=='H':
        w='s.r2.'+tw(-x)+bw+'.u1'; Jvc=vc.norm(Jraw) if Jraw else None
    else:
        w='s.l1.'+bw+'.'+(('x2.' if x>0 else 'y2.')*abs(x))+'u1'; Jvc=vc.norm(Jraw) if Jraw else None
    t1=time.time()
    Jlp=lp.J(w)
    meta.update(x=x,N=N,word=w,len=len(w.split('.')),Jlp=Jlp,Jvc=Jvc,agree=(Jlp==Jvc),tJ=time.time()-t1,t=time.time()-t0)
    if Jlp is not None:
        meta['span']=max(Jlp)-min(Jlp); meta['unit']=(len(Jlp)==1); meta['a2']=lp.a2(Jlp)
    # depth of the forced coincidence: agreement orders at both ends of S1 vs -S2 (vector calculus)
    return meta
