# TEST ONLY (hitpath_test.py monkeypatched the brackets of the TREFOIL; NOT a real hit)
# HIT (cert/run lane, certify.py): CERTIFIED_NONTRIVIAL knot K with V_K = 1
halfword: s.l1.y0.x1.u2
J (lp.J, normalised): +1*t^-7 +1*t^-4 -1*t^-3
V_K (PD bracket, diagram.py): +1*t^1 +1*t^3 -1*t^4
V_K (project bracket, kauffman.py + ident3 normalisation): +1*t^0
V_K (third bracket, audit-2 a2lib): +1*t^1 +1*t^3 -1*t^4
Delta_K: +1*t^0 -1*t^1 +1*t^2
method: nonabelian rep to Aff(F_3), checked on every Wirtinger relator by replay.py
certify.py (cert/run), Aff(F_3), lam=2 (root of Delta mod 3)
certificate (replay.py kind rep):
```
{"kind": "rep", "halfword": "s.l1.y0.x1.u2", "group": "Aff(F_3)", "note": "Aff(F_3), lam=2 (root of Delta mod 3)", "degree": 3, "images": {"1": [2, 1, 0], "2": [1, 0, 2], "3": [0, 2, 1]}, "noncommuting": [1, 2], "checker": "NONTRIVIAL: hom to Aff(F_3) (degree 3), all 3 relators checked, images of generators 1,2 do not commute"}
```
A second independent check (other implementation, e.g. SnapPy) must follow (BRIEF section 5).
