import sys, pickle
sys.path.insert(0,'.')
import jauto
from fractions import Fraction as Fr
K=int(sys.argv[1]); fn=sys.argv[2]
order,trans=jauto.build(K)
D=pickle.load(open(fn,'rb'))
bad=0
for d in D:
    key,la=jauto.run(d['seq'],K,trans)
    dq,lcq,lq=jauto.qlog(key,K)
    lb=tuple(x+y for x,y in zip(la,lq))
    ok = la==d['la'][:K] and lb==d['lb'][:K] and dq==d['dq'] and Fr(lcq)==d['lcq']
    if not ok:
        bad+=1
        if bad<5: print('BAD',d['seq'],key,la,d['la'],lb,d['lb'],dq,d['dq'])
print('K=%d checked %d bad %d'%(K,len(D),bad))
