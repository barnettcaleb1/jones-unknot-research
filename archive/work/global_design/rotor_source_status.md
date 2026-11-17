# Rotor anchor: source/status audit only

Date: 2026-11-03. Bounded primary-source refresh. Branch remains archived; no new rotor, unknot completion, or candidate computation was produced.

## Exact literature outcome

Anstee--Przytycki--Rolfsen, *Knot polynomials and generalized mutation*, Topology and its Applications 32 (1989), 237--249, Theorem 3.1 proves equal Kauffman brackets for n-rotants with n<=5; oriented rotants have equal normalized Jones polynomials. Their Question 3.5 explicitly asks whether the unknot or unlink can have a nontrivial n-rotant. The paper does NOT prove that unknot rotants are unknots.

https://arxiv.org/html/math/0405382

The required operation is a spatial half-turn about an allowed in-plane rotor axis, with over/under data transformed as an actual three-dimensional rotation. Axes through marked boundary points and mirror reflection are excluded by Section 1.1. The rotor has 2n boundary points, two per face, and genuine n-fold symmetry preserving over/under crossings. A generic many-string tangle flip is not covered.

MacColl, *Rotors in Khovanov Homology*, Canadian Mathematical Bulletin 59(1) (2016), 159--169, Question 1.4 again states the unknot-rotant question as open. His Theorem 1.5 gives infinitely many order-four rotant pairs distinguished by Khovanov homology while sharing the Jones polynomial. These examples prevent importing Conway-mutation Khovanov invariance to arbitrary rotants; they do not give an unknot anchor. The 2018 date shown on the Cambridge webpage is not the journal-volume year.

https://arxiv.org/html/1501.00851
https://doi.org/10.4153/CMB-2015-034-6

A targeted literature search found no later primary-source theorem resolving the general unknot-rotant question. This is a bounded search outcome, not a proof of absence.

## Existing archived work: do not rediscover

- `outputs/jones-rotor-topology-and-surgery.txt`: source question, unknot-completion discussion, symmetry obstruction, and an uncompleted symmetric globally nugatory surgery design.
- `outputs/jones-rotor-family-obstruction.txt` and `work/strategy14/braid_rotor_obstruction.txt`: internally audited obstruction for actual boundary-parallel C4 rotors with four arcs and no closed components. It is a scoped deduction, not a published general unknot-rotant theorem.
- `work/strategy15/rotor_topology.txt`: the rotor rotation need not extend across an unknot stator. Compressibility of the splitting sphere does not provide that extension. The appendix records the boundary-parallel-stator reembedding argument, with its scope qualifications.
- `work/research33/rotor_candidate.txt`: the actual four-sector necklace assembled from identical two-string tangles was tested. Its unknot anchor flips to the unknot. More decisively, its flip decomposes into ordinary Conway mutations for every stator, so changing only that stator cannot rescue the design.

## Decision

No general unknot-preservation theorem blocks all 4/5-rotors, and general rotants are not forced to preserve Khovanov homology. Nevertheless, merely re-proposing the APR question is not a new design. Progress would require an ACTUAL non-necklace, non-boundary-parallel rotor with a marked, independently certified unknot completion. No such object was supplied in this audit. Stop this branch pending a new concrete geometric input.
