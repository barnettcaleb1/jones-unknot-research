# What specialization can—and cannot—turn into topology

Task: a bounded structural pass on U5-KL6 after the user's resumption. No braid enumeration or geometric replay. This note proves an algebraic consequence of the banked calibration and identifies an exact obstruction to the proposed relative-homology mechanism. It does not prove Jones unknot detection or KL(6,2).

## Conclusion

The extra divisibility of **one scalar pairing** is not specialization torsion, a new layer of the homological degeneration, or evidence that the cap cycle is a boundary. The calibrated degeneration has only one nontrivial layer. A nonzero cap vector always survives that layer, even when it is orthogonal to a chosen cap.

There is a precise positive replacement: vanishing against a complete set of nine cap probes does detect the specialized relative class. The current Jones hypothesis supplies one prescribed scalar equation, not that complete set. Consequently a successful argument needs a genuinely nonlinear restriction on realizable cap configurations, or a theorem that propagates the given vanishing to additional probes. Relative homology exactness alone cannot supply the missing implication.

## 1. Published geometry: the factor is a gluing construction

Bigelow's §3.3 constructs a **genus-two surface** by joining two punctured-torus copies with an annulus implementing a half-rotation around a puncture. Its relative image contains the factor `(1-q)^2(1+qt)`. Section 3.4 gives the parallel-edge genus-three variant, with an additional `(1-t)` factor after passage to a triangle. Thus the published construction is not simply a product torus already invariant under exchange. Its chain-level gluing and relative boundary are essential. Theorem 6.1 identifies the image of absolute-to-puncture-relative homology at `t=-q^-1` with the `(n-2,2)` Temperley–Lieb module. At n=6 this image has dimension nine.

Primary source: [Stephen Bigelow, *The Lawrence–Krammer Representation*, §§3.3–3.4, Theorem 6.1](https://web.math.ucsb.edu/~bigelow/publications/08.pdf).

This published construction supplies explicit classes killed by a relative map after specialization. It does not assert that zero pairing with one square makes an arbitrary class a sum of these geometric surfaces.

## 2. A local normal-form proposition

Let `k=Q(s)`, `q=s^2`, `h=1+qt`, and `O=k[[h]]`, with `t=(h-1)/q`. Work with the actual divided Budney matrix `G(h)` used in `work/width6_lift/C1_calibration.txt`. This is a statement over a local field of rational q-functions; factors such as `1+q` are units here. It is **not** a Laurent-integral unit statement.

The existing calibration gives:

1. `G(0)` has rank six and left/right radicals of dimension nine.
2. The derivative pairing between those radicals is `(1+q) Gamma_TL` in the explicit cap basis.
3. `Gamma_TL` is nonsingular over k.

For completeness, nonsingularity in (3) does not need a numerical test: in the nine standard two-cap link states, its diagonal entries are `delta^2`, and each off-diagonal nonzero entry has delta-degree at most one. Thus its determinant has unique highest term `delta^18`. Here `delta=-s-s^-1` is transcendental over Q.

**Proposition.** Under these three calibrated facts, `G(h)` is equivalent by invertible left and right O-matrices to

```
diag(I_6, h I_9).
```

In particular `ord_h det G = 9`. Since the raw Budney common factor has exactly one h-factor, the corresponding raw matrix has elementary-divisor valuations

```
1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,
```

and raw determinant order 24.

**Proof.** Choose left and right bases whose final nine vectors reduce to the two radicals. The matrix has block form

```
[ D(h)      h B(h) ]
[ h C(h)    h E(h) ]
```

with `D(0)` invertible. By the derivative calibration, `E(0)` is invertible. Invertible block row and column operations split off D and leave the Schur complement

```
h E(h) - h^2 C(h) D(h)^-1 B(h)
 = h [E(h) - h C(h)D(h)^-1 B(h)].
```

The bracketed matrix is invertible over O, proving the assertion. The raw common factor is h times a unit in this local ring, which gives its asserted valuations. This argument establishes matrix equivalence, not an unqualified sesquilinear congruence. The involution preserves the h-adic valuation since `bar(h)=-h/(1-h)`.

No determinant expansion or new enumeration was performed. The proposition is an elementary consequence of the existing exact rank and derivative identities; its novelty is not asserted.

## 3. Vector depth and pair depth are different

For a free O-module with pairing B, define the vector's universal pairing order by

```
nu(x) = min_y ord_h B(x,y).
```

Equivalently one takes the minimum over any O-basis of test vectors. This order concerns the vector, unlike `ord_h B(x,y0)` for a single chosen probe.

A geometric cap lift whose reduction is a nonzero vector in the nine-dimensional radical has `nu(x)=1` for the divided Budney form and `nu_raw(x)=2` for the raw form. To see this directly, its first derivative against the radical is the nondegenerate TL pairing; some radical basis vector therefore gives an exact first-order term. Choosing a different first-order lift cannot remove that term, because both reductions lie in the zeroth-order radicals.

In the terminology of a pairing filtration, the reductions of vectors pairing to order at least one form the nine-dimensional radical. The reductions of vectors pairing to order at least two are zero. There is no further nonzero vector layer for a hypothetical Jones-zero cap to occupy.

By contrast, for a fixed cap y0, the equation

```
Gamma_TL(x0,y0)=0
```

cuts out an eight-dimensional hyperplane inside the nine-dimensional nondegenerate module. A nonzero vector in that hyperplane remains detectable by another probe. Its unusually high scalar vanishing order against y0 is ordinary orthogonality, not membership in a further vector filtration.

This is an exact obstruction to a proposed argument of the form “a third-order raw zero means the cycle belongs to a deeper degeneration layer, hence it is a slide defect.” The antecedent concerns one probe; the proposed conclusion requires all probes. The known cap-slide split example itself has nonzero cap vectors and a vanishing selected pairing, so it already warns against conflating these statements.

## 4. Relative exactness gives a six-dimensional kernel, not the scalar kernel

Over k, let `A` be the specialized absolute module (dimension 15), let

```
i : A -> V
```

be the absolute-to-relative map with its codomain restricted to its image V (dimension nine), and fix a nonzero cap probe C. The functional `ell_C(z)=Gamma_TL(C,z)` is nonzero. Hence

```
dim ker(i) = 6,
dim ker(ell_C) = 8,
dim ker(ell_C o i) = 14.
```

These are immediate rank-nullity consequences of the published image statement and the nondegenerate calibrated TL form. Thus the vanishing observed by one Jones pairing places an absolute class in a 14-dimensional space, while becoming trivial under the relative map places it in a six-dimensional space. A relative long exact sequence identifies the latter kernel; it does not shrink the former to it.

Even replacing a target by “target minus a known unwound representative” does not change this distinction: zero selected pairing of that difference is still a scalar annihilator condition. Realizing a relative-kernel class by permitted slides would then be a second, geometric issue. Neither implication follows just from the exact sequence.

**Complete-probe lemma.** For any z in V,

```
Gamma_TL(C_j,z)=0 for all nine standard cap states C_j
    iff z=0.
```

Proof: the cap states form a basis and the Gram matrix is nonsingular. This is the correct vector-level recognition theorem. A genuine cap state `rho(beta) C_0` is nonzero because rho(beta) is invertible, so it can never satisfy all nine equations. The lemma is useful for rejecting invalid lifting arguments, but is not a route to unknot detection unless the given topology produces enough additional tests. The actual-unknot closure has not been shown to do so.

## 5. The elementary Bockstein route also vanishes on every lifted cap

Suppose a twisted cellular chain model `C_*` over the local ring is free. The short exact sequence

```
0 -> C_* --h--> C_* -> C_*/hC_* -> 0
```

gives a connecting homomorphism

```
beta : H_2(C_*/hC_*) -> H_1(C_*)[h].
```

If a specialized cap class is represented by the reduction of an actual generic cycle, then beta is zero: choose that closed generic cycle as the lift in the definition of the connecting map. The same applies to differences of such lifts. The canonical square/torus classes being used here have generic representatives. Therefore this basic specialization obstruction vanishes on them regardless of whether the selected Jones pairing vanishes.

This does not rule out every categorical or filtered refinement. It rules out using the elementary connecting map as the missing detector without changing the object or providing additional geometric constraints.

## 6. A viable scope for further work

The geometric question is about the intersection of a braid/cap orbit with an orthogonal hyperplane, not about the radical of the ambient form. That orbit is a nonlinear and highly restricted subset of the nine-dimensional module. Pure linear homology, scalar divisibility, and specialization torsion do not see the distinction between a formal combination of cap states and a single realizable cap system.

A future mechanism must therefore supply one of the following, with an actual independent reason:

- a geometric vanishing-propagation law that gives additional independent probes from the actual unknot closure;
- a rigidity theorem for realizable cap-orbit points in the specified hyperplane, using a topological condition absent from arbitrary linear combinations;
- a refined chain or categorical invariant together with a theorem forcing its cancellation from the Jones hypothesis, rather than simply replacing the scalar by a stronger invariant.

None is established here. The strongest finished result of this pass is the local normal-form/vector-depth proposition and its explicit obstruction to the proposed wall-crossing proof. It narrows which kinds of new definitions could help: a deeper **scalar** jet or an ordinary specialization connecting map will not by itself provide the desired geometric recognition.

## Inputs and status

- Existing calibrated identities: `work/width6_lift/C1_calibration.txt`, `generic_intertwiner.json`, `derivative_gram.json` (banked TRUSTED in the scaffold).
- Canonical mixed pairing: `work/width6_targeted/square_torus_repair.txt`.
- Latest corrections: `collab/msgs/20261103-051758-codex.md`, `20261103-080944-codex.md`.
- Primary published input: Bigelow link above.

All new statements with proofs in this note are algebraic consequences of those inputs. They do not upgrade the unverified geometric Key Lemma. No shared scaffold or status file was edited.
