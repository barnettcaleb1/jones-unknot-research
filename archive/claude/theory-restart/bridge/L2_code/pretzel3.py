# 3-parameter family: pretzel P(n1,n2,n3) = N-closure of horizontal sum of three vertical twist boxes.
from twist2 import add, mul, vstep, N, D, is_mono, DEL
from itertools import product
def vbox(n):
    f,g={}, {0:1}          # [inf] = identity of vertical algebra
    for _ in range(abs(n)): f,g=vstep(f,g,1 if n>0 else -1)
    return f,g
def hsum(t,u):  # (f1 + g1 e)(f2 + g2 e) in horizontal algebra
    f1,g1=t; f2,g2=u
    return mul(f1,f2), add(add(mul(f1,g2),mul(g1,f2)),mul(mul(g1,g2),DEL))
R=6
units=[]
for n in product(range(-R,R+1),repeat=3):
    if sum(1 for x in n if x%2==0)>1: continue      # keep knots only (at most one even entry)
    t=hsum(hsum(vbox(n[0]),vbox(n[1])),vbox(n[2]))
    if is_mono(N(*t)): units.append(n)
print('knot points with monomial bracket:',len(units))
# classify: contains a pair {1,-1}  /  contains 0 (then 2-bridge sum)  / other
pair=[u for u in units if (1 in u and -1 in u)]
zero=[u for u in units if 0 in u and u not in pair]
rest=[u for u in units if u not in pair and u not in zero]
print('with {1,-1} pair (line families):',len(pair))
print('with a 0 entry:',len(zero), zero[:12])
print('other (sporadic):',rest)
