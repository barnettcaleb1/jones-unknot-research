"""Is the dangerous set D made of RESONANT nests?  For each depth-one class representative F_m(Y^N u1 u2) compute the z-orders of
the product P = Y^N u1 u2 at both ends (C1's zjet: ord_top z = -deg_top z; ord_bot z = lowest exponent) and the resonance gap
g = min(|m - (-ord_top z)|... ) i.e. whether the twist brings w = (-t)^-m z to order 0 at an end."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lib, zjet
G=pickle.load(open('greedy_n2.pkl','rb')); D=G['D']
A=pickle.load(open('gen1_R5_n2.pkl','rb'))
R5=lib.rational(5)
def zinfo(rep):
    idx,N,m=rep
    p=vc.Ypow(N,vc.starall([R5[i][1] for i in idx]))
    zt=zjet.zser(p,'top'); zb=zjet.zser(p,'bot')
    if zt is None or zb is None: return None
    dt=-zt[0]; ob=zb[0]          # deg_top z, ord_bot z
    # w = (-t)^-m z : deg_top w = dt - m ; ord_bot w = ob - m
    return dt,ob,m,abs(dt-m),abs(ob-m)
Dk=set(v[0] for v in D.values())
stat={'D':collections.Counter(),'S':collections.Counter()}
special={'D':0,'S':0}; tot={'D':0,'S':0}
for k,(cnt,el,rep) in A.items():
    if not el: continue
    z=zinfo(rep)
    if z is None: continue
    g='D' if k in Dk else 'S'
    tot[g]+=1
    dt,ob,m,gt,gb=z
    res=min(gt,gb)
    stat[g][min(res,4)]+=1
    if not (dt in (0,1) and ob in (-1,0)): special[g]+=1
for g in ('D','S'):
    print(g,'classes',tot[g],'| special product (z not of order one at some end):',special[g],
          '| resonance gap min(|deg_top w|,|ord_bot w|) distribution:',sorted(stat[g].items()))
