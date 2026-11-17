"""Analyze saved fixed-cap Long--Paton cases; no braid search or evaluation."""
import json
from pathlib import Path
import lp_completions as base

HERE = Path(__file__).resolve().parent
lp = base.lp
rows = json.loads((HERE / 'lp_e_fixed_cap_completions.json').read_text())
output = []
for row in rows:
    p = {(a, b): c for a, b, c in row['P_in_s_t']}
    phi = lp.shift(base.divide_one_minus_t(p), -4)
    spec = lp.specialize(phi)
    assert spec == {int(a)-2: c for a, c in row['J_hat_in_s'].items()}

    def line(degree):
        return [{'a_s': a, 'b': b, 'coefficient': c,
                 'collapsed_contribution': int(c * (-1)**b)}
                for (a, b), c in sorted(phi.items()) if a-2*b == degree]

    surviving = max(spec)
    before = max(a-2*b for a, b in phi)
    top = line(surviving)
    before_terms = line(before)
    result = {
        'tau': row['top_cap_transport_tau'],
        'J_A_range': row['J_id_A_range'],
        'J_A_breadth': row['J_id_A_breadth'],
        'Phi_top_s_degree': surviving,
        'Phi_top_terms': top,
        'minimum_geometric_pair_count_on_this_line': sum(abs(z['coefficient']) for z in top),
        'largest_degree_before_cancellation': before,
        'terms_at_largest_degree_before_cancellation': before_terms,
        'coefficient_at_largest_degree_before_cancellation': sum(z['collapsed_contribution'] for z in before_terms),
        'Phi': lp.encode(phi),
        'scope': 'Canonical square-to-torus pairing with compatible lifts. Aggregates give lower bounds, not a full intersection-point list. No global cap-slide minimum certified.'
    }
    output.append(result)
    print('tau', result['tau'], 'degrees', before, surviving,
          'leading line pair-count lower bound', result['minimum_geometric_pair_count_on_this_line'])
(HERE / 'lp_mixed_extrema.json').write_text(json.dumps(output, indent=2) + '\n')
