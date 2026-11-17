# Bounded audit of the annular coefficient ring and preferred framing

16 November 2026. Scope: Sections 2 and 6 of `degree3_cyclotomic_comparison.md`. This audit assumes that the raw folded evaluation and the marked vertex replacement are the topological evaluations asserted in Sections 4–5. It does not independently re-prove those identifications.

## Verdict

The coefficient-ring and preferred-framing steps work. No division by `Q-Q^{-1}` is necessary in annular generation. Two wording repairs make the normalization argument noncircular: derive integer monomial exponents from rationality in `Q`, and derive the common constant sign from the integral congruence rather than choosing signs independently.

## 1. An adequate coefficient ring

Use the Laurent ring `Z_(5)[Q,Q^{-1}]`, allowing the two boundary denominators

\[
D_-=Q^2+Q^{-1}=Q^{-1}(Q^3+1),\qquad
D_+=Q^{-3}+Q^{-1}=Q^{-3}(Q^2+1).
\]

Both have value 2 at `Q=1`. Thus their inverses belong to the local ring of functions regular at `Q=1` over `Z_(5)`. Both are also invertible at every primitive fifth root: `1+zeta_5^j` is a cyclotomic unit for `j=2,3`.

The annular generation argument does not introduce other nonunit denominators. To change a crossing, use

\[
B=B^{-1}+(Q-Q^{-1})(I-E)
\]

or its reverse. This **multiplies** smoothing terms by `Q-Q^{-1}`. The standard induction reduces the number of bad crossings of the unchanged-crossing-number term, while the smoothing terms have fewer crossings. Removing curls uses powers of the invertible twist parameter `r`; removing a contractible circle multiplies by `d`. Neither step divides by `Q-Q^{-1}`, by `d`, or by a quantum integer. The descending representatives give the positive winding generators with framing factors. Therefore only integral spanning, rather than any semisimple idempotent expansion, is being used.

The parameter differences

\[
r_+-r_-=Q^{-2}(Q^5-1),\qquad
d_+-d_-=Q^{-2}\Phi_5(Q)
\]

and the all-winding trace differences are divisible by `Phi_5` in this ring. The same holds for inverse framing factors because `r_+-r_-` is divisible and both parameters are units. The boundary projectors have congruent coefficients: `D_- - D_+=Q^{-3}(Q^5-1)`, and their numerators agree. Consequently the raw difference has the form

\[
F-G=\Phi_5(Q)R(Q)
\]

with `R` regular at `Q=1` over `Z_(5)`. This conclusion does not follow merely from arbitrary rational functions agreeing at complex roots; it follows either from the integral skein calculation just described, or from the integral Laurent-polynomial argument below.

## 2. Integer exponents without a diagram-parity shortcut

All annular generator values, bulk parameters, and projector coefficients in the proof are rational functions of `Q`. Hence the resulting `F` and `G` belong to `Q(Q)`.

The banked ribbon identifications say they differ from the preferred polynomials by ribbon monomials, initially possibly written using `Q^{1/2}`. Since

\[
J(-Q^{-1}),\ V_K(Q^{-2})\in\mathbb Z[Q,Q^{-1}],
\]

their nonzero ratios to `F,G` are rational in `Q`. A monomial `Q^{m/2}` is rational in `Q` only if `m` is even. Therefore there are integer exponents `a,b` and constant signs such that

\[
F=\varepsilon Q^aJ(-Q^{-1}),\qquad
G=\eta Q^bV_K(Q^{-2}).
\]

In particular `F,G` are themselves integral Laurent polynomials once this ribbon identification is established. Their root equality then gives the alternative, simpler proof of integral divisibility: multiply by a Laurent unit to make a polynomial, divide by the monic polynomial `Phi_5`, and use vanishing of the remainder at all primitive fifth roots. The quotient has integer coefficients. This argument bypasses any concern about coefficients chosen in an annular expansion.

## 3. The constant sign must be derived, not adjusted independently

The FT root argument already gives `F(1)=1`. The ribbon identification gives `G(1)` equal to `+1` or `-1`. Because `Phi_5(1)=5` and `R(1)` is 5-integral,

\[
F(1)-G(1)\in5\mathbb Z_{(5)}.
\]

The only possible values are 0 and 2; therefore `G(1)=1`. The two signs agree in the **existing** raw normalization. One must not fix them independently after establishing raw root equality.

It follows that `R(1)=0` exactly. Differentiating gives

\[
F'(1)-G'(1)=5R'(1).
\]

Because the preferred polynomials both have zero first derivative at the relevant base point, the left side equals the integer `a-b`. An integer that belongs to `5 Z_(5)` is divisible by 5. Thus

\[
a-b\in5\mathbb Z,
\]

and the preferred correction factors `Q^{-a}` and `Q^{-b}` agree at every primitive fifth root. The claimed preferred cyclotomic congruence follows from the raw one.

## 4. The local jet alternative is also valid

Modulo five, `Phi_5(Q)=(Q-1)^4`. The same integral calculation therefore proves `F=G` modulo `(5,(Q-1)^4)` directly. Their derivatives agree modulo five, so `a-b` is divisible by five, and

\[
Q^{a-b}=1\pmod{(5,(Q-1)^5)}.
\]

Preferred normalization consequently preserves the entire cubic jet. This is independent of exponential convergence or factorial denominators; after substituting `Q=e^{-h}`, only factorials through degree three enter, all invertible modulo five.

## Scope

No coefficient-ring or framing obstruction remains in the audited steps, after the two normalization repairs above. The substantive all-pattern theorem still rests on the exact raw folded-cover and projector identifications in the separate annular/topological audits; this note must not be cited as an independent proof of those geometric steps.
