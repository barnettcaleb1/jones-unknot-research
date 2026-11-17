"""Biased verification: choose (mu,N) to force a first-order tie at the top or bottom."""
from verify_main import *
rnd=random.Random(77)
stats={'cases':0,'c2zero_nonP1':0,'P1':0,'P1bad':0,'pred_bad':0,'unit':0}
t0=time.time()
for trial in range(12000):
    nb=rnd.choice([2,2,3,3,4,5,6])
    ss=[rnd.choice(pool) for _ in range(nb)]
    rho=sum(1 for s in ss if run(s)[0][0]=='R')
    # candidate (mu,N) giving top ties T1,T2,T3 or bottom ties B1,B2,B3
    cands=[]
    for mu in [m for m in range(-6,7) if m]:
        for N in range(-6,10):
            d=2*rho-3*N
            if (mu>=1 and d==0 and rho%2==0) or (mu<=-2 and d==-1 and rho%2==1) or (mu==-1 and d==-3 and rho%2==0): cands.append((mu,N,'top'))
            if (mu<=-1 and d==-nb and (rho-nb)%2==0) or (mu>=2 and d==1-nb and (rho-nb)%2==1) or (mu==1 and d==3-nb and (rho-nb)%2==0): cands.append((mu,N,'bot'))
    if not cands: continue
    mu,N,where=rnd.choice(cands)
    Jv=neck(mu,N,[box(s) for s in ss]); stats['cases']+=1
    if span(Jv)==0: stats['unit']+=1; print('UNIT!',mu,N,ss)
    if where=='bot':
        kt,rt=predict_top(mu,N,ss); assert kt=='gen'
        e=top(Jv); c=[Jv.get(e-i,0) for i in range(3)]
        if Fraction(c[1],c[0])+1!=rt: stats['pred_bad']+=1
        if c[1]==0:
            if isP1(mu,N,ss):
                stats['P1']+=1
                if c[2]==0: stats['P1bad']+=1
            else: stats['c2zero_nonP1']+=1; print('c2=0 non-P1',mu,N,ss)
    else:
        ssm=[mirror_seq(s) for s in ss]
        kb,rb=predict_top(-mu,nb-N,ssm); assert kb=='gen'
        e=bot(Jv); c=[Jv.get(e+i,0) for i in range(3)]
        if Fraction(c[1],c[0])+1!=rb: stats['pred_bad']+=1
        if c[1]==0:
            if isP1(-mu,nb-N,ssm):
                stats['P1']+=1
                if c[2]==0: stats['P1bad']+=1
            else: stats['c2zero_nonP1']+=1; print('c2=0 non-P1 (bottom)',mu,N,ss)
print(stats,'time',round(time.time()-t0,1))
