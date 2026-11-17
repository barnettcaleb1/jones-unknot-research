from pathlib import Path
import shutil, hashlib, json, zipfile
root=Path.cwd()
base=root/'work/proof12'
out=root/'outputs'
summary='''JONES UNKNOT DETECTION: FINITE TESTS AND A REALIZABILITY OBSTRUCTION
31 October 2026

The general problem remains unresolved in this investigation. This pass
established several restricted results, with separate audits and exact
calculations. None is asserted to be new to the literature.

1. SATELLITE RIGIDITY WITHOUT ANY REGULARITY ASSUMPTION
If a fixed satellite construction preserves equality of ordinary Jones
polynomials for all companions, its output is either V_P(U) or V_P(U)V_K,
according to the winding parity. No assumed rational dependence is needed.
For wrapping bound r, at most floor(r/2) explicit equal-Jones companion pairs
suffice to certify this universal statement. A fixed actual pair of knots
separated by EVERY higher color is the key ingredient. The exact proof and
finite test are in Part I.

2. A POSITIVE NONCANCELLATION THEOREM FOR A RESTRICTED TANGLE CLASS
For an unknot-anchored tangle whose reduced mod-2 Khovanov multicurve consists
of one rational component and one standard special component of length4n,
the preferred zero filling cannot have the Jones polynomial of the
2-component unlink. The proof combines forced Euler cancellation with an
unavoidable surviving class in the Bar-Natan spectral sequence. It works
with arbitrary grading shifts. This is a real realization obstruction;
it is not just a nonvanishing observation about one summand. Part II gives
the precise hypotheses, proof, and a nonvacuous example.

3. A COUNTEREXAMPLE ROUTE THAT BECAME LESS PROMISING
An independently checked symmetric-union calculation restricts every
one-region presentation of the fixed Kinoshita-Terasaka knot to two signed
half-twists and partial Jones polynomial1. A nontrivial partial would have
genus1, meridional rank3, and bridge number at least4. It would simultaneously
refute Jones unknot detection AND the meridional-rank conjecture. Part III
explains the chain and records a more direct constructive alternative:
full twists of a ribbon disk with a fixed nonabelian complement group.
No actual Jones-one candidate was obtained. A concrete two-band template was
subsequently constructed and its entire integer twist family excluded by a
leading-coefficient argument; the final geometry note gives that result.

The main missing step is still geometric: control the classical realization
of cancellation when more special components are present, or construct an
actual knot in a topology-certified family whose Jones polynomial is1.
The satellite theorem concerns all Jones fibers and cannot be applied solely
to the special fiber V=1. These limitations are essential.

The accompanying evidence ZIP contains the full research notes, exact
standard-library verifiers, their data, and an integrity manifest. Finite
checks audit the displayed all-parameter proofs; they do not replace them.

'''
parts=[('PART I — WHOLE-FIBER SATELLITE RIGIDITY',base/'satellite_fiber_rigidity.txt'),('PART II — ONE-SPECIAL-COMPONENT REALIZABILITY OBSTRUCTION',base/'homology/one_special_bn_obstruction.txt'),('PART III — TOPOLOGY AND TARGETED COUNTEREXAMPLE ROUTES',base/'tangle/findings.txt')]
parts.insert(2,('BOUNDARY OF PART II — FOUR FORMAL SPECIAL COMPONENTS',base/'homology/four_special_formal_boundary.txt'))
parts.append(('PART IV — AN ACTUAL TWO-BAND FAMILY EXCLUDED FOR ALL TWISTS',base/'tangle/newfamilyproof.txt'))
report=summary+'\n\n'.join('\n'+'='*72+'\n'+title+'\n'+'='*72+'\n\n'+p.read_text() for title,p in parts)
(out/'jones-finite-tests-and-cancellation.txt').write_text(report)
# Preserve import layout used by the independent braid verifier.
files=[base/'satellite_fiber_rigidity.txt',base/'kt_twist_algebra_audit.py',base/'kt_twist_algebra_audit.json']
for sub in ('braid','homology','tangle'):
    files += [p for p in (base/sub).glob('*') if p.suffix in ('.txt','.py','.json') and p.name not in ('watson.txt','kwz2022.txt')]
files += [root/'work/attack_search/search.py',root/'work/proof11/torus_source_audit.py',root/'work/proof11/torus_source_audit.json',root/'work/proof10/tangle/findings.txt']
readme='''REPRODUCIBLE EVIDENCE — 31 October 2026

No generic Jones unknot-detection proof or counterexample is claimed.
Read jones-finite-tests-and-cancellation.txt first. Novelty is unestablished.
The exact algebra verifiers listed below use Python3 standard-library arithmetic.
Extract this archive, retain its directory layout, and run from its root:

 python3 work/proof12/braid/all_color_collision_check.py
 python3 work/proof12/braid/finite_probe_determinant_check.py
 python3 work/proof12/homology/verify_one_special.py
 python3 work/proof12/tangle/kt_partial_filter.py
 python3 work/proof12/kt_twist_algebra_audit.py
 python3 work/proof12/tangle/kt_leading_verify.py

The first imports the included work/attack_search/search.py. Verifiers write
JSON outputs beside themselves. The archive also includes a prior torus
formula audit and the earlier all-odd-pretzel proof used for the KT bridge
restriction. Primary literature is linked in the research notes, not bundled.

The optional geometry reconstruction scripts in tangle/ require Spherogram
and Regina. These dependencies are not bundled. The stored initial/simplified
planar diagrams and cut-link polynomials are included. Algebra-only checks
can run without these external libraries; they do not independently recompute
the geometric cut-link polynomials.

The mathematical proofs cover all colors, all wrapping bounds, or all n in
their stated hypotheses. Finite exact checks are independent error checks,
not claims of exhaustive verification of the generic unknot problem.
'''
entries={str(p.relative_to(root)):p.read_bytes() for p in sorted(set(files))}
entries['README.txt']=readme.encode()
entries['jones-finite-tests-and-cancellation.txt']=report.encode()
manifest=''.join(hashlib.sha256(v).hexdigest()+'  '+k+'\n' for k,v in sorted(entries.items()))
entries['SHA256SUMS']=manifest.encode()
path=out/'jones-finite-tests-and-cancellation-evidence.zip'
with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
    for k,v in sorted(entries.items()):z.writestr(k,v)
print(json.dumps({'report':str(out/'jones-finite-tests-and-cancellation.txt'),'archive':str(path),'entries':len(entries),'bytes':path.stat().st_size},indent=2))
