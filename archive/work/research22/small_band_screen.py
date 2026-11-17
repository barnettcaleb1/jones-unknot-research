"""Bounded geometric screen, not a test of all ribbon concordances.

Try one short band on one retained diagram for each candidate target.
Only diagrammatically simplified split unknots are capped off. A failure
to find such a component does not prove the link nonsplit.
"""
import ast
from collections import Counter
import json
from pathlib import Path
import random
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'work/braid_classification/packages'))
sys.path.insert(0, str(ROOT/'work/cancellation19'))
from spherogram import Link
from spherogram.links.bands.core import banded_links, normalize_crossing_labels
from independent_pd_bracket import evaluate

random.seed(2201)
rows = {r['name']: r for r in json.loads((ROOT/'work/proof10/homology/polys.json').read_text())}
candidates = json.loads((ROOT/'work/research22/ribbon_final_candidates.json').read_text())['candidates']
targets = sorted({c['target']['name'] for c in candidates})

trefoil = Link(braid_closure=[1, 1, 1])
bt, _ = evaluate(trefoil.PD_code())
expected = {-4: 1, -12: 1, -16: -1}
conventions = [s for s in (1, -1) if
               {s*e-3*trefoil.writhe(): (-1)**trefoil.writhe()*n for e, n in bt.items()} == expected]
assert len(conventions) == 1
sign = conventions[0]

def jones_q(link):
    b, _ = evaluate(link.PD_code())
    w = link.writhe()
    a = {sign*e-3*w: (-1 if w % 2 else 1)*n for e, n in b.items()}
    assert all(e % 4 == 0 for e in a)
    return {-(e//2): n for e, n in a.items()}

def tabulated_euler(row):
    e = Counter()
    for field, n, i, j in ast.literal_eval(row['khovanov_reduced_rational_vector']):
        assert field == 1
        e[j] += (-1 if i % 2 else 1)*n
    return {j:n for j,n in e.items() if n}

out = ROOT/'work/research22/small_band_screen.jsonl'
with out.open('w') as stream:
    for name in targets:
        start = time.monotonic()
        L = Link(ast.literal_eval(rows[name]['pd_notation']))
        normalize_crossing_labels(L)
        P = tabulated_euler(rows[name])
        actual = jones_q(L)
        assert actual == P or actual == {-j:n for j,n in P.items()}, name
        # The two smallest candidate targets receive one extra band length.
        max_len = 3 if name in {'12*n_244', '13*n_420'} else 2
        counts = Counter()
        hits = []
        for M, spec in banded_links(L, max_twists=2, max_band_len=max_len, paths='shortest'):
            counts['bands'] += 1
            M.simplify('global')
            if M.unlinked_unknot_components == 1 and len(M.link_components) == 1:
                counts['diagrammatically_split_unknot'] += 1
                value = jones_q(M)
                if value == actual:
                    counts['Jones_preserving_survivor'] += 1
                    hits.append({'band':str(spec), 'result_PD':M.PD_code(),
                                 'Jones_q':value,
                                 'warning':'Endpoint isotopy and nonzero homological complement NOT certified.'})
        record = {'target':name, 'input_PD':L.PD_code(),
                  'max_band_length':max_len, 'max_half_twists':2,
                  'paths':'shortest', 'counts':dict(counts), 'hits':hits,
                  'seconds':round(time.monotonic()-start,3)}
        stream.write(json.dumps(record)+'\n')
        stream.flush()
        print(name, dict(counts), record['seconds'], flush=True)
