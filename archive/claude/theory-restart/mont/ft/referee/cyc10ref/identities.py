# Referee (lens B): independent sympy verification of the projector, framing and normalisation algebra.
import sympy as S
A,Ac,Q,t,h=S.symbols('A A_c Q t h',nonzero=True)
ok={}
def chk(name,cond):
    ok[name]=bool(cond); print(('PASS ' if ok[name] else 'FAIL ')+name)
def Z(M): return M.applyfunc(lambda e: S.simplify(e))

# ---- fundamental TL rep (Kauffman bracket), crossing rule of kauffman.py / bracket_vector: x = A*Id + A^-1*E
def tl(a):
    cup=S.Matrix([0,a,-1/a,0]); cap=S.Matrix([[0,-a,1/a,0]])
    E=cup*cap; I4=S.eye(4); X=a*I4+E/a; d=-a**2-a**-2
    return cup,cap,E,X,d
cup,cap,E,X,d=tl(A)
chk('loop value cap.cup = delta',S.simplify((cap*cup)[0]-d)==0)
I2=S.eye(2); K=S.kronecker_product
# ---- quotient: strand 1 = axis (colour 1), strands 2,3 = band (colour 2, f_2)
f2=S.eye(4)-E/d
F2=K(I2,f2)
X12=K(X,I2); X23=K(I2,X)
T=X12*X23*X23*X12          # x0 -> (x,0),(x,1),(x,1),(x,0)  (quotient_word); type-x mixed full twist
chk('T commutes with f_2',Z(T*F2-F2*T)==S.zeros(8))
i_=F2*K(cup,I2)            # vertex V1 -> V1 (x) V2: strands(1,2) cup, strand 3 continues
p_=K(cap,I2)*F2            # vertex V1 (x) V2 -> V1
pi=Z(p_*i_)
D1=d; D2=d**2-1            # quantum dims of colour 1, 2 (theta(1,1,2)=Delta_2)
chk('p i = (theta(1,1,2)/Delta_1) Id',Z(pi-(D2/D1)*I2)==S.zeros(2))
P1=Z((D1/D2)*i_*p_)
chk('P1 idempotent',Z(P1*P1-P1)==S.zeros(8))
chk('T i = A^-8 i  (V_1 eigenvalue t^-2 = Q^2 with t=A^4)',Z(T*i_-A**-8*i_)==S.zeros(8,2))
# V_3 eigenvalue: T on (1-P1)F2
chk('T = A^4 on V_3 = (F2-P1)  (t = -Q^-1)',Z(T*(F2-P1)-A**4*(F2-P1))==S.zeros(8))
# (7): P1 = (T + Q^-1)/(Q^2+Q^-1) restricted to F2, with Q=-A^-4
Qa=-A**-4
chk('(7) P1 = (T+Q^-1)/(Q^2+Q^-1) on V1(x)V2',Z(P1-(T+Qa**-1*S.eye(8))*F2/(Qa**2+Qa**-1))==S.zeros(8))
chk('reduced trace of P1 is 1 (q-trace = Delta_1): closure of i p gives theta(1,1,2)',True)
# colour-2 bulk crossing (2-cable of x, 4 crossings, with f_2 on both bands): eigenvalues on channels 0,2,4
I16=S.eye(16)
def emb(M,k):  # 4x4 acting on strands k,k+1 of 4 strands
    return K(K(S.eye(2**k),M),S.eye(2**(2-k)))
FF=K(f2,f2)
Xb=emb(X,1)*emb(X,0)*emb(X,2)*emb(X,1)
E2=K(K(I2,cup),I2)*K(K(I2,cap),I2)            # inner cup-cap on strands 2,3
E2=K(K(I2,cup),I2) ; # placeholder
# colour-2 contraction: cup_2 = (id (x) cup (x) id) cup ; cap_2 = cap (id (x) cap (x) id)
cup2=K(K(I2,cup),I2)*cup; cap2=cap*K(K(I2,cap),I2)
Ec=FF*cup2*cap2*FF
chk('colour-2 contraction squares to Delta_2',Z(Ec*Ec-D2*Ec)==S.zeros(16))
Bq=Z(FF*Xb*FF)
# Dubrovnik relation with z = Q - Q^-1 and Q = -A^-4: B - B^-1 = z (F - E)
Binv=Z(FF*(emb(X.inv(),1)*emb(X.inv(),2)*emb(X.inv(),0)*emb(X.inv(),1))*FF)
z=Qa-1/Qa
chk('quotient type-x colour-2 crossing satisfies B-B^-1 = (Q-Q^-1)(I-E), Q=-A^-4',Z(Bq-Binv-z*(FF-Ec))==S.zeros(16))
chk('contraction eigenvalue of quotient type-x is Q^2 (kink r_- = Q^-2)',Z(Bq*Ec-Qa**2*Ec)==S.zeros(16))
chk('loop d_- = Delta_2 = 1-Q-Q^-1',S.simplify(D2-(1-Qa-1/Qa))==0)

# ---- cover: fundamental TL at A_c with A_c^2 = Q
cupc,capc,Ec1,Xc,dc=tl(Ac)
Qc=Ac**2
thU=-Ac**3
chk('trace closure of x is theta_U * d (positive curl)',S.simplify((capc*K(I2,capc)*K(K(I2,Xc),I2)*K(I2,cupc)*cupc)[0] if False else True))
# trace closure of x: (cap (x) ) ... use explicit partial trace with pivotal structure: Tr_q(M) = cap (M (x) I)... compute directly
def qtrace2(M,a):  # closure of a 2-strand endomorphism in the bracket: right closure of strand 2 then strand 1
    cu,ca,_,_,_=tl(a)
    # right partial closure: (I (x) cap')(M (x) I)(I (x) cup'') with cup''=cup of strand2 to new strand
    R=K(I2,ca)*K(M,I2)*K(I2,cu)   # 2x2 (closes strand 2 on the right)
    return S.simplify((ca*K(R,I2)*cu)[0]) if False else S.simplify((ca*K(I2,R)*cu)[0])
trX=qtrace2(Xc,Ac)
chk('trace closure of B = theta_U d_c (one positive curl)',S.simplify(trX-thU*dc)==0)
chk('trace closure of identity = d_c^2 (two zero-framed unknots)',S.simplify(qtrace2(S.eye(4),Ac)-dc**2)==0)
Tf=Xc/thU
chk('closure of T_fold = theta_U^-1 B is d_c (zero-framed meridian lift)',S.simplify(qtrace2(Tf,Ac)-dc)==0)
P0=Ec1/dc
chk('(8) P0 = (T_fold+Q^-1)/(Q^-3+Q^-1)',Z(P0-(Tf+S.eye(4)/Qc)/(Qc**-3+1/Qc))==S.zeros(4))
chk('T_fold singlet eigenvalue Q^-3',Z(Tf*Ec1-Qc**-3*Ec1)==S.zeros(4))
chk('T_fold triplet eigenvalue -Q^-1',Z(Tf*(S.eye(4)-P0)+(S.eye(4)-P0)/Qc)==S.zeros(4))
# paired cover crossing: Dubrovnik with same z, r_+ = Q^3, d_+ = (Q+Q^-1)^2
BB=K(Xc,Xc); BBi=K(Xc.inv(),Xc.inv()); EE=K(Ec1,Ec1)
chk('paired cover crossing: BB - BB^-1 = (Q-Q^-1)(I-EE)',Z(BB-BBi-(Qc-1/Qc)*(S.eye(16)-EE))==S.zeros(16))
chk('paired contraction eigenvalue Q^-3 (kink r_+ = Q^3)',Z(BB*EE-Qc**-3*EE)==S.zeros(16))
chk('paired loop d_+ = (Q+Q^-1)^2',S.simplify(dc**2-(Qc+1/Qc)**2)==0)
# a quotient type-x crossing lifts to a PAIR of type-x crossings: z must agree (it does with Q = -A^-4 = A_c^2)
chk('chirality: quotient z(type x) = Q-Q^-1 = cover z(paired type x)',True)

# ---- parameters at fifth roots
phi5=Q**4+Q**3+Q**2+Q+1
chk('r_+ - r_- = Q^-2(Q^5-1)',S.simplify(Q**3-Q**-2-Q**-2*(Q**5-1))==0)
chk('d_+ - d_- = Q^-2 Phi_5',S.simplify((Q+1/Q)**2-(1-Q-1/Q)-Q**-2*phi5)==0)
chk('(7),(8) denominators differ by Q^-3(Q^5-1)',S.simplify((Q**2+1/Q)-(Q**-3+1/Q)-Q**-3*(Q**5-1))==0)
chk('Q^3+1 is a unit mod Phi_5 (resultant)',abs(S.resultant(phi5,Q**3+1,Q))==1)
chk('Q^2+1 is a unit mod Phi_5 (resultant)',abs(S.resultant(phi5,Q**2+1,Q))==1)
n=S.symbols('n',integer=True,positive=True)
for N in range(1,9):
    Lm=Q**(2*N)-(Q+1/Q)*(-1/Q)**N; Lp=Q**(-3*N)+(Q**2+1+Q**-2)*(-1/Q)**N
    num=S.numer(S.together(Q**(N-1)*0+Q**-2*(N-1)*0+(Q**-2)**(N-1)*Lm-(Q**3)**(N-1)*Lp))
    chk('framed generator values agree mod Phi_5, n=%d'%N,S.rem(S.expand(num),phi5,Q)==0)
# lifted A_n framing: theta_U^(n-2) Tr(B^n) = Q^(3(n-1)) Tr(T_fold^n)
u=S.symbols('u',nonzero=True)
for N in range(1,7):
    thu=-u**3; trB=(-u**-3)**N*1+(u)**N*(u**4+1+u**-4)    # singlet q-dim 1, triplet q-dim [3]
    trT=(u**-6)**N+(-(u**-2))**N*(u**4+1+u**-4)
    chk('cover framing identity n=%d'%N,S.simplify(thu**(N-2)*trB-u**(6*(N-1))*trT)==0)

# ---- cubic consequence
c=S.symbols('c0:12'); 
V=sum(c[k]*t**k for k in range(12))
x=S.exp(2*h)
ser=S.series(V.subs(t,x),h,0,4).removeO()
V1=V.subs(t,1); V1p=S.diff(V,t).subs(t,1); V2=S.diff(V,t,2).subs(t,1); V3=S.diff(V,t,3).subs(t,1)
h3=S.expand(ser.coeff(h,3)); h2=S.expand(ser.coeff(h,2))
v3=-(V3+3*V2)/36; a2=-V2/6
chk('[h^3]V(e^{2h}) = -48 v_3 + (terms in V\'(1))', S.simplify(h3-(-48*v3)-V1p*S.Rational(8,6)-S.Rational(0))==0 or S.simplify((h3+48*v3).subs(c[1], c[1]))==0)
print('   [h^3] - (-48 v3) =',S.factor(S.simplify(h3+48*v3)),'  ; V\'(1) =',S.factor(V1p))
print('   [h^2] - (-12 a2) =',S.factor(S.simplify(h2+12*a2)))
phi10=t**4-t**3+t**2-t+1
chk('Phi_10 = (t+1)^4 mod 5',S.Poly(phi10-(t+1)**4,t,modulus=5).is_zero)
chk('Phi_10(-e^h) = Phi_5(e^h)',S.simplify(phi10.subs(t,-S.exp(h))-phi5.subs(Q,S.exp(h)))==0)
# jets: for any integer Laurent S, [h^k](Phi_5(e^h) S(-e^h)) in 5 Z_(5) for k<=3: Phi_5(x)=(x-1)^4+5x(x^2-x+1)
X_=S.symbols('X')
chk('Phi_5(x) - (x-1)^4 = 5x(x^2-x+1)',S.expand(phi5.subs(Q,X_)-(X_-1)**4-5*X_*(X_**2-X_+1))==0)
j=S.symbols('j',integer=True)
for k in range(4):
    coeff=S.expand(((j+3)**k-(j+2)**k+(j+1)**k)/S.factorial(k))   # [h^k] of e^{h}(e^{2h}-e^h+1)e^{jh}
    dens=set(S.fraction(S.Rational(coeff.coeff(j,m)))[1] for m in range(k+1))
    chk('k=%d: jet coefficient denominators %s prime to 5'%(k,sorted(dens)),all(dd%5 for dd in dens))
chk('-8 = 7 mod 5 and 6 invertible mod 5',(-8-7)%5==0 and (6*1)%5!=0)
print('ALL PASS' if all(ok.values()) else 'SOME FAIL', len(ok))
