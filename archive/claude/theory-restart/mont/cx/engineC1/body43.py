import sys, pickle, collections
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lib, ser, jets, zjet
from fractions import Fraction as Fr
G=vc.gboxes()
def info(v):
    tp=ser.slope(v,'top',4); bt=ser.slope(v,'bot',4)
    lt=jets.logs(tp[2]); lb=jets.logs(bt[2])
    zt=zjet.zser(v,'top',4); zb=zjet.zser(v,'bot',4)
    return dict(delta=tp[0]-bt[0],sigma=lt[0]+lb[0],tau=lt[1]+lb[1],qt=(tp[0],tp[1],[str(x) for x in lt]),qb=(bt[0],bt[1],[str(x) for x in lb]),
                zt=(zt[0],zt[1],[str(x) for x in zt[2]]) if zt else None, zb=(zb[0],zb[1],[str(x) for x in zb[2]]) if zb else None,
                spa=vc.span(v[0]),spb=vc.span(v[1]))
for i in lib.NONRAT:
    I=info(G[i][1]); print(i,G[i][0]); print('    ',I)
d2=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl','rb'))
print('d2pos',len(d2))
C=collections.Counter()
for b in d2:
    I=info(b[1]); C[(I['delta'],str(I['sigma']),str(I['tau']))]+=1
print(sorted(C.items(),key=lambda x:-x[1])[:30])
