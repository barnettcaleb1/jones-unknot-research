"""Reproduce the equal-genus/fibered-target obstruction; no new knot search."""
import ast
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
rows = {r['name']: r for r in json.loads((ROOT / 'work/proof10/homology/polys.json').read_text())}
prior = json.loads((ROOT / 'work/research22/ribbon_bar_survivors.json').read_text())['candidates']

def genus_top_rank(row):
    text = row['hfk_polynomial_vector'].strip()
    if not text:
        raise ValueError('Missing HFK data: ' + row['name'])
    triples = ast.literal_eval('[' + ','.join('[' + v + ']' for v in text[1:-1].split(';')) + ']')
    genus = max(a for rank, a, maslov in triples)
    return genus, sum(rank for rank, a, maslov in triples if a == genus)

# Independent metadata cross-check. These packages/data were already archived.
sys.path.insert(0, str(ROOT / 'work/proof10/homology/packages'))
import xlrd
sheet = xlrd.open_workbook(str(ROOT / 'work/proof10/homology/knotinfo_data_complete.xls')).sheet_by_index(0)
header = sheet.row_values(0)
metadata = {sheet.cell_value(i, 0): dict(zip(header, sheet.row_values(i))) for i in range(2, sheet.nrows)}

out = []
for candidate in prior:
    source, target = candidate['source'], candidate['target']
    gs, rs = genus_top_rank(rows[source['name']])
    gt, rt = genus_top_rank(rows[target['name']])
    mf = metadata[target['name'].replace('*', '')]['fibered']
    assert mf in ('Y', 'N')
    assert (rt == 1) == (mf == 'Y')
    assert int(metadata[source['name'].replace('*', '')]['three_genus']) == gs
    assert int(metadata[target['name'].replace('*', '')]['three_genus']) == gt
    out.append(dict(source=source, target=target,
                    source_genus=gs, target_genus=gt,
                    source_top_HFK_rank=rs, target_top_HFK_rank=rt,
                    target_fibered_metadata=mf,
                    excluded_equal_genus_fibered_target=(gs == gt and rt == 1)))

dest = ROOT / 'work/research23'
(dest / 'fibered_target_filter.json').write_text(json.dumps(out, indent=2) + '\n')
remaining = [r for r in out if not r['excluded_equal_genus_fibered_target']]
(dest / 'nonfibered_survivors.json').write_text(json.dumps(remaining, indent=2) + '\n')
print(json.dumps(dict(input_directed_pairs=len(out),
                      excluded_directed_pairs=len(out)-len(remaining),
                      remaining_directed_pairs=len(remaining),
                      remaining_simultaneous_mirror_classes=len(remaining)//2,
                      target_top_rank_counts=dict(Counter(r['target_top_HFK_rank'] for r in out))), indent=2))
