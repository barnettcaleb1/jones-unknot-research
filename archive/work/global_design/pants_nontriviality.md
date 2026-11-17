# The marked pants transfer: nontriviality and determinant

2026-11-03. CX-PANTS. Status: TRUSTED, written proof with two independent
internal geometry reads. Published inputs are identified below; priority
of this combination has not been investigated. No counterexample input
has been found.

## Statement

Let Theta be a nonplanar theta graph in S^3 whose three constituent knots
are unknots. Let P be its canonical oriented pair-of-pants thickening
with zero Seifert form, and L=boundary(P). Choose disjoint proper arcs
a,b joining the three boundary components as a tree. Cutting along both
arcs gives an embedded disk D.

Use the two removed narrow strips to specify disjoint two-strand balls
on K(0,0)=boundary(D). Insert m and n full twists to obtain K(m,n), with
local handedness chosen as in pants_twist_transfer.md. Then:

1. K(m,0) and K(0,n) are unknots.
2. K(m,n) is nontrivial whenever mn is nonzero.
3. det K(m,n)=1 for all integers m,n.
4. u(K(1,1))=1.
5. With V(U)=1, delta=-A^2-A^-2, t=A^-4,

       V_K(m,n)-1 = ((1-A^(8m))(1-A^(8n))/delta^2)
                     (V_L-delta^2).                         (1)

In particular, K(1,1) is a specific nontrivial determinant-one,
unknotting-number-one knot, and is Jones-unit exactly when L is
Jones-equal to the three-component unlink.

For a Brunnian theta, put Y*=Huh's normalized Jaeger specialization
tilde{mathfrak J}, which is equivalent to the normalized Yamada invariant.
Huh's Theorem 8 / Corollary 9 gives

       Y*(Theta)-V_L = -3+2/delta^2,

and the same identity holds for the planar theta Theta_0. Consequently

       V_L-delta^2 = Y*(Theta)-Y*(Theta_0).                   (2)

Thus a nonplanar Brunnian theta with the planar normalized Yamada value
would give a Jones counterexample of unknotting number one by this
specified construction. This supplies a reduction, not such a theta.
The normalization in (2) is Y*, not an unadjusted Yamada polynomial.
[Huh, Section 4](https://arxiv.org/html/2206.11450#S4).

## The augmented link is Brunnian

Let C_a,C_b bound the crossing disks of the two cut boxes and set

       Gamma = K(0,0) union C_a union C_b.

Gamma and L are different links. In particular, we do not claim that
the canonical boundary L is Brunnian.

The two circles lie in disjoint balls, so they are an unlink. Forget C_b.
View D as the annulus obtained by cutting P along b, further cut along
the spanning arc a. This annulus has zero framing. Its core is isotopic
to a boundary component of P, hence is an unknot; its framing is zero by
restriction of P's Seifert form. Isotope the annulus and its spanning arc,
with endpoints free, to a planar annulus with a radial arc. Its cut
boundary together with C_a is the standard nugatory pair, an unlink.
Interchange a and b for the other pair. This also proves assertion 1.
Thus Gamma is a homologically trivial Brunnian link.

## The new implication: Gamma unlink forces Theta planar

Suppose Gamma is the three-component unlink. Take the double cover of
S^3 branched over K(0,0)=U; its total space is S^3. Each C_i lies in a
splitting ball disjoint from the branch knot. The cover over these balls
is trivial, so the four lifts of C_a,C_b form a four-component unlink.

Use the specified crossing disks, not newly selected nugatory disks.
Each disk meets K(0,0) twice, and its branched lift is an embedded annulus
A_i. The two annuli are disjoint. Their cores kappa_a,kappa_b can be
simultaneously isotoped to one boundary component of each annulus.
Consequently kappa_a union kappa_b is an unlink. The annular framing is
zero: the two boundary components of each A_i have linking number zero.

Restoring a strip is surgery on its lifted core in precisely this annular
framing. Here is the local marking check. Write the strip ball as the
crossing disk times an interval, with the two original branch strands
vertical. Its cover is A_i times an interval. The other planar smoothing
joins the two front ends and the two back ends. The middle crossing disk
then misses the branch strands and lifts to disks bounded by the lifts
of C_i. Therefore the restored filling meridian is the annular-parallel
slope. There is no additional integer twist. Restoring both strips gives

       Sigma_2(L) = S^3_{0,0}(kappa_a union kappa_b)
                  = #^2(S^1 x S^2).

The unlink is determined by this double branched cover: Plotnick's result
is stated explicitly in Gorchakov, Theorem 2.15. Thus L is the
three-component unlink. We have checked this statement in Gorchakov;
the original Plotnick article was not separately inspected.
[Gorchakov, Theorem 2.15](https://arxiv.org/html/2408.12557v1#S2).

Finally, an unlink canonical boundary forces its theta spine to be planar,
as stated by Kauffman--Simon--Wolcott--Zhao, Section 3, page 209, using
Scharlemann's theorem.
[Kauffman et al. (1993), page 209](https://www.math.uic.edu/~kauffman/ThetaCurves.pdf).
This contradicts the hypothesis on Theta. Hence Gamma is nontrivial.

This argument uses simultaneous disjoint annuli upstairs. It does not
assume that individual nugatory disks can be replaced simultaneously
downstairs, nor that a boundary-parallel arc splits off in a relative
tangle.

## Nontriviality of the twisted knots

For mn nonzero, perform the downstairs crossing-circle surgeries
with coefficients +/-1/m and +/-1/n. The ambient manifold remains S^3
and the remaining component is K(m,n). If it were U, an additional +1
surgery on it would produce S^3. All three slopes on the original Gamma
are finite and nonmeridional. Its zero pairwise linking numbers ensure
that the last preferred longitude is the original preferred longitude.

Mangum--Stanford Theorem 2 says that such an S^3 surgery on a
homologically trivial Brunnian link forces the link to be the unlink.
This contradicts the preceding implication and proves assertion 2.
[Mangum--Stanford, Theorem 2](https://msp.org/agt/2001/1-1/agt-v1-n1-p07-p.pdf).

## Automatic determinant one

This part does not assume that Gamma is the unlink. The zero 2-by-2
Seifert matrix of P has symmetrization zero, so the usual branched-cover
presentation gives H_1(Sigma_2(L);Z)=Z^2.

The two smoothing fillings are distance one from the meridional fillings
giving the cover of K(0,0). Thus Sigma_2(L) is integral surgery on the
two lifted cores in S^3, with integral symmetric linking matrix B.
Since coker B=Z^2, the rank of B is zero: B is the zero matrix. Both
smoothing framings and the linking number of the cores are therefore zero.

A full twist has two crossings. In the branched cover, m full twists
change the meridional slope to mu+/-2m lambda, where lambda is the
zero-framed smoothing slope. Equivalently, the filling coefficient is
plus or minus 1/(2m); m=0 denotes meridional filling. The same holds at
the other core. Since the cores are algebraically split and both finite
surgery numerators have absolute value one, the filled manifold has
trivial first homology. It is Sigma_2(K(m,n)), proving assertion 3.

These upstairs coefficients are not the downstairs crossing-circle
coefficients +/-1/m used in the preceding argument.

Change one of the two crossings in the first full-twist box of K(1,1).
The resulting opposite crossings cancel, giving K(0,1)=U. Hence u<=1;
assertion 2 makes u=1. Neither Delta_K=1 nor a_2(K)=0 has been inferred
from this determinant argument.

## Status and remaining input

The skein identity (1) is the four-closure calculation already recorded
in pants_twist_transfer.md: the closures are U,U2,U2,L. The new work
removes the previously independent nontrivial-Gamma hypothesis and
supplies the determinant and unknotting-number conclusions.

What remains is exactly a nonplanar Brunnian theta with the planar
normalized Yamada value. No example is supplied; the previously checked
equal-Yamada pair does not have that value. No theta enumeration was
performed or proposed. The reduction stays in the unknotting-number-one
part of the Jones problem and does not resolve the general conjecture.
