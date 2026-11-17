import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rauto
for K in (2,3,4):
    t=time.time(); order,trans=rauto.build(K); E=rauto.edges(order,trans)
    inc=[e for e in E if e[1]=='init']
    print('K=%d: %d states, %d transitions, %d dedup edges, edges into init: %d, %.1fs'%(K,len(order),len(trans),len(E),len(inc),time.time()-t))
    degs=sorted(set(k[0] for k in order if isinstance(k,tuple))); print('   state degrees',degs)
