# Sanity check (my computation, not from a source):
#   |J_{r/s}(zeta)| = 2 sin(pi/d) * cosh( dist(S.Q, gamma.Q)/2 ),  zeta = e^{2 pi i/d}, d >= 7,
# where J = q R + (1-q) S is the normalised Jones polynomial of the two-bridge link of slope r/s = gamma(infinity),
# R_q = [[q,1],[0,1]], S_q = [[0,-1/q],[1,0]] (q-deformed modular group), Q = point of the disc fixed by R_q (vector e_1).
import cmath, math, random
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def inv(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]; return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def herm(H,x,y): return sum(x[i].conjugate()*H[i][j]*y[j] for i in range(2) for j in range(2))
random.seed(1)
for d in [7, 9, 14]:
    q=cmath.exp(2j*math.pi/d)
    R=[[q,1],[0,1]]; S=[[0,-1/q],[1,0]]
    # invariant Hermitian form: eigenvectors of R are e1 and v2=(1,1-q) (fixed point 1/(1-q)); H makes them orthogonal.
    # H = [[a,b],[conj b,c]] with <e1,v2>=0 -> a + b(1-q) = 0 ; fix a = -1, then solve c from S-invariance numerically.
    a=-1.0; b=1/(1-q)
    # S-invariance: <S e1, S e1> = <e1,e1> up to |det| normalisation; S e1 = (0,1), det S = 1/q (unit modulus) -> c = a
    # check invariance of H under R and S (up to nothing, since |det|=1):
    c=a
    H=[[a,b],[b.conjugate(),c]]
    def chk(A):
        return max(abs(herm(H,[A[0][j],A[1][j]],[A[0][k],A[1][k]])-H[j][k]) for j in range(2) for k in range(2))
    assert chk(R)<1e-9 and chk(S)<1e-9, (chk(R),chk(S))
    e1=[1,0]; x=[S[0][0],S[1][0]]   # S e1
    worst=0
    for trial in range(200):
        M=[[1,0],[0,1]]
        for _ in range(random.randint(1,12)):
            M=mul(M, random.choice([R,S,inv(R)]))
        y=[M[0][0],M[1][0]]
        J=q*y[0]+(1-q)*y[1]
        ch2=abs(herm(H,x,y))**2/(herm(H,x,x).real*herm(H,y,y).real)
        worst=max(worst, abs(abs(J)-2*math.sin(math.pi/d)*math.sqrt(ch2)))
    print("d=%d: signature det(H)=%.4f (<0 means (1,1)); max deviation of |J| from 2 sin(pi/d) cosh(dist/2): %.2e" % (d, (a*c-abs(b)**2), worst))
