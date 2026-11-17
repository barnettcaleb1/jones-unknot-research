"""CHECK of clipping lemma R4 on all R(5) n=2 products, |N| <= 4: whenever sig(F_7 P) != sig(F_6 P) (resp. -7/-6), R4's threshold
max(delta_t, o_b) + K + 2 (resp. max(-delta_t, -o_b) + K + 2) must exceed 6 (K = 2).  delta_t = deg_top z_P, o_b = ord_bot z_P."""
import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import jbox, lib, vc, zjet
R=lib.rational(5); P=[jbox.from_vec(r[1]) for r in R]
diff=viol=tot=0
for idx in itertools.combinations_with_replacement(range(len(R)),2):
    x=jbox.star(P[idx[0]],P[idx[1]])
    for N in range(-4,5):
        y=jbox.ypow(N,x)
        sg={}
        for m in (6,7,-6,-7):
            try: sg[m]=jbox.signature(jbox.nest(m,y))[0]
            except AssertionError: sg[m]=None
        p=vc.Ypow(N,vc.starall([R[i][1] for i in idx]))
        if p[0]==p[1]: continue
        zt=zjet.zser(p,'top'); zb=zjet.zser(p,'bot')
        if zt is None or zb is None: continue
        dt=-zt[0]; ob=zb[0]
        for a,b,thr in ((7,6,max(dt,ob)+4),(-7,-6,max(-dt,-ob)+4)):
            if sg[a] is None or sg[b] is None: continue
            tot+=1
            if sg[a]!=sg[b]:
                diff+=1
                if thr<=6: viol+=1
print('pairs compared',tot,'differences',diff,'differences with R4 threshold <= 6 (violations):',viol)
