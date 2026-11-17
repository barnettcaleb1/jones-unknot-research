"""Final broad check: forced ties, n up to 8, long boxes; clean-end prediction (N5) and >=2 terms; P1 with long alternating boxes, n=6,12."""
from verify_main import *
rnd=random.Random(4242)
pool2=list(pool)
for _ in range(300):
    k=rnd.randint(6,10); s=[rnd.choice([m for m in range(-6,7) if m]) for _ in range(k)]
    if s[0]==-1: s[0]=-3
    pool2.append(tuple(s))
alt=[]
while len(alt)<60:
    k=rnd.randint(1,7); sgn=-1 if k%2==1 else 1
    s=[]; cur=sgn
    for i in range(k):
        mag=rnd.randint(2 if (i==0 and cur<0) else 1,5); s.append(cur*mag); cur=-cur
    if s[-1]<0: alt.append(tuple(s))
stats={'ties':0,'pred_bad':0,'mono':0,'P1':0,'P1bad':0}
t0=time.time()
for trial in range(2500):
    nb=rnd.choice([2,3,4,5,6,7,8])
    ss=[rnd.choice(pool2) for _ in range(nb)]
    rho=sum(1 for s in ss if run(s)[0][0]=='R')
    cands=[(mu,N,w) for mu in [m for m in range(-7,8) if m] for N in range(-8,14) for w in ('top','bot')
           if (w=='top' and ((mu>=1 and 2*rho-3*N==0 and rho%2==0) or (mu<=-2 and 2*rho-3*N==-1 and rho%2==1) or (mu==-1 and 2*rho-3*N==-3 and rho%2==0)))
           or (w=='bot' and ((mu<=-1 and 2*rho-3*N==-nb and (rho-nb)%2==0) or (mu>=2 and 2*rho-3*N==1-nb and (rho-nb)%2==1) or (mu==1 and 2*rho-3*N==3-nb and (rho-nb)%2==0)))]
    if not cands: continue
    mu,N,w=rnd.choice(cands)
    Jv=neck(mu,N,[box(s) for s in ss]); stats['ties']+=1
    if len(Jv)<2: stats['mono']+=1
    if w=='bot':
        kt,rt=predict_top(mu,N,ss); e=top(Jv); c=[Jv.get(e-i,0) for i in range(2)]
        if kt!='gen' or Fraction(c[1],c[0])+1!=rt: stats['pred_bad']+=1
    else:
        ssm=[mirror_seq(s) for s in ss]; kb,rb=predict_top(-mu,nb-N,ssm); e=bot(Jv); c=[Jv.get(e+i,0) for i in range(2)]
        if kb!='gen' or Fraction(c[1],c[0])+1!=rb: stats['pred_bad']+=1
for n6 in (6,12):
    for trial in range(40):
        ss=[rnd.choice(alt) for _ in range(n6)]
        Jv=neck(-2,n6//3,[box(s) for s in ss]); e=top(Jv); c=[Jv.get(e-i,0) for i in range(3)]
        Y=sum(x2a(s) for s in ss); stats['P1']+=1
        if c[1]!=0 or Fraction(c[2],c[0])!=Y-1: stats['P1bad']+=1
print(stats,'time',round(time.time()-t0,1))
