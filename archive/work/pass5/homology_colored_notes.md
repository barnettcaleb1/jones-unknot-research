# The remaining color-three condition: exact consequences and an independent framing audit

Conventions: \(H_N(C;q)\) is the zero-framed reduced Jones polynomial colored by the \(N\)-dimensional representation, with \(H_N(U)=1\); \(H_2=V_C\). In bracket notation \(q=A^{-4}\), \(\delta=-A^2-A^{-2}\), \(\Delta_2=A^4+1+A^{-4}\), and the unreduced color-three invariant is \(J_2(C)=\Delta_2H_3(C)\).

## Exact equivalence with the zero-framed parallel link

Let \(C^{(2)}\) be the zero-framed two-parallel, with linking number zero. The skein identity \(z^2=S_2+1\) gives

\[
\delta V_{C^{(2)}}=J_2(C)+1.
\]

Since \(\Delta_2+1=\delta^2\),

\[
H_3(C)=1\quad\Longleftrightarrow\quad V_{C^{(2)}}=\delta,
\]

the Jones polynomial of the two-component unlink. The ordinary two-parallel-link problem and this one fixed colored invariant are exactly the same polynomial problem.

The braid agent separately records an even simpler converter to a knot: the ordinary \((2,1)\)-cable of \(C\) has Jones polynomial one if and only if \(H_3(C)=1\). Thus Ren's special pattern is not necessary for converting a nontrivial companion satisfying this condition into a counterexample to ordinary Jones unknot detection.

## Strong necessary ordinary-Jones congruence

[Habiro's integral cyclotomic expansion](https://msp.org/gtm/2002/04/gtm-2002-04-005p.pdf) can be written

\[
H_N(C;q)=\sum_{k=0}^{N-1}C_k(q)(q^{1+N};q)_k(q^{1-N};q)_k,
\qquad C_k\in\mathbb Z[q^{\pm1}],\quad C_0=1.
\]

At color three there are only two nonconstant terms:

\[
H_3-1=(1-q^4)(1-q^{-2})
\bigl[C_1+C_2(1-q^5)(1-q^{-1})\bigr].
\]

Because the Laurent ring is an integral domain, \(H_3=1\) implies

\[
C_1=-C_2(1-q^5)(1-q^{-1}).
\]

Substituting this into the color-two formula proves

\[
\boxed{
V_C(q)-1=-C_2(q)(1-q^5)(1-q^3)(1-q^{-1})^2.
}
\]

Consequently \(V_C-1\) must be divisible by

\[
\Phi_1(q)^4\Phi_3(q)\Phi_5(q)
\]

up to a Laurent unit. In particular:

- \(V_C(\zeta_5)=1\) at every primitive fifth root;
- \(V_C-1\) vanishes to order at least four at \(q=1\);
- the signed integer \(V_C(-1)\) is congruent to one modulo 16, hence \(\det C\equiv\pm1\pmod{16}\).

These are necessary conditions, not a sufficiency theorem. The cyclotomic identity does not force \(C_2=0\), so it does not by itself force the ordinary Jones polynomial to be one. For example, the formal assignment \(C_2=1\), \(C_1=-(1-q^5)(1-q^{-1})\) satisfies the color-three identity with a nonconstant color-two polynomial; no assertion is made that those formal coefficients come from a knot.

As an actual check, exact ordinary Jones calculations for Kinoshita–Terasaka \(11n42\) and Conway \(11n34\) give, in the table's mirror convention,

\[
V_C-1\equiv-3+4q-4q^2+3q^3\pmod{\Phi_5(q)}.
\]

Thus both familiar Alexander-one knots fail the color-three condition. This filter requires only their ordinary Jones polynomial, avoiding a cable calculation.

## Known Jones-trivial links need not be parallel links

[Hedden's proof](https://arxiv.org/pdf/0805.4418), page 2, identifies

\[
\Sigma_2(C^{(2)})\cong S^3_0(C\#C^r),
\]

where \(C^r\) reverses string orientation. Therefore its integral first homology is always \(\mathbb Z\). The previously audited EKT Jones-trivial families have additional nonzero torsion in this group. They therefore cannot be zero-framed two-parallels of any companion. An arbitrary link with the unlink's Jones polynomial is not enough; it must also have this specific annular cable geometry.

Hedden proves that a nontrivial companion forces the two-parallel's Khovanov rank over \(\mathbb F_2\) to be at least 12, versus four for the unlink. His proof explicitly uses Floer summands of Euler characteristic zero. This explains the remaining gap: the geometric homology is forced to grow, while its Euler characteristic can cancel. The cited theorem detects the unknot using homology, not the Jones polynomial of the cable.

## Independent geometric audit of the normalization

We constructed the actual zero-framed two-parallel of the trefoil, independently of the Ren satellite formulas. Starting with \(\sigma_1^3\), replace each crossing by the four-strand block \(\sigma_2\sigma_1\sigma_3\sigma_2\), then append \(\sigma_1^{-6}\) to remove the blackboard linking number three. The resulting 18-crossing link has two components and linking number zero.

Regina computes its ordinary Jones polynomial as

\[
V_{C^{(2)}}(x)=-x^{23}+x^{21}+x^{17}-x^9-x^5-x,
\qquad x=q^{1/2}.
\]

Using the skein identity and dividing by \(\Delta_2\) gives

\[
H_3(C;q)=q^{11}-q^{10}-q^9+q^8-q^7+q^5+q^2.
\]

This matches the independent Habiro trefoil expansion term for term. Its first logarithmic derivative is zero and its second is \(-16\), confirming the colored normalization used in the all-companion theorem. This is a direct geometric cable audit; it does not claim an independent 60-crossing planar computation of every Ren satellite.

Exact code and results are in `homology_cable_audit.py/.json`.
