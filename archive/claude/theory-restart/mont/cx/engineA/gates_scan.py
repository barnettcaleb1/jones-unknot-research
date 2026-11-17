"""Gates (a_2 = 0, J(zeta_10) = 1, (t+1)-adic order of J-1) on stored near-miss configurations."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, scan, units2
from vc import span
def Jpair(rec):
    (d,rt,rb,sJ,sA,mu,N)=rec[0]; T1,T2=rec[2],rec[3]
    T=units2.pair_tree(mu,N,T1,T2)
    return vc.Jtree(T), T
out=[]
for f in sys.argv[1:]:
    r=pickle.load(open(f,'rb'))
    lists=[r.get('two_end',[]),r.get('rel_span',[]),r.get('min_span',[])]
    for L in lists:
        for rec in L:
            if not isinstance(rec[0],tuple) or len(rec)<4 or not isinstance(rec[2],tuple): continue
            try: J,T=Jpair(rec)
            except Exception as e: continue
            if J is None: continue
            g=scan.gates({e:c for e,c in J.items()})
            out.append((g['a2']==0, g['cyc10'], g['ord1'], span(J), rec[0], f, vc.hw(T)))
out.sort(key=lambda x:(-(x[0]+x[1]),-x[2],x[3]))
c=collections.Counter((x[0],x[1]) for x in out)
print('configs',len(out),'gate counts (a2==0, J(z10)==1):',dict(c))
for x in out[:12]: print(x[:5],x[5],x[6][:160])
