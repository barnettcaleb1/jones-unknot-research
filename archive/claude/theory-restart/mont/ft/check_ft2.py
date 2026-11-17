# Separate the two move types: on-axis flips (x0<->y0) only, and off-axis symmetric-pair flips (x_i<->y_i, i>=1) only.
import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
rnd=random.Random(int(sys.argv[1]))
for kind in ('axis','offaxis'):
    res={}; done=0; tries=0
    while done<40 and tries<40000:
        tries+=1
        w=fs.gen(rnd,rnd.randint(8,18))
        if not w: continue
        toks=w.split('.')
        if kind=='axis': fl=[i for i,a in enumerate(toks) if a in ('x0','y0')]
        else: fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit() and a[1:]!='0']
        m=rnd.choice([3,4,5])
        if len(fl)<m: continue
        sites=rnd.sample(fl,m); Js={}; ok=True
        for S in itertools.product([0,1],repeat=m):
            Jw=lp.J(flip(toks,[s for s,b in zip(sites,S) if b]))
            if Jw is None: ok=False; break
            Js[S]=Jw
        if not ok: continue
        done+=1
        for k in range(0,6):
            alt=sum((-1)**sum(S)*M(Js[S],k) for S in Js)
            res.setdefault((m,k),[0,0])[0 if alt==0 else 1]+=1
    print(kind,'samples',done)
    for key in sorted(res):
        if key[0]>key[1] or key[0]==key[1]: print('  ',key,res[key],'PRED ZERO' if key[0]>key[1] else 'order m attained?')
