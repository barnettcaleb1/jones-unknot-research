"""Class-level census of THREE-factor products (pool = library A u R(8) u frontier sets) for two-ended ties of order >= 3,
horizontal |mu| <= 12 and vertical 3 <= |a| <= 13.  Exact (hash on jet classes; no sampling).  argv: frontier tags..."""
import sys, pickle, collections, time, itertools
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, front
from fractions import Fraction as Fr
t0=time.time()
L=pickle.load(open('libA_jets.pkl','rb'))
jets=[(b[3],b[4]) for b in L['boxes']]; src=[('L',i) for i in range(len(L['boxes']))]
for tag in sys.argv[1:]:
    F=pickle.load(open('fr_%s.pkl'%tag,'rb'))
    jets+=F['jets']; src+=[(tag,i) for i in range(len(F['jets']))]
print('pool',len(jets),flush=True)
# key2 class -> {(l2t,l2b): representative index}, plus (l3t,l3b) sets for depth-4 test
C2=collections.defaultdict(dict)
for x,(tp,bt) in enumerate(jets):
    k2=front.key2(tp,bt); C2[k2].setdefault((tp[2][1],bt[2][1]),[]).append(x)
K2=list(C2); print('key2 classes',len(K2),round(time.time()-t0,1),flush=True)
# second-order data of a class: (delta, dmod3, lc_t, l1_t, lc_b, l1_b)
def add2(a,b): return (a[0]+b[0],(a[1]+b[1])%3,a[2]*b[2],a[3]+b[3],a[4]*b[4],a[5]+b[5])
T=front.targets()
def tkey(Tg):
    (_,Tt,Tb)=Tg
    return (Tt[0]-Tb[0], Tt[0]%3, Fr(Tt[1]), Tt[2][0], Fr(Tb[1]), Tb[2][0])
# index classes by key2 for lookup of the third class
idx={k:i for i,k in enumerate(K2)}
hits=collections.Counter(); ex={}; n2=collections.Counter()
for Tg in T:
    tk=tkey(Tg); t2t=Tg[1][2][1]; t2b=Tg[2][2][1]
    for i in range(len(K2)):
        a=K2[i]
        for j in range(i,len(K2)):
            b=K2[j]
            s=add2(a,b)
            need=(tk[0]-s[0],(tk[1]-s[1])%3,tk[2]/s[2],tk[3]-s[3],tk[4]/s[4],tk[5]-s[5])
            k=idx.get(need)
            if k is None or k<j: continue
            c=K2[k]
            n2[Tg[0][0]]+=1
            # third order: l2 sums
            A=C2[a]; B=C2[b]; Cc=C2[c]
            sumAB=collections.defaultdict(list)
            for (xa,ya),ra in A.items():
                for (xb,yb),rb in B.items():
                    sumAB[(xa+xb,ya+yb)].append((ra[0],rb[0]))
            for (xc,yc),rc in Cc.items():
                nd=(t2t-xc,t2b-yc)
                if nd in sumAB:
                    hits[Tg[0]]+=1
                    ex.setdefault(Tg[0],[]).append((sumAB[nd][0][0],sumAB[nd][0][1],rc[0]))
    print(Tg[0],'class-triples meeting order 2:',n2[Tg[0][0]],'order-3 class hits',hits[Tg[0]],round(time.time()-t0,1),flush=True)
pickle.dump(dict(hits=hits,ex=ex,src=src),open('fr_triples_%s.pkl'%'_'.join(sys.argv[1:] or ['lib']),'wb'))
print('done',dict(hits))
