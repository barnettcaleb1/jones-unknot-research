"""Referee: consequence of Prop 4.2(e) (classical limit A=1: every box is +-identity): a(v)(1) = b(v)(1) = +-1, i.e. J(s.B)(1) = +-1,
and J_mu(1) = v1(1) for every twisted closure (X(1) = diag(1,-1), so e1^T X^mu = (1,0) at t=1)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
bodies=gen_bodies_nontriv(2468, 25, Lmin=4, Lmax=12, kmax=5)
ok=bad=0
for B in bodies:
    j=J('s.'+B); v=ev(j,1)
    for m in (-2,1,3):
        jm=J(jn('s.r2',tw(m),B,'u1'))
        if abs(ev(jm,1))!=1: bad+=1; print('J_mu(1) not +-1',B,m)
    if abs(v)==1: ok+=1
    else: bad+=1; print('J(1) not +-1',B,v)
print('J(s.B)(1) = +-1 and J_mu(1) = +-1:',ok,'bodies ok; bad',bad)
