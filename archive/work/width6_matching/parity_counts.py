"""Matching-resolved signed information from three saved LP mixed polynomials.

No new braid generation, geometry, minimization or point enumeration.
Parity classes correspond to the two matchings up to one global swap.
"""
from pathlib import Path
from collections import defaultdict
import json

HERE=Path(__file__).resolve().parent
rows=json.loads((HERE.parent/'width6_targeted/lp_mixed_extrema.json').read_text())
out=[]
for r in rows:
    phi={(a,b):c for a,b,c in r['Phi']}
    parity=[]
    for p in (0,1):
        pp={(a,b):c for (a,b),c in phi.items() if b%2==p}
        specialized=defaultdict(int)
        for (a,b),c in pp.items():specialized[a-2*b]+=c*(-1 if p else 1)
        parity.append({'canonical_b_parity':p,'generic_monomials':len(pp),
            'incidence_count_lower_bound':sum(abs(c) for c in pp.values()),
            'specialized_signed_polynomial':{d:c for d,c in sorted(specialized.items()) if c}})
    d=r['Phi_top_s_degree']
    top=[]
    for p in (0,1):
        terms=[{'a_s':a,'b':b,'raw_coefficient':c,
                'specialized_contribution':c*(-1 if p else 1)}
               for (a,b),c in sorted(phi.items()) if a-2*b==d and b%2==p]
        lb=sum(abs(t['raw_coefficient']) for t in terms)
        top.append({'canonical_b_parity':p,'terms':terms,
                    'incidence_count_lower_bound':lb,
                    'incidence_count_parity':lb%2,
                    'specialized_signed_sum':sum(t['specialized_contribution']for t in terms)})
    before=r['largest_degree_before_cancellation']
    btop=[{'canonical_b_parity':p,
           'specialized_signed_sum':sum(c*(-1 if p else 1)for (a,b),c in phi.items()
               if a-2*b==before and b%2==p)}for p in(0,1)]
    result={'tau':r['tau'],'parity_classes':parity,
            'total_incidence_count_lower_bound':sum(x['incidence_count_lower_bound']for x in parity),
            'top_surviving_degree':d,'top_surviving_by_matching_up_to_swap':top,
            'top_generic_collapsed_degree':before,'top_generic_collapsed_signed_sums':btop,
            'scope':'Exact signed polynomial information and lower bounds for this fixed generic lift; no unsigned geometric counts or minimum are claimed.'}
    out.append(result)
    print('tau',r['tau'],'parity lower bounds',[x['incidence_count_lower_bound']for x in parity],
          'top signed',[x['specialized_signed_sum']for x in top])
(HERE/'parity_counts.json').write_text(json.dumps(out,indent=2)+'\n')
