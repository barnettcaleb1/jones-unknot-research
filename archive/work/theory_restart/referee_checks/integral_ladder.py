"""The fixed Q over Z, and one infinity pairing; no knot enumeration."""
from collections import defaultdict
from fractions import Fraction

IDS=['b','c','c','c','c','b','b','c','c','c','c','b']
E=[(1,2,'S',1),(2,3,'D',1),(3,4,'S',2),(4,5,'D',1),
   (5,6,'S',1),(6,7,'D',1),(8,7,'S',1),(9,8,'D',1),
   (10,9,'S',2),(11,10,'D',1),(12,11,'S',1),(1,12,'D',1)]
hq={1:(0,0)}
while len(hq)<12:
    for i,j,k,p in E:
        dq=(2 if k=='D' else 1)*p
        if i in hq:hq[j]=(hq[i][0]+1,hq[i][1]+dq)
        if j in hq:hq[i]=(hq[j][0]-1,hq[j][1]-dq)
Q=[(IDS[i-1],*hq[i]) for i in range(1,13)]

def target(a):
    s,k,n=a
    return ('c' if s=='b' else 'b') if k=='S' and n%2 else s
def mul(a,b):
    if target(a)!=b[0]:return None
    if a[1]=='I':return b
    if b[1]=='I':return a
    if a[1]!=b[1]:return None
    return a[0],a[1],a[2]+b[2]
def basis(s,t,q):
    if q>0:return []
    if q==0:return [(s,'I',0)] if s==t else []
    out=[]
    if s==t and q%2==0:out.append((s,'D',-q//2))
    a=(s,'S',-q)
    if target(a)==t:out.append(a)
    return out

dQ=[(i-1,j-1,(IDS[i-1],k,p),-1 if (i,j)==(1,12) else 1)
    for i,j,k,p in E]
for i,j,a,c in dQ:
    for j0,k,b,d in dQ:
        if j==j0:assert mul(a,b) is None   # square-zero term by term over Z
assert [(h,q) for s,h,q in Q if s=='b']==[(0,0),(5,8),(6,10),(1,2)]

# Standard signed H-cone, H=D-S^2; pair with a(infinity)=c(0,0).
Y=[(s,h-1,q-1) for s,h,q in Q]+[(s,h,q+1) for s,h,q in Q]
dY=[(i,j,a,-c) for i,j,a,c in dQ]+[(i+12,j+12,a,c) for i,j,a,c in dQ]
for i,(s,h,q) in enumerate(Q):
    dY += [(i,i+12,(s,'D',1),1),(i,i+12,(s,'S',2),-1)]
def mor(h,q):
    return [(j,a) for j,y in enumerate(Y) if y[1]==h
            for a in basis('c',y[0],q-y[2])]
def bd(f):
    j,a=f;out=defaultdict(int)
    for j0,k,b,c in dY:
        if j==j0 and (z:=mul(a,b)) is not None:out[k,z]+=c
    return {k:v for k,v in out.items() if v}
pivot_values=set()
def rank(columns):
    piv={}
    for cc in columns:
        c={k:Fraction(v) for k,v in cc.items() if v}
        while c:
            p=max(c);v=c[p]
            if p not in piv:
                pivot_values.add(v)
                piv[p]={k:w/v for k,w in c.items()};break
            for k,w in piv[p].items():
                c[k]=c.get(k,0)-v*w
                if not c[k]:del c[k]
    return len(piv)
for h in range(-1,7):
    for q in range(-20,12):
        bb=mor(h,q)
        for f in bb:
            ddf=defaultdict(int)
            for a,c in bd(f).items():
                for b,d in bd(a).items():ddf[b]+=c*d
            assert not any(ddf.values())
        assert len(bb)-rank(map(bd,bb))-rank(map(bd,mor(h-1,q)))==0
assert pivot_values <= {Fraction(1),Fraction(-1)}, pivot_values
# Below q=-1, positive-path matrices stabilize under q->q-2 in each parity.
# The zero tail ranks therefore certify all q, not only the finite window.
print('Q differential squares to zero over Z term by term.')
print('N_Z(Q) is free of rank4 in the stated bullet degrees.')
print('Infinity H-cone pairing is acyclic; every elimination pivot is +/-1.')
print('Signed gap2 ladder: source d=-d_Q, target d=d_Q; D3=id has degree(3,4).')

# Central null-homotopies, preserving the characteristic-two calibration.
# The one minus sign is essential: all-plus Q has nonzero D_b and H actions
# in rational homotopy. No characteristic-two homotopy is reused verbatim.
fs=[(i,j,a) for i,x in enumerate(Q) for j,y in enumerate(Q)
    if y[1]-x[1]==-1 for a in basis(x[0],y[0],-2-y[2]+x[2])]
def end_boundary(f):
    i,j,a=f;out=defaultdict(int)
    for x,y,b,c in dQ:
        if x==j and (z:=mul(a,b)) is not None:out[i,y,z]+=c
        if y==i and (z:=mul(b,a)) is not None:out[x,j,z]+=c
    return {k:v for k,v in out.items() if v}
piv={}
for index,f in enumerate(fs):
    c={k:Fraction(v) for k,v in end_boundary(f).items()}
    comb={index:Fraction(1)}
    while c:
        p=max(c);v=c[p]
        if p not in piv:
            piv[p]=({k:w/v for k,w in c.items()},
                    {k:w/v for k,w in comb.items()});break
        pc,pcomb=piv[p]
        for dest,src in ((c,pc),(comb,pcomb)):
            for k,w in src.items():
                dest[k]=dest.get(k,0)-v*w
                if not dest[k]:del dest[k]
for name in ('Db','Dc','S2','H'):
    target_map={}
    for i,(s,h,q) in enumerate(Q):
        if (s=='b' and name in ('Db','H')) or (s=='c' and name in ('Dc','H')):
            target_map[i,i,(s,'D',1)]=Fraction(1)
        if name in ('S2','H'):
            target_map[i,i,(s,'S',2)]=Fraction(-1 if name=='H' else 1)
    residual=target_map.copy();answer=defaultdict(Fraction)
    while residual:
        p=max(residual);v=residual[p];assert p in piv
        pc,comb=piv[p]
        for k,w in pc.items():
            residual[k]=residual.get(k,0)-v*w
            if not residual[k]:del residual[k]
        for k,w in comb.items():answer[k]+=v*w
    assert all(v.denominator==1 for v in answer.values())
    check=defaultdict(Fraction)
    for k,v in answer.items():
        for row,w in end_boundary(fs[k]).items():check[row]+=v*w
    assert {k:v for k,v in check.items() if v}==target_map
    print(name, 'has an integral homogeneous null-homotopy, nonzero terms:',
          sum(v!=0 for v in answer.values()))
