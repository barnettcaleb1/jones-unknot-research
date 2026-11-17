# Two-bridge mechanism for the Phi_5 identity. J side: TH-2BR rho(Y) (y0), rho(X) (x1) at t = xi (primitive 10th root).
# V side: 4-plat s.l1.W.u2 in the 2-dim matching space {a=(12)(34), b=(14)(23)}: y0 -> Y_2 = A^-1 + A U_2, x1 -> X_1 X_3 = (A + A^-1 U_1)^2,
# start vector a = (1,0), final pairing (1, delta); V-parameter A with A^-4 = xi^2.
# (1) check the V-side model against kauffman.bracket on random 2-bridge words; (2) compare projective characters.
import cmath, random, itertools
import clib, lp, kauffman
def mat_mul(P,Q): return [[sum(P[i][k]*Q[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def Vside(A):
    d=-A**2-A**-2
    U1=[[d,1],[0,0]]; U2=[[0,0],[1,d]]
    I=[[1,0],[0,1]]
    Y2=[[A**-1*I[i][j]+A*U2[i][j] for j in range(2)] for i in range(2)]
    X1=[[A*I[i][j]+A**-1*U1[i][j] for j in range(2)] for i in range(2)]
    X13=mat_mul(X1,X1)
    return {'y0':Y2,'x1':X13,'x0':inv(Y2) if False else None,'d':d}
def inv(M):
    a,b=M[0]; c,d=M[1]; D=a*d-b*c
    return [[d/D,-b/D],[-c/D,a/D]]
def Vbracket_model(word,A):
    S=Vside(A); Yi=inv(S['y0']); Xi=inv(S['x1'])
    # crossing letters: y0, x0 (= mirror of y0 crossing: X_2 = A + A^-1 U_2), x1, y1 (= Y_1 Y_3)
    d=S['d']; I=[[1,0],[0,1]]
    U1=[[d,1],[0,0]]; U2=[[0,0],[1,d]]
    X2=[[A*I[i][j]+A**-1*U2[i][j] for j in range(2)] for i in range(2)]
    Y1=[[A**-1*I[i][j]+A*U1[i][j] for j in range(2)] for i in range(2)]
    M={'y0':S['y0'],'x0':X2,'x1':S['x1'],'y1':mat_mul(Y1,Y1)}
    v=[1,0]
    for L in word.split('.')[2:-1]:
        m=M[L]; v=[m[0][0]*v[0]+m[0][1]*v[1], m[1][0]*v[0]+m[1][1]*v[1]]
    return v[0]+d*v[1]
# (1) model check
rnd=random.Random(3); ok=0; tot=0
for _ in range(40):
    W=[rnd.choice(['y0','x0','x1','y1']) for _ in range(rnd.randint(1,7))]
    w='s.l1.'+'.'.join(W)+'.u2'
    kb=kauffman.bracket(w)
    if kb is None: continue
    A=cmath.exp(0.37j)+0.1
    val=sum(c*A**e for e,c in kb.items()); mod=Vbracket_model(w,A)
    tot+=1; ok+= abs(val-mod)<1e-8*max(1,abs(val))
print('V-side 2x2 model matches kauffman.bracket:',ok,'/',tot)
# (2) projective characters at t = xi (J) vs A_V^-4 = xi^2 (V)
def Jside(t):
    return {'y0':[[1,0],[t**-3,t**-3]],'x1':[[1,1-t**4],[0,-t]]}
def pchar(M): 
    tr=M[0][0]+M[1][1]; det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return tr*tr/det
for k in (1,3,7,9):
    xi=cmath.exp(2j*cmath.pi*k/10)
    for AV in [cmath.exp(-1j*(cmath.phase(xi**2)+2*cmath.pi*m)/4) for m in range(4)]:
        assert abs(AV**-4-xi**2)<1e-9
        J=Jside(xi); V=Vside(AV)
        words=['y0','x1','y0.x1','y0.y0.x1','y0.x1.x1','y0.x1.y0.x1.x1']
        res=[]
        for wd in words:
            MJ=[[1,0],[0,1]]; MV=[[1,0],[0,1]]
            for L in wd.split('.'):
                MJ=mat_mul(J[L],MJ); MV=mat_mul(V[L],MV)
            res.append(abs(pchar(MJ)-pchar(MV))<1e-9)
        print('xi=e^(2pi i %d/10), A_V=%s: projective characters equal on test words:'%(k,str(round(cmath.phase(AV),3))),res)
