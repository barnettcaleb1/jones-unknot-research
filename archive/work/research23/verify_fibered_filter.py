"""Portable, standard-library verifier for the fibered-target certificate.

Uses the small archived candidate_source_subset.json and ribbon_bar_survivors.json,
not the full KnotInfo spreadsheet, polynomial database, or third-party packages.
Put those files beside this script in a flat extracted archive, or retain the
research22/research23 directory layout. The original fibered_target_filter.py
records the independent spreadsheet cross-check and is retained as provenance.
"""
import ast
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def locate(name):
    for directory in (HERE, HERE.parent / 'research22', Path.cwd(),
                      Path.cwd() / 'work/research22',
                      Path.cwd() / 'work/research23'):
        path = directory / name
        if path.is_file():
            return path
    raise FileNotFoundError('Missing archived input: ' + name)

def read(name):
    return json.loads(locate(name).read_text())

def key(record):
    return (record['source']['name'], record['source']['mirror'],
            record['target']['name'], record['target']['mirror'])

def mirror_class(record):
    s, sm, t, tm = key(record)
    return min((s, sm, t, tm), (s, not sm, t, not tm))

def genus_top_rank(row):
    text = row['hfk_polynomial_vector'].strip()
    if not text:
        raise ValueError('Missing HFK vector for ' + row['name'])
    triples = ast.literal_eval('[' + ','.join('[' + v + ']' for v in text[1:-1].split(';')) + ']')
    assert all(isinstance(rank, int) and rank > 0 for rank, _, _ in triples)
    genus = max(a for _, a, _ in triples)
    assert genus == -min(a for _, a, _ in triples)
    top_rank = sum(rank for rank, a, _ in triples if a == genus)
    return genus, top_rank

subset = read('candidate_source_subset.json')
rows = {r['name']: r for r in subset['polynomial_records']}
metadata = {r['name']: r for r in subset['metadata_records']}
prior = read('ribbon_bar_survivors.json')['candidates']
certificate = {key(r): r for r in read('fibered_target_filter.json')}
assert len(certificate) == len(prior)
remaining = []
for pair in prior:
    assert pair['any_length_bars']['pass']
    result = certificate[key(pair)]
    computed = []
    for endpoint in ('source', 'target'):
        name = pair[endpoint]['name']
        assert name.replace('*', '') in metadata
        genus, top_rank = genus_top_rank(rows[name])
        assert result[endpoint + '_genus'] == genus
        assert result[endpoint + '_top_HFK_rank'] == top_rank
        computed.append((genus, top_rank))
    (gs, rs), (gt, rt) = computed
    assert gs == gt, 'The asserted equal-genus scope has changed'
    excluded = gs == gt and rt == 1
    assert result['excluded_equal_genus_fibered_target'] == excluded
    # This field records the separately performed original XLS cross-check.
    # The mathematical filter is independently recomputed above from HFK.
    if 'target_fibered_metadata' in result:
        assert result['target_fibered_metadata'] == ('Y' if rt == 1 else 'N')
    if not excluded:
        remaining.append(pair)

assert {key(r) for r in remaining} == {key(r) for r in read('nonfibered_survivors.json')}
classes = {mirror_class(r) for r in remaining}
one_band_classes = {mirror_class(r) for r in remaining if r['one_band']['pass']}
long_bar = [r for r in remaining if not r['one_band']['pass']]
assert len(classes) == 7
assert len(one_band_classes) == 6
assert len(long_bar) == 2
assert all(r['source']['name'] == '13*n_5018' and
           r['target']['name'] == '13*n_1003' and
           r['minimum_maximum_bar_length'] == 2 for r in long_bar)
assert len(prior) == 48 and len(remaining) == 14
print(json.dumps(dict(verified=True, input_directed_pairs=len(prior),
                     fibered_target_exclusions=len(prior)-len(remaining),
                     remaining_directed_pairs=len(remaining),
                     remaining_mirror_classes=len(classes),
                     remaining_length_one_bar_classes=len(one_band_classes),
                     remaining_minimum_bar_length_two_classes=1), indent=2))
