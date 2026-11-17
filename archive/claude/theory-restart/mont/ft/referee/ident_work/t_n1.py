# Claim 9: N_k = sum J_e e^k finite type of order <= k; N_1 in 8Z; level-1 symbol of N_1 on T^, Tv, C+, C-.
import sys, random, itertools, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, mytrav as T, lp, flat_search as fs
seed=int(sys.argv[1]); rnd=random.Random(seed); t0=time.time()
def gw():
    return fs.gen(rnd,rnd.randint(8,22)) if rnd.random()<0.5 else R.gen2(rnd,rnd.randint(8,20),maxw=5,pw=0.3)
# (a) N1 in 8Z and level-1 symbols
sym={}; n8=0; tot=0; tries=0
while tot<300 and tries<20000:
    tries+=1; w=gw()
    if not w: continue
    J=lp.J(w)
    if J is None: continue
    sd=T.site_data(w)
    if sd is None: continue
    tot+=1; N1=R.nmom(J,1); n8+= (N1%8==0)
    toks=w.split('.')
    for t in rnd.sample(sorted(sd),min(3,len(sd))):
        J2=lp.J(R.flip(toks,[t+1]))
        if J2 is None: continue
        kind,lab,sg=sd[t]
        val=sg*(N1-R.nmom(J2,1))
        sym.setdefault(kind+lab,{}); sym[kind+lab][val]=sym[kind+lab].get(val,0)+1
print('N1 in 8Z: %d/%d'%(n8,tot))
print('level-1 symbol of N1 (sigma*(N1(w)-N1(w flipped))) by element type:',sym)
# (b) order: Delta^m N_k = 0 for m > k
res={}
done=0; tries=0
while done<80 and tries<20000:
    tries+=1; w=gw()
    if not w or lp.J(w) is None: continue
    toks=w.split('.'); fl=[i for i,a in enumerate(toks) if a[0] in 'xy' and a[1:].isdigit()]
    m=rnd.choice([2,3,4])
    if len(fl)<m: continue
    sites=rnd.sample(fl,m); Js={}; ok=True
    for S in itertools.product([0,1],repeat=m):
        Jw=lp.J(R.flip(toks,[s for s,b in zip(sites,S) if b]))
        if Jw is None: ok=False; break
        Js[S]=Jw
    if not ok: continue
    done+=1
    for k in range(0,5):
        alt=sum((-1)**sum(S)*R.nmom(Js[S],k) for S in Js)
        res.setdefault((m,k),[0,0])[0 if alt==0 else 1]+=1
print('Delta^m N_k: (m,k) -> [zero, nonzero]  (prediction zero for m>k)')
for key in sorted(res): print('  ',key,res[key],'<- must be zero' if key[0]>key[1] else '')
print('time %.0fs'%(time.time()-t0))
