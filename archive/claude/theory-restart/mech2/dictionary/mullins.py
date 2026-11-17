import json,collections,itertools
from fractions import Fraction as Fr
T=json.load(open('table.json')); A=json.load(open('alex.json'))
rows=[]
for a in T:
    if 'err' in a: continue
    k=a['k']; j=a['j']
    al=A[a['name'].replace('^','-')]['alex']; n=len(al); mid=(n-1)//2
    a2=sum(c*(i-mid)**2 for i,c in enumerate(al))//2
    J=collections.Counter()
    for (x,b) in a['L']: J[k+x+4*b]+=(-1)**((x+b)%2)
    d2=sum(c*e*(e-1)*(-1)**(e-2) for e,c in J.items())
    rows.append((a['name'],k,j,a2,d2,a['dim'],a['sigma']))
def solve(M,y):
    # exact least squares check: find solution of first independent rows, then verify all
    n=len(M[0]); 
    from fractions import Fraction as F
    aug=[[F(v) for v in r]+[F(b)] for r,b in zip(M,y)]
    piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,len(aug)) if aug[i][c]!=0),None)
        if p is None: continue
        aug[r],aug[p]=aug[p],aug[r]
        aug[r]=[v/aug[r][c] for v in aug[r]]
        for i in range(len(aug)):
            if i!=r and aug[i][c]!=0:
                f=aug[i][c]; aug[i]=[u-f*v for u,v in zip(aug[i],aug[r])]
        piv.append(c); r+=1
    incons=[row for row in aug[r:] if row[-1]!=0]
    sol=[F(0)]*n
    for i,c in enumerate(piv): sol[c]=aug[i][-1]
    return sol,len(incons)
for feats,names in [ (lambda r:[r[3],r[2],r[1],1],'a2,j,k,1'), (lambda r:[r[3],r[2],r[1],r[1]**2,r[2]**2,r[1]*r[2],1],'a2,j,k,k2,j2,kj,1')]:
    M=[feats(r) for r in rows]; y=[r[4] for r in rows]
    sol,inc=solve(M,y)
    print(names,[str(s) for s in sol],'inconsistent rows:',inc)
for r in rows[:14]: print(r)
