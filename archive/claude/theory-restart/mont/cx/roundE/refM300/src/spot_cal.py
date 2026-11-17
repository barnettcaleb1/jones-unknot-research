import sys, time, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import spot_lib, vc, lp, eng
items,pool=spot_lib.load()
def depth(w):
    d=0; md=0
    for L in w.split('.'):
        if L[0] in 'rl': d+=1; md=max(md,d)
        elif L[0]=='u': d-=1
    return md
shallow=[[x for x in pool[c] if depth(vc.word(items[x][1]))<=3] for c in range(300)]
rng=random.Random(5)
for k,kind in [(2,'V'),(2,'H'),(3,'V'),(3,'H')]:
    cs=[c for c in range(300) if shallow[c]]
    xs=[rng.choice(shallow[rng.choice(cs)]) for _ in range(k)]
    vecs=[items[x][2] for x in xs]; trees=[items[x][1] for x in xs]
    p=vc.starall(vecs)
    cands=[c for c in eng.hclosures(p) if c[0]!='all'] if kind=='H' else eng.vclosures(p)
    x,N,Jraw=rng.choice(cands)
    body=('p',trees+([('w',('Y' if N>0 else 'y')*abs(N))] if N else []))
    bw=vc.word(body)
    w=('s.r2.'+spot_lib.tw(-x)+bw+'.u1') if kind=='H' else ('s.l1.'+bw+'.'+(('x2.' if x>0 else 'y2.')*abs(x))+'u1')
    t=time.time(); J=lp.J(w); dt=time.time()-t
    print(kind,k,'ncand',len(cands),'x',x,'N',N,'len',len(w.split('.')),'depth',depth(w),'time %.1fs'%dt,'agree',J==vc.norm(Jraw),flush=True)
