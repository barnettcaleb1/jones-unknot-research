# Check C2: signature of the Hermitian form invariant under reduced Burau of B_3 at t = e^{i theta}.
# Reduced Burau (one standard convention): s1 -> [[-t,1],[0,1]], s2 -> [[1,0],[t,-t]].
import cmath, math
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def adj(A): return [[A[j][i].conjugate() for j in range(2)] for i in range(2)]
def H_of(x):  # x = (a, c, br, bi) real
    a,c,br,bi = x; b = complex(br,bi); return [[a,b],[b.conjugate(),c]]
def residual_rows(mats):
    rows=[]
    basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    cols=[]
    for e in basis:
        H=H_of(e); col=[]
        for A in mats:
            D=mul(mul(adj(A),H),A)
            for i in range(2):
                for j in range(2):
                    z=D[i][j]-H[i][j]; col += [z.real, z.imag]
        cols.append(col)
    return [[cols[k][r] for k in range(4)] for r in range(len(cols[0]))]
def nullvec(M):
    # Gaussian elimination, return a null vector of the 4-column matrix (assumes 1-dim nullspace)
    M=[r[:] for r in M]; piv=[]; r=0
    for c in range(4):
        p=max(range(r,len(M)), key=lambda i: abs(M[i][c]))
        if abs(M[p][c])<1e-9: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[v/pv for v in M[r]]
        for i in range(len(M)):
            if i!=r: f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    free=[c for c in range(4) if c not in piv]
    assert len(free)==1, (piv, free)
    x=[0.0]*4; x[free[0]]=1.0
    for i,c in enumerate(piv): x[c]=-M[i][free[0]]
    return x
for deg in [10, 60, 100, 119, 121, 140, 170, 180, -100, -150, 2*180/7+180, 180-360/7, 180-360/14]:
    th=math.radians(deg); t=cmath.exp(1j*th)
    s1=[[-t,1],[0,1]]; s2=[[1,0],[t,-t]]
    x=nullvec(residual_rows([s1,s2])); a,c,br,bi=x
    det=a*c-(br*br+bi*bi)
    sig = "definite" if det>1e-9 else ("(1,1)" if det<-1e-9 else "degenerate")
    print("theta=%8.3f deg  1+2cos(theta)=%+.4f  invariant form: %s" % (deg, 1+2*math.cos(th), sig))
