"""Independent bounded regression of the *unbounded* root classifier.

This regression tests the implementation; the highest-degree proof supplies
the unbounded certificate. No floating point numbers or external packages.
"""
import json,random
from pathlib import Path
from braid_all_powers import solve_integer_roots,eval_coeff
from tl5_block import verify_all_basis_traces

def on_line(point,line):
    delta=[a-b for a,b in zip(point,line['origin'])]
    step=line['step'];z=None
    for d,s in zip(delta,step):
        if not s:
            if d:return False
        else:
            if d%s:return False
            q=d//s
            if z is not None and z!=q:return False
            z=q
    return True

def contained(point,solution):
    return solution['all_pairs'] or list(point) in solution['roots'] or any(on_line(point,L) for L in solution['lines'])

rng=random.Random(20261031)
cases=[[{},{},{},{}],[{0:1},{},{},{}],[{},{0:1},{0:-1},{}],
       [{0:1},{},{},{0:-1}],[{0:1},{0:-1},{0:-1},{0:1}]]
for _ in range(1500):
    cases.append([{e:c for e in range(-4,5) if (c:=rng.choice([0,0,0,-2,-1,1,2]))} for _ in range(4)])
for coeff in cases:
    sol=solve_integer_roots(coeff)
    for m in range(-12,13):
        for n in range(-12,13):
            assert contained((m,n),sol)==(not eval_coeff(coeff,m,n)),(coeff,m,n,sol)

root=Path(__file__).resolve().parent
saved=json.loads((root/'braid_all_powers_results.json').read_text())
for row in saved['rows']:
    coeff=[{int(e):c for e,c in p.items()} for p in row['coefficients']]
    assert solve_integer_roots(coeff)==row['solution']
    assert not row['nonzero_roots'] and not row['nonzero_families']
    assert not row['solution']['all_pairs']
report={'synthetic_cases':len(cases),'brute_force_points_per_case':625,
        'synthetic_point_checks':625*len(cases),'saved_certificates_replayed':len(saved['rows']),
        'TL5_basis_trace_checks':verify_all_basis_traces(),'status':'passed'}
(root/'independent_checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report))
