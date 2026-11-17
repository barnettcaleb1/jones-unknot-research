# The modulo-five third-moment route: exact bulk congruence and the remaining boundary problem

16 November 2026. Bounded theoretical audit; no scan and no fitted identity.

## Verdict

The bulk quantum-group parameters explain precisely why the prime **5** and the **third jet** occur together. The root color-two theory has orthogonal BMW parameters of formal dimension `N=-1`; folding the ordinary Jones theory of the double cover gives dimension `N=4`. Their braid parameters agree modulo five to order five, and their loop parameters agree to order four. This is an exact algebraic calculation below.

This does **not** yet prove

\[
\frac{M_3(K,h)}{36}\equiv 7v_3(K)\pmod5.
\]

The quotient invariant is a reduced **axis-and-vertex** evaluation, not an ordinary closed Kauffman polynomial. A comparison of that boundary theory, or a proof that the residual invariant of order at most two vanishes, remains necessary. Matching three-chord symbols alone is insufficient. The report does not promote the observed integrality of `iota` to a theorem.

## 1. The exact jet statement to prove

Keep the conventions of `ft_integral_referee.md` and `osp_casimir_exact.md`. Write

\[
t=-e^h,\qquad J(-e^h)=\sum_{k\ge0}\frac{M_k}{k!}h^k,
\]

and use the ordinary Jones normalization

\[
v_3(K)=-\frac{V_K'''(1)+3V_K''(1)}{36},\qquad
V_K''(1)=-6a_2(K).
\]

Since `V_K'(1)=0`,

\[
V_K(e^{2h})=1-12a_2(K)h^2-48v_3(K)h^3+O(h^4).
\]

The already proved moment identities give

\[
J(-e^h)=1-12a_2(K)h^2+\frac{M_3}{6}h^3+O(h^4).
\]

Thus, after localizing integers away from 5, the desired congruence is equivalent to

\[
\boxed{\quad J(-e^h)\equiv V_K(e^{2h})\pmod{(5,h^4)}.\quad} \tag{1}
\]

Indeed, its cubic coefficient says `M_3=-288v_3` modulo five; dividing by 36 gives `M_3/36=-8v_3=7v_3` modulo five. Factorials through degree three are units at five, so there is no exponential-denominator ambiguity in this comparison.

The banked exact formula

\[
\frac{M_3}{36}=2H'(-1)-7a_2(K),\qquad
H=\frac{J-1}{(t^4-1)(t^3+1)},
\]

then rewrites the same conjecture as

\[
H'(-1)\equiv a_2(K)+v_3(K)\pmod5.
\]

This reformulation has no extra content until (1), or the equivalent residual identity, is proved.

## 2. A parameter calculation with no singular specialization

Put

\[
Q=-t^{-1}=e^{-h},\qquad z=Q-1.
\]

The generic color-two eigenvalues in the verified local model are

\[
q^{-4},\ -q^{-2},\ q^2,
\qquad q^2=t.
\]

In terms of `Q`, these are

\[
Q^2,\ Q,\ -Q^{-1}.
\]

Consequently the bulk braid has the orthogonal BMW eigenvalue parameters

\[
(Q,-Q^{-1},r^{-1}),\qquad r_-=Q^{-2}.
\]

The subscript denotes the formal dimension `N=-1`, since the orthogonal dimension convention is `r=Q^{N-1}`. Its loop scalar is the verified color-two quantum dimension

\[
d_-=1-Q-Q^{-1}
     =1+\frac{r_--r_-^{-1}}{Q-Q^{-1}}.
\]

For the folded `SO(4)` vector theory, the corresponding parameters are

\[
r_+=Q^3,\qquad
d_+=2+Q^2+Q^{-2}
    =1+\frac{r_+-r_+^{-1}}{Q-Q^{-1}}.
\]

There are exact Laurent-polynomial identities

\[
\begin{aligned}
r_+-r_-&=Q^{-2}(Q^5-1),\\
d_+-d_-&=Q^{-2}\Phi_5(Q),
\end{aligned} \tag{2}
\]

where `Phi_5(Q)=1+Q+Q^2+Q^3+Q^4`. In characteristic five,

\[
Q^5-1=(Q-1)^5,\qquad \Phi_5(Q)=(Q-1)^4.
\]

Therefore

\[
r_+\equiv r_-\pmod{(5,z^5)},\qquad
d_+\equiv d_-\pmod{(5,z^4)}. \tag{3}
\]

These are polynomial divisibilities, so no quantum integer is divided by at the root. In particular the loop-dimension comparison loses exactly one order from the braid-parameter comparison. This accounts for a cubic-jet statement rather than an arbitrary-order congruence.

**Bulk consequence.** Any fixed expression in the ordinary BMW generators whose evaluation is a polynomial in `Q^{+-1}`, `r^{+-1}`, and `d`, with coefficients regular at `Q=1` modulo five, has equal evaluations through cubic order under these two parameter assignments. More generally the same holds for a rational expression whose denominators specialize to units modulo five. This is just substitution in (3); it does not require diagonalizing a braid at a nonsemisimple point.

For ordinary framed Kauffman skein evaluations this is the applicable parameter comparison. It is not, by itself, a theorem about the marked quotient invariant: its vertices and its mixed axis crossings are additional generators.

## 3. Why the axis cannot be omitted

In the verified integral construction, the quotient invariant is evaluated by

\[
i:V_1\longrightarrow V_1\otimes V_2,\qquad
p:V_1\otimes V_2\longrightarrow V_1,
\qquad pi=I,
\]

and by mixed monodromies on `V_1 tensor V_2`. The final scalar is read from an endomorphism of `V_1`. It is **not** obtained by dividing a closed trace by its dimension: that dimension vanishes at the special point.

The folding picture for the ordinary Jones polynomial uses `U tensor U`, with `dim U=2`, as the four-dimensional vector. At the classical point the axis induces the interchange of the two sheets, and the selected endpoint is the antisymmetric singlet. Away from that point, identifying its mixed crossing and vertex operators with the quotient operators is a boundary/defect comparison. It does not follow from the equality of the three bulk braid eigenvalue parameters.

Even a comparison of mixed eigenvalues is insufficient. It leaves their eigenspaces, the intertwiners at the two vertices, pivotal maps, and preferred framing unverified. The generic quotient mixed matrix acts on a six-dimensional space with a dynamic color-one factor; a folded reflection acting on the four-dimensional vector is not automatically the same structure.

A concrete marking caution comes from the existing local certificates. Their mixed full twist `T` has eigenvalues `q^{-4},q^2`. After normalizing by the eigenvalue on the attached channel, its other eigenvalue is `t^3`. The halfword generator `Y=y0` used in TH-2BR has normalized ratio `t^{-3}`. Hence **Y corresponds to `T^{-1}` in this comparison**. Ignoring that inverse gives the wrong sign for the on-axis principal insertion.

## 4. What the principal comparison supplies, and what it does not

The companion report `degree3_weight_comparison.md` treats the principal tensor comparison. Its relevant algebraic mechanism is:

\[
\operatorname{sdim}(\mathbb C^{1|2})=-1\equiv4
     =\dim(U\otimes U)\pmod5,
\]

with root parity `Pi` corresponding to minus the interchange `-g` of the two `U` factors. In particular

\[
\operatorname{str}(\Pi)=3\equiv-2=\operatorname{tr}(-g)\pmod5.
\]

The root Casimir is `Omega=P-K`; the straight off-axis insertion is `-2Omega`. With the correct inverse for `Y`, the on-axis preferred insertions also agree modulo five. These calculations are stronger than fitting values of `M_3` on knots: they compare the local operators on marked singular configurations.

Nevertheless an equality of third symbols says only that

\[
R(K,h)=M_3(K,h)+288v_3(K)\pmod5
\]

has equivariant finite-type order at most two, provided the symbol comparison includes the entire marked evaluation. It does not say `R=0`. Mirror-oddness does not dispose of this issue: no classification of mirror-odd equivariant invariants of order at most two has been proved here.

Ordinary knot finite-type classification is not a substitute. An allowed on-axis move is a full twist versus its inverse, and the marked axis and the two vertices are retained. Nor may a classification of ordinary spatial-theta finite-type invariants silently be used without comparing these move filtrations.

## 5. A useful boundary calibration, not a boundary proof

One further parameter identity supports the same mechanism. A generic color-two loop linking the color-one axis once has reduced Hopf value

\[
\frac{[6]}{[2]}=q^4+1+q^{-4}=1+Q^2+Q^{-2}.
\]

The candidate folded value in the marking with reflection `-g` is the negative fundamental loop value `-(Q+Q^{-1})`. Their difference is again

\[
1+Q^2+Q^{-2}+Q+Q^{-1}=Q^{-2}\Phi_5(Q). \tag{4}
\]

Thus both the unlinked-loop and the once-linked-loop calibrations agree through cubic order modulo five. Equation (4) is exact algebra; identifying the candidate folded value with every corresponding relative closure still belongs to the boundary problem.

In particular, these two loop values do not generate the entire relative solid-torus BMW skein by an established argument here. Winding braids and relative endpoint states must be controlled. Treating that skein as a polynomial ring in a single simple core circle would import the much simpler Kauffman-bracket situation and leave a gap.

## 6. Precise remaining tasks

There are two legitimate routes to finish the modulo-five assertion.

1. Prove the marked relative BMW comparison through degree three, including the mixed crossing, `i,p`, pivotal structure, reduced-axis scalar, and preferred framing. Equations (2)–(4) give its bulk parameters and elementary boundary calibrations. An explicit diagrammatic presentation whose complete defining relations specialize equally would suffice; eigenvalues alone would not.
2. Starting from the complete principal-symbol comparison, classify or otherwise determine the residual `R` of order at most two for the exact allowed moves. Its base values and first and second differences must be proved zero on a generating set of marked configurations, with all degree-zero sectors addressed.

Neither route is completed in this report. No universal geometric identification or integrality theorem for `iota` is claimed. The genuine reduction is that the cubic congruence has a specific prime-five BMW origin and a sharply isolated **relative boundary/lower-order** remainder, rather than an unexplained numerical coincidence.

## 7. Follow-up boundary lead from the parent calculation

After the bounded report was written, the parent supplied a possible way to replace all local boundary matrices by annular skein evaluations. The attached-channel projector is

\[
P_1=\frac{T-tI}{t^{-2}-t}.
\]

Its denominator is 2 at `t=-1`, hence a unit modulo five. The original reduced-axis partial traces of the mixed powers are

\[
L_n^-=Q^{2n}-(Q+Q^{-1})(-Q^{-1})^n,
\]

and the proposed folded traces are

\[
L_n^+=Q^{-3n}+(Q^2+1+Q^{-2})(-Q^{-1})^n.
\]

Their exact difference is

\[
L_n^- - L_n^+
=Q^{-3n}(Q^{5n}-1)-Q^{-2}\Phi_5(Q)(-Q^{-1})^n,
\]

which vanishes modulo `(5,(Q-1)^4)` for every integer `n`. Thus matching **all** these mixed winding-power traces has no additional algebraic obstruction.

There is a directly relevant annular spanning result. Alexander T. Pokorny, *Dubrovnik Skein Theory and Power Sum Elements* (2021), Section 2.4, printed pages 27–28, states the polynomial-annulus description on positive-winding generators and attributes it to V. G. Turaev, *Conway and Kauffman modules of a solid torus*, Journal of Mathematical Sciences 52 (1990), no. 1, 2799–2805. See [the primary thesis](https://escholarship.org/content/qt0dx137gc/qt0dx137gc.pdf). The stated generation argument uses crossing changes plus lower-crossing terms. Only generation is needed here, so an idempotent basis over the fraction field should be avoided.

The missing diagrammatic checks in this version are specific:

* Identify the standard positive-winding annular generator with the mixed-power closure used in `L_n`, retaining its ribbon framing. The former is a closed cycle braid on `n` strands; the latter is presented as a two-colored full-twist closure. Their relation must be stated as a marked framed-link identity, not inferred from matching winding number.
* Convert the two theta vertices to a partial trace with `P_1`, and then to actual closed annular skein elements. This must cover arbitrary quotient diagrams, not only a body already presented as an endomorphism with one color-two strand at each end.
* Verify that the folded reduction and its framing are exactly the ordinary Jones invariant of the branched double-cover knot. Equality of the reduced trace formulas on generators does not by itself make that topological identification.

If these checks hold over the ring regular modulo five, annular generation and the trace formulas would complete the entire jet comparison, including the lower-order residual. They are recorded as a precise potential completion, not as accomplished steps of the present report.

## 8. Bounded follow-up: the winding-generator marking is correct

The first geometric check in Section 7 has a direct proof for every positive integer `n`.

Let `U_n union C_n` be the closure of the two-strand braid `sigma_1^{2n}`, with `U_n` designated as the axis. Its two components are parallel slope-`(1,n)` curves on the usual unknotted torus. They cobound an embedded annulus, and each is an unknot. Shrinking that annulus isotopes `C_n`, in the complement of `U_n`, onto the boundary of a tubular neighborhood of `U_n`. In the preferred meridian–zero-longitude coordinates of this unknot,

\[
[C_n]=\lambda_U+n\mu_U.
\]

The meridional coefficient is `n` because the linking number of the two components of the positive braid closure is `n`; the longitudinal coefficient is one because `C_n` is an annular parallel of `U_n`.

The exterior of `U_n` is a solid torus. With its preferred coordinates one has

\[
\mu_{\mathrm{ext}}=\lambda_U,\qquad
\lambda_{\mathrm{ext}}=\mu_U
\]

up to the simultaneous orientation signs that have already been fixed by positive linking. Therefore `C_n` is the positive slope-`(n,1)` torus curve in that solid torus: it winds `n` times longitudinally and once meridionally. This is precisely the annular closure `A_n` of the positive cycle braid

\[
\sigma_1\sigma_2\cdots\sigma_{n-1}.
\]

The argument determines the marking, not merely the homotopy class. Any ambient isotopy taking the designated unknot `U_n` to the standard axis carries its preferred longitude to the preferred longitude. Hence there is no unrecorded Dehn twist of the complement in this identification.

There is one ribbon correction. In the two-strand closure all crossings are between the two different components; consequently the moving component's blackboard self-framing is zero. The annular diagram `A_n` is one component with `n-1` positive self-crossings, hence has blackboard self-framing `n-1`. Thus, writing `theta_V` for the positive ribbon twist of the moving color,

\[
\operatorname{ev}(A_n)=\theta_V^{\,n-1}\,
\operatorname{Tr}^{\mathrm{red}}_{\mathrm{axis},V}(T^n).
\]

Both axis framings are zero. For `n=1` this is the ordinary Hopf calibration with no correction; for `n=2,3` the correction is one or two positive moving-strand twists. A negative braid convention reverses all these signs consistently.

In the BMW convention of Section 2 the vector twist is `r`, so the two correction factors have quotient `Q^{5(n-1)}`. They therefore agree not only through cubic order modulo five, but already modulo `Phi_5(Q)`. This resolves the winding-generator marking issue; the arbitrary-theta projector closure and the folded-cover identification remain to be checked separately.


## Later completion in this turn

The complete annular covering comparison is now written in `degree3_cyclotomic_comparison.md` and recorded TRUSTED pending Claude's read in reply20261116-221023-codex. Its final internal audits include `degree3_cyclotomic_referee.md`, `degree3_annular_closure_audit.md` and `degree3_coefficient_framing_audit.md`. It supplies the full preferred Phi10 congruence and hence the modulo-five third-moment identity, including the lower-order residual. Earlier pending statements in this report describe the intermediate stage. The independent geometric identification of iota remains open, and the exact exclusions in this report, where present, stand.
