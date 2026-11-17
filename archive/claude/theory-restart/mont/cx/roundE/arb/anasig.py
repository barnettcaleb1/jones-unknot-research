"""anatomy of gen1 signatures: positive end potentials (rho_a > 0 or rho_b > 0), phi = (rho_a+rho_b)/2 > -1/2, sigma/delta ranges."""
import sys, pickle, collections
from fractions import Fraction as Fr
for f in sys.argv[1:]:
    tot=pickle.load(open(f,'rb'))
    el={k:v for k,v in tot.items() if v[1]}
    pa=[k for k in el if k[0][0]>0 or k[1][0]>0]; pb=[k for k in el if k[0][2]>0 or k[1][2]>0]
    ph=[k for k in el if max((k[0][0]+k[0][2])/2,(k[1][0]+k[1][2])/2)>Fr(-1,2)]
    print(f,'eligible',len(el),'| a-potential',len(pa),'b-potential',len(pb),'| phi > -1/2 at an end',len(ph))
    print('   sigma values',sorted(collections.Counter(k[2] for k in el).items())[:20])
    print('   delta values',sorted(collections.Counter(k[3] for k in el).items()))
    print('   max rho_a',max(max(k[0][0],k[1][0]) for k in el),'max rho_b',max(max(k[0][2],k[1][2]) for k in el))
    for k in (pa+pb)[:6]: print('   POS',k,el[k][2])
