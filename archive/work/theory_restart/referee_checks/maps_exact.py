"""Independent audit of the report's one 12-generator special over F_2.
No imports from the report's verifier; algebra basis is a path type and length.
"""
from collections import defaultdict
from itertools import product
ID=['b','c','c','c','c','b','b','c','c','c','c','b']
# Paths are (source idempotent, kind, exponent); I exponent 0.
def end(a):
    s,k,n=a
    return ('c' if s=='b' else 'b') if k=='S' and n%2 else s
def degree(a):return 0 if a[1]=='I' else -(2 if a[1]=='D' else 1)*a[2]
def multiply(a,b): # a then b
    if end(a)!=b[0]:return None
    if a[1]=='I':return b
    if b[1]=='I':return a
    if a[1]!=b[1]:return None
    return (a[0],a[1],a[2]+b[2])
def add(s,k):
    if k in s:s.remove(k)
    else:s.add(k)
def product_maps(f,g): # f then g
    out=set()
    for i,j,a in f:
        for j2,l,b in g:
            if j2==j:
                z=multiply(a,b)
                if z:add(out,(i,l,z))
    return out
edges=[(1,2,'S',1),(2,3,'D',1),(3,4,'S',2),(4,5,'D',1),(5,6,'S',1),(6,7,'D',1),(8,7,'S',1),(9,8,'D',1),(10,9,'S',2),(11,10,'D',1),(12,11,'S',1),(1,12,'D',1)]
d={(i-1,j-1,(ID[i-1],k,n)) for i,j,k,n in edges}
assert not product_maps(d,d)
hq={0:(0,0)}
while len(hq)<12:
    for i,j,a in d:
        if i in hq:hq[j]=(hq[i][0]+1,hq[i][1]-degree(a))
        if j in hq:hq[i]=(hq[j][0]-1,hq[j][1]+degree(a))
assert all(hq[j]==(hq[i][0]+1,hq[i][1]-degree(a)) for i,j,a in d)
def boundary(f):return product_maps(f,d)^product_maps(d,f)
Kb={(12-i,i-1,(ID[i-1],'I',0)) for i in range(1,7)}
Kc={(i-1,j-1,('c','I',0)) for i,j in [(3,2),(5,4),(8,9),(10,11)]}
Ks={(i-1,j-1,(ID[i-1],k,n)) for i,j,k,n in [(2,1,'S',1),(4,3,'I',0),(6,5,'S',1),(7,8,'S',1),(9,10,'I',0),(11,12,'S',1)]}
Db={(i,i,('b','D',1)) for i,s in enumerate(ID) if s=='b'}
Dc={(i,i,('c','D',1)) for i,s in enumerate(ID) if s=='c'}
S2={(i,i,(s,'S',2)) for i,s in enumerate(ID)}
for name,K,z in [('Db',Kb,Db),('Dc',Kc,Dc),('S2',Ks,S2)]:
    assert boundary(K)==z, (name,boundary(K)^z)
    degs={(hq[j][0]-hq[i][0],hq[j][1]-hq[i][1]+degree(a)) for i,j,a in K}
    print(name,'dK+Kd = z.id; homotopy degrees:',degs)
def alg_basis(s,t,q):
    if q>0:return []
    if q==0:return [(s,'I',0)] if s==t else []
    out=[]
    if s==t and q%2==0:out.append((s,'D',-q//2))
    a=(s,'S',-q)
    if end(a)==t:out.append(a)
    return out
def mor_basis(h,q):
    return [(i,j,a) for i,j in product(range(12),repeat=2) if hq[j][0]-hq[i][0]==h for a in alg_basis(ID[i],ID[j],q-hq[j][1]+hq[i][1])]
def rank(sets):
    piv={}
    for st in sets:
        st=set(st)
        while st:
            p=max(st)
            if p in piv:st ^= piv[p]
            else:piv[p]=st;break
    return len(piv)
def hdim(h,q):
    return len(mor_basis(h,q))-rank(boundary({a}) for a in mor_basis(h,q))-rank(boundary({a}) for a in mor_basis(h-1,q))
ans={(h,q):n for h in range(-7,8) for q in range(-28,13) if (n:=hdim(h,q))}
print('End H degrees:',ans,'total',sum(ans.values()))
assert sum(ans.values())==16
print('gen h,q extrema:',min(h for h,q in hq.values()),max(h for h,q in hq.values()),min(q for h,q in hq.values()),max(q for h,q in hq.values()))
# q<-12 algebra powers all positive for all generator pairs; along each parity,
# the coefficient matrices of dHom stabilize (path exponents change uniformly).
# Thus the two zero tails q=-27,-28 certify all lower degrees.
assert all(hdim(h,q)==0 for h in range(-7,8) for q in [-27,-28])
print('Hom0 shift window:', sorted({(-q,h-q//2) for h,q in ans}))
print('Ext1 shift window:', sorted({(-q,h-q//2-1) for h,q in ans}))
