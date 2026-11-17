# Find a swap word (no axis letters) with K' = trefoil and compare J with the N=3 coloured Jones of the trefoil,
# J_3(3_1) = q^2 + q^5 - q^7 + q^8 - q^9 - q^10 + q^11 (recalled; one chirality, normalised J(unknot)=1) up to q <-> 1/q and units.
import random, itertools
import clib, lp
from c1_constituents import constituents
target={2:1,5:1,7:-1,8:1,9:-1,10:-1,11:1}
def unitnorm(P):
    # normalise a Laurent poly by +-t^k so that P = 1 mod (t+1)^2 (lp.normalize) for comparison
    return lp.normalize(P)
tn=unitnorm(target); tm=unitnorm({-e:c for e,c in target.items()})
letters=['x1','y1','x2','y2']
found=0
for L in range(2,7):
    for body in itertools.product(letters,repeat=L):
        for cap,cup in (('l1','u1'),('r1','u1'),('l1','u2'),('r1','u2'),('l2','u1'),('r2','u1')):
            w='s.'+cap+'.'+'.'.join(body)+'.'+cup
            J=lp.J(w)
            if J is None or J=={0:1}: continue
            Vi,Vo=constituents(w)
            if Vo in ({1:1,3:1,4:-1},{-1:1,-3:1,-4:-1}):
                print(w,' K\'=',sorted(Vo.items()),' J=',sorted(J.items()))
                print('    equals normalised J_3(trefoil)?',J==tn,' or its mirror?',J==tm)
                found+=1
                if found>=2: raise SystemExit
