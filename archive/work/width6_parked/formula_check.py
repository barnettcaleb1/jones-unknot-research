"""Geometric parked-point decomposition; no residual definition of w0.

Reference constants come from independently traced configuration paths.
All variable windings come from actual closed ONE-point target/source paths.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,json,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_instrument'))
import combinatorial_winding as cw
import combinatorial_exact_pairing as ep
import transport_exact_intersections as ti

def decode_curves(raw):return [[tuple(F(x)for x in p)for p in c]for c in raw]

def path(c,start,end):
    if start>end:return list(reversed(path(c,end,start)))
    return [ep.at(c,start)]+[c[k]for k in range(int(start)+1,int(end)+1)if start<k<end]+[ep.at(c,end)]

def reference_monodromy(source,target,ints,bm,m):
    base=[ints[0][bm][0],ints[1][1-bm][0]]
    ref=[ints[0][m][0],ints[1][1-m][0]]
    starts=[None,None];ends=[None,None]
    for k in(0,1):
        starts[bm if k==0 else 1-bm]=base[k]['b_param']
        ends[m if k==0 else 1-m]=ref[k]['b_param']
    current=[ep.at(target[k],starts[k])for k in(0,1)]
    trace=[tuple(current)]
    for k in(0,1):
        for z in path(target[k],starts[k],ends[k])[1:]:
            current[k]=z;trace.append(tuple(current))
    for k in(0,1):
        label=m if k==0 else 1-m
        for z in path(source[k],ref[k]['a_param'],base[k]['a_param'])[1:]:
            current[label]=z;trace.append(tuple(current))
    return cw.configuration_monodromy(trace),trace

def clean(p):return {k:int(v)for k,v in p.items()if v}
def enc(p):return [[k,int(v)]for k,v in sorted(p.items())if v]

def load_case(name):
    root=HERE.parent/'width6_instrument'
    if name=='witness_reduced':
        saved=json.loads((root/'transport_simplified_pairing_14.json').read_text())
        source=decode_curves(saved['source_curves'])
        target=[ti.figure8(1,2,F(saved['target_radius'])),ti.figure8(3,4,F(saved['target_radius']))]
        ints=[[ti.intersection_records(c,t)[0]for t in target]for c in source]
    elif name=='witness_full':
        saved=json.loads((root/'combinatorial_exact_witness14.json').read_text())
        source,target,ints,_=ti.rational_model(saved['word'])
    elif name=='nonzero_control':
        metadata=json.loads((root/'arc_noncancellation_exact.json').read_text())
        word=metadata['effective_matrix_word']
        saved=ep.exact_model(word,progress=0)
        source,target,ints,_=ti.rational_model(word)
    else:raise ValueError(name)
    return saved,source,target,ints

def run(name):
    start=time.monotonic();saved,source,target,ints=load_case(name)
    counts=[[len(x)for x in r]for r in ints]
    bm=saved['base_matching']
    assert counts==saved['intersection_counts']
    refs={};anchors={};parked=[];records=saved['records'];index=0
    base=[ints[0][bm][0],ints[1][1-bm][0]]
    global_sign=base[0]['sign']*base[1]['sign']*(-1 if bm else 1)
    sr=[ep.CrossingCurve(c,'ray')for c in source]
    tr=[ep.CrossingCurve(c,'ray')for c in target]
    punctures=[(F(j),F(0))for j in range(1,7)]
    total=Counter();matching_totals={}
    for m in(0,1):
        if not ints[0][m] or not ints[1][1-m]:continue
        xref,yref=ints[0][m][0],ints[1][1-m][0]
        (am,bm_ref),reference_path=reference_monodromy(source,target,ints,bm,m)
        parity=m^bm
        assert (bm_ref-parity)%2==0
        kappa=(bm_ref-parity)//2
        ref_sign=xref['sign']*yref['sign']*(-1 if m else 1)*global_sign
        refs[m]={'a_m':am,'b_m':bm_ref,'parity':parity,'kappa_m':kappa,'raw_sign_m':ref_sign,
                 'path':[[[str(v)for v in z]for z in pair]for pair in reference_path]}
        def loop_winding(first,p,center):
            ref=xref if first else yref
            src=0 if first else 1;tgt=m if first else 1-m
            return tr[tgt].change(ref['b_param'],p['b_param'],center)+sr[src].change(p['a_param'],ref['a_param'],center)
        ax=[sum(loop_winding(True,x,p)for p in punctures)for x in ints[0][m]]
        ay=[sum(loop_winding(False,y,p)for p in punctures)for y in ints[1][1-m]]
        wy=[loop_winding(False,y,xref['point'])for y in ints[1][1-m]]
        # The saved record order is x-major. Build the independent parked sums
        # while checking each individual exponent/sign in that same order.
        inners=[Counter()for y in ints[1][1-m]]
        winding_ranges=[[None,None]for y in ints[1][1-m]]
        for i,x in enumerate(ints[0][m]):
            for j,y in enumerate(ints[1][1-m]):
                wx=loop_winding(True,x,y['point'])
                a=am+ax[i]+ay[j]
                b=bm_ref+2*wy[j]+2*wx
                sign=ref_sign*x['sign']*xref['sign']*y['sign']*yref['sign']
                assert records[index]==[m,i,j,a,b,sign],(name,index,records[index],[m,i,j,a,b,sign])
                assert b-parity==2*(kappa+wy[j]+wx)
                inners[j][ax[i]-2*wx]+=x['sign']*xref['sign']
                rr=winding_ranges[j];rr[0]=wx if rr[0]is None else min(rr[0],wx);rr[1]=wx if rr[1]is None else max(rr[1],wx)
                index+=1
        subtotal=Counter()
        for j,y in enumerate(ints[1][1-m]):
            inner=clean(inners[j]);outer_degree=am-bm_ref+ay[j]-2*wy[j]
            outer_sign=ref_sign*(-1 if bm_ref%2 else 1)*y['sign']*yref['sign']
            for degree,c in inner.items():subtotal[degree+outer_degree]+=outer_sign*c
            parked.append({'matching':m,'parked_index':j,'position':[str(v)for v in y['point']],
                           'A_y':ay[j],'w0_geometric':wy[j],'w0_with_matching_boundary':kappa+wy[j],
                           'outer_degree':outer_degree,'outer_sign':outer_sign,
                           'inner_pairing':enc(inner),'first_loop_winding_range':winding_ranges[j]})
        matching_totals[m]=enc(subtotal)
        total.update(subtotal)
    assert index==len(records)
    expected={int(k):v for k,v in saved['TL_line_specialization'].items()}
    assert clean(total)==expected,(clean(total),expected)
    result={'case':name,'status':'PASS_EVERY_RECORD_AND_PARKED_SUM','configuration_count':index,
            'intersection_counts':counts,'base_matching':bm,'matching_references':refs,
            'parked_positions':parked,'matching_sums':matching_totals,'total_specialization':enc(total),
            'seconds':time.monotonic()-start,
            'formula':'b=b_m+2 wind_xm(gamma_other[y_m,y]+c1[y,y_m])+2 wind_y(gamma_first[x_m,x]+c0[x,x_m])',
            'non_tautological_check':'Every winding is computed from actual one-point closed paths; matching reference constants are traced configuration paths, not residuals from saved b.'}
    dest=HERE/f'formula_{name}.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print('RESULT',name,index,result['seconds'],result['total_specialization'],flush=True)
    return result

if __name__=='__main__':run(sys.argv[1]if len(sys.argv)>1 else'witness_reduced')
