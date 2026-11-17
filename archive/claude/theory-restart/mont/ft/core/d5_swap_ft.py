# F2 restricted to swap words (no axis letters): Delta^m M_k = 0 for m > k? (m random arc flips)
import random, itertools, collections
import clib, lp
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
rnd=random.Random(17); res=collections.defaultdict(lambda:[0,0]); done=0; tries=0
letters=['x1','y1','x2','y2','x3','y3']
while done<40 and tries<100000:
    tries+=1
    body=[rnd.choice(letters) for _ in range(rnd.randint(6,11))]
    w='s.'+rnd.choice(['l1','r1','l2','r2'])+'.'+'.'.join(body)+'.'+rnd.choice(['u1','u2','u3'])
    toks=w.split('.'); fl=[i for i,a in enumerate(toks) if a[0] in 'xy']
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
        alt=sum((-1)**sum(S)*clib.M(Js[S],k) for S in Js)
        res[(m,k)][0 if alt==0 else 1]+=1
print('swap samples',done)
bad=sum(v[1] for (m,k),v in res.items() if m>k)
print('violations of Delta^m M_k = 0 for m>k:',bad)
print('order attained (m=k nonzero):',{key:v for key,v in sorted(res.items()) if key[0]==key[1]})
