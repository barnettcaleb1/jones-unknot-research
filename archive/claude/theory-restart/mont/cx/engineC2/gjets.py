import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
def jet(p,end,K=7):
    if end=='top':
        d=max(p); return d,[p.get(d-i,0) for i in range(K)]
    d=min(p); return d,[p.get(d+i,0) for i in range(K)]
for nm,(i,j) in [('G11',(0,0)),('G13',(0,1)),('G31',(1,0)),('G33',(1,1))]:
    print(nm)
    for m in [2,4,6,8,10,12]:
        p=tab[m][i][j]
        dt,ct=jet(p,'top'); db,cb=jet(p,'bot')
        print('  m=%2d top deg %3d %s | bot deg %4d %s'%(m,dt,ct,db,cb))
