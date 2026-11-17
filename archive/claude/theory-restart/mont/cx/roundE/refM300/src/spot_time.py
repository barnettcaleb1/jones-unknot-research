import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import spot_lib
for s in range(5):
    t=time.time(); m=spot_lib.run(1000+s)
    print(s,m['kind'],len(m['xs']),len(m['rats']),'ncand',m['ncand'],'len',m.get('len'),'tJ %.2f'%m.get('tJ',-1),'agree',m.get('agree'),'span',m.get('span'),'units_vc',m['units_vc'],flush=True)
