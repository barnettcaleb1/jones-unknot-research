# Claim 11: untwisted Whitehead double of the trefoil, own construction (clasp + framing twists on the OTHER band than the
# builder's), V_L, a_2, v_3, Alexander values of the symmetric word, lp.J of the local-knot inversion directly (no Schur).
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, alex
from rlib import *
from c9_local import longknot_letters, inv
def wh_double(clasp='x', band=4, twist=None):
    base=braid_ops(2,[1,1,1])           # cap0 cap1 x2 x2 x2 cup1 cup0 ; writhe +3
    w,_=writhe(base)
    if twist is None: twist=-w
    d=cable2(base[:-2])                 # doubled caps + doubled braid; band positions: strand p -> (2p,2p+1)
    p=band
    tw=[('y' if twist<0 else 'x',p)]*(2*abs(twist))
    cl=[('cap',p+2),(clasp,p+1),(clasp,p+1),('cup',p)]
    return d+tw+cl+cable2(base[-2:])
if __name__=='__main__':
    for clasp in ('x','y'):
        ops=wh_double(clasp)
        V=jones(ops); print('clasp',clasp,'writhe',writhe(ops),' V_L =',sorted(V.items()))
        print('   a2 =',a2_of(V),' v3 =',v3_of(V))
        hw='s.'+'.'.join(longknot_letters(ops))
        print('   half-word:',hw)
        for tv in (2,3,5,-1):
            print('   |Delta_K(%d)| (stripped) ='%tv, alex.alex_eval(hw,tv))
        t0=time.time(); J=lp.J(hw); print('   lp.J (%.1fs) ='%(time.time()-t0), sorted(J.items()))
        print('   lp.J(-e^h) coeffs h^0..h^5:',[str(x) for x in ev_h(J,5)])
        print('   KL-convention J(-e^h) = lp.J(1/t):',[str(x) for x in ev_h(inv(J),5)])
