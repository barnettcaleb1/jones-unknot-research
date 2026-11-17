Evidence for jones-virtual-torus-exclusion.txt

The main result is a family exclusion, not a solution of the general Jones
unknot-detection problem. All standard unknotted-Heegaard-torus markings of
the explicitly given three-crossing surface diagram are covered.

Core verification uses only Python 3's standard library. From the unpacked
directory run, in this order:

  python3 virtual_surface_states.py
  python3 verify_all_markings.py
  python3 verify_flat_braid.py
  python3 verify_virtual_marking_jets.py

The first reconstructs the actual ribbon surface and its complete state sum.
The second checks the full Laurent identities and independently checks the
jet formulas. The third verifies the exact flat-torus realization and the
strict longitude monotonicity giving a closed two-strand braid. The fourth
is an independent exact check of the torus-state Taylor calculation.

Completeness over all integer markings is the written Diophantine proof,
not an inference from a finite computer search. See the main report and
virtual_marking_jets.txt.

exact_eight_markings.json contains additional explicit rational polygons,
their planar diagrams, and simplification results for all eight unit-Jones
markings. The closed-two-braid proof does not depend on that replay.

nonaxis_convention_control.json and exact_nonaxis_control.json record an
additional non-axis convention check. The planar projection's Jones variable
is inverted relative to the algebra convention (global mirroring). The unit
Jones condition and the unknot conclusion are invariant under this inversion.

The JSON evidence is human-readable and the core scripts regenerate their
associated outputs. No external mathematical library is needed for the core.
