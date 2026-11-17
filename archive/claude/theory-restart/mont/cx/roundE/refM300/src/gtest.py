"""consistency test of the certificate functionals on ACTUAL rational boxes (exact Laurent data, no automaton): for each of
the 955 certificates, G(box) >= g0 (g0 = own automaton min) for 3,000 random normal forms at the certificate's weak end
(bottom data computed directly at t = 0); count attainment G = g0."""
import sys, pickle, random, collections
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import certcheck as CC, rlaurent as RL
from nf_exact import exact_vec, forms
import lpg
C=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/certs_M300.pkl','rb'))
CL={cl['name']:cl for cl in lpg.closure_classes()}
random.seed(8)
NF=forms(10); boxes=random.sample(NF,3000)
data={'top':[],'bot':[]}
for ms in boxes:
    a,b=exact_vec(ms)
    for end in ('top','bot'):
        _,_,la=RL.logdata(a,end,2); _,_,lb=RL.logdata(b,end,2)
        data[end].append((la[0],lb[0]-la[0],la[1],lb[1]-la[1]))     # (rho_a, rho_q, l2a, lambda_q)
viol=0; att=0; tested=0
for (cn_,nm,m),cert in C.items():
    if nm=='tie': continue
    cl=CL[cn_]
    rows=dict(lpg.case_rows(cl['p'],cl['q'])) [nm] if m is None else dict(lpg.case_rows(cl['p'],cl['q'],m=m))[nm]
    uc=cert['u'][19:19+len(rows)]
    ca=sum(u*r[0][0] for u,r in zip(uc,rows)); cq=sum(u*r[0][1] for u,r in zip(uc,rows))
    cl2=sum(u*r[0][2] for u,r in zip(uc,rows)); cL=sum(u*r[0][3] for u,r in zip(uc,rows))
    g0=CC.gmin(ca,cq,cl2,cL); tested+=1
    vals=[ca*x[0]+cq*x[1]+cl2*x[2]+cL*x[3] for x in data[cl['end']]]
    if min(vals)<g0: viol+=1
    if min(vals)==g0: att+=1
print('certificates tested %d: G(box) >= g0 for all 3,000 actual boxes in %d; violations %d; min attained by an actual box in %d'%(tested,tested-viol,viol,att))
