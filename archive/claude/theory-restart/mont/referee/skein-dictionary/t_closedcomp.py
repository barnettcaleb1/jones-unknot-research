"""Control: a body with an extra closed colour-two component (excluded by the note's hypothesis).
Regular model near the root: the extra loop linking the axis w' times contributes the root trace 3 (w' odd) or -1 (w' even)."""
import sys, numpy as np
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from regmodel import *
h=1e-10; q=1j*np.exp(h/2); s=np.sqrt(q+1/q)
for B in ['l1.u1','l1.x0.u1','l1.x0.x0.u1','y0.l1.x0.u1']:
    beta=body_operator(B,q,s); a,b,res=channels(beta,q,s)
    print(B,'a(root)=%s b(root)=%s'%(np.round(a,4),np.round(b,4)))
