Evidence for the 31 October 2026 proof-mechanism pass

Start with outputs/jones-proof-mechanisms.txt. The general Jones unknot
problem is not solved here. The restricted pretzel result has an explicit
symbolic proof; finite experiments are supplementary checks.

Pure Python (standard library only):
 python3 work/proof9/toric/pretzel_moments.py
 python3 work/proof9/toric/pretzel_locus_audit.py
 python3 work/proof9/homology/kt_bar_check.py
 python3 work/proof9/homology/formal_band_test.py

The locus audit also reruns the complete exact exponent-collision solver.
The moments script asserts the displayed identities in both parity cases.

Optional independent topology checks require Spherogram and Regina in the
Python environment (or work/braid_classification/packages). They are not
bundled. Run the solver before pretzel_audit.py; run lando_probe.py before
extreme_layers.py. Previously generated JSON results are included.

Detailed human audits are in work/proof9/tangle/*txt,
work/proof9/quantum/handlebody_vacuum_lemma.txt, and
work/proof9/homology/result.txt. The homology note separates its optional
preprint-dependent rank observation from the main proof mechanisms.

No novelty claim is made for any mathematical statement in this archive.
