# Normalised weight system check: [h^m] Delta^m J (J = lp.J, normalised) == 2^m sum_{T subset sites} prod_{i in T}(-Sigma_i) Sigma(sites - T)
import sys, random, itertools, math
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/osp')
import ftraw, lp, flat_search as fs
from fractions import Fraction as Fr
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2]); ok=bad=0; nz=0; done=0
while done<N:
    w=fs.gen(rnd,rnd.randint(8,16))
    if not w: continue
    toks=w.split('.'); fl=[i for i,a in enumerate(toks) if a[0] in 'xy' and a[1:].isdigit()]
    m=rnd.choice([2,3,4])
    if len(fl)<m: continue
    sites=rnd.sample(fl,m); Js={}; good=True
    for S in itertools.product([0,1],repeat=m):
        J=lp.J(ftraw.flip(toks,[s for s,b in zip(sites,S) if b]))
        if J is None: good=False; break
        Js[S]=J
    if not good: continue
    done+=1
    lhs=Fr(sum((-1)**sum(S)*M(J,m) for S,J in Js.items()),math.factorial(m))
    sig1={s:ftraw.statesum(w,{s}) for s in sites}
    rhs=Fr(0)
    for r in range(m+1):
        for T in itertools.combinations(sites,r):
            rest=set(sites)-set(T)
            val=ftraw.statesum(w,rest) if rest else Fr(1)
            p=Fr(1)
            for i in T: p*=-sig1[i]
            rhs+=p*val
    rhs*=2**m*(-1)**m   # lp.J uses t = A^{+4} (J_raw maps A^e -> t^{e/4}), i.e. h -> -h relative to t = A^-4
    if lhs==rhs: ok+=1
    else: bad+=1; print('BAD',w,sites,lhs,rhs)
    if lhs!=0: nz+=1
print('samples',done,'match',ok,'mismatch',bad,'nonzero top-order',nz)
