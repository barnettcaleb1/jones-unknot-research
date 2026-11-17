# Section 7 (p.26-27) unsimplified Moody polynomials, typed from the paper (layout lines 1282, 1305, 1319).
data = {
 "M_Phi (Fig 7.1, no parity)":      "+0 +2 +4 -3 -1 +-3 +-1 +1",
 "M_PhiGamma (Fig 7.3, parity)":    "+0 +2 +4 -3 -1 +-4 +-2 +0",
 "M_Gamma (Fig 7.4, parity)":       "-0 -2 +1 +-1 -0 -2 +3 +1 +-1 --2 -0 +-1 +-3 --2 -0 +1 +-1 +-3 --2 -0",
}
for name, s in data.items():
    terms = [(1 if tok[0] == '+' else -1, int(tok[1:])) for tok in s.split()]
    m = len(terms)
    Mm1 = sum(e * (-1) ** (k % 2) for e, k in terms)
    simp = {}
    for e, k in terms: simp[k] = simp.get(k, 0) + e
    simp = {k: v for k, v in sorted(simp.items()) if v}
    c = [e * (-1) ** (k % 2) for e, k in terms]
    W = [terms[i + 1][1] - terms[i][1] for i in range(m - 1)]
    par = all((terms[i][0] != terms[i + 1][0]) == (W[i] % 2 != 0) for i in range(m - 1))
    print(f"{name}: m={m}, M(-1)={Mm1}, sum|coeff|={sum(abs(v) for v in simp.values())}, "
          f"parity-consistent signs={par}, single c-sign={len(set(c))==1}, simplified={simp}")
