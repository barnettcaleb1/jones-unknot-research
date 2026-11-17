import json,collections,cmath
from fractions import Fraction as Fr
T=json.load(open('table.json')); A=json.load(open('alex.json'))
def polydiv(J):
    """R = (J-1)/((1-t^4)(1+t^3)) as dict exponent->coeff (exact Laurent division)"""
    P=dict(J); P[0]=P.get(0,0)-1
    P={e:c for e,c in P.items() if c}
    if not P: return {}
    # divide by D(t)=1+t^3-t^4-t^7 (lowest term 1)
    D={0:1,3:1,4:-1,7:-1}
    R={}
    while P:
        e=min(P); c=P[e]
        R[e]=c
        for d,v in D.items():
            P[e+d]=P.get(e+d,0)-c*v
            if P[e+d]==0: del P[e+d]
        if len(R)>500: raise ValueError('not divisible')
    return R
rows=[]
for a in T:
    if 'err' in a: continue
    k=a['k']; j=a['j']
    al=A[a['name'].replace('^','-')]['alex']; n=len(al); mid=(n-1)//2
    a2=sum(c*(i-mid)**2 for i,c in enumerate(al))//2
    m4=sum(c*(i-mid)**4 for i,c in enumerate(al)); a4=Fr(m4-2*a2,24)
    J=collections.Counter()
    for (x,b) in a['L']: J[k+x+4*b]+=(-1)**((x+b)%2)
    R=polydiv({e:c for e,c in J.items() if c})
    R1=sum(R.values()); Rm1=sum(c*(-1)**e for e,c in R.items())
    Ri=sum(c*(1j)**e for e,c in R.items())
    w=cmath.exp(1j*cmath.pi/3)
    Rw=sum(c*w**e for e,c in R.items())
    det=abs(sum(c*(-1)**i for i,c in enumerate(al)))
    rows.append(dict(name=a['name'],k=k,j=j,a2=a2,a4=int(a4),R1=R1,Rm1=Rm1,Ri=(round(Ri.real),round(Ri.imag)),Rw=(round(Rw.real,3),round(Rw.imag,3)),absRw2=round(abs(Rw)**2,3),det=det,sig=a['sigma'],nR=sum(abs(c) for c in R.values())))
assert all(r['R1']==r['j'] for r in rows)
assert all(r['Rm1']==-r['a2'] for r in rows)
print('R(1) = j and R(-1) = -a2 hold for all',len(rows))
for r in rows[:46]:
    print('%-7s k=%3d j=%2d a2=%2d a4=%3d det=%2d | R(i)=%s  |R(i)|^2=%d | R(w)=%s |R(w)|^2=%s | terms %d'%(r['name'],r['k'],r['j'],r['a2'],r['a4'],r['det'],r['Ri'],r['Ri'][0]**2+r['Ri'][1]**2,r['Rw'],r['absRw2'],r['nR']))
json.dump(rows,open('roots.json','w'))
