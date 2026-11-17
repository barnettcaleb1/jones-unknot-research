"""H two-ended tie at order 3 for ONE d2 box + n rational (n pinned by the delta-law).  mB = 0, both ends r >= 2.
 T3 (both ends r >= 3) needs the tau-law n = tau(B) - tau*; T2: one end ('weak') has r = 2 exactly with
 D2 := l2(s1) - l2(s2) = tau* - tau(B) + n (strong end D2 = 0), and the Phi_3 pattern's first condition there is
     D3 = D2 (1 - X1),   D3 = l3(w1) - l3(w3) - sum l3(q) (weak end),   X1 = l1(w1) + sum rho_a      (PROVED, see REPORT 7)
 which is LINEAR in the rational sums for fixed (k, n).  Rows: P = P0 (mB = 0), Lambda pinned by D2, the D3 row."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import lpg, f1o3, classes, exact, runner, eng, h3b
from fractions import Fraction as Fr
items=exact.load_items()
P=pickle.load(open('pairs_d2.pkl','rb')); lab=P['labels']
op1=sorted(set(lab[c[0]] for c,n,o in P['res'] if len(c)==1 and o))
d2={c.label:c for c in classes.d2pos()}
def wl(mu,end):
    w1,w3=eng.W(mu); return f1o3.lj(w1,end),f1o3.lj(w3,end)
res={}
for mu in (1,-1):
    o,sgs,ds=h3b.WJ[mu]
    taustar=sum(wl(mu,e)[0][1]-wl(mu,e)[1][1] for e in ('top','bot'))
    for l in op1:
        c=d2[l]
        if c.sig!=sgs: continue            # tie needs mB = 0
        n=int(c.dl-ds)
        if n<0: continue
        for x in classes.SIGS[c.key]:
            d3=f1o3.boxdata3(items[x][2])
            tau=sum(d3[e][4]-d3[e][1] for e in ('top','bot'))
            T3=(n==tau-taustar)
            verdicts=[]
            for end in ('top','bot'):
                (p1,p2,p3),(q1,q2,q3)=wl(mu,end)
                D2=taustar-tau+n
                if D2==0: verdicts.append('D2=0'); continue
                b=lpg.Cls(c.key,1,l); cl=dict(kind='H',name='tie3',end=end,p=(p1,p2),q=(q1,q2),sigstar=Fr(sgs))
                ra,la,rb,lb=c.end(end)
                L=lpg.build([b],cl,[],n,kmin=0,fixk={0:1})
                L.lb[L.iN]=Fr(n); L.add_eq({L.iN:Fr(1)},Fr(n))
                # P = P0 with mB = 0
                L.add_eq(L.zrow((0,1,0,0)),p1-q1-rb+ra)
                # Lambda = p2 - q2 - lambda_q(B) - D2
                L.add_eq(L.zrow((0,0,0,1)),p2-q2-(lb-la)-D2)
                # D3 row: p3 - q3 - l3q(B) - L3q = D2 (1 - p1 - ra - alpha)  ->  -L3q + D2*alpha = D2(1-p1-ra) - p3 + q3 + l3q(B)
                l3qB=d3[end][5]-d3[end][2]
                r={}
                for jj,s in enumerate(lpg.FINS):
                    if f1o3.FL3[s]: r[L.iG+jj]=-f1o3.FL3[s]
                for i,(a,bb,l1,l2) in enumerate(lpg.EI):
                    if l1: r[L.iF+i]=r.get(L.iF+i,0)+D2*l1
                L.add_eq(r,D2*(1-p1-ra)-p3+q3+l3qB)
                d=runner.decide(L)
                verdicts.append(d[0])
            res[(mu,l,x)]=(n,tau,T3,verdicts)
import collections
cnt=collections.Counter((v[2],tuple(v[3])) for v in res.values())
print('H mu=+-1 ties, single a-potential d2 boxes: instances',len(res))
pos=collections.Counter()
for (mu,l,x),v in res.items():
    c=d2[l]; pe='top' if c.top[0]>0 else ('bot' if c.bot[0]>0 else '?')
    openend='top' if v[3][0]!='closed' else ('bot' if v[3][1]!='closed' else 'none')
    pos[(pe,openend)]+=1
print('  (a-positive end, open weak end):',dict(pos))
for k,v in sorted(cnt.items(),key=str): print('  T3 possible=%s  T2 verdict (weak top, weak bot)=%s : %d'%(k[0],k[1],v))
