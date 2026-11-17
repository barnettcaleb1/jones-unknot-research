import sys, pickle, glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import theta, sym, plat2, relabel, constit, vc
tot=0; nontriv=0
for f in sorted(glob.glob('e4_*_4.pkl')):
    out,units=pickle.load(open(f,'rb'))
    for w,tg,Tr,N in units:
        T=('p',[Tr,('w',('Y' if N>0 else 'y')*abs(N))]) if N else Tr
        body=vc.word(T)
        ev=sym.symmetric(plat2.top_events(w)+sym.body(body,0))
        J=theta.J_events(ev); tot+=1
        k1=constit.trivial_constituent(ev); sis=relabel.sister_is_unit(ev)
        if J!={0:1} or not k1 or not sis:
            nontriv+=1; print('CHECK',w,body,'J',J,'K1 unknot',k1,'sister unit',sis,flush=True)
print('E4 unit pairs re-verified',tot,' flagged',nontriv)
