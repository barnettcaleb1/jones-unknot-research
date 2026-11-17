"""Exact geometry + exact monodromy, with certified local arc isotopies.

The ear deletion is conservative and is not a tightness/minimality algorithm.
"""
from fractions import Fraction as F
import time
import transport_pl as pl
import transport_simplify as ts
import transport_exact_intersections as ti
import combinatorial_exact_pairing as ep


def exact_model(word,source_caps=((1,2),(3,4)),keep_records=True,
                vertex_limit=15000,pair_limit=2000000,simplify_seconds=3,progress=50000,certificate=False):
    begun=time.monotonic()
    intervals=[sorted(pair)for pair in source_caps]
    if len(intervals)!=2 or max(intervals[0][0],intervals[1][0])<=min(intervals[0][1],intervals[1][1]):
        raise ValueError('source_caps must specify two disjoint horizontal standard arcs; use braid transports for other cap classes')
    source,history=ts.braid_curves([[pl.point(a),pl.point(b)]for a,b in source_caps],
          [-g for g in word],limit=vertex_limit,simplify_seconds=simplify_seconds,certificate=certificate)
    for radius in(F(13,50),F(17,61),F(19,67),F(23,83)):
        target=[ti.figure8(1,2,radius),ti.figure8(3,4,radius)]
        ints=[];checks=[]
        for curve in source:
            row=[]
            for t in target:
                a,b=ti.intersection_records(curve,t);row.append(a);checks.append(b)
            ints.append(row)
        if not any(c['potential_collinear_segments']or c['vertex_intersections']for c in checks):break
    else:raise RuntimeError('All rational target radii had nontransverse intersections')
    count=sum(len(ints[0][m])*len(ints[1][1-m])for m in(0,1))
    if count>pair_limit:raise RuntimeError(f'Pair limit {pair_limit} exceeded: {count}')
    previous=ep.rational_model
    try:
        ep.rational_model=lambda *args:(source,target,ints,checks)
        result=ep.exact_model(word,source_caps,keep_records,progress)
    finally:ep.rational_model=previous
    result.update({'simplification_history':history,'source_curves':[pl.encode(c)for c in source],
            'target_radius':str(radius),'transport_seconds':round(time.monotonic()-begun,3),
            'simplification_certificate':'Each removed vertex swept an exact triangle disjoint from every puncture and every other source segment except retained common endpoints.'})
    return result

if __name__=='__main__':
    import json
    from pathlib import Path
    word=[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]
    result=exact_model(word,certificate=True)
    Path(__file__).with_name('transport_simplified_pairing_14.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('RESULT',result['configuration_count'],result['polynomial'],result['TL_line_specialization'],result['transport_seconds'])
