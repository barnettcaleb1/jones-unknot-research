import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import plat2, lp, fastS
for W0 in ['AbAd','aBaD','abAd','AAbd']:
    out=[]
    for n in range(1,9):
        w=W0*n
        if not plat2.is_arc(w): out.append((n,'loop')); continue
        J=plat2.J(w)
        out.append((n,lp.span(J),sorted(J.items()) if lp.span(J)<=8 else '...'))
    print(W0); [print('   ',o) for o in out]
