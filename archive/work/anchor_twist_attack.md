# Bounded Jones attack: the anchor-dependent twist route

Prepared 31 October 2026. This is a partial calculation, not a proof of unknot detection or a counterexample. The identities below are elementary skein consequences; no novelty is claimed.

## Exact reduction

Use the paper's normalization

\[
x^{-2}V_+-x^2V_-=(x-x^{-1})V_0,\qquad p=x-x^{-1}.
\]

Let \(K_m\) be an anti-parallel two-strand twist family, indexed by the number of added positive full twists. Oriented smoothing one crossing in the twist removes the remaining twists by Reidemeister I; write \(H\) for this fixed smoothing polynomial. Changing that crossing cancels an adjacent pair, giving

\[
V_{m+1}=x^4V_m+px^2H.
\]

For an anchor with \(V_0=1\), put

\[
D=x^4-1+px^2H=px^2(H+x+x^{-1}).
\]

Then, for positive integer \(m\),

\[
V_m=1+D\sum_{j=0}^{m-1}x^{4j}.
\]

The same expression is valid for all integers if the sum is interpreted as \((x^{4m}-1)/(x^4-1)\), a Laurent polynomial.

Consequences:

1. If \(H=-(x+x^{-1})\), every member of the twist family has Jones polynomial 1.
2. Otherwise, \(V_m\ne1\) for every \(m\ne0\), because the Laurent polynomial ring is an integral domain.
3. In case 2, the upper Laurent degree grows as \(4m+\max\deg D-4\) for sufficiently large positive \(m\). A JVP degree bound \(B\) confines Laurent support to \([-B,B+1]\), so no uniform JVP degree bound exists. In fact, once the upper degree dominates the fixed negative support, the JVP degree is \(4m+\max\deg D-5\).

Thus length-independent degree compression for a Jones-trivial anchor is equivalent to its smoothing having exactly the Jones polynomial of the two-component unlink. This is the missing crossing-propagation conclusion itself, rather than a consequence of the anchor.

For a general anchor \(V_0\), the analogous defect is \((x^4-1)V_0+px^2H\), and the family is either constant in Jones polynomial or has unbounded degree.

## An explicit unknot anchor refutes the unrestricted repair

Take the usual three-crossing trefoil shadow and switch its unknotting crossing. This is now a diagram of the unknot. The seed smoothing has

\[
H=-x-x^5.
\]

Starting at this unknot and adding one positive full twist restores the trefoil:

\[
V_1=x^2+x^6-x^8.
\]

The second positive full twist gives

\[
V_2=x^2-x^4+2x^6-x^8+x^{10}-x^{12}.
\]

For \(m\ge1\), the JVP degree is \(4m+3\). Equivalently, replacing the seed by an odd block of \(L\) positive crossings gives degree \(2L+5\), while its mixed-sign net-writhe \(-1\) state cancels back to the Jones-trivial anchor. Therefore simply adding the hypothesis \(V_K=1\) to the rejected uniform-bound claim does not repair it.

Important limitation: this anchor is a nonminimal diagram of the unknot. A new statement restricted to crossing-minimal diagrams of hypothetical nontrivial Jones-trivial knots is not refuted by this example; it remains unproved.

## The low-order function on the entire cube

Let \(c_2=a_2+b_2\) be the paper's coefficient. On knots, \(c_2=-3A_2\), where \(A_2\) is the Conway \(z^2\) coefficient. This can be proved directly without citing a derivative identity. Expand at the root \(x(p)=(p+\sqrt{p^2+4})/2\), so \(x^{\pm2}=1\pm p+p^2/2+O(p^3)\). For a two-component link write its expansion as \(-2+h_1p+O(p^2)\). Applying the Jones skein relation at an intercomponent crossing shows \(h_1(L_+)-h_1(L_-)=-3\); at a self-crossing the difference is zero. The two-component unlink has \(h_1=0\), so \(h_1=-3\operatorname{lk}\). The knot skein relation at order \(p^2\) then gives \(c_2(K_+)-c_2(K_-)=-3\operatorname{lk}(L_0)\). Compare with the Conway skein relation and the value zero at the unknot to obtain the stated identity.

For the explicit family above,

\[
c_2(K_m)=-3m.
\]

For an odd residual cube of length \(L\), with sign vector \(\varepsilon\), Reidemeister II cancellation leaves net twist \(w=\sum_i\varepsilon_i\). Since \(m=(w+1)/2\),

\[
c_2(\varepsilon)=-\frac32\left(\sum_i\varepsilon_i+1\right).
\]

This is a nonzero affine Boolean function. It vanishes on every state of the anchor layer \(w=-1\), yet is nonzero on most of the cube. Finite type plus an anchor plus arbitrarily large cube dimension does not force vanishing.

## Two-crossing endpoint obstruction

If the two crossing chords \(u,v\) interlace, smoothing \(u\) splits the knot into two components and smoothing \(v\) then merges them. Since the zero-order Jones coefficient for an \(r\)-component link is \((-2)^{r-1}\), the unnormalized mixed difference is

\[
\partial_u\partial_v c_2=2(-2)+1=-3.
\]

Thus the four knots in an interlacing two-crossing face cannot all have Jones polynomial 1. If three do, the fourth has \(c_2=\pm3\). The standard trefoil shadow with one crossing fixed positive gives the concrete example: one face vertex is the trefoil and the other three are unknots. This verifies the eventual endpoint obstruction while demonstrating the difficulty of the propagation needed to reach it.

## Search implication and remaining bottleneck

An unknot-anchored anti-parallel twist family has either exactly one Jones-trivial parameter or all parameters Jones-trivial. A useful search target is therefore a nonnugatory crossing circle of the unknot whose smoothing has the two-component unlink's Jones polynomial. Finding one would yield Jones-trivial knots for every twist parameter. The established no-cosmetic-generalized-crossing theorem for the unknot ensures nonzero twists at a nonnugatory crossing circle are nontrivial. We do not assert that such a crossing circle exists, nor that the infinitely many parameters necessarily give pairwise distinct knot types without a separate argument.

Primary research reference confirming the cosmetic-crossing fact: Balm and Kalfagianni, *Cosmetic crossings of twisted knots*, introduction, citing Scharlemann--Thompson:
https://users.math.msu.edu/users/kalfagia/BalmK4.pdf

There are already nontrivial two-component links with precisely the unlink's Jones polynomial, so the condition on \(H\) alone is not a contradiction. The missing feature is their occurrence as the smoothing at a nonnugatory crossing in an unknot diagram. Thistlethwaite's original examples are 15- and 17-crossing links, both satellites of the Hopf link:
https://homepages.math.uic.edu/~kauffman/tj.pdf

Another rigorously formulated attack route: Sikora, *Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals*, Canadian Journal of Mathematics 76(2) (2024), 707--727. Theorem 1.3 gives a topological consequence of Jones detection: a framed system of two tangle equations with a rational solution has no second solution. A counterexample to that uniqueness could disprove Jones detection.
https://doi.org/10.4153/S0008414X23000755

## Verification

`work/anchor_twist_attack.py` uses exact integer Laurent-polynomial arithmetic. It checks forward and backward skein recurrences for \(-12\le m\le12\), reduction and reconstruction in the JVP basis, the closed form, the predicted degree, and the affine \(c_2\) formula for every net-sign class through \(L=23\). All checks passed.
