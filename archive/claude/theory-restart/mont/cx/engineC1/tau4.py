import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
from fractions import Fraction as Fr
D=pickle.load(open('libA_jets.pkl','rb')); Bx=D['boxes']; nN=D['nN']
J=collections.Counter()
for k,T,tag,tp,bt in Bx:
    dl=tp[0]-bt[0]; sg=tp[2][0]+bt[2][0]; ta=tp[2][1]+bt[2][1]
    J[(dl,sg,ta)]+=1
print('distinct (delta,sigma,tau):',len(J))
# test candidate linear laws: tau - a*sigma - b*delta >= c ; print min of tau - sigma, tau + sigma, etc. per delta
byd=collections.defaultdict(list)
for (dl,sg,ta),v in J.items(): byd[dl].append((sg,ta,v))
for dl in sorted(byd):
    L=byd[dl]
    print('delta=%d n=%d  sigma range [%s,%s]  tau range [%s,%s]  min(tau-sigma)=%s min(tau+sigma)=%s  min(tau - sigma^2/2)=%s'%(dl,sum(x[2] for x in L),min(x[0] for x in L),max(x[0] for x in L),min(x[1] for x in L),max(x[1] for x in L),min(x[1]-x[0] for x in L),min(x[1]+x[0] for x in L),min(x[1]-x[0]**2/2 for x in L)))
