# A global geometric candidate: link-compatible Turaev destabilization

Design proposal, not a proof. No computation. This is the weaker of the two new candidates; its geometric bridge is not established.

## Object and known endpoints

For a diagram D of an arbitrary classical knot K, use its link-adapted Turaev Heegaard diagram (Sigma,alpha,beta,D). The all-A and all-B states provide the two sides, and D is alternating on Sigma. [Armond–Druivenga–Kindred, arXiv:1408.1304, Theorem 4.1](https://arxiv.org/pdf/1408.1304) characterizes precisely which such marked Heegaard diagrams come from Turaev surfaces.

Every positive-genus Heegaard splitting of S3 is stabilized by Waldhausen's theorem; see the [Schleimer exposition](https://arxiv.org/abs/0904.0182). This produces a pair of compressing disks whose boundaries intersect once. It does NOT say that the pair is compatible with the marked knot diagram. That distinction is the entire difficulty, and parallels the relative-position errors already found in the earlier width work.

Define a compatible cancellation to mean a cancelling disk pair, together with an isotopy of the marked link and the required attaching-circle slides, such that destabilization gives another diagram satisfying the Armond–Druivenga–Kindred Turaev conditions, represents the SAME knot, and lowers the surface genus. This definition asks for an actual geometric certificate, not just an algebraic rank reduction.

## Proposed mechanism

Expand the bracket using the checkerboard ribbon graph or quasi-trees, but retain the attaching curves alpha,beta as additional geometric data. Group states according to the strands crossing a neighborhood of a chosen candidate cancelling handle. One seeks an equality-case theorem: if the whole knot has V=1, at least one ambient cancelling pair can be made compatible in the above sense.

This would turn polynomial cancellation into removal of an actual handle. It is a precise proposed mechanism, but no positivity or state-pairing theorem currently supplies it. Merely knowing that the unmarked Heegaard surface destabilizes would be an invalid proof.

## End-to-end chain

1. Choose a classical diagram and its Turaev data. Published.
2. Translate Jones equality into the exact state/quasi-tree sum, retaining the attaching curves rather than forgetting the S3 realization. Published dictionary; the extra organization is a proposed setup.
3. Positive genus plus V=1 forces a compatible cancelling pair. OPEN, central crux.
4. Perform the geometric cancellation and retain a Turaev diagram of the same knot of smaller genus. Part of the certificate in step3; any proposed local rule must prove this, not assume it.
5. Iterate until genus zero. Conditional elementary induction.
6. A genus-zero Turaev knot is alternating; V=1 then forces the unknot by the alternating crossing-number theorem. Published.

One may instead choose a genus-minimizing Turaev diagram: step3 would contradict positive minimal genus immediately. The problem is still step3, not the minimization.

## Why it is different, and why it may fail

This is not N2's claim that the first hypothetical extreme must survive. Actual homology may cancel at both extremes; a handle move could depend on internal state sectors and three-dimensional attaching data. It is also not the U5 quotient problem: every knot has this construction and no actual unknot surgery is assumed.

Classicality is substantive: Sigma is a Heegaard surface of S3, with its actual pair of disk systems. An arbitrary virtual diagram on a surface does not supply that marked S3 splitting. One component must enter the compatibility theorem. A possible place to use it is that a connected spanning surface with one boundary component has a nondegenerate mod-two intersection pairing, whereas extra boundary components give a radical. That observation does not yet prove compatible cancellation or explain why EKT links fail it; the B1 gate is not solved merely by mentioning it.

The known Turaev-genus-one detection theorem of [Lowrance–Spyropoulos, 2017](https://nyjm.albany.edu/j/2017/23-71v.pdf) supports a genus organization, but its coefficient argument does not prove this stronger geometric cancellation statement. Extending from genus one cannot be assumed inductive.

## First page, before any search

Specify the local marked-handle certificate and derive its exact skein identity. Check that it survives the permitted disk slides and represents the same link. Then look for a combinatorial condition in the grouped state sum that forces this certificate. A statement using only genus, signature, determinant, or ambient stabilization is already too weak.

If no such condition appears on that page, park the route. No evidence here warrants a large computation or an assertion that Jones equality selects the needed disks. Novelty is unassessed; the proposal is new to this board, not claimed new to the literature.
