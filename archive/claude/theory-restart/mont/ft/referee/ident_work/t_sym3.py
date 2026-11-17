# Claim 3: level-3 symbol of D (sigma1 sigma2 sigma3 * alternating sum) in 8Z; rule on '2 chords + 1 tangency':
#   D-symbol = 8 (-1)^{#odd chords} [T inside both chords];  plus level-4 alternating sums of D vanish (FT).
import sys, random, itertools, time, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, mytrav as T, lp, flat_search as fs
from fractions import Fraction as Fr
seed=int(sys.argv[1]); N=int(sys.argv[2]); rnd=random.Random(seed); t0=time.time()
cache={}
def Dval(w):
    if w in cache: return cache[w]
    J=lp.J(w)
    if J is None: cache[w]=None; return None
    V=R.VK(w)
    if V is None: cache[w]=None; return None
    a2,v3,j4=R.vinv(V); cache[w]=Fr(R.mom(J,3)-432*v3,180); return cache[w]
def gw():
    r=rnd.random()
    if r<0.4: return fs.gen(rnd,rnd.randint(8,20))
    return R.gen2(rnd,rnd.randint(8,20),maxw=rnd.choice([3,5]),pw=rnd.choice([0.2,0.4]))
stats=dict(cfg=0,not8=0,rule_n=0,rule_bad=0,lev4=0,lev4bad=0); vals={}; badrule=[]
while stats['cfg']<N and time.time()-t0<230:
    w=gw()
    if not w or Dval(w) is None: continue
    seq=T.events2(w); sd=T.site_data(w,seq)
    if sd is None: continue
    toks=w.split('.')
    m=3 if rnd.random()<0.85 else 4
    if rnd.random()<0.5 and m==3:
        # bias toward 2 chords + 1 tangency
        ch=[t for t in sd if sd[t][0]=='C']; tg=[t for t in sd if sd[t][0]=='T']
        if len(ch)<2 or len(tg)<1: continue
        sites=rnd.sample(ch,2)+rnd.sample(tg,1)
    else:
        if len(sd)<m: continue
        sites=rnd.sample(sorted(sd),m)
    alt=0; ok=True
    for S in itertools.product([0,1],repeat=m):
        v=Dval(R.flip(toks,[s+1 for s,b in zip(sites,S) if b]))
        if v is None: ok=False; break
        alt+=(-1)**sum(S)*v
    if not ok: continue
    if m==4:
        stats['lev4']+=1; stats['lev4bad']+= (alt!=0); continue
    sg=1
    for s in sites: sg*=sd[s][2]
    sym=sg*alt; stats['cfg']+=1
    vals[sym]=vals.get(sym,0)+1
    if sym.denominator!=1 or sym%8!=0: stats['not8']+=1
    kinds=sorted(sd[s][0] for s in sites)
    if kinds==['C','C','T']:
        stats['rule_n']+=1
        pos={}
        for p,(t,k,d) in enumerate(seq): pos.setdefault(t,[]).append(p)
        tsite=[s for s in sites if sd[s][0]=='T'][0]; csites=[s for s in sites if sd[s][0]=='C']
        pT=pos[tsite][0]
        inside=all(min(pos[c])<pT<max(pos[c]) for c in csites)
        nodd=sum(1 for c in csites if sd[c][1]=='-')
        pred=8*(-1)**nodd*(1 if inside else 0)
        if pred!=sym:
            stats['rule_bad']+=1
            if len(badrule)<8: badrule.append(dict(w=w,sites=sites,sym=str(sym),pred=pred,inside=inside,nodd=nodd,
                                     data=[sd[s] for s in sites],order=[(s,pos[s]) for s in sites]))
print(stats,'time %.0fs'%(time.time()-t0))
print('D-symbol value distribution:',sorted(((str(k),v) for k,v in vals.items()),key=lambda x:-x[1]))
for b in badrule: print('RULE FAIL',b)
