"""End-type classification of library-A boxes by the z-order at each end (z = (q-1)/(q-e2)):  generic classes and their
(delta, sigma, tau); non-generic boxes have |ord z| <= 3 at some end."""
import sys, pickle, collections
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import zjet
from fractions import Fraction as Fr
L=pickle.load(open('libA_jets.pkl','rb'))
C=collections.Counter(); X=collections.defaultdict(set)
def cl(o): return 'S' if o>=4 else ('L' if o<=-4 else str(o))
for (k,T,tag,tp,bt),v in zip(L['boxes'],L['vecs']):
    zt=zjet.zser(v,'top'); zb=zjet.zser(v,'bot')
    if zt is None or zb is None: continue
    key=(cl(zt[0]),cl(zb[0]))
    dst=(tp[0]-bt[0],tp[2][0]+bt[2][0],tp[2][1]+bt[2][1])
    C[key]+=1; X[key].add(dst)
print('(top z-class, bottom z-class): count, distinct (delta,sigma,tau)  [S: ord z >= 4 (q~1), L: ord z <= -4 (q~e2)]')
for k,v in sorted(C.items(),key=lambda x:-x[1]):
    xs=sorted(X[k]); print('  %-10s %6d  %s'%(k,v,[(a,str(b),str(c)) for a,b,c in xs[:6]]+(['...%d'%len(xs)] if len(xs)>6 else [])))
