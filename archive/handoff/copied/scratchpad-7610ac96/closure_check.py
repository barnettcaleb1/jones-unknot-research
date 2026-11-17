import sympy as sp
A=sp.symbols('A'); y,x,u=sp.symbols('y x u')
d=-A**2-A**-2
# b = 0-tangle (=), c = infinity tangle (||); Conway closures:
# D joins NW-SW, NE-SE: D(b)=1 circle, D(c)=2 circles ; N joins NW-NE, SW-SE: N(b)=2 circles, N(c)=1 circle
D=lambda yy,xx: yy*d+xx*d**2
N=lambda yy,xx: yy*d**2+xx*d
# impose D(T)=u*d (unknot, framing unit u); solve x
xs=sp.solve(sp.Eq(D(y,x),u*d),x)[0]
print("x =",sp.simplify(xs))
print("N(T) =",sp.simplify(sp.expand(N(y,xs))), " ; expected (d^2-1)y+u :", sp.simplify(N(y,xs)-((d**2-1)*y+u))==0)
# if additionally N(T)=u*d^2 (2-comp unlink, same framing unit) then y=u, x=0
sol=sp.solve([sp.Eq(D(y,x),u*d),sp.Eq(N(y,x),u*d**2)],[y,x])
print("both closures trivial ->",sol)
# example: integral tangle [2] = sigma^2 with sigma = A b + A^-1 c, composition: b neutral, c*c = d c
def mult(p,q):
    (y1,x1),(y2,x2)=p,q
    return (sp.expand(y1*y2), sp.expand(y1*x2+x1*y2+d*x1*x2))
s=(A,A**-1); t2=mult(s,s)
print("[2] =",t2, " D([2]) =",sp.factor(D(*t2)), " N([2]) =",sp.factor(N(*t2)))
# t=-1 point: A=exp(i pi/4): d=0
print("delta at A^4=-1:", sp.simplify(d.subs(A,sp.exp(sp.I*sp.pi/4))))
