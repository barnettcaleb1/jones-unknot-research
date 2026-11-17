import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import relabel, theta, sym, plat2
from kauffman import padd
D2={4:1,0:1,-4:1}
for ev in [theta.from_halfword('s.l1.y0.x1.u2'), sym.symmetric(plat2.top_events('aa'))]:
    D=theta.bracket(relabel.expand_A1(ev,False)); De=theta.bracket(relabel.expand_A1(ev,True))
    r=theta.pmul(theta.DELTA,D); padd(r,De,-1)
    print('r',sorted(r.items()))
    print(' div by Delta2:',theta.pdiv(r,D2) is not None,' div by delta:',theta.pdiv(r,theta.DELTA) is not None)
    print(' D',sorted(D.items())); print(' De',sorted(De.items()))
