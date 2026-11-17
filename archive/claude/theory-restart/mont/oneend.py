import sys, random, time
sys.path.insert(0,'.')
from lp import *
rnd=random.Random(17)
def rword(L):
    w=''
    while len(w)<L:
        c=rnd.choice('XxYy')
        if w and {'X':'x','x':'X','Y':'y','y':'Y'}[w[-1]]==c: continue
        w+=c
    return w
PHI3=P((1,0),(1,1),(1,2))
def ends(mu,k,vs):
    p=vs[0]
    for v in vs[1:]: p=star(p,v)
    p=apply('Y'*k if k>=0 else 'y'*(-k), p)
    A=a_of(p); B=b_of(p)
    w1=add(mono(1),mul(P((1,0),(1,2)), mono(mu, (-1)**(mu%2))))
    w3=mul(P((1,0),(1,2)), sub(ONE, mono(mu,(-1)**(mu%2))))
    T1=mul(w1,A); T3=mul(w3,B)
    S=add(T1,T3)            # = J_raw * Phi3
    Jr=close(mu,p)
    # unit position: k0 with t^-k0 * Jr normalised
    s=sum(c*(-1)**(e%2) for e,c in Jr.items()); d=sum(e*c*(-1)**((e-1)%2) for e,c in Jr.items())
    k0=d//s if s in (1,-1) and d%s==0 else None
    toptie = top(T1)==top(T3); bottie = bot(T1)==bot(T3)
    return dict(T0=top(S),B0=bot(S),k0=k0,toptie=toptie,bottie=bottie,span=span(Jr),
                topcancel=toptie and T1[top(T1)]+T3[top(T3)]==0, botcancel=bottie and T1[bot(T1)]+T3[bot(T3)]==0)
pool=[]
while len(pool)<400:
    w=rword(rnd.randint(1,7)); v=apply(w)
    if len(v[0])>1: pool.append((w,v))
stats=dict(n=0,both_cancel=0,crit_fail=0,top_cancel=0,bot_cancel=0)
fails=[]
for trial in range(40000):
    n=rnd.choice([2,2,3,3,4]); bs=rnd.sample(pool,n)
    mu=rnd.choice([m for m in range(-5,6) if m!=0]); k=rnd.randint(-4,4)
    e=ends(mu,k,[v for _,v in bs]); stats['n']+=1
    stats['top_cancel']+=e['topcancel']; stats['bot_cancel']+=e['botcancel']
    if e['topcancel'] and e['botcancel']: stats['both_cancel']+=1
    # criterion: an end without cancellation whose degree is incompatible with J_raw = +-t^k0 (top k0+2, bottom k0)
    ok=False
    if not e['topcancel'] and e['T0']!=e['k0']+2: ok=True
    if not e['botcancel'] and e['B0']!=e['k0']: ok=True
    if not ok:
        stats['crit_fail']+=1
        if len(fails)<8: fails.append((mu,k,[w for w,_ in bs],e))
print(stats)
for f in fails: print('FAIL',f)
