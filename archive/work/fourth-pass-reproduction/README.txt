JONES UNKNOT INVESTIGATION: FOURTH PASS
31 October 2026

Main result: for the three-twist Ren-pattern family and every companion C,
V(P_{p,q,n}(C))=1 iff (p,q,n)=(-1,1,0) and reduced color-three Jones(C)=1.
Here p,q range over all odd integers and n over all integers.
For C the unknot the sole Jones-one closure is an actual unknot.
The general Jones unknot-detection problem is not resolved.

The four-page proof is delivered separately as jones-fourth-pass.pdf.
Its editable source is fourth-pass-note/main.tex.

To reproduce the central arithmetic and both exhaustive, unbounded solvers,
unpack this archive and run Python 3.10+ from its root:

  python3 pass4/tangle_ren_twists.py
  python3 pass4/ren_jones_locus.py
  python3 pass4/braid_locus_audit.py
  python3 pass4/homology_full_family.py
  python3 pass4/braid_ren_cable.py

These five commands use only the Python standard library. The scripts write
JSON results next to their sources, so elapsed-time fields may change.
The first command regenerates four exact annular skein blocks using all
132 TL6 basis diagrams; the published PD state-sum result is also supplied.

Optional independent diagram checks require Spherogram 2.4.1 and Regina 7.4.1
(tested under Python 3.13). Install them in the chosen Python environment;
the scripts also look in braid_classification/packages, if that directory
exists. These packages are not bundled. Run:

  python3 pass4/tangle_ren_geometry.py
  python3 pass4/tangle_ren_site_map.py
  python3 pass4/homology_ren_satellite.py

Geometry JSON records contain exact diagrams and the two independent
zero-crossing unknot simplifications. Notes explain all normalizations.

Sources: Ren, arXiv:2609.11084v2; Habiro, Geometry & Topology Monographs 4
(2002), 55-68. This is a research calculation, not a peer-reviewed publication.
No novelty claim is made.
