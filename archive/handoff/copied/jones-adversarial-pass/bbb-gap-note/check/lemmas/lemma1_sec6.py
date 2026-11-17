# Checks for the note's Lemma 1 and the Section 6 moment identity.
# Exact integer arithmetic only.  Run: python3 -I lemma1_sec6.py
from fractions import Fraction as F
import random

# ---------- Lemma 1 on the paper's own unsimplified polynomials ----------
# (sign, exponent) in order along beta, transcribed from the paper:
# Fig 3.1(a), Fig 3.1(b) (p.6), Section 7 (pp.26-27).
ex = {
    "Fig3.1a  M=1-t":            [(1, 0), (-1, 1)],
    "Fig3.1b  M=2-2t+t^2-t^-1":   [(1, 0), (-1, 1), (1, 2), (-1, 1), (-1, -1), (1, 0)],
    "Sec7 M_Phi (no parity)":     [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (1, -3), (1, -1), (1, 1)],
    "Sec7 M_PhiGamma":            [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (1, -4), (1, -2), (1, 0)],
    "Sec7 M_Gamma":               [(-1, 0), (-1, 2), (1, 1), (1, -1), (-1, 0), (-1, 2), (1, 3), (1, 1),
                                   (1, -1), (-1, -2), (-1, 0), (1, -1), (1, -3), (-1, -2), (-1, 0),
                                   (1, 1), (1, -1), (1, -3), (-1, -2), (-1, 0)],
}
simplified_claimed = {   # simplified forms printed in the paper, as {exp: coeff}
    "Fig3.1a  M=1-t": {0: 1, 1: -1},
    "Fig3.1b  M=2-2t+t^2-t^-1": {0: 2, 1: -2, 2: 1, -1: -1},
    "Sec7 M_Phi (no parity)": {0: 1, 2: 1, 4: 1, 3: -1, -3: 1, -1: 1},
    "Sec7 M_PhiGamma": {0: 2, 2: 1, 4: 1, 3: -1, 1: -1, -4: 1, -2: 1},
    "Sec7 M_Gamma": {-3: 2, -2: -3, -1: 4, 0: -5, 1: 3, 2: -2, 3: 1},
}
print("== Lemma 1 on the paper's examples ==")
for name, v in ex.items():
    m = len(v)
    W = [v[i + 1][1] - v[i][1] for i in range(m - 1)]           # Lemma 3.1: W_i = k_{i+1}-k_i
    changing = [v[i][0] != v[i + 1][0] for i in range(m - 1)]
    parity = all(changing[i] == (W[i] % 2 != 0) for i in range(m - 1))
    shadow = [e * (-1) ** (k % 2) for e, k in v]                 # eps_i (-1)^{k_i}
    simp = {}
    for e, k in v:
        simp[k] = simp.get(k, 0) + e
    simp = {k: c for k, c in simp.items() if c}
    l1 = sum(abs(c) for c in simp.values())
    Mm1 = sum(c * (-1) ** (k % 2) for k, c in simp.items())
    bad = [i + 1 for i in range(m - 1) if changing[i] != (W[i] % 2 != 0)]
    print(f"{name:28s} m={m:2d} M(-1)={Mm1:4d} L1={l1:2d} parity={parity!s:5s} "
          f"single-sign={len(set(shadow)) == 1!s:5s} violating-disks={bad} W={W}")
    assert simp == simplified_claimed[name], name
    if parity:
        assert len(set(shadow)) == 1 and abs(Mm1) == m == l1

# ---------- the literal statement of Lemma 1 needs the parity representative ----------
# Insert a finger-move bigon (two new consecutive points, same exponent, opposite signs,
# an empty disk between them) into the parity representative of Fig 3.1(b).
v = ex["Fig3.1b  M=2-2t+t^2-t^-1"]
e0, k0 = v[2]
v2 = v[:3] + [(-e0, k0), (e0, k0)] + v[3:]   # q3 -> bigon pair -> continue (W=0 then W=0)
m2 = len(v2)
W2 = [v2[i + 1][1] - v2[i][1] for i in range(m2 - 1)]
ch2 = [v2[i][0] != v2[i + 1][0] for i in range(m2 - 1)]
print("\n== non-minimal representative (one finger move) ==")
print("m =", m2, " M(-1) =", sum(e * (-1) ** (k % 2) for e, k in v2), " W =", W2)
print("disks with W=0 (empty bigons) are sign-changing:", [ch2[i] for i in range(m2 - 1) if W2[i] == 0])
print("parity holds for this representative:", all(ch2[i] == (W2[i] % 2 != 0) for i in range(m2 - 1)))

# ---------- Section 6 identity: M(t) = c p(-t)  =>  M^{(j)}(-1) = c (-1)^j p^{(j)}(1) ----------
def deriv_at(poly, j, x):
    """j-th derivative of Laurent polynomial {exp: coeff} at x (Fraction)."""
    s = F(0)
    for k, c in poly.items():
        ff = 1
        for r in range(j):
            ff *= (k - r)
        s += c * ff * F(x) ** (k - j)
    return s

random.seed(1)
for trial in range(300):
    ks = [random.randint(-6, 6) for _ in range(random.randint(1, 12))]
    c = random.choice((1, -1))
    p = {}
    for k in ks:
        p[k] = p.get(k, 0) + 1
    M = {k: c * (-1) ** (k % 2) * a for k, a in p.items()}      # M(t) = c p(-t)
    for j in range(6):
        assert deriv_at(M, j, -1) == c * (-1) ** j * deriv_at(p, j, 1)
print("\nidentity M^(j)(-1) = c(-1)^j p^(j)(1): verified on 300 random multisets, j<6")

# ---------- normalisation: raw factorial moments are not shift invariant ----------
ks = [0, 1, 2, 1, -1, 0]                     # exponents of Fig 3.1(b)
def fmom(ks, j):
    s = 0
    for k in ks:
        ff = 1
        for r in range(j):
            ff *= (k - r)
        s += ff
    return s
for d in (0, 1, 3):
    sh = [k + d for k in ks]
    print(f"shift d={d}: factorial moments j=0..3 = {[fmom(sh, j) for j in range(4)]}, "
          f"p'(1) mod p(1) = {fmom(sh, 1) % fmom(sh, 0)}")

# ---------- equal low moments, different span (so span is not a bounded-order moment) ----------
# p1 = p2 + (s-1)^(d+1) s^K with the top of (s-1)^(d+1) s^K one past the top of p2:
# power sums of order <= d agree, the spans differ.
from math import comb
for d in (1, 2, 3, 4):
    C = comb(d + 1, (d + 1) // 2) + 1
    p2 = {k: C for k in range(0, d + 2)}               # exponents 0..d+1, each with multiplicity C
    K = 1                                               # (s-1)^(d+1) s^K occupies K..K+d+1 = d+2
    p1 = dict(p2)
    for r in range(d + 2):
        p1[K + r] = p1.get(K + r, 0) + comb(d + 1, r) * (-1) ** (d + 1 - r)
    assert all(v >= 0 for v in p1.values())
    A = [k for k, v in p1.items() for _ in range(v)]; B = [k for k, v in p2.items() for _ in range(v)]
    ps = lambda S, j: sum(x ** j for x in S)
    print(f"d={d}: sizes {len(A)},{len(B)}; power sums j<= {d+1}: "
          f"{[ps(A, j) for j in range(d + 2)]} vs {[ps(B, j) for j in range(d + 2)]}; "
          f"spans {max(A) - min(A)} vs {max(B) - min(B)}")
