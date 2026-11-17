# Classification CONJECTURE (claim 8): level-m symbols constant on each type.  Types from the builder's classifier
# (read-only import of ident/chord.py); all values and signs from my own code.  Tested quantities: M_3, v_3(K), D,
# v_3(K_in), N_3 at level 3; G4 (= M_4 part) and M_4 at level 4; and delta-dependence of the M_k symbols.
import sys, random, itertools, time, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, mytrav as T, constit as C, lp, flat_search as fs
import chord
from fractions import Fraction as Fr
m=int(sys.argv[1]); seed=int(sys.argv[2]); tmax=float(sys.argv[3]); rnd=random.Random(seed); t0=time.time()
cache={}
def vals(w):
    if w in cache: return cache[w]
    v=R.all_vals(w)
    if v is None: cache[w]=None; return None
    if m==2:
        ki=C.inv_tokens(C.tokens(w,'in'),with_alex=False)
        if ki is None: cache[w]=None; return None
        out={'M2':v['M2'],'a2':v['a2'],'N2':v['N2'],'Kin.a2':ki['a2']}
        cache[w]=out; return out
    if m==4:
        out={'M4':v['M4'],'G4':v['G4'],'N4':R.nmom(v['J'],4),'D':v['D']}
        cache[w]=out; return out
    out={'M3':v['M3'],'M4':v['M4'],'v3':v['v3'],'D':v['D'],'G4':v['G4'],'N3':v['N3']}
    if m==3:
        ki=C.inv_tokens(C.tokens(w,'in'),with_alex=False)
        if ki is None: cache[w]=None; return None
        out['Kin.v3']=ki['v3']
    cache[w]=out; return out
def gw():
    r=rnd.random()
    if m==4 and r<0.7: return fs.gen(rnd,rnd.randint(6,12))
    if r<0.5: return fs.gen(rnd,rnd.randint(10,24))
    return R.gen2(rnd,rnd.randint(10,22),maxw=rnd.choice([3,5,7]),pw=rnd.choice([0.2,0.35]))
bytype={}; n=0
while time.time()-t0<tmax:
    w=gw()
    if not w or vals(w) is None: continue
    sd=T.site_data(w)
    if sd is None or len(sd)<m: continue
    sites=sorted(rnd.sample(sorted(sd),m))
    d=chord.diagram(w,sites)
    if d is None: continue
    ty=chord.dstr(d); toks=w.split('.'); alt={}; ok=True
    for S in itertools.product([0,1],repeat=m):
        v=vals(R.flip(toks,[s+1 for s,b in zip(sites,S) if b]))
        if v is None: ok=False; break
        for k,x in v.items(): alt[k]=alt.get(k,0)+(-1)**sum(S)*x
    if not ok: continue
    sg=1
    for s in sites: sg*=sd[s][2]
    sym={k:sg*x for k,x in alt.items()}
    n+=1; bytype.setdefault(ty,[]).append((w,sites,sym))
keys=list(next(iter(bytype.values()))[0][2].keys())
rep={t:L for t,L in bytype.items() if len(L)>1}
incons={k:[] for k in keys}
for t,L in rep.items():
    for k in keys:
        s=set(str(x[2][k]) for x in L)
        if len(s)>1: incons[k].append((t,sorted(s)))
print('level %d: configs %d, types %d, repeated types %d (configs in them %d)'%(m,n,len(bytype),len(rep),sum(len(L) for L in rep.values())))
for k in keys: print('  %-7s inconsistent types: %d %s'%(k,len(incons[k]),incons[k][:3]))
# delta dependence: compare symbols of types differing only by flipping all/one deltas
def dflip(ty,i):
    # flip delta of the i-th tangency token in the type string
    out=[]; c=0; j=0; s=ty
    toks=[]; k=0
    while k<len(s):
        if s[k]=='T': toks.append(s[k:k+3]); k+=3
        else: toks.append(s[k:k+2]); k+=2
    ti=[q for q,tk in enumerate(toks) if tk[0]=='T']
    if i>=len(ti): return None
    q=ti[i]; tk=toks[q]; toks[q]=tk[:2]+('v' if tk[2]=='^' else '^'); return ''.join(toks)
dd={k:[0,0] for k in keys}
for t,L in bytype.items():
    for i in range(3):
        t2=dflip(t,i)
        if t2 and t2 in bytype and t2!=t:
            for k in keys:
                same= str(L[0][2][k])==str(bytype[t2][0][2][k])
                dd[k][0 if same else 1]+=1
print('  delta-flip pairs (type vs same type with one delta flipped; non-canonical pairs may be missed): [same, different]')
for k in keys: print('   ',k,dd[k])
print('time %.0fs'%(time.time()-t0))
