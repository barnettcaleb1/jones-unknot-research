# Independent check of the Section 7 data of BBB (pp. 26-27), transcribed from the page images.
# Each polynomial is the paper's UNSIMPLIFIED Moody polynomial: list of (sign, exponent) in order along beta.
from fractions import Fraction as F

def simplify(terms):
    d = {}
    for s, e in terms:
        d[e] = d.get(e, 0) + s
    return {e: c for e, c in d.items() if c != 0}

def ev(d, t):
    return sum(F(c) * F(t) ** e for e, c in d.items())

data = {
    # p.26: M_Phi = t^0 + t^2 + t^4 - t^3 - t + t^-3 + t^-1 + t  = 1 + t^2 + t^4 - t^3 + t^-3 + t^-1
    "M_Phi (paper: no parity)": ([(1,0),(1,2),(1,4),(-1,3),(-1,1),(1,-3),(1,-1),(1,1)],
                                 {0:1,2:1,4:1,3:-1,-3:1,-1:1}),
    # p.26: M_{Phi.Gamma} = t^0 + t^2 + t^4 - t^3 - t + t^-4 + t^-2 + t^0 = 2 + t^2 + t^4 - t^3 - t + t^-4 + t^-2
    "M_PhiGamma (paper: parity)": ([(1,0),(1,2),(1,4),(-1,3),(-1,1),(1,-4),(1,-2),(1,0)],
                                   {0:2,2:1,4:1,3:-1,1:-1,-4:1,-2:1}),
    # p.27: M_Gamma, 20 terms, = 2t^-3 - 3t^-2 + 4t^-1 - 5 + 3t - 2t^2 + t^3
    "M_Gamma (paper: parity)": ([(-1,0),(-1,2),(1,1),(1,-1),(-1,0),(-1,2),(1,3),(1,1),(1,-1),(-1,-2),
                                 (-1,0),(1,-1),(1,-3),(-1,-2),(-1,0),(1,1),(1,-1),(1,-3),(-1,-2),(-1,0)],
                                {-3:2,-2:-3,-1:4,0:-5,1:3,2:-2,3:1}),
    # p.6, Fig 3.1(b) (B_3, all 3-braids satisfy parity): W = 1,1,-1,-2,1 ; M = 2 - 2t + t^2 - t^-1
    "Fig3.1b": ([(1,0),(-1,1),(1,2),(-1,1),(-1,-1),(1,0)], {0:2,1:-2,2:1,-1:-1}),
}
for name, (terms, printed_simpl) in data.items():
    simp = simplify(terms)
    W = [terms[i+1][1] - terms[i][1] for i in range(len(terms)-1)]
    parity_ok = all((terms[i][0] != terms[i+1][0]) == (W[i] % 2 != 0) for i in range(len(W)))
    shadow = {s * (-1) ** (e % 2) for s, e in terms}
    print(f"{name}:")
    print(f"   #terms m = {len(terms)}, sum|coeff| of simplified = {sum(abs(c) for c in simp.values())}")
    print(f"   simplified matches paper's printed form: {simp == printed_simpl}")
    print(f"   M(-1) from unsimplified = {ev(simplify(terms), -1)}, from paper's simplified = {ev(printed_simpl, -1)}")
    print(f"   W (= k_(i+1)-k_i) = {W}")
    print(f"   sign change iff |W_i| odd at every step: {parity_ok};  eps_i*(-1)^k_i constant: {len(shadow)==1}")
    print(f"   M(1) = {ev(printed_simpl, 1)}")
