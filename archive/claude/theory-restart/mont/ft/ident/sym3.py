# symbol-level fit: Delta^3 M_3 vs Delta^3 of v3 of K and constituents, over random triples of flip sites
import sys, random, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag, lp, flat_search as fs
import sympy as sp
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
rnd=random.Random(int(sys.argv[1])); m=int(sys.argv[2]); N=int(sys.argv[3])
keys=['K','Kin','Kout','Uin','Uout']
recs=[]
tries=0
while len(recs)<N and tries<5000:
    tries+=1
    w=fs.gen(rnd,rnd.randint(8,14))
    if not w: continue
    toks=w.split('.')
    fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
    if len(fl)<m: continue
    sites=rnd.sample(fl,m)
    alt={}; ok=True
    for S in itertools.product([0,1],repeat=m):
        ww=flip(toks,[s for s,b in zip(sites,S) if b])
        J=lp.J(ww)
        if J is None: ok=False; break
        inv=diag.all_invariants(ww)
        if inv is None or any(inv[k] is None for k in keys): ok=False; break
        sg=(-1)**sum(S)
        vals={'M2':M(J,2),'M3':M(J,3),'M4':M(J,4)}
        for k in keys:
            for q in ('a2','v3','j4','a4'): vals[k+'.'+q]=inv[k][q]
        for kk,v in vals.items(): alt[kk]=alt.get(kk,0)+sg*v
    if not ok: continue
    alt['w']=w; alt['sites']=sites
    recs.append(alt)
print('samples',len(recs))
json.dump([{k:(str(v) if not isinstance(v,(list,str,int)) else v) for k,v in r.items()} for r in recs],open('sym%d_%s.json'%(m,sys.argv[1]),'w'))
def fit(target, feats):
    A=sp.Matrix([[sp.Rational(str(d[f])) for f in feats] for d in recs])
    b=sp.Matrix([sp.Rational(str(d[target])) for d in recs])
    ATA=A.T*A
    if ATA.det()==0: return 'singular, rank %d'%A.rank()
    x=ATA.LUsolve(A.T*b); res=A*x-b
    return [str(v) for v in x], 'maxres', max(abs(v) for v in res)
if m==3:
    for feats in (['K.v3'],['K.v3','Kin.v3','Kout.v3'],['K.v3','Uin.v3','Uout.v3'],['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3']):
        print(feats, fit('M3',feats))
    print('nonzero M3 symbols:',sum(1 for r in recs if r['M3']!=0))
