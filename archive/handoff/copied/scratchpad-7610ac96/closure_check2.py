import cmath, random
random.seed(1)
ok=True
for trial in range(5):
    A=cmath.exp(1j*random.uniform(0.1,3.0))*random.uniform(0.7,1.3)
    d=-A**2-A**-2
    D=lambda y,x: y*d+x*d**2      # D(b)=1 circle, D(c)=2 circles
    N=lambda y,x: y*d**2+x*d      # N(b)=2 circles, N(c)=1 circle
    y=complex(random.random(),random.random()); u=complex(random.random(),random.random())
    x=(u-y)/d                     # forced by D(T)=u*d
    ok &= abs(D(y,x)-u*d)<1e-9
    ok &= abs(N(y,x)-((d*d-1)*y+u))<1e-9          # N(T) = (d^2-1) J + u
    # both closures trivial with same unit => y=u, x=0  (linear system)
    # solve [[d,d^2],[d^2,d]] [y,x] = [u d, u d^2]
    det=d*d-d**4; ys=(u*d*d - d*d*u*d*d)/det; xs=(d*u*d*d - d*d*u*d)/det
    ok &= abs(ys-u)<1e-9 and abs(xs)<1e-9
    # integral tangle [2]: sigma = A b + A^-1 c ; b neutral, c*c=d c
    y1,x1=A,1/A
    y2,x2=y1*y1, y1*x1+x1*y1+d*x1*x1
    ok &= abs(D(y2,x2)-d*A**-6)<1e-9              # unknot with writhe 2: (-A^3)^-2 d
    ok &= abs(N(y2,x2)-d*(-A**4-A**-4))<1e-9      # Hopf link
print("all identities hold:",ok)
A=cmath.exp(1j*cmath.pi/4); print("delta at A=e^{i pi/4}:",abs(-A**2-A**-2))
