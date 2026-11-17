Read outputs/jones-two-band-taylor-obstruction.txt first.

Two independent checks use standard Python only:
  python3 work/research37/verify_certificate.py
  python3 work/research37/replay_independent_brackets.py
The first checks the full saved polynomial identities, normalizations,
and Taylor orders. The second independently recomputes all 48 full cut
polynomials from their planar diagrams by the Kauffman state sum.

Geometric regeneration scripts additionally require Spherogram and Regina.
The saved port maps and orientation choices are included for inspection.
The algebraic proof covers every integer parameter, not just the checked
corners. Six of the original 22 records remain explicitly unmarked and
are outside this conclusion. No full Jones unknot-detection proof or
counterexample has been obtained, and no novelty claim is made.
