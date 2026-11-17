"""exact check of depth-one positive-potential boxes found by gen1 (R(5) children)."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb'); sys.path.insert(1,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import vc, lib, ser, jets, zjet
from fractions import Fraction as Fr
from jbox_val import bdata
R=lib.rational(5)
tot=pickle.load(open('gen1_R5_n2.pkl','rb'))
el={k:v for k,v in tot.items() if v[1]}
pos=[k for k in el if k[0][0]>0 or k[1][0]>0 or k[0][2]>0 or k[1][2]>0]
for k in pos:
    idx,N,m=el[k][2]
    T=('n',m,[R[i][2] for i in idx]+([('w',('Y' if N>0 else 'y')*abs(N))] if N else []))
    v=vc.vec(T)
    ek,elig=bdata(v)
    p=vc.Ypow(N,vc.starall([R[i][1] for i in idx]))
    zt=zjet.zser(p,'top'); zb=zjet.zser(p,'bot')
    print('words',[R[i][2][1] for i in idx],'N',N,'m',m,'| exact sig == jet sig:',ek==k,'elig',elig,'| z_P ord top/bot',zt[0] if zt else None,zb[0] if zb else None,
          '| top (ra,la,rb,lb)',[str(x) for x in ek[0]],'bot',[str(x) for x in ek[1]],'sigma',ek[2],'delta',ek[3])
