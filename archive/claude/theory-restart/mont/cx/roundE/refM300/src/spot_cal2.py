import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import spot_lib2, lp
for s in range(6):
    m=spot_lib2.build(500+s)
    t=time.time(); J=lp.J(m['word']); dt=time.time()-t
    print(m['kind'],len(m['xs']),len(m['rats']),m['how'],'ncand',m['ncand'],'len',m['len'],'depth',m['depth'],'time %.1fs'%dt,'agree',J==m['Jvc'],'span',(max(J)-min(J)) if J else None,flush=True)
