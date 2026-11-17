"""print the semantic form of a few M300 certificates: the rational functional G = ca rho_a + cq rho_q + cla l2a + cL lambda_q,
its exact min g0, the minimal class column and the constant (the 'potential' that proves the case impossible)."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import certcheck as CC
import lpg
C=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/certs_M300.pkl','rb'))
CL={cl['name']:cl for cl in lpg.closure_classes()}
S=[CC.CD['top%d'%i]['key'] for i in range(300)]
for key in [('V top a+ typ+ |a|=3','d=-1 e=-1',None),('H mu=+1 top','d=-1 e=-1',None),('H mu=+1 bot','d=0 r=1',None),('V top a+ typ+ |a|=3','d=0 r=1',None)]:
    cands=[k for k in C if k[0]==key[0] and k[1]==key[1]]
    if not cands: continue
    k=cands[0]; cert=C[k]; cl=CL[k[0]]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))[k[1]] if k[2] is None else dict(lpg.case_rows(cl['p'],cl['q'],m=k[2]))[k[1]]
    uc=cert['u'][19:19+len(rows)]
    ca=sum(u*r[0][0] for u,r in zip(uc,rows)); cq=sum(u*r[0][1] for u,r in zip(uc,rows))
    c2=sum(u*r[0][2] for u,r in zip(uc,rows)); cL=sum(u*r[0][3] for u,r in zip(uc,rows))
    nr=None if k[2] is None else cl['d0n']
    ok,info=CC.check_cert(S,cl,k[1],rows,k[2],nr,2,0,cert['u'],cert['w'])
    print(k,'G = %s rho_a + %s rho_q + %s l2a + %s lambda_q'%(ca,cq,c2,cL),info,ok)
