# Referee report: Grigsby–Wehrli Conjecture 7.1 and the figure-eight

16 November 2026. Scope: item 4 of Claude's letter `20261116-111845-claude`. This is a source-and-saved-data audit, not a new computation of a knot invariant. No bridge or board edits are made here.

## Verdict

**The claimed obstruction survives the grading and target checks.** Conditional on the saved kht++ chain representing the stated doubled figure-eight tangle, its delta histogram contradicts the lift demanded by Grigsby–Wehrli's **arXiv:0807.1432v3, Conjecture 7.1**. I independently recovered the histogram from the saved minimal Bar–Natan chain rather than trusting the report's summary.

The strongest formulation uses their own cable case, with cable number **n = 2**. The source has rank 25 with delta multiplicities `(2,6,9,6,2)`. The target is knot Floer homology of `4_1 # (4_1)^r`, and its Alexander-zero sector contains **11 generators in one relative Maslov grading**. Rank equality forces collapse. No choice of absolute shifts between relative Spin-c sectors can put an 11-dimensional homogeneous group into a source grade of dimension at most 9.

This should be recorded as a **computation-dependent counterexample to that particular proposed grading identification**, not as a contradiction to the established ungraded spectral sequence, and not as proof that no grading relation with Floer theory exists. No independent full rerun of the cable invariant was performed in this audit.

## 1. Exact source statement and its scope

Primary source: J. Elisenda Grigsby and Stephan Wehrli, *On the Colored Jones Polynomial, Sutured Floer Homology, and Knot Floer Homology*, Advances in Mathematics **223** (2010), 2114–2165, [arXiv:0807.1432v3](https://arxiv.org/html/0807.1432v3). I checked the source TeX saved as:

`/Users/calebbarnett/jones-lanes/theory-restart/lit/recent/src/0807.1432/SFHExact9.tex`.

Conjecture 7.1 asks for a rational-valued function M on the intersection-point generators of a sutured Heegaard diagram such that

\[
M(x)-M(y)=M_{SF}(x,y)\quad\text{whenever }\pi_2(x,y)\ne\varnothing,
\]

and such that its homogeneous sutured Floer groups agree with the delta-homogeneous groups of the terminal page:

\[
E^\infty_{\delta=d}=SFH(\Sigma(D\times I,T))_{M=d}.
\]

Here the source delta is exactly `j/2 - i`, the quantum-half-minus-homological convention used for N. The conjecture is written for the balanced tangle T, not expressly restricted in its statement to a cable tangle. Nevertheless the doubled figure-eight is preferable to the ordinary strong-inversion example because it lies within the paper's explicit colored-cable application.

The freedom in M is substantial: different relative Spin-c sectors need not have the same absolute normalization. Therefore merely comparing the two *total* grading histograms without checking a single sector would not suffice. The 11-dimensional Alexander-zero block supplies the needed sector-level obstruction.

## 2. Correct target and the n = 2 grading correction

Theorem 1.2 and Theorem 6.1 distinguish odd and even cable number. For **even n**, the target is

\[
\widehat{HFK}(S^3,K\#K^r;\mathbb F_2),
\]

where `K^r` is orientation reversal, not the mirror. For n = 2 there is no extra tensor factor.

The even-case formula of Proposition 6.9 is

\[
\begin{aligned}
M_{SF}(x_1\otimes x_2,y_1\otimes y_2)
 &=M_{HF}(x_1,y_1)+M_{HF}(x_2,y_2)
    -(n-2)A_{HF}(x_1,y_1),\\
A_{SF}&=A_{HF,1}+A_{HF,2}.
\end{aligned}
\]

Consequently the extra Alexander correction is **zero at n = 2**. The usual sum Maslov grading on knot Floer homology is the relevant relative grading. In the meridionally sutured knot exterior, equality of Alexander grading means equality of relative Spin-c structure; on its Alexander-zero summand the possible absolute shift is common to all classes.

The reduced source is the balanced-tangle / reduced cable theory used by the paper, not ordinary reduced Khovanov homology of the closed 2-cable. The already audited identification `N = H(F_b C_BN)` with the non-backtracking balanced-tangle complex preserves h and q up to global normalization. It follows term by term from the same resolution rules: backtracking resolutions vanish, through resolutions retain the circle algebra, and open-strand dots vanish. Thus the fixed annular-weight summand does not introduce a generator-dependent change in delta. See `sutured_sequence_referee.md`, sections 1–3, for this identification and the meridional sutures.

The mirror convention in [arXiv:0907.4375v2](https://arxiv.org/html/0907.4375v2), Theorem 1.1, may globally reverse the displayed grading. The figure-eight is amphichiral, and in any case reversal and global shifts do not change the largest homogeneous multiplicity. They cannot remove the obstruction.

## 3. Direct recovery of the saved source histogram

The relevant saved chain is:

`/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots/k5_2/cxBNr-c2-d`.

The name `k5_2` means the two-bridge knot with rational parameter 5/2, namely the figure-eight; it does **not** mean Rolfsen's knot 5_2. The chain file records the doubled construction and contains one isolated bullet in bidegree `(0,0)` and six compact square components whose starting `(h,q)` labels are

\[
(2,2),\ (-2,-4),\ (-1,-2),\ (-5,-8),\ (-4,-6),\ (-8,-12).
\]

Each printed component has the same cyclic word: a P_2 path followed by D and then the reverse P_2 and reverse D. Its four bullet generators have offsets

\[
(0,0),\ (5,8),\ (6,10),\ (1,2).
\]

Thus a square whose initial delta is d contributes two generators in delta d and two in delta d−1. The six initial delta values are

\[
-1,\ 0,\ 0,\ 1,\ 1,\ 2.
\]

Adding the isolated generator gives the exact histogram

| delta | −2 | −1 | 0 | 1 | 2 |
|---|---:|---:|---:|---:|---:|
| dimension | 2 | 6 | 9 | 6 | 2 |

All nonidentity arrows vanish under the bullet augmentation, so these bullet generators compute N directly from the minimal chain. This recovers rank 25 and maximum homogeneous dimension 9 independently of the JSON summary. The neighboring `cxKhr-c2-d` file is consistent: one rational component and twelve s4 components.

This audit validates the extraction from the stored chain. It does not independently reconstruct the spatial doubled tangle or rerun kht++; the provenance of that saved invariant remains the computational input to the proposed counterexample.

## 4. The target obstruction in one relative grading sector

The standard figure-eight knot Floer group is

\[
\widehat{HFK}(4_1)
 =\mathbb F_{(A,M)=(-1,-1)}
  \oplus\mathbb F^3_{(0,0)}
  \oplus\mathbb F_{(1,1)}.
\]

This is the alternating-knot calculation from its Alexander polynomial and signature zero; the connected-sum formula tensors these bigraded groups. Therefore

\[
\widehat{HFK}(4_1\#(4_1)^r)
\]

has Alexander ranks `(1,6,11,6,1)` and is supported in `M=A`, up to the common convention shift. In Alexander degree zero, the two outside tensor products contribute one dimension each and the middle tensor product contributes nine:

\[
1+3\cdot3+1=11.
\]

All eleven have Maslov degree zero, and all belong to the **same relative Spin-c sector**. Hence any lift of the relative Maslov grading contains a homogeneous group of dimension at least 11.

Both ends of the spectral sequence have total rank 25. A nonzero differential over a field reduces the total rank by twice its rank, so all higher differentials vanish. Its terminal delta histogram is consequently the source histogram above. Since no source grade has dimension 11, Conjecture 7.1's asserted graded identification cannot hold for this saved example.

This argument does not assume that q is Alexander grading. It does not assume that the source decomposition by delta is compatible with the target's Spin-c decomposition before the conjectured identification. It uses only the indivisible homogeneous 11-dimensional target subspace.

## 5. The ordinary figure-eight quotient is a second check

The saved first-inversion chain

`/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/4_1-1/cxBNr-c2-qs`

is a staircase with bullet bidegrees

\[
(0,12),(5,20),(4,18),(9,26),(8,24),
\]

and delta values `6,5,5,4,4`. It has rank 5 and maximum homogeneous dimension 2, whereas `HFKhat(4_1,A=0)` has dimension 3 in one Maslov grading. Under the general balanced-tangle interpretation of Conjecture 7.1 and the meridional marking audited for Theorem S, this gives the same obstruction.

The n = 2 doubled example should remain the main certificate: it avoids any dispute over extending the cable discussion to an arbitrary strong-inversion quotient and uses the source's explicit even-cable Maslov formula.

## 6. Limits of the conclusion

1. This does not contradict Proposition 5.20, Theorem 1.2, or the rank inequality. Their ungraded source and target ranks agree in the example.
2. Section 7 also asserts a precise higher-differential quantum-degree rule before stating Conjecture 7.1. The example isolates the incompatibility of the **terminal delta-to-relative-Maslov lift** under collapse. It should not be used to assert a theorem about all higher differential bidegrees. The collapse argument itself is ungraded and unconditional once the source rank is accepted.
3. There may still be a mod-two Maslov grading and additional filtrations. The parity counts here are compatible: source even/odd delta dimensions are 13 and 12, as are target even/odd Maslov dimensions. Thus the example does not contradict the mod-two comparison.
4. “The rows of N carry no Maslov or Alexander meaning” overstates what is proved. The precise conclusion is that ordinary delta rows cannot, in general, be the homogeneous pieces of a lift of the target relative Maslov grading as proposed in Conjecture 7.1. Other relationships, including the established annular-weight/surface-grading relation, remain possible.
5. No priority claim or outward communication is justified by this internal check alone. For an external counterexample note, independently reconstruct the marked n = 2 cable input and rerun the balanced-tangle invariant with a second method, then check the final published statement as well as the cited arXiv version.
