"""ORDER 3 for the two-ended frontier, HORIZONTAL closures, ONE dangerous depth-one box B (each order-3 subclass of the dangerous
n=2 classes) + n rational boxes (n PINNED by the delta-law, n = delta(B) - delta*(mu)), every mu-class (|mu| >= 4 split into
mu = +-4 and |mu| >= 5 at order 3), each end as the weak end.
 * tie (sigma(B) = sigma*): T3 (both ends r >= 3) needs the tau-law n = tau(B) - tau*; T2 (weak end r = 2 exactly):
   D2 = tau* - tau(B) + n and the first Phi_3 condition D3 = D2 (1 - X1) (lpgen tie3 rows, generalised to every mu).
 * 'd=0 r=1' (m = mB = sigma(B) - sigma* != 0): the order-2 row (C1) and the ORDER-3 EQUALITY (derived in REPORT sec. 7)
      d3 = -m [1/2 - Y2 + (1 - X1)^2/2 - m^2/6],  d3 = l3(s1) - l3(s2), Y2 = l2(s2), X1 = l1(s1)
   sliced in X1 for |1 - X1| < T, and for |1 - X1| >= T the exact linear relaxation (1-X1)^2/2 >= (T/2)|1-X1|.
Rational part exact on the K=3 automaton (edge l1,l2,l3 of D; terminal l1,l2,l3 of q; f1o3.EL3/FL3).  Exact Farkas certificates."""
import sys, pickle, collections, time
from fractions import Fraction as Fr
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import lpg, f1o3, eng, h3b, runner
from multiprocessing import Pool
T=6
def wl(mu,end):
    w1,w3=eng.W(mu); return f1o3.lj(w1,end),f1o3.lj(w3,end)
def comb(*ps):
    out={}
    for c,r in ps:
        for i,x in r.items(): out[i]=out.get(i,0)+c*x
    return out
def rowsL(L):
    RA=lambda k:{L.iF+i:(l1,l2,f1o3.EL3[i])[k-1] for i,(a,b,l1,l2) in enumerate(lpg.EI) if (l1,l2,f1o3.EL3[i])[k-1]}
    RQ=lambda k:{L.iG+j:(lpg.FIN[s][0],lpg.FIN[s][1],f1o3.FL3[s])[k-1] for j,s in enumerate(lpg.FINS) if (lpg.FIN[s][0],lpg.FIN[s][1],f1o3.FL3[s])[k-1]}
    return RA,RQ
def base(key,cl,n):
    b=lpg.Cls(key,1,'B'); L=lpg.build([b],cl,[],n,kmin=0,fixk={0:1}); L.add_eq({L.iN:Fr(1)},Fr(n)); return L,b
def decide(L):
    d=runner.decide(L); return d[0]
def one(job):
    key,d3,mu,end,mu3=job
    o,sgs,ds=h3b.WJ[mu]; sig=Fr(key[2]); dl=Fr(key[3])
    n=dl-ds
    if n<0 or n.denominator!=1: return (job,'n<0')
    n=int(n)
    (p1,p2,p3),(q1,q2,q3)=wl(mu3,end)
    cl=dict(kind='H',name='H mu=%+d %s'%(mu,end),end=end,p=(p1,p2),q=(q1,q2),sigstar=Fr(sgs))
    ra,la,rb,lb=key[0] if end=='top' else key[1]
    l3a,l3b=(d3[0],d3[1]) if end=='top' else (d3[2],d3[3])
    m=sig-Fr(sgs)
    if m==0:
        # tie
        tau=sum((k[3]-k[1]) for k in (key[0],key[1]))
        taus=sum(wl(mu3,e)[0][1]-wl(mu3,e)[1][1] for e in ('top','bot'))
        T3=(n==tau-taus)
        D2=taus-tau+n
        if D2==0: return (job,'tie: D2=0 (T3 possible)' if T3 else 'tie: D2=0')
        L,b=base(key,cl,n); RA,RQ=rowsL(L)
        L.add_eq(L.zrow((0,1,0,0)),p1-q1-rb+ra)
        L.add_eq(L.zrow((0,0,0,1)),p2-q2-(lb-la)-D2)
        r=comb((-1,RQ(3)),(D2,RA(1)))
        L.add_eq(r,D2*(1-p1-ra)-p3+q3+(l3b-l3a))
        v=decide(L)
        return (job,'tie T3=%s T2:%s'%(T3,v))
    # d=0 r=1
    rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m)).get('d=0 r=1')
    L0=lpg.build([lpg.Cls(key,1,'B')],cl,rows,n,kmin=0,fixk={0:1}); L0.add_eq({L0.iN:Fr(1)},Fr(n))
    if decide(L0)=='closed': return (job,'r1: closed@2')
    opn=[]
    for x in list(range(-T+1,T))+['big+','big-']:
        L,b=base(key,cl,n)
        for coef,a in rows:
            r=L.zrow(coef); rhs=lpg.evalaff(a,ra,la,rb,lb,sig)-a[5]*sig+a[5]*m   # rows already include mB=m via a[5]*mB
            L.add_eq(r,lpg.evalaff(a,ra,la,rb,lb,m))
        RA,RQ=rowsL(L)
        X1=comb((1,RA(1)))                 # X1 = p1 + ra + alpha
        Y2=comb((1,RA(2)),(1,RQ(2)))       # Y2 = q2 + lb + La + Lam
        d3=comb((-1,RQ(3)))                # d3 = p3 - q3 + l3a - l3b - L3q
        cX1=p1+ra; cY2=q2+lb; cd3=p3-q3+l3a-l3b
        # Q := (1-X1)^2/2 = -d3/m - 1/2 + Y2 + m^2/6
        Qf=comb((-1/m,d3),(1,Y2)); cQ=-cd3/m-Fr(1,2)+cY2+m*m/6
        if isinstance(x,int):
            xv=1-x                          # 1 - X1 = x  ->  X1 = 1 - x
            L.add_eq(X1,xv-cX1)
            L.add_eq(Qf,Fr(x*x,2)-cQ)
        else:
            s=1 if x=='big+' else -1        # s (1 - X1) >= T  and  Q >= (T/2) s (1 - X1)
            L.add_ub({i:s*v for i,v in X1.items()},s*(1-cX1)-T)        # s(1 - cX1 - X1f) >= T  <=>  s X1f <= s(1-cX1) - T
            # Q - (T/2) s (1 - X1) >= 0  <=>  -(Qf) - (T/2) s X1f <= cQ - (T/2) s (1 - cX1)
            L.add_ub(comb((-1,Qf),(-Fr(T,2)*s,X1)),cQ-Fr(T,2)*s*(1-cX1))
        v=decide(L)
        if v!='closed': opn.append(x)
    return (job,'r1: order3 %s'%('CLOSED' if not opn else 'open at '+str(opn)))
if __name__=='__main__':
    t0=time.time()
    K3=pickle.load(open('gen1k3_R5_n2.pkl','rb'))
    C=pickle.load(open('certtest2.pkl','rb')); safe=set(C['safe'])
    G=pickle.load(open('greedy_n2.pkl','rb'))
    Dkeys=[v[0] for l,v in G['D'].items() if l not in safe]
    jobs=[]
    for key in Dkeys:
        for d3 in K3.get(key,{}):
            for mu in h3b.MUS:
                mus3=[mu] if abs(mu)<4 else [mu,5 if mu>0 else -5]
                for mu3 in mus3:
                    for end in ('top','bot'): jobs.append((key,d3,mu,end,mu3))
    print('dangerous n=2 classes',len(Dkeys),'with order-3 data',sum(1 for k in Dkeys if k in K3),'jobs',len(jobs),flush=True)
    with Pool(3) as P: res=P.map(one,jobs,chunksize=8)
    c=collections.Counter(r[1] for r in res)
    for k,v in sorted(c.items(),key=lambda x:-x[1]): print('  %-40s %d'%(k,v))
    # per class: closed for all H configurations?
    per=collections.defaultdict(list)
    for (key,d3,mu,end,mu3),v in res: per[key].append(v)
    OK=('n<0','r1: closed@2','r1: order3 CLOSED','tie T3=False T2:closed')
    good=[k for k,vs in per.items() if all(v in OK for v in vs)]
    print('dangerous classes whose single-box H two-ended cases are ALL closed at order 3:',len(good),'of',len(per))
    pickle.dump(dict(res=res,good=good),open('o3h.pkl','wb'))
    print('time',round(time.time()-t0,1))
