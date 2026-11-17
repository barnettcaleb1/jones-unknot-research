"""Finite computation proving the decategorified recursion (Lemma 1 of the report).
V6 = skein module of the disc with boundary points (t; p0,...,p4): 5 crossingless matchings.
M_A = 'y0.y1.y1.y0' (strand 0 makes a full twist with the band (1,2)),  M_B = 'x2.x1.x3.x2' (band (1,2) crosses band (3,4)),
acting by stacking below.  psi_0 = 'r1.r2' (strand 0 and the doubled cap).  Closing: 'u0'.
Functionals on V6:  l0 = <T(inf)> = y + d z,  lJ = y, where after 'u0' the state is y [Q_0] + z [Q_inf].
We verify, with q = A^2, alpha = q^-6, beta = -q^2, omega = 1 - beta^-2, lamA = q^4 (unit of an A-letter), lamB = q^-4:
  lG := (l0 - lJ) / (-q^-6 (1-q^8)),   lGam := (lG M_B)/lamB - beta lG
  l0 M_A = lamA l0,  l0 M_B = lamB l0,
  lG M_A = lamA lG,  lGam M_B = lamB lGam,
  lGam M_A = lamA (alpha lGam + l0 + omega lG),
  lG(psi_0) = lGam(psi_0) = 0.
"""
import sympy as sp, itertools
from tl import run, start, cap, cup, crossing, norm, A, d, Q0, Qinf
q=sp.symbols('q')
# basis of V6: all crossingless matchings of t,b0..b4 : generate by applying things
def matchings(points):
    if not points: yield []; return
    a=points[0]
    for k in range(1,len(points),2):
        b=points[k]
        for m1 in matchings(points[1:k]):
            for m2 in matchings(points[k+1:]):
                yield [(a,b)]+m1+m2
pts=[('t',0)]+[('b',i) for i in range(4,-1,-1)]   # cyclic order around the disc: t, then bottom points right to left
basis=[norm(m) for m in matchings(pts)]
assert len(basis)==5
def apply(word,m):
    st,n=run(word,state=({m:sp.Integer(1)},5))
    return st,n
def matrix(word):
    M=sp.zeros(5,5)
    for j,m in enumerate(basis):
        st,n=apply(word,m); assert n==5
        for mm,c in st.items(): M[basis.index(mm),j]=c
    return M
MA=matrix('y0.y1.y1.y0'); MB=matrix('x2.x1.x3.x2')
MAi=matrix('x0.x1.x1.x0'); MBi=matrix('y2.y1.y3.y2')
assert sp.simplify(MA*MAi-sp.eye(5))==sp.zeros(5,5) and sp.simplify(MB*MBi-sp.eye(5))==sp.zeros(5,5)
# functionals
lJ=sp.zeros(1,5); l0=sp.zeros(1,5)
for j,m in enumerate(basis):
    st,n=apply('u0',m); assert n==3
    y=st.get(Q0,0); z=st.get(Qinf,0)
    lJ[0,j]=y; l0[0,j]=sp.expand(y+d*z)
psi0,_=run('r1.r2'); v0=sp.Matrix([psi0.get(m,0) for m in basis])
S=lambda e: sp.simplify(e.subs(A,sp.sqrt(q)))
MA=MA.applyfunc(S); MB=MB.applyfunc(S); lJ=lJ.applyfunc(S); l0=l0.applyfunc(S); v0=v0.applyfunc(S)
al=q**-6; be=-q**2; om=1-be**-2; lamA=q**4; lamB=q**-4
lG=((l0-lJ)/(-q**-6*(1-q**8))).applyfunc(sp.simplify)
lGam=((lG*MB)/lamB-be*lG).applyfunc(sp.simplify)
Z=lambda M: all(sp.simplify(x)==0 for x in M)
print('l0 MA = lamA l0      :', Z(l0*MA-lamA*l0))
print('l0 MB = lamB l0      :', Z(l0*MB-lamB*l0))
print('lG MA = lamA lG      :', Z(lG*MA-lamA*lG))
print('lGam MB = lamB lGam  :', Z(lGam*MB-lamB*lGam))
print('lGam MA = lamA(al lGam + l0 + om lG):', Z(lGam*MA-lamA*(al*lGam+l0+om*lG)))
print('l0(psi0) =', sp.simplify((l0*v0)[0]), ' lG(psi0) =', sp.simplify((lG*v0)[0]), ' lGam(psi0) =', sp.simplify((lGam*v0)[0]))
print('rank of span(l0,lG,lGam):', sp.Matrix.vstack(l0,lG,lGam).rank())

print('--- restricted to the orbit subspace W ---')
# W = span of the orbit of psi0
vecs=[v0]; W=sp.Matrix.hstack(v0)
changed=True
while changed:
    changed=False
    for M in (MA,MB):
        for i in range(W.shape[1]):
            w=(M*W[:,i]).applyfunc(sp.simplify)
            W2=sp.Matrix.hstack(W,w)
            if W2.rank()>W.rank():
                W=W2; changed=True
print('dim W =',W.shape[1])
# invariance under inverses as well
for M in (MA.inv(),MB.inv()):
    for i in range(W.shape[1]):
        assert sp.Matrix.hstack(W,(M*W[:,i]).applyfunc(sp.simplify)).rank()==W.rank()
R=lambda l: (l*W).applyfunc(sp.simplify)       # restriction of a functional to W (coordinates in the basis W)
def find(lamAs,lamBs):
    for lamA in lamAs:
        for lamB in lamBs:
            if Z(R(l0*MA)-lamA*R(l0)) and Z(R(l0*MB)-lamB*R(l0)): return lamA,lamB
lamA,lamB=find([q**k for k in range(-12,13)],[q**k for k in range(-12,13)])
print('lamA =',lamA,' lamB =',lamB)
lGam=((lG*MB)/lamB-be*lG)
print('lG MA = lamA lG      :', Z(R(lG*MA)-lamA*R(lG)))
print('lGam MB = lamB lGam  :', Z(R(lGam*MB)-lamB*R(lGam)))
print('lGam MA = lamA(al lGam + l0 + om lG):', Z(R(lGam*MA)-lamA*(al*R(lGam)+R(l0)+om*R(lG))))
print('l0(psi0) =', sp.simplify((l0*v0)[0]), ' lG(psi0) =', sp.simplify((lG*v0)[0]), ' lGam(psi0) =', sp.simplify((lGam*v0)[0]))
print('rank of (l0,lG,lGam) on W:', sp.Matrix.vstack(R(l0),R(lG),R(lGam)).rank())

print('--- correct normalisation: raw eigenvalues q^4 (A), q^-4 (B) on the two-dimensional sector ---')
c2=q**2/(1+q**2+q**4)
lg=((q**4*(lJ*MB)-be*lJ)/(1-be))
print('lJ MA = q^4 lJ                          :', Z(R(lJ*MA)-q**4*R(lJ)))
print('lg MB = q^-4 lg                         :', Z(R(lg*MB)-q**-4*R(lg)))
print('lg MA = q^4 (al lg + (1-al) c2 lJ)      :', Z(R(lg*MA)-q**4*(al*R(lg)+(1-al)*c2*R(lJ))))
print('lJ(psi0) =', sp.simplify((lJ*v0)[0]), ' lg(psi0) =', sp.simplify((lg*v0)[0]), ' l0(psi0)=',sp.simplify((l0*v0)[0]))
print('l0 invariant: ', Z(R(l0*MA)-R(l0)), Z(R(l0*MB)-R(l0)))
