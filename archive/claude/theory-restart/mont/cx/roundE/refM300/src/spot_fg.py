"""foreground helper: process missing seeds in [A, B) sequentially (same task() as spot_run.py) until T seconds elapse."""
import sys, time, os
sys.argv=[sys.argv[0],'0','1','1','300']+sys.argv[1:]
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import importlib.util
spec=importlib.util.spec_from_file_location('spot_run','/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src/spot_run.py')
SR=importlib.util.module_from_spec(spec); spec.loader.exec_module(SR)
A=int(sys.argv[5]); B=int(sys.argv[6]); T=float(sys.argv[7])
t0=time.time(); done=0
for s in range(A,B):
    if time.time()-t0>T: break
    if os.path.exists(SR.HERE+'spot_res/%d.pkl'%s): continue
    SR.task(s); done+=1
print('processed',done,'seeds; last',s,'elapsed %.0fs'%(time.time()-t0))
