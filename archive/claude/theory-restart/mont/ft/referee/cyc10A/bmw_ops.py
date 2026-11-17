"""Lens A (1): operator-level Dubrovnik/BMW checks, built only from the Kauffman-bracket TL representation.
Type-x crossing = A*1 + A^-1*e (the letter x of kauffman.py / flat_search.py). Original: t = A^4, Q = -A^-4.
Cover: bracket variable a with a^2 = Q. Everything exact (sympy)."""
import sympy as S
A, a, Q = S.symbols('A a Q', nonzero=True)
res = {}
def chk(name, cond):
    res[name] = bool(cond); print(('PASS ' if cond else 'FAIL ') + name)
def zero(M): return all(S.simplify(x) == 0 for x in M)

def TLrep(var, n):
    """e_i on (C^2)^{otimes n}, standard U_q(sl2) TL rep with loop value -var^2-var^-2."""
    e = S.zeros(4)
    e[1,1] = -var**2; e[1,2] = 1; e[2,1] = 1; e[2,2] = -var**-2
    def at(i):  # e acting on factors i,i+1 (0-based)
        return S.kronecker_product(S.kronecker_product(S.eye(2**i), e), S.eye(2**(n-i-2)))
    return [at(i) for i in range(n-1)]

# ---- sanity of the TL rep
d0 = -A**2 - A**-2
E3 = TLrep(A, 3)
chk('TL: e^2 = delta e', zero(E3[0]*E3[0] - d0*E3[0]))
chk('TL: e1 e2 e1 = e1', zero(E3[0]*E3[1]*E3[0] - E3[0]))
chk('TL: e2 e1 e2 = e2', zero(E3[1]*E3[0]*E3[1] - E3[1]))

# ---- ORIGINAL colour-2 theory as 2-cables with f2, on (C^2)^{x4}
n = 4; E = TLrep(A, n); I16 = S.eye(16)
sx = [A*I16 + A**-1*E[i] for i in range(3)]        # type-x crossings sigma_1..3 (0-based 0..2)
sxi = [A**-1*I16 + A*E[i] for i in range(3)]
chk('TL: sigma x inverse', zero(sx[0]*sxi[0] - I16))
f2a = I16 - E[0]/d0; f2b = I16 - E[2]/d0; F = f2a*f2b
X = sx[1]*sx[0]*sx[2]*sx[1]                          # cabled crossing, same pattern as quotient_word
Xi = sxi[1]*sxi[2]*sxi[0]*sxi[1]
chk('cabled crossing inverse', zero(X*Xi - I16))
chk('f2 x f2 commutes with cabled crossing', zero(X*F - F*X))
Eo = F*E[1]*E[0]*E[2]*E[1]*F                         # colour-2 cup-cap (nested), projected
Bo = F*X; Boi = F*Xi
t = A**4; Qo = -A**-4
dm = 1 - Qo - Qo**-1; rm = Qo**-2
chk('orig: E^2 = d_- E with d_- = 1-Q-Q^-1', zero(Eo*Eo - dm*Eo))
chk('orig: B E = Q^2 E  (contraction eigenvalue r_-^-1)', zero(Bo*Eo - Qo**2*Eo))
chk('orig: E B = Q^2 E', zero(Eo*Bo - Qo**2*Eo))
chk('orig: Dubrovnik B - B^-1 = (Q-Q^-1)(F - E)', zero(Bo - Boi - (Qo - Qo**-1)*(F - Eo)))
# eigenvalues of B_orig on the 9-dim image of F: minimal polynomial check
lam = S.symbols('lam')
mp = (Bo - Qo**2*F)*(Bo - Qo*F)*(Bo + Qo**-1*F)
chk('orig: (B-Q^2)(B-Q)(B+Q^-1) = 0 on V2xV2', zero(mp))
rk = lambda M: M.subs(A, S.Rational(3,2)).rank()
chk('orig: channel ranks 1,3,5', [rk((Bo - Qo*F)*(Bo + Qo**-1*F)), rk((Bo - Qo**2*F)*(Bo + Qo**-1*F)), rk((Bo - Qo**2*F)*(Bo - Qo*F))] == [1,3,5])

# ---- COVER: folded pair on (U1 x U2) x (U3 x U4), sheetwise crossings on factors (1,3),(2,4)
def e_pair(var, i, j):
    """TL generator acting on tensor factors i<j of (C^2)^{x4} (others identity), via permutation conjugation."""
    e = TLrep(var, 2)[0]
    import itertools
    M = S.zeros(16)
    for col in range(16):
        bits = [(col >> (3-k)) & 1 for k in range(4)]
        sc = 2*bits[i] + bits[j]
        for r in range(4):
            if e[r, sc] != 0:
                nb = bits.copy(); nb[i] = r//2; nb[j] = r % 2
                row = sum(nb[k] << (3-k) for k in range(4))
                M[row, col] += e[r, sc]
    return M
e13 = e_pair(a, 0, 2); e24 = e_pair(a, 1, 3)
s13 = a*I16 + a**-1*e13; s24 = a*I16 + a**-1*e24
s13i = a**-1*I16 + a*e13; s24i = a**-1*I16 + a*e24
BW = s13*s24; BWi = s13i*s24i; EW = e13*e24
dp = (a**2 + a**-2)**2
chk('cover: E_W^2 = d_+ E_W, d_+=(Q+Q^-1)^2', zero(EW*EW - dp*EW))
chk('cover: Dubrovnik B - B^-1 = (a^2-a^-2)(I - E_W)', zero(BW - BWi - (a**2 - a**-2)*(I16 - EW)))
chk('cover: B E_W = a^-6 E_W = Q^-3 E_W', zero(BW*EW - a**-6*EW))
mpc = (BW - a**2*I16)*(BW + a**-2*I16)*(BW - a**-6*I16)
chk('cover: (B-Q)(B+Q^-1)(B-Q^-3)=0', zero(mpc))
rkc = lambda M: M.subs(a, S.Rational(3,2)).rank()
chk('cover: channel ranks 9,6,1', [rkc((BW + a**-2*I16)*(BW - a**-6*I16)), rkc((BW - a**2*I16)*(BW - a**-6*I16)), rkc((BW - a**2*I16)*(BW + a**-2*I16))] == [9,6,1])

# ---- parameter identities (1)
rp = Q**3; rmq = Q**-2; dmq = 1 - Q - Q**-1; dpq = (Q + Q**-1)**2
phi5 = Q**4 + Q**3 + Q**2 + Q + 1
chk('(1a) r_+ - r_- = Q^-2 (Q^5-1)', S.simplify(rp - rmq - Q**-2*(Q**5 - 1)) == 0)
chk('(1b) d_+ - d_- = Q^-2 Phi5', S.simplify(dpq - dmq - Q**-2*phi5) == 0)
chk('consistency d = 1 + (r - r^-1)/(Q-Q^-1) both sides',
    S.simplify(dmq - 1 - (rmq - 1/rmq)/(Q - 1/Q)) == 0 and S.simplify(dpq - 1 - (rp - 1/rp)/(Q - 1/Q)) == 0)
print('ALL PASS' if all(res.values()) else 'SOME FAIL', len(res))
