"""Exact geometric square-to-torus pairing with independent matrix calibration.

The geometric enumerator never obtains its intersection records from matrices.
Calibration is mandatory and happens after enumeration. Input uses the archived
TL matrix-word and cap-state conventions; variables in geometric output are q,t.
"""
from pathlib import Path
from collections import Counter
import argparse,json,time
from run_calibration import lp,divide_one_minus_t,monomial_match
from combinatorial_exact_pairing import exact_model

HERE=Path(__file__).resolve().parent
CAPS={r['target']:r for r in lp.TRANSPORT}

def cap_exponent(i):return int(next(iter(CAPS[i]['unit'])))

def effective_word(word,i,j):
    return CAPS[i]['word'][::-1]+word+[-g for g in CAPS[j]['word']]

def extrema(records):
    lines={}
    for matching,x,y,a,b,sign in records:
        z=lines.setdefault(a-b,{'point_pairs':0,'signed_sum':0,'exchange_exponents':Counter(),
                              'raw_signed_counts_by_b':Counter()})
        z['point_pairs']+=1;z['signed_sum']+=sign*(-1 if b%2 else 1)
        z['exchange_exponents'][b]+=1;z['raw_signed_counts_by_b'][b]+=sign
    if not lines:return {}
    answer={'highest_geometric_line':{'degree':max(lines),**lines[max(lines)]}}
    nonzero=[k for k,v in lines.items()if v['signed_sum']]
    if nonzero:
        answer['highest_surviving_line']={'degree':max(nonzero),**lines[max(nonzero)]}
        answer['lowest_surviving_line']={'degree':min(nonzero),**lines[min(nonzero)]}
    return answer

def run(word,i=7,j=7,keep_records=True,simplify=False):
    eff=effective_word(word,i,j)
    if simplify:
        from transport_simplified_pairing import exact_model as enumerator
    else:
        enumerator=exact_model
    result=enumerator(eff,keep_records=True)
    actual={(a,b):c for a,b,c in result['polynomial']}
    phi=lp.shift(divide_one_minus_t(lp.pairing(word,i,j)),-4)
    seed=lp.shift(divide_one_minus_t(lp.pairing(eff,7,7)),-4)
    assert phi==lp.shift(seed,cap_exponent(j)-cap_exponent(i))
    assert all(a%2==0 for a,b in seed)
    wanted={(a//2,b):c for(a,b),c in seed.items()}
    unit=monomial_match(actual,wanted)
    if unit is None:
        raise AssertionError('Geometric polynomial failed exact generic matrix calibration')
    result.update(input_matrix_word=word,source_cap_index=i,target_cap_index=j,
                  effective_matrix_word=eff,calibration='PASS: exact generic polynomial',
                  seed_deck_unit=unit,extremal_configuration_data=extrema(result['records']))
    if unit:
        result['unit_relative_to_normalized_original_Phi']={
            's_exponent':2*unit['q']+cap_exponent(i)-cap_exponent(j),
            't_exponent':unit['t'],'sign':unit['sign']}
    else:
        result['unit_relative_to_normalized_original_Phi']='Undetermined when both polynomials are zero'
    result['normalization']='Phi=q^-2 P/(1-t); Phi at t=-q^-1 equals q^-1 J_hat; q=s^2'
    result['scope']='Actual intersections in the chosen representative; no minimality or splitting-disk certificate'
    if not keep_records:result.pop('records',None);result.pop('one_point_intersections',None)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--word',default='[]',help='JSON signed generator list in archived matrix convention')
    p.add_argument('--source-cap',type=int,default=7);p.add_argument('--target-cap',type=int,default=7)
    p.add_argument('--summary-only',action='store_true');p.add_argument('--output',required=True)
    p.add_argument('--simplify',action='store_true',help='Use certified local triangle isotopies after each generator')
    a=p.parse_args();result=run(json.loads(a.word),a.source_cap,a.target_cap,not a.summary_only,a.simplify)
    Path(a.output).write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('CALIBRATED',result['configuration_count'],'pairs',result['polynomial'],flush=True)
