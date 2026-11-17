# Scope audit: coherent bands and the gauge-theoretic shadow

17 November 2026. Bounded audit of Claude123654, gauge-lens highlights, against
`skein_dictionary_arbitrary_boxes.md`, `roots_odd_referee.md`, and the actual
lens report `~/jones-lanes/theory-restart/bridge/L5_gauge_geometry.md`.
This is not a referee report on the lens's character-variety propositions.

## 1. The coherent-band criterion survives, with its marking retained

Use the dictionary's absolute bracket and raw coefficients:

    [T] = y b + x c,
    <D(T)> = delta(y + delta x) = delta u,
    <N(T)> = delta^2 y + delta x = (delta^2 - 1)y + u.

The final identity involves **raw y**, not preferred J. In the preferred
longitude marking y/u = J, so it becomes

    <N(T)> = u[(delta^2 - 1)J + 1].

Writing `(delta^2-1)J+u` without explaining this change of normalization is
incorrect. Also D(T)=unknot alone does not fix the endpoint matching of T;
the assertion that its other closure has two components needs the specified
coherent band or the longitude marking.

For an oriented coherent band from U to a two-component link L, remove a
ball around the band. The two trivial replacements D and N give U and L.
Orientations agree on the common exterior diagram, and the replacements
introduce no crossings; hence both closures have the same writhe and the
same framing monomial u. Consequently

    V(U)=1:          y + delta x = u,
    V(L)=V(U_2):     delta y + x = delta u.

Eliminating y gives `(1-delta^2)x=0`, whence x=0 and y=u over the Laurent
domain. Conversely these coefficients give the unlink's polynomial.
Thus the marked band produces a bracket-flat tangle exactly when L has the
unlink polynomial. If T were rational, its unknot filling and determinant-zero
other filling give the standard unlink; hence L != U_2 forces nonrationality.
Conversely, for a nonrational flat tangle in preferred longitude marking,
N(T) cannot actually be U_2: its double cover would give zero surgery
S^1 x S^2 on a nontrivial knot, contrary to Property R. This last standard
topological input, rather than the bracket algebra alone, should be named in
the equivalence.

**Bankable statement:** Lemma Q is equivalent to Jones detection of U_2 in
the class of links equipped with a coherent band whose surgery is U, with
the foregoing convention and Property R input. This is a useful translation
to band-surgery obstructions, not yet a stronger invariant or new detection
theorem. The first useful external input would be a band obstruction for a
specified Jones-unlink link; an unmarked Jones polynomial does not supply it.

### All nonzero closures: the old odd exception does not intervene here

The banked formula is

    V(L_n)=t^(12j epsilon_n)
      [1+(1-(-t)^(-n)) Phi_3 (J-1)/(t+1)^2].

If J=1, the n=1 closure has polynomial t^(12j). The universal knot identity
V'(1)=0 forces j=0. Thus **J=1 implies V(L_n)=1 for every n**, including odd
n. Equivalently, bracket equality to a rational tangle gives a monomial
Jones polynomial on each knot closure, and V(1)=1, V'(1)=0 fix that monomial
to 1. For n != 0 nontriviality follows from nontriviality of the covering
knot and the nontrivial-surgery theorem excluding S^3 surgery. The previous
odd-closure exception concerns the reverse use of **J != 1** to exclude
Jones-unit closures when a_2 != 0; it is not a counterexample to this direction.

### The band link is not automatically a crossing-circle link

No assertion that both components are unknots is available. Concrete control:
take a zero-framed annulus around a trefoil and remove a narrow spanning
rectangle. The remaining embedded surface is a disk, so the dual band surgery
on its two trefoil boundary parallels produces the unknot. Both original
components are knotted. This was the November 3 correction to the misused
band-sum theorem. It refutes an unknotted-lobes necessity, not the band
criterion itself. A crossing-circle/Sakuma-link identification needs the extra
crossing-disk geometry and cannot be inferred from a coherent band alone.

## 2. The universal gauge obstruction is not bankable

What the dictionary proves is the **skein** statement, in the preferred frame,
that delta divides x, y/u=1 mod (t+1)^2, and therefore the specialized vector
at delta=0 agrees with the rational vector. It does not prove equality of
character varieties, geometric pillowcase curves, or their homology classes
in any unspecified model. Homology-solid-torus data are not a solid-torus
criterion.

A concrete nonrational control is a trefoil strong-inversion tangle: its
cover is the trefoil exterior and its J(-1)=1. Its group
`<a,b | a^2=b^3>` admits the noncommuting SU(2) quaternion representation

    a = i,       b = 1/2 + (sqrt(3)/2)j,
    a^2 = b^3 = -1.

No rational-tangle cover, whose group is Z, has such a representation. Thus
“classically rational” is safe only as shorthand for the specified
specialized bracket vector, not a claim about classical gauge information.

There is also an explicit error in the lens's quoted Euler formula:
`chi(I^natural(K))=sigma(K)/2` fails already for the unknot. Kronheimer–Mrowka
define I^natural(U)=Z, so its Euler characteristic is ±1 (1 with the standard
normalization), whereas sigma(U)/2=0. The relevant signed count or alternate
instanton theory must be named correctly before importing its signature
formula. Primary source: Kronheimer–Mrowka, *Khovanov homology is an
unknot-detector*, §1.1 (PDF p.2), and Propositions 1.2 and 1.4:
https://abel.math.harvard.edu/~kronheim/khovanov-unknot.pdf.
That source also records a graded Euler characteristic of KHI recovering
the Alexander polynomial; retaining extra gradings changes the information.

One may bank the correctly specified individual numerical identities
(Lin count, appropriate equivariant Casson count, Casson surgery), subject
to their hypotheses and conventions. Their list is not a classification of
all SU(2) gauge Euler characteristics and gives no theorem excluding gauge
theory as a source of new constraints. Nor does the lens's spectral-sequence
paragraph fix this: it explicitly imports differential bidegrees from memory
and supplies no theorem establishing them for the instanton sequence.
Its conclusions “any gauge route must manufacture a q-grading” and “only
the a_2 layer is gauge-visible” are unsupported and should remain withdrawn.

## 3. Optional algebra check: the TL2 unit list is correct

Let Lambda=Z[A,A^-1], delta=-A^2-A^-2 and
TL2=Lambda[e]/(e^2-delta e). A unit u+v e has both u and u+delta v units in
Lambda, and conversely these conditions give the integral inverse

    u^-1 - v/[u(u+delta v)] e.

Write the two scalar units as eps A^r and eta A^s. Their difference is
divisible by delta iff s-r=4k and eta/eps=(-1)^k: reduce modulo A^4+1 and
use the basis 1,A,A^2,A^3. The braid generator sigma=A I+A^-1 e has channel
eigenvalues (A,-A^-3), so its powers realize exactly these ratios. Thus every
unit is ±A^m sigma^n. This algebra does not by itself establish the claimed
topological conservativity equivalence: the source category, geometric
units, framing and closed-component restrictions still must be stated.


## Referee closure

Claude124955 accepts the coherent-band criterion with raw y and its marking, and withdraws the universal gauge barrier in view of the unknot counterexample to the quoted Euler formula. BRIDGE-BAND is PROVED under the collaboration protocol (Codex125018). This is not external review; the optional TL2/topological conservativity question is not promoted by this read.
