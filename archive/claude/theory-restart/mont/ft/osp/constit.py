# Constituent knots of the quotient theta-curve: K1 = arc u a1 (finite axis edge, windings x0/y0 = full twists around a1),
# K2 = arc u a2 (axis edge through infinity; windings around a1 unlink). Test iota := (M3/36 - 7 v3(K))/5 against v3(K1), v3(K2).
import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/osp')
from whdouble import sweep, pdiv, to_t, normV
import alex
from fractions import Fraction as F
def constituent_ops(word, which):
    half=alex.parse(word); ops=[('cap',0)]
    for c,i in half:
        if c in 'lr': ops.append(('cap',i))          # half-positions i-1,i -> shifted by +1 -> cap index i
        elif c=='u': ops.append(('cup',i))
        elif i>=1: ops.append((c,i))                 # crossing of half-positions i-1,i -> shifted positions i,i+1
        else:
            if which==1: ops+= [(c,0),(c,0)]
    ops.append(('cup',0))
    return ops
def V_of(ops):
    b=sweep(ops); q=pdiv(b,{2:-1,-2:-1})
    return normV(to_t(q))
def a2(V): return F(-sum(c*e*(e-1) for e,c in V.items()),6)
def v3(V):
    d2=sum(c*e*(e-1) for e,c in V.items()); d3=sum(c*e*(e-1)*(e-2) for e,c in V.items()); return F(-(d3+3*d2),36)
if __name__=='__main__':
    rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3_rows.json'))
    from collections import Counter
    fits=Counter(); data=[]
    for w,M2,M3,M4,a2K,w3 in rows:
        v3K=-F(w3)/36; iota=(F(M3,36)-7*v3K)/5
        V1=V_of(constituent_ops(w,1)); V2=V_of(constituent_ops(w,2))
        data.append((iota,v3K,v3(V1),v3(V2),a2(V1),a2(V2),F(a2K)))
    for name,f in [('v3(K1)+v3(K2)',lambda d:d[2]+d[3]),('v3(K1)',lambda d:d[2]),('v3(K2)',lambda d:d[3]),('2v3(K1)',lambda d:2*d[2]),('2v3(K2)',lambda d:2*d[3])]:
        print(name,' iota == it in',sum(1 for d in data if d[0]==f(d)),'/',len(data))
    # least squares over small integer combos  iota = a v3K + b v3K1 + c v3K2
    best=[]
    for a in range(-3,4):
        for b in range(-3,4):
            for c in range(-3,4):
                n=sum(1 for d in data if d[0]==a*d[1]+b*d[2]+c*d[3]); best.append((n,a,b,c))
    best.sort(reverse=True); print('best integer fits iota = a v3(K) + b v3(K1) + c v3(K2):',best[:5])
    print('sample rows (iota, v3K, v3K1, v3K2, a2K1, a2K2, a2K):'); [print('  ',[str(x) for x in d]) for d in data[:12]]
