import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import s1window, fastS, vc, lp
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
# P from frequencies == (1+t^2) * Phat from the table, random boxes and m
ok=0
for w in ['XY','XXY','xYY','XyXY']:
    v=vc.rat(w); terms=s1window.coeffs(v)
    for m in [2,-4,6,12]:
        for N in [-1,0,2]:
            vN=(v[0],lp.shift(v[1],-3*N))
            ok+= s1window.P_at(terms,m,N)==lp.mul(s1window.Dc,fastS.Phat(tab[m],vN))
print('frequency P == (1+t^2) Phat:',ok,'/ 48')
# sanity unit: identity box with N such that J=1 (S-neck m=2,B=y0 gave J=1)
terms=s1window.coeffs(((0,),) and ({0:1},{0:1}))
print([ (m,N) for m in [-2,2] for N in range(-3,4) if s1window.P_at(terms,m,N) in (s1window.TARGET,s1window.NTARGET)])
