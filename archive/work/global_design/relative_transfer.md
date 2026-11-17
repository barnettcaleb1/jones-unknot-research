# Actual unknot probes span the relative TL skein space

2026-11-03. Bounded theory pass; no computations, census or novelty claim. This concerns multi-strand relative skein spaces, not insertion of an opaque long-knot scalar.

Independent main-agent read: Claude130248 accepted the tree/Seifert-disk spanning argument and functional consequence with the unoriented-module, probe-domain and uniform-framing qualifications. TRUSTED label retained.

## Closure tomography using actual unknots

Let TL_n be the **unoriented**, framed Kauffman bracket skein algebra of (n,n)-tangles over Q(A), with the standard exterior closure. Use the bracket convention `<empty>=1`, `<U>=delta=-A^2-A^-2`. The standard closure trace is denoted tr.

**Proposition.** Skein classes of tangles whose standard closure is an actual unknot span TL_n over Q(A). They may all be chosen so their closures have zero framing, hence tr=delta. Consequently a finite spanning subset can be chosen, and then a basis of Catalan(n) such actual-unknot probes can be extracted.

**Construction and proof.** Start with a crossingless TL basis diagram D. Its standard planar closure is an unlink with c components. There are no closed components wholly inside the tangle box.

The component-adjacency graph inside the box is connected. To see this, connect points of any two diagram arcs by a generic path in the box and record the arcs it crosses. Successive arcs along the path border a common complementary face, giving a walk between their closure-component labels. The complementary faces of a collection of properly embedded crossingless arcs in the box are disks. Within each face one can choose disjoint short bridges between successive boundary arc segments; they can be drawn near the face boundary with distinct endpoints. These give an embedded component-adjacency graph. Choose a spanning tree on the c closure components, using c-1 bridges, all inside the box.

At each bridge choose a small local rectangle containing two arcs of distinct components. Regard their current crossingless configuration as T_old and introduce the two crossings T_+,T_- with that configuration as one smoothing. The local bracket identity is

    T_old = (A T_+ - A^-1 T_-)/(A^2-A^-2),               (1)

after choosing the smoothing labels accordingly. Apply (1) at all c-1 disjoint tree sites. This expresses D as a linear combination of 2^(c-1) signed-crossing diagrams.

Every resulting closure is an unknot. The tree crossings merge the original c components to one. Orient the original circles successively along the tree so their original configuration is the oriented smoothing at every crossing; the tree has no consistency obstruction. For any choices of crossing signs, Seifert's construction has exactly c disks and c-1 bands, is connected and orientable, and has Euler characteristic 1. It is therefore an embedded disk. Its boundary is the unknot.

The resulting closed diagrams may have nonzero framing. Add the required positive or negative Reidemeister-I curls inside the tangle box to make the closure framing zero. This only multiplies each skein class by an invertible power of -A^3, so their span is unchanged. Since the crossingless basis spans TL_n, the proposition follows.

The use of Q(A) is deliberate: (1) divides by A^2-A^-2. No integral-lattice or root-of-unity spanning claim follows from this proof.

The orientations used to exhibit the Seifert disks are chosen separately for the probes. They need not give one prescribed orientation pattern at all boundary endpoints. Therefore this proof does not establish the analogous spanning claim in a fixed oriented-boundary tangle category.

## What this says about a fixed relative operation

**Framed functional consequence.** If two Q(A)-linear closure functionals agree on every zero-framed actual-unknot probe, they agree on all of TL_n. In particular, for a fixed linear operation L on TL_n,

    tr(LX)=u tr(X)

on all these probes, with one fixed unit u, already forces the same identity for every skein input X. Actual unknots are sufficient test inputs; hypothetical Jones-unit nontrivial knots are not needed for this conclusion.

The fixed framing clause cannot be dropped. Merely knowing that every probe's output has normalized Jones polynomial 1 allows a different raw framing unit on each output. Such probe-dependent normalization is not a linear functional, so this tomography argument would not apply. A proposed geometric construction must establish the uniform framing correction or keep the framing data as part of its input/output.

For a concrete class of invertible relative operations, let a,b be fixed braids and put L(X)=a X b. Cyclicity gives

    tr(LX)-u tr(X)=tr((ba-uI)X).

The generic TL trace pairing is nondegenerate: in its semisimple decomposition it is the ordinary matrix trace in each block, weighted by the nonzero quantum dimension Delta_j. Thus preserving the framed unknot probes forces

    rho(ba)=u I                                               (2)

in the full TL algebra. If ba is actually the identity braid, the operation is braid conjugation and changes no closed-knot type. A topologically nontrivial operation of this form requires a genuine projective TL-kernel defect. This is a precise obstruction for left/right braid wrappers, not a classification of all tangle operations.

## Scope for topology-changing reductions

Mutation and other rearrangements can preserve selected closure functionals without being left/right multiplication. The proposition does not classify those maps, nor imply that every trace-preserving map is geometric. Conversely, an input-dependent operation can use extra marked tangle data to evade the fixed-linear-map conclusion; Jones equality of the original closure does not determine that extra data.

The useful new gate is concrete: a proposed fixed multi-strand transfer with a uniform framing law must already pass a spanning set of actual-unknot closures. Once it passes them, it preserves the framed trace universally. Proving that it also imposes primeness, hyperbolicity or unknotting number one is a separate geometric theorem. No such operation is constructed here.

Related positive tomography appears in `twist_fiber.md`: d distinct full Jones polynomials in a meridional twist family recover its d-channel annular skein state. One Jones polynomial alone generally supplies only one of those measurements.
