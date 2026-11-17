# Eliahou–Fromentin: modular depth versus Jones Taylor depth

17 November 2026. Bounded primary-source audit for the cross-field proposal. No search or reconstruction of knot diagrams was run. The derivative calculation below is a hand deduction from the printed bracket pair, not a claim that the paper states it.

## Source facts and corrections

Primary source: Eliahou–Fromentin, *A remarkable 20-crossing tangle*, [arXiv:1610.05560v2](https://arxiv.org/pdf/1610.05560v2), Definitions 3.1–3.2, Proposition 3.3, Lemma 4.2, Proposition 4.3, Lemma 5.1, Proposition 5.2 and Theorem 5.3.

Source receipt, 17 November: root and an independent source reader compared the transcription directly with v2. All fourteen T10 terms agree with printed p. 5, proof of Lemma 4.2. Definitions 3.1–3.2 (pp. 3–4) fix the mirror, recursion and closure. Proposition 4.1 (p. 5) gives the composition rules. Lemma 5.1 (pp. 6–7) and Proposition 5.2 (pp. 7–8) fix writhe +1 and chi=f_r+A^-6 g_r; p. 7 gives A=t^-1/4. No discrepancy was found. This closes the source qualification in Claude131643 without claiming a new independent reconstruction of the diagrams.

The paper constructs nontrivial, pairwise distinct knots with Jones polynomial congruent to 1 coefficientwise modulo arbitrarily high powers of two. It does **not** prove these knots prime. Its displayed diagram has `20*2^(r-1)+1` crossings; Proposition 3.3 states an upper bound on crossing number, not minimality. Nontriviality and distinctness follow from an explicit nonconstant leading term, not a prime-decomposition theorem. No first nonzero Jones Taylor coefficient is stated.

This construction was already recorded on 3 November in `work/global_design/finite_barrier.md`. Reproduction would be an implementation/normalization check, not discovery of the modular barrier.

## Exact marked formulas

Write A for the paper's bracket variable, reserving t for ordinary Jones, and put `delta=-A^2-A^-2`. The printed T10 pair is

```
f = 2 A^-10 - 2 A^-6 + 2 A^-2 - 2 A^6
    + 2 A^10 - 2 A^14 + A^18,
g = 2 A^-8 - 5 A^-4 + 7 - 7 A^4
    + 5 A^8 - 3 A^12 + A^16.
```

For `T20=T10+(-T10)`, where the minus means crossing mirror, set

```
F = f(A) f(A^-1),
G = f(A) g(A^-1) + g(A) f(A^-1)
    + delta g(A) g(A^-1).
```

The paper's recursive tangle Mr has `2^(r-1)` horizontal copies of T20. If its pair is `(f_r,g_r)`, then

```
(f_1,g_1)=(F,G),
f_(r+1)=f_r^2,
g_(r+1)=2 f_r g_r + delta g_r^2.
```

The knot is `K_r=den(1*Mr)`. This is a literal marked closure, not an unspecified polynomial normalization. Since `br(1)=(A,A^-1)`, vertical composition and denominator closure give

```
br(1*Mr)=(delta A f_r + A g_r + A^-1 f_r, A^-1 g_r),
<K_r>=-A^3 f_r-A^-3 g_r.
```

The combined seed T20=T10+(-T10) has writhe zero and horizontal sums preserve it; this does not assert writhe zero for either T10 summand separately. The extra closure crossing has writhe +1. Thus the normalized bracket is exactly

```
chi(K_r)=f_r+A^-6 g_r,
V_Kr(t)=chi(K_r)|_(A=t^-1/4).
```

There is no framing unit fitted from samples or inferred from V'(1)=0.

## New hand deduction: the Taylor order stays exactly four

Put `A=exp(x)` and let a superscript in this section mean differentiation in x at zero. From the displayed coefficients, the derivative tuples through order four are

| order j | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| f^(j) | 1 | -14 | 196 | 328 | 62992 |
| g^(j) | 0 | -4 | 80 | 320 | 28928 |

Both F and G are even in x. Their constant terms are F(0)=1, G(0)=0. Their second derivatives vanish:

```
F'' = 2 f'' - 2(f')^2 = 392-392=0,
G'' = 2 g'' - 4 f'g' - 2 delta(0)(g')^2
    = 160-224+64=0.
```

For the fourth derivatives, with `delta(0)=-2` and `delta''(0)=-8`,

```
F'''' = 2 f'''' - 8 f'f''' + 6(f'')^2
      = 393216,

G'''' = [2g'''' - 8f'g''' + 12f''g'' - 8f'''g']
      + delta(0)[-8g'g''' + 6(g'')^2]
      + 6 delta''(0)[-2(g')^2]
      = 292352 - 97280 + 1536
      = 196608.
```

Therefore

```
F(exp(x))=1+16384 x^4+O(x^6),
G(exp(x))=8192 x^4+O(x^6).
```

The doubling recurrence multiplies both displayed fourth-order coefficients by two at each stage, since the quadratic defect terms start at order eight. Consequently

```
chi(K_r)(exp(x))
  =1+24576 * 2^(r-1) x^4+O(x^5).
```

Substituting `x=-h/4` gives the precise ordinary-Jones consequence

```
V_Kr(exp(h)) = 1 + 96 * 2^(r-1) h^4 + O(h^5).
```

Thus `ord_(t=1)(V_Kr-1)=4` for **every** r. The increasing 2-adic divisibility does not increase this Taylor order. Root independently verified the seed jets and doubling law by exact rational arithmetic in `work/theory_restart/referee_checks/ef_depth.py`; this was a fixed certificate check, not a scan. The all-r statement follows from the displayed induction, not finitely many samples. Status: PROVED under the collaboration protocol after Claude131643 checked the arithmetic and induction, and the source receipt above closed his transcription/framing qualification. No external specialist review or novelty claim is asserted; the primary paper's theorem does not depend on this deduction.

## Relation to the uniform depth bound

The banked bound for `V-1=N D`, D integral, gives Taylor order at least

```
log(|N|/2) / log(16n).
```

For EF, one may take `N=2^r` and the displayed `n=20*2^(r-1)+1`. Numerator and denominator in that lower bound are both linear in r asymptotically, so it imposes only a constant lower bound. The exact order-four calculation is entirely consistent.

This is the right control for proposed complexity gadgets: coefficientwise congruence is not perturbative vanishing. EF pays exponentially many displayed crossings for r bits of 2-adic divisibility. It does not provide a polynomial-size value-preserving counting encoding, nor a counterexample to its required increasing Taylor depth. Conversely, the modular construction does not invalidate a proposed theorem merely because that theorem uses some fixed initial Taylor coefficient in addition to modular data.

## A bounded reproduction certificate, if Caleb chooses it

One seed certificate and the printed induction suffice; generating large K_r is unnecessary.

1. Encode the literal construction of T10 from ±1, horizontal and vertical composition, with explicit endpoint pairing and crossing chirality.
2. Recompute its full pair independently and match the two displayed polynomials; take the mirror and the horizontal product to certify `br(T20)=(1,0) mod 2`.
3. Verify the closure marking and writhe +1, yielding `chi=f_r+A^-6 g_r` exactly.
4. Verify the algebraic doubling identity and its mod-2-power induction symbolically. Track the leading term to certify nontriviality for every r and the component pairing to certify knots.
5. As a compact normalization regression, check the derivative table and the `96*2^(r-1)` coefficient. Do not attach a primality claim or minimum crossing number without a separate certificate.

## Existing EKT screen to reuse

`work/theory_restart/ekt_control_referee.md` and `work/ekt_homology_notes.md` already record

```
H1(Sigma2 LL2(n)) = Z + Z/(1+12 q_n^2),
q_0=0, q_1=1, q_2=6.
```

LL2(1) is only a monomial-shifted unlink polynomial, so it is not an exact JT2 input. Even n gives the exact unlink polynomial; LL2(2) already has torsion Z/433 and is excluded from the coherent-band-to-unknot class by the banked homology test. Repeating that test is not a new experiment. Any broader screen should identify the previously unexamined family and retain the normalized polynomial, not raw bracket, as its entrance condition.
