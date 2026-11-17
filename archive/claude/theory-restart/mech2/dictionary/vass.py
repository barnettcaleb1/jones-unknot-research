import json,collections
from fractions import Fraction as Fr
T=json.load(open('table.json')); A=json.load(open('alex.json'))
rows=[]
for a in T:
    if 'err' in a: continue
    k=a['k']; j=a['j']
    al=A[a['name'].replace('^','-')]['alex']; n=len(al); mid=(n-1)//2
    a2=sum(c*(i-mid)**2 for i,c in enumerate(al))//2
    # a4: Conway coefficient: Delta(t)=sum a_{2i} z^{2i}, z=t^{1/2}-t^{-1/2}; use moments: sum c_i (i-mid)^4 = 2 a2 + 24 a4  (since (z^2)^1 -> e^{x}-2+e^{-x}, etc.)
    m4=sum(c*(i-mid)**4 for i,c in enumerate(al))
    a4=Fr(m4-2*a2,24)
    # J(t) = t^k * sum (-t)^a (-t^4)^b ; exponents e=k+a+4b, sign (-1)^(a+b)
    J=collections.Counter()
    for (x,b) in a['L']: J[k+x+4*b]+=(-1)**((x+b)%2)
    J0=sum(J.values()); J1=sum(c*e for e,c in J.items()); J2=sum(c*e*(e-1) for e,c in J.items()); J3=sum(c*e*(e-1)*(e-2) for e,c in J.items())
    assert J0==1 and J1==-8*j,(a['name'],J0,J1,j)
    # log derivatives in u=log t: L2 = sum c e^2 - (sum c e)^2
    E2=sum(c*e*e for e,c in J.items()); E3=sum(c*e**3 for e,c in J.items())
    L2=E2-J1*J1
    L3=E3-3*E2*J1+2*J1**3
    rows.append(dict(name=a['name'],k=k,j=j,a2=a2,a4=a4,L2=L2,L3=L3,sig=a['sigma'],dim=a['dim']))
json.dump([{**r,'a4':str(r['a4'])} for r in rows],open('vass.json','w'))
for r in rows[:40]:
    print('%-7s k=%3d j=%2d a2=%2d  L2=%5d  L2+48a2=%5d  (L2+48a2)/8=%s   L3=%d'%(r['name'],r['k'],r['j'],r['a2'],r['L2'],r['L2']+48*r['a2'],Fr(r['L2']+48*r['a2'],8),r['L3']))
