import sys; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
import time
t0=time.time()
bs=gen_bodies_nontriv(202, 15)
for B in bs: print(B, len(J('s.'+B)), span(J('s.'+B)))
print('time',round(time.time()-t0,1))
