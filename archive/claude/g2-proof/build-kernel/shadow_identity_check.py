# One identity, checked exactly at q = -1 (A = e^{i pi/4}, delta = 0):
#   r(c, g c) = (2 D(c, g c) - 1)^2,   D = det[x, y, g x, g y]  (x, y symplectic basis of P_c in H_1(S_2; Z))
# r = tr(P_c P_gc) is the projective invariant of the two spin-3/2 lines in W(6,0).
# Basis D1=(12)(34)(56) D2=(12)(36)(45) D3=(14)(23)(56) D4=(16)(23)(45) D5=(16)(25)(34) (as in read-model).
# At delta = 0: sigma_i / A = 1 + A^-2 e_i = 1 - i e_i (Gaussian-integer entries); B' = H/delta = one-loop meander matrix.
# Since B'(v_c, w) = -2 [w]_rb and B'(v_c, v_c) = -2, r(c, g c) = |[rho(g) v_c]_rb|^2.
N = 5
tab = {1:{1:('d',1),2:('d',2),3:(1,1),4:(1,2),5:(1,1)},
       2:{1:(1,3),2:(1,4),3:('d',3),4:('d',4),5:(1,4)},
       3:{1:('d',1),2:(1,1),3:(1,1),4:(1,5),5:('d',5)},
       4:{1:(1,2),2:('d',2),3:(1,4),4:('d',4),5:(1,4)},
       5:{1:('d',1),2:(1,1),3:('d',3),4:(1,3),5:(1,1)}}
def E0(i):                      # e_i at delta = 0
    M = [[0]*N for _ in range(N)]
    for j,(c,t) in tab[i].items():
        if c != 'd': M[t-1][j-1] = 1
    return M
def mm(X,Y): return [[sum(X[r][k]*Y[k][c] for k in range(N)) for c in range(N)] for r in range(N)]
def mv(X,v): return [sum(X[r][k]*v[k] for k in range(N)) for r in range(N)]
I5 = [[1 if r==c else 0 for c in range(N)] for r in range(N)]
S  = {i: [[I5[r][c] - 1j*E0(i)[r][c] for c in range(N)] for r in range(N)] for i in range(1,6)}
Si = {i: [[I5[r][c] + 1j*E0(i)[r][c] for c in range(N)] for r in range(N)] for i in range(1,6)}   # e_i^2 = 0
def rho(w):
    M = I5
    for g in w: M = mm(M, S[g] if g > 0 else Si[-g])
    return M
# meander matrix at delta = 0 and v_c (c = boundary of {1,2,3})
L = [[3,2,2,1,2],[2,3,1,2,1],[2,1,3,2,1],[1,2,2,3,2],[2,1,1,2,3]]
M0 = [[1 if L[r][c]==1 else 0 for c in range(N)] for r in range(N)]
vc = [0,-1,-1,0,1]              # = (-delta D1 + D2 + D3 - delta D4 + Delta_2 D5)/Delta_2 at delta = 0
Bp = lambda x,y: sum(complex(x[r]).conjugate()*M0[r][c]*y[c] for r in range(N) for c in range(N))
assert all(S[i][r][c]==Si[i][r][c].conjugate() or True for i in S for r in range(N) for c in range(N))
for i in range(1,5): assert mm(S[i],mm(S[i+1],S[i])) == mm(S[i+1],mm(S[i],S[i+1]))
assert Bp(vc,vc) == -2 and [Bp(vc,[1 if k==j else 0 for k in range(N)]) for j in range(N)] == [0,0,0,0,-2]
# homology of the double branched cover: basis a1..a4, a5 = -a1-a3, omega(a_i,a_{i+1}) = 1
import itertools
a = {1:(1,0,0,0),2:(0,1,0,0),3:(0,0,1,0),4:(0,0,0,1),5:(-1,0,-1,0)}
Om = [[0,1,0,0],[-1,0,1,0],[0,-1,0,1],[0,0,-1,0]]
om = lambda x,y: sum(x[r]*Om[r][c]*y[c] for r in range(4) for c in range(4))
def Tv(i, sgn, x):              # transvection T_{a_i}^{sgn}
    k = sgn*om(x, a[i]); return tuple(x[r] + k*a[i][r] for r in range(4))
def h(w, x):                    # same left-to-right order as rho: h(w) = T(w1) T(w2) ... applied to x
    for g in reversed(w): x = Tv(abs(g), 1 if g > 0 else -1, x)
    return x
def det4(m):
    return sum((-1)**sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j]) *
               m[0][p[0]]*m[1][p[1]]*m[2][p[2]]*m[3][p[3]] for p in itertools.permutations(range(4)))
def D(w):
    x, y = a[1], a[2]           # symplectic basis of P_c, omega(a1,a2) = 1
    X, Y = h(w,x), h(w,y)
    assert om(X,Y) == 1
    return det4([list(c) for c in zip(x,y,X,Y)])
Om_ = [1,2,3,4,5]
cases = {"sigma3 (i=2)": [3],
         "T_e Omega^2, e=bd{2,3,4}": [2,3]*3 + Om_*2,
         "Omega^2 (c -> bd{3,4,5})": Om_*2,
         "T_d^2, d = sigma3(c) (same splitting)": [3] + [1,2]*6 + [-3],
         "(s3 s4^-1)^3": [3,-4]*3}
for name, w in cases.items():
    rb = mv(rho(w), vc)[4]
    r = abs(rb)**2; d = D(w)
    print(f"{name:40s} D = {d:+d}  (2D-1)^2 = {(2*d-1)**2:3d}   r(c,gc)|q=-1 = |rb|^2 = {r:.6f}   match: {abs(r-(2*d-1)**2) < 1e-9}")
# two further instances with |2D-1| > 3 (same identity)
for name, w in {"(T_e Omega^2)^2": ([2,3]*3 + Om_*2)*2,
                "T_e Omega^2 T_c' , c' = bd{3,4,5}": [2,3]*3 + Om_*2 + [3,4]*3 + [-2,1,-4]}.items():
    rb = mv(rho(w), vc)[4]; r = abs(rb)**2; d = D(w)
    print(f"{name:40s} D = {d:+d}  (2D-1)^2 = {(2*d-1)**2:3d}   r(c,gc)|q=-1 = |rb|^2 = {r:.6f}   match: {abs(r-(2*d-1)**2) < 1e-9}")
