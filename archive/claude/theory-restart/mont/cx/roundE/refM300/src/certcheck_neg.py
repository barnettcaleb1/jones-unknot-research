"""negative controls for the own certificate checker: (1) class set enlarged by the 60 d2pos classes; (2) kmin=1 (single
box, n = 0 allowed); (3) random perturbations of multipliers; (4) planted 'rational-like' class (all zero data) and the
(-1,0) generic class duplicated with a positive potential.  The checker must REJECT in these situations."""
import sys, pickle, random, collections
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import certcheck as CC
import lpg, classes
C=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/certs_M300.pkl','rb'))
CD=CC.CD
S=[CD['top%d'%i]['key'] for i in range(300)]
SD=S+[v['key'] for k,v in CD.items() if k.startswith('d2_')]
CL={cl['name']:cl for cl in lpg.closure_classes()}; TC={tc['name']:tc for tc in lpg.tie_classes()}
def setup(key):
    cn_,nm,m=key
    if nm=='tie':
        tc=TC[cn_]; return dict(tc,end='top'),[],tc['n']
    cl=CL[cn_]
    if m is None: return cl,dict(lpg.case_rows(cl['p'],cl['q']))[nm],None
    return cl,dict(lpg.case_rows(cl['p'],cl['q'],m=m))[nm],cl['d0n']
def run(Sx,kmin,nmin,perturb=None):
    cnt=collections.Counter()
    for key,cert in C.items():
        cl,rows,nr=setup(key)
        u=list(cert['u']); w=list(cert['w'])
        if perturb: u,w=perturb(u,w)
        ok,info=CC.check_cert(Sx,cl,key[1],rows,key[2],nr,kmin,nmin,u,w)
        cnt[ok]+=1
    return cnt
print('(0) as stored (top-300, kmin=2, nmin=0):',dict(run(S,2,0)))
print('(1) S = top-300 + 60 d2pos classes:',dict(run(SD,2,0)))
print('(2) kmin=1, nmin=0 (single box, no rational box allowed):',dict(run(S,1,0)))
print('    kmin=1, nmin=1:',dict(run(S,1,1)))
random.seed(3)
def pert(u,w):
    u=list(u); idx=[i for i in range(19,len(u)) if u[i]!=0]
    if idx:
        i=random.choice(idx); u[i]=u[i]*Fr(random.choice([0,-1,2,Fr(1,2)]))
    return u,w
print('(3) one random case/slice/nrule multiplier perturbed (x0, x-1, x2, x1/2):',dict(run(S,2,0,pert)))
# (4) planted classes: an extra class with the data of a single RATIONAL box (rho_a etc. from an R_1 box) can make
# two-box products imitate n rational boxes; and a class with positive b-potential
pl=[((Fr(-1),Fr(-1,2),Fr(0),Fr(-1)),(Fr(0),Fr(-1,2),Fr(-1),Fr(-1)),Fr(0),-1)]   # rational-box-like signature (R_1/S_0 type)
print('(4) S = top-300 + one planted rational-like class:',dict(run(S+pl,2,0)))
pl2=[((Fr(-2),Fr(0),Fr(1),Fr(0)),(Fr(-3),Fr(0),Fr(-3),Fr(0)),Fr(4),-1)]
print('    S = top-300 + one planted b-potential class (rho_b = +1 at top):',dict(run(S+pl2,2,0)))
