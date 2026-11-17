"""PHI-LEMMA checks with own data: (i) sup over all non-integral rational boxes of phi = rho_a + rho_q/2 (own automaton,
exact), (ii) phi_j = (ra_j + rb_j)/2 at BOTH ends for the 300 top classes and the 60 d2pos classes, (iii) lambda_q bounds,
(iv) the vertical d=0 inequalities for every V class at |mB| >= 4 (r=1) and every mB (r=0), (v) the horizontal d=0 bound
(n = delta.k - delta* >= 0 with delta_j <= -1) and slice coverage, (vi) the generalised phi-lemma constants of D36."""
import sys, pickle
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rauto
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
CD=pickle.load(open(HERE+'classdata.pkl','rb')); W=pickle.load(open(HERE+'wdata.pkl','rb'))
for K in (2,3,4):
    order,trans=rauto.build(K); E=rauto.edges(order,trans); FIN={k:rauto.qdata(k,K) for k in order if k!='init'}
    phimax=rauto.extremum(order,E,FIN,lambda l:l[0],lambda f:f[2][0]/2,'max')
    lqmax=max(f[2][1] for f in FIN.values()); lqmin=min(f[2][1] for f in FIN.values())
    rqset=sorted(set(f[2][0] for f in FIN.values()))
    print('K=%d: sup phi over rational boxes = %s ; lambda_q range [%s, %s] ; rho_q values %s'%(K,phimax,lqmin,lqmax,rqset))
tops=[CD['top%d'%i]['key'] for i in range(300)]
d2=[(k,v['key']) for k,v in CD.items() if k.startswith('d2_')]
def phi(key,end): e=key[0] if end=='top' else key[1]; return (e[0]+e[2])/2
def lq(key,end): e=key[0] if end=='top' else key[1]; return e[3]-e[1]
print('top-300: max phi over classes and ends =',max(phi(k,e) for k in tops for e in ('top','bot')),
      ' max |lambda_q| =',max(abs(lq(k,e)) for k in tops for e in ('top','bot')),
      ' delta values',sorted(set(k[3] for k in tops)),' sigma values',sorted(set(k[2] for k in tops)))
# vertical d=0 inequalities, per V class (p,q) at the weak end, Lmax = 2
for a in (3,-3,5,-5):
    o,sg,ds=W['V'][a]
    for end in ('top','bot'):
        p,q,_=o[end]; p1,p2=p[0],p[1]; q1,q2=q[0],q[1]
        r0=1-(p1+q1)/2           # r=0: sum phi must equal this; impossible if > -N/2 for all N >= 1, i.e. if >= 0
        worst=None
        for m in [Fr(x) for x in range(4,60)]+[Fr(-x) for x in range(4,60)]:
            # need N(1/2 - 2/|m|) <= -1 + (p1+q1)/2 + |q2-p2|/|m| for some N >= 1
            lhs_min=(Fr(1,2)-Fr(2)/abs(m))*1 if Fr(1,2)-Fr(2)/abs(m)>=0 else None
            rhs=-1+(p1+q1)/2+abs(q2-p2)/abs(m)
            feasible = (lhs_min is None) or (lhs_min<=rhs)
            if feasible: worst=m
        print('  V a=%+d weak %s: p=(%s,%s) q=(%s,%s): r=0 needs sum phi = %s (>0: impossible);  r=1 feasible at some |mB|>=4? %s'%(a,end,p1,p2,q1,q2,r0,worst))
# horizontal d=0: n = delta.k - delta* >= 0, delta_j <= -1  => |k| <= -delta*
for mu in (1,2,3,4):
    o,sg,ds=W['H'][mu]
    print('  H mu=%d: delta*=%s => |k| <= %s ; sigma* = %s ; with sigma_j in {0,1}: mB in [%s, %s] (slices cover sigma.k in [-8,8])'%(mu,ds,-ds,sg,-sg,-ds-sg))
# D36 generalised phi-lemma constants
d2open={'d2_457','d2_459','d2_460','d2_497','d2_536','d2_565','d2_895','d2_902','d2_1232','d2_1238','d2_1247','d2_1494','d2_2557','d2_2780','d2_3075','d2_3076','d2_3077','d2_3933','d2_4277','d2_4643','d2_5150','d2_5152','d2_5153','d2_5154'}
D36=[(l,k) for l,k in d2 if l not in d2open]
print('D36 classes:',len(D36),' boxes',sum(CD[l]['n'] for l,k in D36))
print('  max phi_e over D36 classes/ends =',max(phi(k,e) for l,k in D36 for e in ('top','bot')),
      ' max |lambda_q,e| =',max(abs(lq(k,e)) for l,k in D36 for e in ('top','bot')),
      ' sigma values',sorted(set(k[2] for l,k in D36)),' delta values',sorted(set(k[3] for l,k in D36)))
print('  all 60 d2pos: max phi',max(phi(k,e) for l,k in d2 for e in ('top','bot')),' max |lambda_q|',max(abs(lq(k,e)) for l,k in d2 for e in ('top','bot')))
