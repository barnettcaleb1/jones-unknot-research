"""Independent PD bracket checks for the surviving table candidates."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'work/braid_classification/packages'))
sys.path.insert(0, str(ROOT/'work/cancellation19'))
from spherogram import Link
from independent_pd_bracket import evaluate

path = ROOT/'work/proof10/homology/polys.json'
rows = {r['name']:r for r in json.loads(path.read_text())}
candidates = json.loads((ROOT/'work/research22/ribbon_final_candidates.json').read_text())['candidates']
names = sorted({c[end]['name'] for c in candidates for end in ['source','target']})
T = Link(braid_closure=[1,1,1])
bt,_ = evaluate(T.PD_code())
want = {-4:1,-12:1,-16:-1}
options = [s for s in (1,-1) if
           {s*e-3*T.writhe(): (-1)**T.writhe()*n for e,n in bt.items()} == want]
assert len(options)==1
sign = options[0]
out = []
for name in names:
    row = rows[name]
    L = Link(ast.literal_eval(row['pd_notation']))
    b,_ = evaluate(L.PD_code())
    w = L.writhe()
    a = {sign*e-3*w: (-1 if w%2 else 1)*n for e,n in b.items()}
    assert all(e%4==0 for e in a)
    jones = {-e//2:n for e,n in a.items()}
    euler = Counter()
    for field,n,i,j in ast.literal_eval(row['khovanov_reduced_rational_vector']):
        assert field==1
        euler[j] += (-1 if i%2 else 1)*n
    euler = {j:n for j,n in euler.items() if n}
    matches = jones==euler
    mirrored = jones=={-j:n for j,n in euler.items()}
    assert matches or mirrored, name
    out.append({'name':name,'PD':L.PD_code(),'writhe':w,'Jones_q':jones,
                'PD_matches_table_orientation':matches,
                'PD_matches_mirror_of_table':mirrored})
result = {'method':'Independent frontier bracket evaluation; known trefoil calibration',
          'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
          'checked_knots':len(out),'records':out}
(ROOT/'work/research22/candidate_polynomial_verification.json').write_text(json.dumps(result,indent=2))
print('Verified candidate endpoint polynomials from PD codes:', len(out))
