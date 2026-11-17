"""Independent check of the CH^4 first lemma (referee-prior-fresh-eyes).
W(6,0): basis a=(12)(34)(56) b=(12)(36)(45) c=(14)(23)(56) d=(16)(23)(45) e=(16)(25)(34).
sigma_i -> A + A^-1 e_i.  Exact Laurent polynomials in A as dict exp->int.
"""
import itertools, random, cmath, math
import numpy as np

# ---------- matchings ----------
basis = [((1,2),(3,4),(5,6)), ((1,2),(3,6),(4,5)), ((1,4),(2,3),(5,6)),
         ((1,6),(2,3),(4,5)), ((1,6),(2,5),(3,4))]
def norm(m):
    return tuple(sorted(tuple(sorted(p)) for p in m))
basis = [norm(m) for m in basis]
idx = {m:i for i,m in enumerate(basis)}

def partner(m):
    d={}
    for x,y in m: d[x]=y; d[y]=x
    return d

def act_e(i, m):
    """e_i on cup diagram m: returns (loops, new matching)."""
    p = partner(m)
    if p[i]==i+1: return 1, m
    a, b = p[i], p[i+1]
    new = [pr for pr in m if i not in pr and i+1 not in pr]
    new += [(i,i+1),(a,b)]
    return 0, norm(new)

def loops(m, n):
    pm, pn = partner(m), partner(n)
    seen=set(); cnt=0
    for s in range(1,7):
        if s in seen: continue
        cnt+=1; x=s
        while True:
            seen.add(x); y=pm[x]; seen.add(y); x=pn[y]
            if x==s: break
    return cnt

# ---------- Laurent polys ----------
def padd(p,q,s=1):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,0)+s*v
        if r[k]==0: del r[k]
    return r
def pmul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            r[k1+k2]=r.get(k1+k2,0)+v1*v2
    return {k:v for k,v in r.items() if v}
def mono(k,c=1): return {k:c}
delta = {2:-1,-2:-1}
def pev(p,A): return sum(v*A**k for k,v in p.items())
def pspan(p): return (max(p)-min(p)) if p else None

# e_i matrices (exact): column j = e_i(basis_j)
def e_mat(i):
    M=[[{} for _ in range(5)] for _ in range(5)]
    for j,m in enumerate(basis):
        l,n = act_e(i,m)
        M[idx[n]][j] = padd(M[idx[n]][j], delta if l else {0:1})
    return M
E = {i:e_mat(i) for i in range(1,6)}

def apply_gen(g, v):
    """g = +-i ; sigma_i = A + A^-1 e_i ; sigma_i^-1 = A^-1 + A e_i."""
    i=abs(g); s = 1 if g>0 else -1
    ev = [ {} for _ in range(5)]
    for r in range(5):
        for j in range(5):
            if E[i][r][j] and v[j]:
                ev[r]=padd(ev[r], pmul(E[i][r][j], v[j]))
    out=[]
    for r in range(5):
        out.append(padd(pmul(mono(s), v[r]), pmul(mono(-s), ev[r])))
    return out

def apply_word(w, v):
    for g in reversed(w):   # rightmost acts first
        v = apply_gen(g, v)
    return v

q2 = {2:1,-2:1}           # [2]
q3 = {4:1,0:1,-4:1}       # [3]
vc = [q2, {0:1}, {0:1}, q2, q3]

# ---------- numeric helpers ----------
def num_mat_gen(g, A):
    i=abs(g); s=1 if g>0 else -1
    Em = np.array([[pev(E[i][r][j],A) if E[i][r][j] else 0 for j in range(5)] for r in range(5)],dtype=complex)
    return A**s*np.eye(5) + A**(-s)*Em
def num_word(w, A):
    M=np.eye(5,dtype=complex)
    for g in w: M = M @ num_mat_gen(g,A)
    return M
def gram(dl):
    return np.array([[dl**loops(m,n) for n in basis] for m in basis],dtype=float)

if __name__=="__main__":
    out=[]
    # 1. T_c v_c = A^6 v_c exactly
    Tc = [1,2]*3
    w = apply_word(Tc, vc)
    ok = all(padd(w[r], pmul(mono(6), vc[r]), -1)=={} for r in range(5))
    out.append(f"T_c v_c == A^6 v_c exactly: {ok}")
    # sigma_1 v_c = A v_c exactly (f_3 killed by e1,e2)
    w1 = apply_word([1], vc); ok1 = all(padd(w1[r], pmul(mono(1), vc[r]), -1)=={} for r in range(5))
    out.append(f"sigma_1 v_c == A v_c exactly: {ok1}")
    # 2. signature of Gram over delta
    out.append("signature (pos,neg,zero) of Gram G(delta):")
    for dl in [-1.9,-1.6,-1.3,-1.1,-0.9,-0.618034,-0.3,0.3,0.618034,0.9,1.05,1.2,1.3,1.4,1.45,1.618034,1.9,2.5]:
        ev=np.linalg.eigvalsh(gram(dl))
        out.append(f"  delta={dl:+.4f}: ({sum(ev>1e-9)},{sum(ev<-1e-9)},{sum(abs(ev)<=1e-9)})")
    # 3. identity H(v_c,w) = -[3][4] w_e at random A on circle; H(v,w)=conj(v)^T G w
    th=1.13; A=cmath.exp(1j*th); dl=(-A**2-A**-2).real; G=gram(dl)
    q = lambda n: (A**(2*n)-A**(-2*n))/(A**2-A**-2)
    vcn=np.array([pev(p,A) for p in vc])
    wr=np.random.randn(5)+1j*np.random.randn(5)
    out.append(f"H(v_c,w) + [3][4] w_e = {abs(np.conj(vcn)@G@wr + q(3)*q(4)*wr[4]):.2e}")
    out.append(f"H(v_c,v_c) + [3]^2[4] = {abs(np.conj(vcn)@G@vcn + q(3)**2*q(4)):.2e}")
    # 4. random braids: N exact, inequalities, N(zeta16) = zeta16^{e(beta)}
    random.seed(7)
    viol=0; maxdev16=0; checked=0; maxdev_pi3=[]
    for trial in range(300):
        L=random.randint(4,24)
        word=[random.choice([1,2,3,4,5])*random.choice([1,-1]) for _ in range(L)]
        v=apply_word(word, vc); N=v[4]
        esum=sum(1 if g>0 else -1 for g in word)
        z=cmath.exp(3j*math.pi/8)
        maxdev16=max(maxdev16, abs(pev(N,z)-z**esum))
        for th in np.linspace(math.pi/3+1e-3, 3*math.pi/8-1e-3, 9):
            A=cmath.exp(1j*th); q3v=abs((A**6-A**-6)/(A**2-A**-2))
            if abs(pev(N,A)) < q3v-1e-9: viol+=1
        for th in np.linspace(3*math.pi/8+1e-3, 5*math.pi/8-1e-3, 9):
            A=cmath.exp(1j*th)
            if abs(A**2-A**-2)<1e-9: continue
            q3v=abs((A**6-A**-6)/(A**2-A**-2))
            if abs(pev(N,A)) > q3v+1e-9: viol+=1
        checked+=1
    out.append(f"random braids {checked}: inequality violations={viol}; max |N(z16)-z16^e(beta)| = {maxdev16:.2e}")
    # 5. unitarity check numerically at theta in arc
    th=1.10; A=cmath.exp(1j*th); dl=(-A**2-A**-2).real; G=gram(dl)
    M=num_word([1,-3,2,5,-4,2,2,3],A)
    out.append(f"theta=1.10 delta={dl:.4f}: ||M^H G M - G|| = {np.linalg.norm(M.conj().T@G@M-G):.2e}")
    # 6. tangent rotation of T_c: eigen on v_c^perp / eigen on v_c
    MT=num_word(Tc,A)
    evals=np.linalg.eigvals(MT)
    out.append(f"T_c eigenvalues at theta=1.10: {np.round(evals,6)}; A^-12={np.round(A**-12,6)}")
    print("\n".join(out))
