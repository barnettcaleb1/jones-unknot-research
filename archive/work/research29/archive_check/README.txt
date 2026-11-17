Jones unknot investigation — pass 29 evidence
1 November 2026 UTC

No proof or counterexample to Jones unknot detection is supplied.

The principal result is a precisely specified Watson family with one
ordinary Jones polynomial and unbounded dimension-three colored Jones
span. Its all-parameter proof uses Watson invariance and generic fusion;
the finite calculations verify actual diagrams and normalization. This
rules out a proposed intermediate bound, not the original conjecture.
There is no claim that this family or deduction is new in the literature.

The second result explains why positivity of surface quantum traces
does not itself control the invariant after filling into S^3. The third
is a limited exclusion for a braid-kernel construction. Neither provides
the missing global geometric theorem.

Files:
  colored_global.txt                 Family definition and general proof.
  colored_audit.txt                  Independent fusion/normalization audit.
  watson_color3_samples.json         Eight actual PDs and cable polynomials.
  colored_family_certificate.json    Normalized exact arithmetic certificate.
  verify_colored_family.py           Arithmetic and optional diagram replay.
  positivity_geometry.txt           Exact positivity obstructions and sources.
  curve_projector.txt                Same-subset twist restriction and scope.
  verify_joint_support.py            Exact classical joint eigenspace weights.
  MANIFEST.sha256                    Integrity hashes.

Portable verification, requiring only Python 3:
  python3 verify_colored_family.py
  python3 verify_joint_support.py

Full diagram regeneration additionally requires Python 3.13 with the
tested Regina 7.4 and Spherogram 2.4.1 packages:
  python3 verify_colored_family.py --diagrams --packages /path/to/packages
The optional JONES_REPLAY_PACKAGES environment variable also sets this
directory. Platform-specific binaries are not included in the archive.
The main investigation regenerated all eight samples twice, including
an independent root replay after the package-path correction.

Proof obligations and limits:
  * A fixed even-twist permutation and one endpoint trace establish
    knot connectivity for every parameter; finite samples alone do not.
  * Watson's theorem supplies the ordinary-polynomial equality for all
    parameters. The script does not reprove this published theorem.
  * Fusion gives a finite exponential expression for every parameter;
    the eighth recurrence check is not an induction proof by itself.
  * Normalized H3(1)=1 and H3'(1)=0 prevent unequal samples from differing
    by a sole moving monomial. Multiple slopes give unbounded span.
  * Ordinary Khovanov homology remains constant in this simple-tangle
    family, so the ordinary-rank proof scaffold survives this test.

Strategic continuation:
The complete positive scaffold needs a bound on reduced rational
Khovanov rank throughout just one nonempty ordinary Jones fiber.
For an anchor J in that fiber, a hypothetical V_K=1 would imply
r(J#K^m)=r(J)r(K)^m, forcing r(K)=1 and then the unknot.
The bound remains unproved. A full counterexample scaffold instead
needs an actual noncentral generic Jones braid-kernel element; Ito
supplies the topological endpoint once that input exists. No such
element is supplied here. Additional local estimates should only be
pursued if they furnish one of these missing global inputs.
