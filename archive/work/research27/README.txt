JONES UNKNOT DETECTION: BING REALIZATION AND GLOBAL MECHANISM AUDIT
Research pass 27, 1 November 2026 UTC

STATUS
No proof of Jones unknot detection and no counterexample have been obtained.
These are research deductions from cited published inputs, with exact algebra
checks. No claim of novelty, formal verification, or external peer review.

THE COMPLETE CONDITIONAL ENDPOINT
If there exists a nontrivial knot C whose normalized dimension-three colored
Jones polynomial H_3(C) equals 1, the actual Bing pattern P_C produces a
nontrivial Jones-one knot on every nontrivial companion J. The topology and
the polynomial calculation are included. The missing premise is the existence
of C. This is the same premise reached by the previous Whitehead construction.

EXACT RESULT
For delta=-A^2-A^-2, q=A^-4, and annular core z, our derivation gives

 [P_C] = delta H_3(C) + (1-H_3(C)) z^2/delta,

 V_{P_C(J)}-1 = -(delta^2-1)/delta^2
                         (H_3(C)-1)(H_3(J)-1).

The rational-function identities use zero framing and H_N(U)=1. No value at
a pole and no geometric wrapping number are inferred. Two nonzero input
deviations cannot cancel. This makes further two-input searches in this family
unproductive without a new way to obtain an H_3-unit knot.

CONTENTS
* tangle_realization.txt: actual pattern, annular reconstruction, topology,
  satellite product, and a separate necessary condition for a local move.
* bing_formula_audit.txt: independent checks and normalization details.
* verify_bing_formula.py: portable exact Laurent-algebra checks; standard
  Python library only. Run: python3 verify_bing_formula.py
* braid_mechanism.txt: why disk/sphere point-pushing does not automatically
  annihilate the missing generic Jones blocks; dense image is not faithfulness.
* homology_global.txt: canonical connected-sum Smith inequalities are automatic;
  additional ribbon/Steenrod observations and exact scope of Gujral-Wang.
* manifest.json: SHA-256 hashes of every other archive member.

PROOF SCAFFOLD IMPLICATIONS
The global proof route still needs a bound on bridge number, homology rank,
or quantum spread throughout one specified nonempty whole Jones fiber.
Connected sums then finish the proof. A bound only on a diagram family does
not cover that fiber. A bound only on the unit fiber is an equivalent
reformulation of the original question, not evidence for a solution.

The braid counterexample route still needs an actual nontrivial braid in the
full generic Jones kernel. Ito's theorem supplies the nontrivial-knot endpoint.
Partial kernels and formal matrices do not supply this premise.

PRIMARY SOURCES
Suzuki, Bing doubling and the colored Jones polynomial, Theorem 3.2,
Corollary 4.4 and Lemma 6.1: https://arxiv.org/pdf/1305.0602
Cimasoni, Slicing Bing doubles, Section 1:
https://www.unige.ch/~cimasoni/Bing.pdf
Kuperberg, Denseness and Zariski denseness of Jones braid representations,
Theorem 1.1: https://msp.org/gt/2011/15-1/gt-v15-n1-p02-s.pdf
Kasahara, Propositions 2.4 and 2.6: https://arxiv.org/pdf/0803.0304
Stoffregen-Zhang, Localization in Khovanov homology, Theorem 1.1 and (1.6):
https://arxiv.org/pdf/1810.04769

LIMITS OF THE CHECKS
The Python verifier checks elementary polynomial identities only. It does not
verify Suzuki's theorem, topological incompressibility, or any missing global
premise. Primary papers are linked rather than reproduced in this archive.
The living synthesis is outputs/jones-full-proof-scaffolds.md.
