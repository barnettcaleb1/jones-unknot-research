"""One exact formal pairing: Mor(a(1), Cone(H:Q->Q)), over F_2.

Independent of Claude's typeD.py and matching code. Q is the banked 12-generator
compact BN component. This is a definition check, not a knot search.
"""
from itertools import product

ID = ['b','c','c','c','c','b','b','c','c','c','c','b']
EDGES = [(1,2,'S',1),(2,3,'D',1),(3,4,'S',2),(4,5,'D',1),
         (5,6,'S',1),(6,7,'D',1),(8,7,'S',1),(9,8,'D',1),
         (10,9,'S',2),(11,10,'D',1),(12,11,'S',1),(1,12,'D',1)]

def target(a):
    s,k,n=a
    return ('c' if s=='b' else 'b') if k=='S' and n%2 else s
def deg(a): return -(2 if a[1]=='D' else 1)*a[2]
def mul(a,b):
    if target(a)!=b[0]: return None
    if a[1]=='I': return b
    if b[1]=='I': return a
    if a[1]!=b[1]: return None
    return (a[0],a[1],a[2]+b[2])
def basis(s,t,q):
    if q>0:return []
    if q==0:return [(s,'I',0)] if s==t else []
    ans=[]
    if s==t and q%2==0: ans.append((s,'D',-q//2))
    a=(s,'S',-q)
    if target(a)==t:ans.append(a)
    return ans
def toggle(S,x):
    if x in S:S.remove(x)
    else:S.add(x)
def rank(cols):
    piv={}
    for c in cols:
        c=set(c)
        while c:
            p=max(c)
            if p in piv:c ^= piv[p]
            else:piv[p]=c;break
    return len(piv)

hq={1:(0,0)}
while len(hq)<12:
    for i,j,k,p in EDGES:
        d=(2 if k=='D' else 1)*p
        if i in hq:hq[j]=(hq[i][0]+1,hq[i][1]+d)
        if j in hq:hq[i]=(hq[j][0]-1,hq[j][1]-d)
Q=[(ID[i-1],*hq[i]) for i in range(1,13)]
dQ=[(i-1,j-1,(ID[i-1],k,p)) for i,j,k,p in EDGES]
X=[('c',-1,-2),('b',0,-1)]
dX=[(0,1,('c','S',1))]
Y=[(s,h-1,q-1) for s,h,q in Q]+[(s,h,q+1) for s,h,q in Q]
dY=dQ+[(i+12,j+12,a) for i,j,a in dQ]
for i,(s,h,q) in enumerate(Q):
    dY += [(i,i+12,(s,'D',1)),(i,i+12,(s,'S',2))]

def mor(h,q):
    return [(i,j,a) for i,j in product(range(len(X)),range(len(Y)))
            if Y[j][1]-X[i][1]==h
            for a in basis(X[i][0],Y[j][0],q-Y[j][2]+X[i][2])]
def boundary(f):
    i,j,a=f;out=set()
    for j0,l,b in dY:
        if j==j0 and (z:=mul(a,b)) is not None:toggle(out,(i,l,z))
    for l,i0,b in dX:
        if i==i0 and (z:=mul(b,a)) is not None:toggle(out,(l,j,z))
    return out
def homdim(h,q):
    return len(mor(h,q))-rank(boundary(f) for f in mor(h,q))-rank(boundary(f) for f in mor(h-1,q))

# All possible Hom homological degrees are bounded by the generator differences.
hlo=min(y[1]-x[1] for x in X for y in Y)
hhi=max(y[1]-x[1] for x in X for y in Y)
qhi=max(y[2]-x[2] for x in X for y in Y)
positive_path_threshold=min(y[2]-x[2] for x in X for y in Y)
for h in range(hlo,hhi+1):
    for q in range(-24,qhi+1):
        next_basis=set(mor(h+1,q))
        for f in mor(h,q):
            df=boundary(f)
            assert df<=next_basis,('wrong Hom differential degree',h,q,f,df)
            ddf=set()
            for g in df: ddf ^= boundary(g)
            assert not ddf,('Hom differential does not square to zero',f,ddf)
out={(h,q):m for h in range(hlo,hhi+1) for q in range(-24,qhi+1)
     if (m:=homdim(h,q))}
expected={(0,0):1,(1,2):1,(2,4):1,(3,6):2,(4,8):1,(5,10):1,(6,12):1}
assert out==expected,(out,expected)
# For q<positive_path_threshold every morphism coefficient is a positive path.
# The shift q->q-2 sends D^a to D^(a+1) and S^a to S^(a+2), preserving each
# nonzero multiplication and every equality among output paths. Thus boundary
# matrices stabilize in each parity. These two zero tails certify exhaustion.
assert -23<positive_path_threshold and -24<positive_path_threshold
assert all(homdim(h,q)==0 for h in range(hlo,hhi+1) for q in (-23,-24))
print('Exact compact-Q slope-one closure:',out)
print('Hom degree and square-zero checks passed; stable tails below q=',positive_path_threshold)

# One pawn and two identical adjacent-delta copies of the eight-point multiset.
positions=[0,1,2,3,3,4,5,6]
# Upper Q source labels 0..7, pawn 8; lower hQ targets 0..7.
sources=positions+[0]
matching=[(0,1),(8,2),(1,3),(2,4),(3,5),(4,6),(5,7)]
assert len({a for a,b in matching})==7==len({b for a,b in matching})
assert all(positions[b]>sources[a] for a,b in matching)
print('Seven admissible pairs; three survivors. Hall witness: upper positions>=3'
      ' have five generators, but only three lower targets at positions>3.')
