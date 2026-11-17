import sys, pickle, collections
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import zjet
from fractions import Fraction as Fr
D=pickle.load(open('libA_jets.pkl','rb')); Bx=D['boxes']; V=D['vecs']
res=pickle.load(open('tau2.pkl','rb'))
for mu in (1,-2,2):
    C,ex=res[mu]
    print('mu',mu)
    for key,(i,j) in sorted(C.items())[:0]: pass
    for key,(i,j) in sorted(ex.items())[:14]:
        zi=(zjet.zser(V[i],'top'),zjet.zser(V[i],'bot')); zj=(zjet.zser(V[j],'top'),zjet.zser(V[j],'bot'))
        f=lambda z: '(%d,%s,%s)'%(z[0],z[1],','.join(str(x) for x in z[2][:2])) if z else 'NONE'
        print('  D=%s (%s,%s) x%d | b1 z_top %s z_bot %s | b2 z_top %s z_bot %s'%(key[0],key[1],key[2],C[key],f(zi[0]),f(zi[1]),f(zj[0]),f(zj[1])))
