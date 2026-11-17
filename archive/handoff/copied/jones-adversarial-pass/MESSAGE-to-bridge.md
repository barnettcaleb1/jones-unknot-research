> Public archival edition, prepared 17 November 2026. Historical AI-generated research/review record; not external specialist review. Private instructions and correspondence discussion have been removed with markers, and local paths anonymized. Mathematical claims and verdicts remain historical and may be superseded by the current ledger. No research or computation was rerun for this edition.

# Historical adversarial-pass review, 3 November 2026

[Redacted: private correspondence or workflow instructions.] The review considered the board, letters and lane files through 15:30 and the genus-two verification and design rounds.

WHERE THINGS STAND

The morning was all breadth. Between 10:30 and 12:36 the board logged 34 outputs (7 equivalences, 18 barriers, 8 dictionaries, 1 sieve), every one correct and none narrowing T. The afternoon went better because each lane had one precise question and a referee before anything was banked, and that produced G2-SEP, G2-FINITE, Theorem A, G2-ZRHO and the BBB gap. Now the coordinated target is G2-TWIST, nobody has a mechanism for it,. [Redacted: private correspondence or workflow instructions.]

CHANGE OF ORDER

Burau_4 is now the smallest open rung. G2-TWIST, W(5,1), genus-two faithfulness and T all imply it, so none of them can be easier, and if Burau_4 is unfaithful they are all false and T fails by Ito Cor 3. It also has the most concrete architecture on the board. If BBB's Lemmas 6.3 to 6.6 hold, two-sided parity removes all cancellation (their Lemma 4.2), and the step that cannot work on BI_4 is the comparison of counts, because counts are t = -1 values. None of this makes it cheap. The structure chat points out that a kernel element has infinite (t+1)-adic depth, so any repair has to control moments of every order, which is the full Moody comparison of Thm 2.3,. [Redacted: private correspondence or workflow instructions.]

Multiset statement (~/jones-lanes/g2-proof/ref-transfer/ref-transfer.md, section 4). For every nontrivial proper product Phi in Brun_4 ∩ BI_4, with Gamma the push from Prop 6.7 before its Furthermore modification, the exponent multisets of M_{f(Phi)Gamma} and M_Gamma differ up to translation. Under parity M(-t) has coefficients of one sign, so each multiset is the coefficient vector of M(-t), and once Gamma is written as a braid word both polynomials are Burau matrix products. A size-m comparison cannot separate elements of (t+1)-adic depth above m, so the statement includes the claim that no such Phi is that deep relative to its intersection number.

A statistic that escapes the moment argument is the span. Under parity it is the range of the height function k_i along the arc, since Lemma 3.1 makes each step k_{i+1} - k_i equal to ±|P(Delta_i)|, and on f(Phi)Gamma the 4-disk steps become 5-disk steps. A span inequality between the two arcs is the natural first lemma for the holder. Expect it to be hard, since it is a statement about extreme degrees of Burau_4 images.

[Redacted: private correspondence or workflow instructions.] Proposed falsification check: write Gamma as a braid word for the explicit Phi in ~/jones-lanes/g2-proof/BBB-GAP.md and compare the two polynomials. If either M(-t) has coefficients of both signs, parity fails on that side and the error is in Lemmas 6.3 to 6.6. If the multisets agree, the unmodified push is dead and a different Gamma construction would be required. If they differ, nothing general is decided and the proof attempt can start. G2-TWIST stays the target that faces T, second in line.

RECORD THESE (from my designers and referees; full reports in ~/jones-adversarial-pass/workflow-results.json, scripts in ~/jones-adversarial-pass/work/)

- The collision value N = ±A^k[3] passes every Hermitian, integrality and root-of-unity test we have, including Theorem A at zeta8 and the (A^4-1)^2 divisibility. So does the non-collision value 2A^4 + A^-4. No argument built only from those can prove the span bound or exclude a collision.
- Schottky bounds in Mess word length are false. Take c = ∂{1,2,3}, x = s3(c), c' = s3^2(c), z = s2 s3^-1(c) (four splittings, so the squared twists generate F_4) and B = R_c R_x R_c' R_x^-1 R_c^-1 R_z. Then D(B^4) = 200 < 208. A conjugated letter keeps pair overlap at most 8 however long the conjugator is.
- N is not sign-coherent for 38% of partition-preserving pairs, and along Torelli words the span adds while intersection numbers multiply, so naive adequacy arguments fail.
- On the arc 1 < delta < sqrt 2 the form has signature (4,1), but by G2-DENSE the image is dense there, so complex hyperbolic geometry gives no discreteness. Funar arXiv:2009.05961 section 2.6 already puts the genus-two representation in PU(1,4).
- The 3-bridge plat argument (a genus-two kernel gives 3-bridge knots with V = 1) is complete with two fixes: cite Ichihara-Saito arXiv:1209.0097 Claims 1-2 for the distance growth, and conjugate by tau_c^N so both laminations avoid the disk sets.

[Redacted: private workflow rules.]

WHAT A BREAKTHROUGH HAS TO CONTAIN

It has to see below t = -1. Every knot with V = 1 has determinant 1 and every kernel element is in Torelli, and in both cases t = -1 sees only the homology of a double branched cover. It has to control exact extreme coefficients. It has to use that K is classical, since there are links with the unlink's polynomial and virtual knots with V = 1. Several statements on the board have Khovanov or Floer versions that are already known: Kronheimer-Mrowka for the unknot, Batson-Seed for unlinks, Khovanov-Seidel for faithful braid group actions on arcs. In each case the open part is that a difference the categorified invariant sees can disappear in its Euler characteristic. For G2-TWIST that makes the open part exactly the Eliahou-Kauffman-Thistlethwaite phenomenon restricted to 3-bridge links, so a mechanism there would explain why their cancellation needs bridge number above 3.

[Redacted: message-delivery instructions.]
