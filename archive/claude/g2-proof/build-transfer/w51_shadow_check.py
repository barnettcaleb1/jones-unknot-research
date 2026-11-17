# Sanity check (one identity): on W(5,1) = W(6,0)|B_5 (Kauffman convention sigma_i -> A + A^-1 e_i),
# at A = exp(i pi/4) (A^4 = -1, the parity/"q=-1" point) the square of the 3|3 twist T_c = (s1 s2)^3
# is the scalar A^-12, while T_c itself and s1 are not scalar.  Basis/table copied from read-model.
import cmath
N = 5
A = cmath.exp(1j*cmath.pi/4); d = -A**2 - A**-2
tab = {1:{1:('d',1),2:('d',2),3:(1,1),4:(1,2),5:(1,1)},
       2:{1:(1,3),2:(1,4),3:('d',3),4:('d',4),5:(1,4)},
       3:{1:('d',1),2:(1,1),3:(1,1),4:(1,5),5:('d',5)},
       4:{1:(1,2),2:('d',2),3:(1,4),4:('d',4),5:(1,4)},
       5:{1:('d',1),2:(1,1),3:('d',3),4:(1,3),5:(1,1)}}
def E(i):
    M = [[0j]*N for _ in range(N)]
    for j, (c, t) in tab[i].items(): M[t-1][j-1] = d if c == 'd' else 1
    return M
def mm(X, Y): return [[sum(X[r][k]*Y[k][c] for k in range(N)) for c in range(N)] for r in range(N)]
I = [[complex(r == c) for c in range(N)] for r in range(N)]
S = {i: [[A*I[r][c] + A**-1*E(i)[r][c] for c in range(N)] for r in range(N)] for i in range(1, 5)}
def word(w):
    M = I
    for g in w: M = mm(M, S[g])
    return M
def scalar_dev(M, s): return max(abs(M[r][c] - (s if r == c else 0)) for r in range(N) for c in range(N))
T = word([1, 2]*3); T2 = mm(T, T)
print("A^4 =", round((A**4).real, 12), "; delta =", abs(d) < 1e-12 and 0)
print("T_c^2 - A^-12 I: max dev", scalar_dev(T2, A**-12))
print("T_c   - A^-6 I : max dev", round(scalar_dev(T, A**-6), 6), "(nonzero: T_c not scalar)")
print("s1    - A I    : max dev", round(scalar_dev(S[1], A), 6), "(nonzero)")
