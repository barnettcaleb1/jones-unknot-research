# Exact check: projective characters tr^2/det of TH-2BR rho at t = xi and the 4-plat TL rep at A (A^-4 = xi^2), with xi = s A^-2,
# agree on X, Y, XY modulo A^10 + s (i.e. xi^5 = -1). Also irreducibility (commutator trace != 2) and boundary eigen-data.
import sympy as sp
A=sp.symbols('A')
for s in (1,-1):
    xi=s*A**-2
    d=-A**2-A**-2
    YJ=sp.Matrix([[1,0],[xi**-3,xi**-3]]); XJ=sp.Matrix([[1,1-xi**4],[0,-xi]])
    U1=sp.Matrix([[d,1],[0,0]]); U2=sp.Matrix([[0,0],[1,d]]); I=sp.eye(2)
    YV=A**-1*I+A*U2; XV=(A*I+A**-1*U1)**2
    def pch(M): return sp.together(M.trace()**2/M.det())
    ok=[]
    for nm,(MJ,MV) in {'X':(XJ,XV),'Y':(YJ,YV),'XY':(XJ*YJ,XV*YV),'XYinv':(XJ*YJ.inv(),XV*YV.inv())}.items():
        diff=sp.together(pch(MJ)-pch(MV))
        num=sp.numer(diff)
        r=sp.rem(sp.Poly(sp.expand(num*A**200),A),sp.Poly(A**10+s,A))
        ok.append((nm, r.is_zero))
    # irreducibility: tr(X Y X^-1 Y^-1) != 2 generically mod A^10+s
    com=XJ*YJ*XJ.inv()*YJ.inv()
    trc=sp.together(com.trace()-2)
    print('s=%d:'%s, ok, ' tr[X,Y]-2 (J side) =',sp.factor(trc))
