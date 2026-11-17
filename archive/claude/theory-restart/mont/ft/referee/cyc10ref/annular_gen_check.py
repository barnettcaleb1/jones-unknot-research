# Referee spot check (Section 3; needed for the chirality of the T-lift):
# E_-(A_n) = reduced bracket of (colour-1 braid axis U) u (annular closure of sigma_1...sigma_{n-1}, colour 2, type x),
# compared with claimed r_-^(n-1) L_n^-,  r_- = Q^-2,  L_n^- = Q^(2n) - (Q+Q^-1)(-Q^-1)^n,  Q = -A^-4 (lp J convention).
# The type-y closure is compared too, to show the test distinguishes chirality. Pure python, numeric random complex A.
# Quantum trace in this TL rep: Tr_q(M) = Tr(M g^{(x)N}), g = diag(-A^2, -A^-2) (derived from the cup/cap below).
import random, cmath
def local(M4,k,N,v):
    # apply 4x4 M4 on strands k,k+1 (strand 0 = most significant bit) to vector v of length 2^N
    out=[0j]*len(v); sh=N-k-2
    for b in range(len(v)):
        if v[b]==0: continue
        hi=(b>>sh)&3
        base=b&~(3<<sh)
        for r in range(4):
            c=M4[r][hi]
            if c: out[base|(r<<sh)]+=c*v[b]
    return out
def run(A,n,typ):
    d=-A**2-A**-2
    cup=[0,A,-1/A,0]; cap=[0,-A,1/A,0]
    E=[[cup[i]*cap[j] for j in range(4)] for i in range(4)]
    Xx=[[(A if i==j else 0)+E[i][j]/A for j in range(4)] for i in range(4)]
    Xy=[[(1/A if i==j else 0)+E[i][j]*A for j in range(4)] for i in range(4)]   # inverse crossing (A -> A^-1)
    X=Xx if typ=='x' else Xy
    f2=[[(1 if i==j else 0)-E[i][j]/d for j in range(4)] for i in range(4)]
    N=1+2*n
    ops=[]  # applied right-to-left: M = Fp beta Fp W ; list in order of application to a vector
    for k in list(range(N-1))+list(reversed(range(N-1))): ops.append((Xx,k))   # W (applied first)
    for c in range(n): ops.append((f2,1+2*c))
    for s in range(1,n):
        a=2*s-1
        for k in (a+1,a,a+2,a+1): ops.append((X,k))
    for c in range(n): ops.append((f2,1+2*c))
    g=[-A**2,-A**-2]
    tot=0j
    for b in range(2**N):
        v=[0j]*(2**N); v[b]=1
        for M4,k in reversed(ops) if False else ops:
            v=local(M4,k,N,v)
        gb=1
        for i in range(N): gb*=g[(b>>(N-1-i))&1]
        tot+=gb*v[b]
    return tot/d
random.seed(5)
for trial in range(2):
    A=complex(random.uniform(0.6,1.3),random.uniform(0.2,0.9)); Q=-A**-4
    for n in (1,2,3):
        claimed=Q**(-2*(n-1))*(Q**(2*n)-(Q+1/Q)*(-1/Q)**n)
        mirror=Q**(2*(n-1))*(Q**(-2*n)-(Q+1/Q)*(-Q)**n)
        vx=run(A,n,'x'); vy=run(A,n,'y')
        print('A=%.3f%+.3fi n=%d |E(x)-claimed|=%.1e |E(y)-claimed|=%.1e |E(y)-mirror|=%.1e'%(A.real,A.imag,n,abs(vx-claimed),abs(vy-claimed),abs(vy-mirror)))
