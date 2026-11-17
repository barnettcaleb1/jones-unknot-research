# Artin action on F_n (letters +-j), right action: x.(w1 w2) = (x.w1).w2
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return out
def winv(w): return [-x for x in reversed(w)]
def sig(i,s):
    # sigma_i^s substitution on generators
    if s>0: return {i:[i,i+1,-i], i+1:[i]}
    else:   return {i:[i+1], i+1:[-(i+1),i,i+1]}
def subst(w,m):
    out=[]
    for x in w:
        a=abs(x); img=m.get(a,[a])
        out+= img if x>0 else winv(img)
    return red(out)
def act(n,w):
    imgs={j:[j] for j in range(1,n+1)}
    for g in w:
        m=sig(abs(g),1 if g>0 else -1)
        imgs={j:subst(imgs[j],m) for j in imgs}
    return imgs
def comm(a,b): return a+b+winv(a)+winv(b)
def A(i,j):
    up=list(range(j-1,i,-1)); return up+[i,i]+winv(up)
a=[1,2]*6; b=comm(comm(A(1,4),A(2,4)),A(3,4)); phi0=comm(a,b)
# sanity: braid relations in Artin action
assert act(4,[1,2,1])==act(4,[2,1,2]) and act(4,[1,3])==act(4,[3,1]) and act(4,[1,-1])=={j:[j] for j in range(1,5)}
im=act(4,phi0)
print("image lengths:",{j:len(v) for j,v in im.items()})
print("Phi0 trivial in B4 (Artin)?", all(im[j]==[j] for j in im))
# purity: x_j maps to conjugate of x_j
for j,v in im.items():
    k=len(v)//2; assert v[k]==j and red(v[:k]+v[k+1:])==[] , j
print("pure: yes")
for i in range(1,5):
    kill=lambda w: red([x for x in w if abs(x)!=i])
    triv=all(kill(im[j])==[j] for j in im if j!=i)
    print(f"forget strand {i}: induced automorphism of F_3 trivial? {triv}")
# also each inner piece nontrivial in B4
print("b trivial?", all(v==[j] for j,v in act(4,b).items()))
