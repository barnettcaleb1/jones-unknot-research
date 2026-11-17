import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import fastS, vc, lp
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
for pw in ['XY','XXY','XyY'[:0]+'XYY']:
    p=vc.rat(pw)
    for m in [2,4]:
        row=[]
        for k in range(-8,9):
            if k==0: continue
            v=vc.F(k,p)
            best=None
            for N in range(-12,13):
                vN=(v[0],lp.shift(v[1],-3*N)); R=fastS.R_of(tab[m],vN)
                s=lp.span(R)
                if best is None or s<best[0]: best=(s,N)
            row.append((k,best[0]))
        print('p=%s m=%d  (k, min_N span J):'%(pw,m),row)
