"""own exact check of the rational end laws used by M300 / tie3: for every normal form u(m) with sum|m_i| <= SMAX:
delta = span b - span a = -1, sigma = l1_top(q) + l1_bot(q) = 0, tau = l2_top(q) + l2_bot(q) = -1, |lc q| = 1 both ends,
span a >= 4 (rational part of Tot), rho_b = l1(b) <= 0 at both ends (BX3)."""
import sys, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rlaurent as RL
from fractions import Fraction as Fr
from nf_exact import exact_vec, forms
SMAX=int(sys.argv[1])
bad=collections.Counter(); n=0; minspan=99
for ms in forms(SMAX):
    a,b=exact_vec(ms); n+=1
    dl=RL.pspan(b)-RL.pspan(a)
    lq={}; lcq={}; rb={}
    for end in ('top','bot'):
        da,ca,la=RL.logdata(a,end,2); db,cb,lb=RL.logdata(b,end,2)
        lq[end]=(lb[0]-la[0],lb[1]-la[1]); lcq[end]=Fr(cb,ca); rb[end]=lb[0]
    if dl!=-1: bad['delta']+=1
    if lq['top'][0]+lq['bot'][0]!=0: bad['sigma']+=1
    if lq['top'][1]+lq['bot'][1]!=-1: bad['tau']+=1
    if abs(lcq['top'])!=1 or abs(lcq['bot'])!=1: bad['lc']+=1
    if max(rb.values())>0: bad['rho_b>0']+=1
    minspan=min(minspan,RL.pspan(a))
print('normal forms sum|m| <= %d: %d boxes; violations %s; min span a %d'%(SMAX,n,dict(bad),minspan))
