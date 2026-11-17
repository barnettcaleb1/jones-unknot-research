import sys, pickle, glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
allres={}
for f in glob.glob(sys.argv[1]):
    res,units,n=pickle.load(open(f,'rb'))
    for k,v in res.items():
        if k not in allres or len(v[0])<len(allres[k][0]): allres[k]=v
print('distinct nonunit J:',len(allres))
rows=[(1-v[1]/v[2] if v[2]>0 else 0, v[1], v[2], v[3], v[4], v[0]) for k,v in allres.items()]
rows.sort(reverse=True)
print('top rho (1 - halfspan/predicted):')
for r in rows[:8]: print('  rho %.3f  halfspan %.1f pred %.1f a2 %s z10 %s  w=%s'%r)
hs=sorted(rows,key=lambda r:r[1])
print('smallest half-spans:',[(r[1],r[5],r[3],r[4]) for r in hs[:10]])
g=[r for r in rows if r[3]==0 and r[4]]
print('doubly gated:',len(g),sorted([(r[1],r[5]) for r in g])[:10])
a2z=[r for r in rows if r[3]==0]
print('a2=0:',len(a2z),sorted([(r[1],r[5],r[4]) for r in a2z])[:10])
