import sys, random, time
sys.path.insert(0,'nest')
from nlib import *
import alex
# Habiro: J_N(4_1) = sum_k prod_{j<=k} {N+j}{N-j},  {m} = q^(m/2)-q^(-m/2); for N=3 the products are Laurent in q
def braced(m):  # {m}{m'} products with m+m' even handled by pairing: {a}{b} = q^((a+b)/2) - q^((a-b)/2) - q^((b-a)/2) + q^(-(a+b)/2)
    pass
def pair(a,b): return clean({(a+b)//2:1, (a-b)//2:-1, (b-a)//2:-1, -(a+b)//2:1}) if (a+b)%2==0 else None
N=3
CJ={0:1}; pr={0:1}
for j in range(1,N):
    pr=mul(pr,pair(N+j,N-j)); CJ=add(CJ,pr)
print('J_3(4_1) =',fmt(CJ))
targets={tuple(sorted(normalize(CJ).items())), tuple(sorted(normalize({-e:c for e,c in CJ.items()}).items()))}
rnd=random.Random(4); t0=time.time(); hits=0; d25=0
for it in range(20000):
    if time.time()-t0>240: break
    a=[rnd.choice(['x2','y2']) for _ in range(rnd.randint(1,3))]
    b=[rnd.choice(['x2','y2','x3','y3']) for _ in range(rnd.randint(2,5))]
    c=[rnd.choice(['x2','y2']) for _ in range(rnd.randint(0,2))]
    w='s.l1.'+'.'.join(a+['r3']+b+[rnd.choice(['u3','u2'])]+c+['u1'])
    if alex.alex_eval(w,-1)!=25: continue
    Jw=J(w)
    if Jw is None: continue
    d25+=1
    if tuple(sorted(Jw.items())) in targets:
        hits+=1
        print('HIT',w,'D(2)=',alex.alex_eval(w,2),'(Delta_41(2)^2 = 1)','D(3)=',alex.alex_eval(w,3),'(Delta_41(3)^2=1)')
        if hits>=3: break
print('det-25 words tried',d25,'hits',hits,'time',round(time.time()-t0,1))
