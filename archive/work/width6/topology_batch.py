"""Reproduce cheap geometric classification of the supplied exact-zero cases.

Consumes probe_candidates.json; does not generate or search any braid words.
Property R is a trusted theorem-level implication applied only after actual
unlink/unknot simplification, never merely to their Jones polynomials.
"""
import json,collections,random
from pathlib import Path
import probe
import topology_classifier as tc
HERE=Path(__file__).resolve().parent

def run():
    rows=json.loads((HERE/'probe_candidates.json').read_text());out=[]
    for k,r in enumerate(rows):
        o=tc.classify(r['word'],r['i'],r['j']);o['family']=r['family']
        if o['classification']=='unknown':
            C=probe.closure_checks(r['word'],r['i'],r['j']);o['closure_checks']=C
            N=C['numerator_closure'];D=C['denominator_closure']
            if N['simplified_crossings']==0 and N['simplified_components']==2 and D['simplified_crossings']==0 and D['simplified_components']==1:
                o['classification']='split_certified_property_R'
                o['certificate']='Actual N=unlink2 and actual D=unknot; branched cover, Property R, rational-tangle classification.'
        if o['classification']=='unknown':
            z=tc.classify_with_III(r['word'],r['i'],r['j'],seed=k,steps=2000)
            if z['classification']!='unknown':
                o['classification']=z['classification'];o['relative_RIII_certificate']=z
        if o['classification']=='unknown':
            T=probe.tangle(r['word'],r['i'],r['j']);moves=tc.simplify_open(T)
            for step in range(2001):
                pairs,mixed,over=tc.components_and_mixed(T,True)
                if len(set(over))<=1:
                    o['classification']='split_certified_uniform_over'
                    o['uniform_over_certificate']={'steps':step,'remaining_crossings':len(T.crossings),'mixed_crossings':mixed,'over_component_indices':over,'moves':moves};break
                ts=tc.triangles(T)
                if not ts:break
                t=random.Random(k+step).choice(ts)
                moves.append(['R3',[(e.crossing.label,e.strand_index) for e in t]])
                tc.move_III(T,t);moves.extend(tc.simplify_open(T))
        out.append(o)
    (HERE/'topology_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(dict(collections.Counter(r['classification'] for r in out)))

if __name__=='__main__':run()
