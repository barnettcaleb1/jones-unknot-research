"""consistency: the certificate functionals' exact minima on the own K=4 automaton equal those on K=3 (order-2 data are
determined at K = 2; a finer automaton must give the same walk set of order-2 vectors)."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rauto, certcheck as CC
import lpg
o4,t4=rauto.build(4); E4=rauto.edges(o4,t4); F4={k:rauto.qdata(k,4) for k in o4 if k!='init'}
o2,t2=rauto.build(2); E2=rauto.edges(o2,t2); F2={k:rauto.qdata(k,2) for k in o2 if k!='init'}
C=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/certs_M300.pkl','rb'))
CL={cl['name']:cl for cl in lpg.closure_classes()}
same=0; diff=0
for (cn_,nm,m),cert in C.items():
    if nm=='tie': continue
    cl=CL[cn_]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))[nm] if m is None else dict(lpg.case_rows(cl['p'],cl['q'],m=m))[nm]
    uc=cert['u'][19:19+len(rows)]
    ca=sum(u*r[0][0] for u,r in zip(uc,rows)); cq=sum(u*r[0][1] for u,r in zip(uc,rows))
    c2=sum(u*r[0][2] for u,r in zip(uc,rows)); cL=sum(u*r[0][3] for u,r in zip(uc,rows))
    g3=CC.gmin(ca,cq,c2,cL)
    g4=rauto.extremum(o4,E4,F4,lambda l:ca*l[0]+c2*l[1],lambda f:cq*f[2][0]+cL*f[2][1],'min')
    g2=rauto.extremum(o2,E2,F2,lambda l:ca*l[0]+c2*l[1],lambda f:cq*f[2][0]+cL*f[2][1],'min')
    if g3==g4==g2: same+=1
    else: diff+=1
print('certificate functionals: min on K=2, K=3, K=4 automata identical in %d / %d'%(same,same+diff))
