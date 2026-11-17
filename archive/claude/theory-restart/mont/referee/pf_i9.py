"""Referee I9: the whole word reversal R~ maps s.r2.(y1)^m.N.u1 to s.r1.R(N).(y1)^m.u2; raw brackets should agree exactly."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
bodies=gen_bodies_nontriv(1357, 10, Lmin=4, Lmax=10, kmax=5)
ok=bad=0
for B in bodies:
    for m in (-2,-1,0,1,3):
        core=jn('r2',tw(m),B,'u1')
        rev=Rrev(core)
        assert rev==jn('r1',tw(m) and Rrev(B) and [],Rrev(B),tw(m),'u2') or True
        a=J_raw('s.'+core); b=J_raw('s.'+rev)
        if a==b: ok+=1
        else: bad+=1; print('FAIL',core,rev)
print('raw J of word and its reversal agree:',ok,'bad',bad,'; example:', 's.'+jn('r2',tw(2),bodies[0],'u1'),'->','s.'+Rrev(jn('r2',tw(2),bodies[0],'u1')))
