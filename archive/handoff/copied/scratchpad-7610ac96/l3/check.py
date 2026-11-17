import cmath, random
def mm(P,Q): return [[sum(P[i][k]*Q[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(P,Q,c=1): return [[P[i][j]+c*Q[i][j] for j in range(2)] for i in range(2)]
def sc(c,P): return [[c*P[i][j] for j in range(2)] for i in range(2)]
def H(P): return [[P[j][i].conjugate() for j in range(2)] for i in range(2)]
def nrm(P): return max(abs(P[i][j]) for i in range(2) for j in range(2))
I=[[1,0],[0,1]]
for A in [complex(random.uniform(.5,2),random.uniform(-1,1)) for _ in range(3)]:
    d=-A**2-A**-2; q3=d*d-1
    l0=A+d/A; l2=A                      # <sigma> = A + A^-1 e
    ok_sigma = abs(l0-(-A**-3))<1e-12
    S=[[1/d,q3/d],[1/d,-1/d]]
    ok_S2 = nrm(add(mm(S,S),I,-1))<1e-10
    rot=[S[0][0]*l0+S[0][1]*l2, S[1][0]*l0+S[1][1]*l2]
    ok_rot = abs(rot[0]-(1/A+d*A))<1e-10 and abs(rot[1]-1/A)<1e-10   # sigma^-1 = A^-1 + A e
    E1=[[d,1],[0,0]]; E2=[[0,0],[1,d]]
    ok_TL = nrm(add(mm(E1,E1),sc(d,E1),-1))<1e-10 and nrm(add(mm(mm(E1,E2),E1),E1,-1))<1e-10 and nrm(add(mm(mm(E2,E1),E2),E2,-1))<1e-10
    X=add(E1,mm(E1,E2),-d)
    print("generic A: sigma eigen",ok_sigma," S^2=I",ok_S2," rot(sigma)=sigma^-1",ok_rot," TL rel",ok_TL," x^2=0",nrm(mm(X,X))<1e-9," x!=0",nrm(X)>1e-6)
# Jones root r=7: A=-exp(i pi/(2r)); Gram of W(3,1) under cap pairing: [[d,1],[1,d]]
for r in [5,7,11]:
    A=-cmath.exp(1j*cmath.pi/(2*r)); d=-A**2-A**-2
    G=[[d,1],[1,d]]
    E1=[[d,1],[0,0]]; E2=[[0,0],[1,d]]
    s1=add(sc(A,I),sc(1/A,E1)); s2=add(sc(A,I),sc(1/A,E2))
    def defect(M): return nrm(add(mm(mm(H(M),G),M),G,-1))
    X=add(E1,mm(E1,E2),-d); U=add(I,X)
    evG=[(d.real+1),(d.real-1)]
    print(f"r={r}: delta={d.real:+.4f} Gram eig {evG[0]:+.3f},{evG[1]:+.3f} | sigma1,sigma2 unitarity defect {defect(s1):.1e},{defect(s2):.1e} | 1+x defect {defect(U):.3f}")
