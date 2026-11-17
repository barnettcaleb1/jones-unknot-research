# Sanity check: are the moments M_k = sum_e J_e (-1)^e e^k (k! x h^k-coefficient of J(-e^h))
# equivariant finite-type of order <= k w.r.t. flipping crossing letters (x_i <-> y_i) in half-words?
import sys, random, itertools, cmath
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs
from fractions import Fraction
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs:
        a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
KMAX=6
res={}   # (m,k) -> [zero count, nonzero count]
roots={'J(1)=1':[0,0],'J(i)=1':[0,0],'J(z6)=1':[0,0]}
done=0; tries=0
while done<int(sys.argv[2] if len(sys.argv)>2 else 60) and tries<20000:
    tries+=1
    w=fs.gen(rnd,rnd.randint(8,16))
    if not w: continue
    toks=w.split('.')
    fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
    if len(fl)<6: continue
    J0=lp.J(w)
    if J0 is None: continue
    # root checks
    for name,x in (('J(1)=1',1),('J(i)=1',1j),('J(z6)=1',cmath.exp(1j*cmath.pi/3))):
        v=sum(c*x**e for e,c in J0.items())
        roots[name][0 if abs(v-1)<1e-9 else 1]+=1
    m=rnd.choice([3,4,5,6])
    sites=rnd.sample(fl,m)
    Js={}
    ok=True
    for S in itertools.product([0,1],repeat=m):
        ww=flip(toks,[s for s,b in zip(sites,S) if b])
        Jw=lp.J(ww)
        if Jw is None: ok=False; break
        Js[S]=Jw
    if not ok: continue
    done+=1
    for k in range(0,KMAX+1):
        alt=sum((-1)**sum(S)*M(Js[S],k) for S in Js)
        key=(m,k); res.setdefault(key,[0,0]); res[key][0 if alt==0 else 1]+=1
print('samples',done,'tries',tries)
print('roots (ok,fail):',roots)
print('alternating sums Delta^m M_k: (m,k) -> [zero, nonzero]   [prediction: zero whenever m>k]')
for key in sorted(res): print(key, res[key], 'PRED ZERO' if key[0]>key[1] else '')
