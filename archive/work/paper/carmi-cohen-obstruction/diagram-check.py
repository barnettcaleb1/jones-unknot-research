#!/usr/bin/env python3.13
"""Exact check of five prescribed rational diagrams, with a uniform mirror.

This script does not enumerate a knot family or search for alternatives.
Only L in (1, 3, 5, 7, 23) causes a diagram to be constructed.
"""

from pathlib import Path
import json
import platform
import sys

ROOT = Path(__file__).resolve().parents[3]
PACKAGES = ROOT / "work/braid_classification/packages"
sys.path.insert(0, str(PACKAGES))

import regina
import spherogram
from spherogram.links.tangles import RationalTangle

OUT = Path(__file__).resolve().parent
VALUES = (1, 3, 5, 7, 23)
BASE = {2: 1, 6: 1, 8: -1}
INHOMOGENEOUS = {2: 1, 4: -1, 6: 1, 8: -1}


def clean(poly):
    return {e: c for e, c in sorted(poly.items()) if c}


def add(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
    return clean(out)


def recurrence(L):
    # Intermediate values here are formal polynomials only, never diagrams.
    out = BASE.copy()
    for _ in range(3, L + 1, 2):
        out = add({e + 4: c for e, c in out.items()}, INHOMOGENEOUS)
    return clean(out)


def coefficients(poly):
    return clean({e: int(str(poly[e]))
                  for e in range(poly.minExp(), poly.maxExp() + 1)})


def evaluate_diagram(link):
    pd_zero = [list(c) for c in link.PD_code()]
    pd_one = [[v + 1 for v in c] for c in pd_zero]
    regina_link = regina.Link.fromPD(pd_one)
    jones = regina_link.jones(regina.Algorithm.Treewidth)
    return {
        "spherogram_PD_zero_based": pd_zero,
        "regina_PD_one_based": pd_one,
        "crossings": len(link.crossings),
        "spherogram_writhe": link.writhe(),
        "spherogram_components": len(link.link_components)
                                  + link.unlinked_unknot_components,
        "regina_components": regina_link.countComponents(),
        "raw_Regina_Jones_string": str(jones),
        "raw_Regina_Jones_coefficients": coefficients(jones),
    }


result = {
    "scope": "Only the five prescribed L values; no alternative family search.",
    "L_values_requested": list(VALUES),
    "python": platform.python_version(),
    "spherogram": spherogram.__version__,
    "regina_version_string": regina.versionString(),
    "package_root": str(PACKAGES),
    "original_family": "RationalTangle(2*L+1, 2).numerator_closure()",
    "selected_family": "RationalTangle(2*L+1, 2).numerator_closure().mirror()",
    "normalization": {
        "Regina_variable": "x is the square root of the usual Jones variable t; exponents in t are doubled.",
        "selected_diagram": "Uniform mirror of the proposed positive rational fraction.",
        "conversion_from_selected_raw_Regina": "Identity: no monomial, sign, or writhe adjustment is made.",
        "conversion_from_original_raw_Regina": "Replace x by x^(-1), realized by the explicitly constructed mirrored diagram.",
        "reference": "Installed regina.Link.jones.__doc__: Adams convention; right-hand trefoil example x^-2+x^-6-x^-8.",
        "target_base_coefficients": BASE,
        "target_recurrence": "V_L=x^4*V_(L-2)+x^2-x^4+x^6-x^8, odd L>=3",
    },
    "records": [],
}

for L in VALUES:
    original_link = RationalTangle(2 * L + 1, 2).numerator_closure()
    original = evaluate_diagram(original_link)
    selected = evaluate_diagram(original_link.mirror())
    expected = recurrence(L)
    actual = selected["raw_Regina_Jones_coefficients"]
    mirrored_original = clean({-e: c for e, c in
                               original["raw_Regina_Jones_coefficients"].items()})
    delta = add(actual, {e: -c for e, c in expected.items()})
    record = {
        "L": L,
        "rational_fraction": [2 * L + 1, 2],
        "original_diagram": original,
        "selected_mirror_diagram": selected,
        "normalized_Jones_coefficients": actual,
        "recurrence_expected_coefficients": expected,
        "actual_minus_expected": delta,
        "actual_mirror_equals_exponent_inversion": actual == mirrored_original,
        "exact_match": actual == expected,
        "single_component": selected["regina_components"] == 1
                            and selected["spherogram_components"] == 1,
    }
    result["records"].append(record)
    print(json.dumps({"L": L, "crossings": selected["crossings"],
                      "raw_Regina_Jones": selected["raw_Regina_Jones_string"],
                      "exact_match": record["exact_match"]}), flush=True)
    if not (record["exact_match"] and record["single_component"]
            and record["actual_mirror_equals_exponent_inversion"]):
        result["status"] = "STOP: candidate family failed at this prescribed diagram"
        break
else:
    result["status"] = "PASS: all five specified mirrored diagrams match exactly"

result["L_values_checked"] = [r["L"] for r in result["records"]]
(OUT / "diagram-check.json").write_text(json.dumps(result, indent=2) + "\n")
print(result["status"])
