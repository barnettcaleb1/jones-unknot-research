# Referee: two-bridge mechanism (claim 8), numerically with mpmath at high precision, own code.
# (i) projective characters tr^2/det of TH-2BR rho(X), rho(Y) at t = xi vs 4-plat TL matrices at A (A^-4 = xi^2),
#     for X, Y, XY, XY^-1 and also longer words; irreducibility. (ii) matrix-element identity
#     e1^T rho_J(W)(xi) e1 = (-A^-3)^{#y0-#x0} A^{6(#x1-#y1)} <K_W>(A)   [builder's displayed formula]
#     tested on random words with both possible letter orders; (iii) J(xi) = V_K(xi^2) exactly (via lp.J, rlib.VK).
import random, itertools, mpmath as mp
import rlib, lp, kauffman
mp.mp.dps=40
def mm(P,Q): return [[P[i][0]*Q[0][j]+P[i][1]*Q[1][j] for j in range(2)] for i in range(2)]
def inv(M):
    a,b=M[0]; c,d=M[1]; D=a*d-b*c; return [[d/D,-b/D],[-c/D,a/D]]
def tr(M): return M[0][0]+M[1][1]
def det(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def pch(M): return tr(M)**2/det(M)
def Jmats(t):
    Y=[[1,0],[t**-3,t**-3]]; X=[[1,1-t**4],[0,-t]]
    return {'y0':Y,'x0':inv(Y),'x1':X,'y1':inv(X)}
def Vmats(A):
    d=-A**2-A**-2; I=[[1,0],[0,1]]
    U1=[[d,1],[0,0]]; U2=[[0,0],[1,d]]
    Y2=[[A**-1*I[i][j]+A*U2[i][j] for j in range(2)] for i in range(2)]
    X2=[[A*I[i][j]+A**-1*U2[i][j] for j in range(2)] for i in range(2)]
    X1=[[A*I[i][j]+A**-1*U1[i][j] for j in range(2)] for i in range(2)]
    Y1=[[A**-1*I[i][j]+A*U1[i][j] for j in range(2)] for i in range(2)]
    return {'y0':Y2,'x0':X2,'x1':mm(X1,X1),'y1':mm(Y1,Y1)},d
def prod(mats,W,order):
    M=[[1,0],[0,1]]
    for L in (W if order=='LtoR' else W[::-1]): M=mm(M,mats[L])
    return M
xis=[mp.exp(2j*mp.pi*k/10) for k in (1,3,7,9)]
rnd=random.Random(55)
maxdev=0; irr=[]
for xi in xis:
    for m in range(4):
        A=mp.exp(-1j*(mp.arg(xi**2)+2*mp.pi*m)/4)
        assert abs(A**-4-xi**2)<1e-30
        J=Jmats(xi); V,d=Vmats(A)
        isprim=abs(xi+A**-2)<1e-20 or abs(xi-A**-2)<1e-20
        for W in (['x1'],['y0'],['x1','y0'],['x1','x0'],['x1','y0','x1','x1','x0','y1','y0']):
            dev=abs(pch(prod(J,W,'LtoR'))-pch(prod(V,W,'LtoR')))
            maxdev=max(maxdev,dev)
        C=mm(mm(J['x1'],J['y0']),mm(inv(J['x1']),inv(J['y0'])))
        irr.append(abs(tr(C)-2))
print('max |pchar_J - pchar_V| over xi, A, test words:',mp.nstr(maxdev,5),' min |tr[X,Y]-2| (J side):',mp.nstr(min(irr),5))
# (ii) matrix element identity on random 2-bridge words, both orders
def bracket_at(word,A):
    kb=kauffman.bracket(word); return sum(c*A**e for e,c in kb.items())
res={'LtoR':0,'RtoL':0}; tot=0
for _ in range(60):
    L=rnd.randint(1,12); W=[rnd.choice(['y0','x0','x1','y1']) for _ in range(L)]
    w='s.l1.'+'.'.join(W)+'.u2'
    if lp.J(w) is None: continue
    tot+=1
    xi=xis[rnd.randrange(4)]; s=rnd.choice([1,-1]); A=mp.sqrt(s/xi)      # xi = s A^-2
    assert abs(xi-s*A**-2)<1e-30
    nY=W.count('y0')-W.count('x0'); nX=W.count('x1')-W.count('y1')
    rhs=(-A**-3)**nY*A**(6*nX)*bracket_at(w,A)
    for order in ('LtoR','RtoL'):
        M=prod(Jmats(xi),W,order); lhs=M[0][0]
        if abs(lhs-rhs)<1e-25*max(1,abs(rhs)): res[order]+=1
print('matrix element identity holds (out of %d words): '%tot,res)
# (iii) exact J(xi) = V_K(xi^2): via Phi_5 | J(-t) - V_K(t^2) on all 2-bridge words of length 8 (exhaustive, reduced)
cnt=ok=0
for W in itertools.product(['y0','x0','x1','y1'],repeat=8):
    if any(W[i][1:]==W[i+1][1:] and W[i][0]!=W[i+1][0] for i in range(7)): continue
    w='s.l1.'+'.'.join(W)+'.u2'; J=lp.J(w)
    if J is None: continue
    V=rlib.VK(w); f=rlib.psub(rlib.subst_neg(J),rlib.subst_pow(V,2)); cnt+=1
    if not f or rlib.divmod_laurent(f,rlib.MODD) is not None: ok+=1
print('length-8 two-bridge words: Conjecture D (full modulus) holds',ok,'/',cnt)
