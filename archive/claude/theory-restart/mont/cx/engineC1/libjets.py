"""Slope end-jets (deg, lc, log-jet order K) at both ends for library A boxes (engineA spec) -> pickle."""
import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, e2b, jets
K=3
spec={'Ra': 5, 'Rb': 8, 'NN': 3, 'M': [1, -1, 2, -2, 3, -3]}
t0=time.time()
nested,rat=e2b.build(spec); allb=nested+rat
print('built',len(nested),len(rat),time.time()-t0,flush=True)
out=[]
for b in allb:
    tp=ser.slope(b[1],'top',K); bt=ser.slope(b[1],'bot',K)
    out.append((b[0],b[2],b[3],(tp[0],tp[1],jets.logs(tp[2])),(bt[0],bt[1],jets.logs(bt[2]))))
pickle.dump(dict(nN=len(nested),boxes=out,vecs=[b[1] for b in allb]),open('libA_jets.pkl','wb'))
print('done',time.time()-t0)
