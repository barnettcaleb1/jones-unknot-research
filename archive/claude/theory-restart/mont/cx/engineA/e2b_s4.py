"""Re-run stage S4 (small pairs, all (mu,N) candidates) with the corrected bound span a1 + span a2 <= 15 (Tot <= 13, mu = +-1)."""
import sys, json, collections, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, e2b
from vc import span
spec=json.loads(sys.argv[1]); bound=int(sys.argv[2])
t0=time.time()
nested,rat=e2b.build(spec); allb=nested+rat; nN=len(nested)
small=[x for x in range(len(allb)) if span(allb[x][1][0])<=bound-4]
n=0; units=[]
for i in small:
    if i>=nN: continue
    for j in small:
        if j<nN and j<i: continue
        if span(allb[i][1][0])+span(allb[j][1][0])>bound: continue
        p=vc.star(allb[i][1],allb[j][1])
        for mu,N,J in eng.hclosures(p):
            n+=1
            if mu!='all' and len(J)==1: units.append((mu,N,allb[i][2],allb[j][2]))
print('S4 bound',bound,'small boxes',len(small),'checks',n,'units',len(units),round(time.time()-t0,1))
for u in units[:10]: print(u)
