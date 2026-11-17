"""Moment tables from saved, already validated incidence records only.

No geometric transport, segment intersections, winding recomputation, or braid
search occurs. The per-record A,W,eta are recovered using saved matching anchors.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,time
HERE=Path(__file__).resolve().parent
WORK=HERE.parent

def falling(w,k):
    z=1
    for i in range(k):z*=w-i
    return z

def clean(p):return {a:c for a,c in p.items()if c}
def enc(p):return [[a,c]for a,c in sorted(p.items())if c]

def moment(records,k):
    p=Counter()
    for x,A,W,eta in records:p[A]+=eta*falling(W,k)
    return clean(p)

def degree_data(records,k,d):
    xs=[(x,A,W,eta,eta*falling(W,k))for x,A,W,eta in records if A==d and falling(W,k)]
    raw=Counter('positive'if t[3]>0 else'negative'for t in xs)
    weighted=Counter('positive'if t[4]>0 else'negative'for t in xs)
    return {'degree':d,'record_count':len(xs),'positive_raw_sign':raw['positive'],
            'negative_raw_sign':raw['negative'],'positive_weighted_sign':weighted['positive'],
            'negative_weighted_sign':weighted['negative'],
            'weighted_coefficient':sum(t[4]for t in xs),'W_counts':dict(Counter(t[2]for t in xs)),
            'single_raw_sign':len(raw)==1,'single_weighted_sign':len(weighted)==1,
            'records':[[x,W,eta,weight]for x,A,W,eta,weight in xs]}

def moment_info(records,k):
    p=moment(records,k)
    info={'k':k,'polynomial':enc(p),'zero':not p}
    active=[A for x,A,W,e in records if falling(W,k)]
    if active:
        info['highest_potential_degree']=degree_data(records,k,max(active))
        info['lowest_potential_degree']=degree_data(records,k,min(active))
    if p:
        info['highest_surviving_degree']=degree_data(records,k,max(p))
        info['lowest_surviving_degree']=degree_data(records,k,min(p))
    return info

def load_records(case):
    if case=='witness_reduced':p=WORK/'width6_instrument/transport_simplified_pairing_14.json'
    elif case=='witness_full':p=WORK/'width6_instrument/combinatorial_exact_witness14.json'
    elif case=='nonzero_control':p=HERE/'tables_nonzero_recovered_records.json'
    else:raise ValueError(case)
    a=json.loads(p.read_text())
    if 'records'not in a:raise ValueError('Missing raw records; cannot infer moments from specialized sums')
    return a,p

def run(case):
    begin=time.monotonic();saved,record_path=load_records(case)
    formula_path=WORK/f'width6_parked/formula_{case}.json'
    formula=json.loads(formula_path.read_text())
    meta={(r['matching'],r['parked_index']):r for r in formula['parked_positions']}
    anchors={int(m):r for m,r in formula['matching_references'].items()}
    grouped=defaultdict(list)
    for m,x,y,a,b,sign in saved['records']:grouped[m,y].append((x,a,b,sign))
    assert len(grouped)==len(meta)
    rows=[]
    for key,entries in sorted(grouped.items()):
        m,y=key;park=meta[key];ref=anchors[m]
        first=next(e for e in entries if e[0]==0)
        records=[]
        for x,a,b,sign in entries:
            assert (b-ref['b_m'])%2==0
            A=a-ref['a_m']-park['A_y']
            W=(b-ref['b_m'])//2-park['w0_geometric']
            eta=sign*first[3]
            records.append((x,A,W,eta))
        assert records[0][1:]==(0,0,1)
        S=Counter()
        spec=Counter()
        for x,A,W,eta in records:S[A,W]+=eta;spec[A-2*W]+=eta
        S=clean(S);spec=clean(spec)
        assert enc(spec)==park['inner_pairing'],(case,key,enc(spec),park['inner_pairing'])
        moments=[moment_info(records,k)for k in range(3)]
        lowest=None
        if S:
            max_order=len({W for A,W in S})-1
            for k in range(max_order+1):
                v=moments[k]if k<3 else moment_info(records,k)
                if not v['zero']:lowest=v;break
            assert lowest is not None
        row={'matching':m,'parked_index':y,'position':park['position'],
             'record_count':len(records),'records_columns':['source_point_index','A','W','eta'],
             'records':[list(v)for v in records],
             'S_q_u':[[A,W,c]for(A,W),c in sorted(S.items())],
             'all_moments_zero':not S,'mu_0_1_2':moments,'lowest_nonzero_moment':lowest,
             'inner_at_u_q_minus2':enc(spec),'inner_survives_specialization':bool(spec),
             'outer_sign':park['outer_sign'],'outer_degree':park['outer_degree'],
             'outer_contribution':enc({d+park['outer_degree']:c*park['outer_sign']for d,c in spec.items()})}
        rows.append(row)
    stats={'parked_positions':len(rows),'total_incidence_records':sum(r['record_count']for r in rows),
           'all_moments_zero':sum(r['all_moments_zero']for r in rows),
           'lowest_nonzero_moment_counts':dict(Counter(r['lowest_nonzero_moment']['k']if r['lowest_nonzero_moment']else'none'for r in rows)),
           'mu0_zero':sum(r['mu_0_1_2'][0]['zero']for r in rows),
           'surviving_inner_positions':sum(r['inner_survives_specialization']for r in rows)}
    p1=[r for r in rows if r['inner_survives_specialization'] and
        not r['lowest_nonzero_moment']['highest_surviving_degree']['single_weighted_sign']]
    p1either=[r for r in rows if r['inner_survives_specialization'] and
        not any(r['lowest_nonzero_moment'][end]['single_weighted_sign']for end in('highest_surviving_degree','lowest_surviving_degree'))]
    p2=[r for r in rows if r['mu_0_1_2'][0]['zero']and not r['all_moments_zero']and
        any(r['lowest_nonzero_moment'][end]['single_weighted_sign']for end in('highest_surviving_degree','lowest_surviving_degree'))]
    stats.update(P1_top_failures=len(p1),P1_both_extrema_mixed=len(p1either),
                 P2_lowest_nonzero_has_pure_extremum=len(p2))
    witnesses={name:[{'matching':r['matching'],'parked_index':r['parked_index'],
                         'lowest_nonzero_moment':r['lowest_nonzero_moment'],
                         'inner_at_u_q_minus2':r['inner_at_u_q_minus2'],
                         'outer_contribution':r['outer_contribution']}for r in chosen[:5]]
               for name,chosen in [('P1_top_failure',p1),('P1_both_mixed',p1either),('P2_failure',p2)]}
    result={'case':case,'source_record_file':str(record_path.relative_to(WORK)),
            'source_formula_file':str(formula_path.relative_to(WORK)),
            'method':'Reconstruction from saved exact incidence records and independently validated path anchors; no new geometry',
            'statistics':stats,'prediction_witnesses':witnesses,'parked_positions':rows,
            'seconds':time.monotonic()-begin}
    (HERE/f'tables_{case}.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    (HERE/f'tables_{case}_summary.json').write_text(json.dumps({k:v for k,v in result.items()if k!='parked_positions'},indent=2)+'\n')
    print(case,json.dumps(stats),flush=True)
    return result

def nonzero_from_saved_metadata():
    """Recover exact moment polynomials when the saved W range is a singleton.

    The 4,005 raw incidences were not archived. This routine does not reconstruct
    them. Their already verified winding range, [0,0] at every parked position,
    makes every higher moment zero and identifies S with its specialization.
    Counts on the surviving line give a separate exact partial sign certificate.
    """
    case='nonzero_control'
    formula_path=WORK/'width6_parked/formula_nonzero_control.json'
    control_path=WORK/'width6_instrument/arc_noncancellation_exact.json'
    formula=json.loads(formula_path.read_text())
    control=json.loads(control_path.read_text())
    assert 'records'not in control
    assert all(p['first_loop_winding_range']==[0,0]for p in formula['parked_positions'])
    assert control['extremal_configuration_data']['highest_surviving_line']['point_pairs']==21
    assert control['extremal_configuration_data']['highest_surviving_line']['exchange_exponents']=={'1':21}
    m1=[p for p in formula['parked_positions']if p['matching']==1]
    assert Counter(p['A_y']for p in m1)==Counter({0:2,-1:18,-2:3})
    assert all(p['inner_pairing']==[[-2,-1]]for p in m1)
    # Because the coefficient of q^-4 and q^-3 in mu_0 vanishes, their
    # unaggregated record counts are even. At q^-2 the coefficient is -1,
    # so that count is odd. Solve the archived line-count equation exactly.
    possible_counts=[]
    for n4 in range(0,22,2):
        for n3 in range(0,22,2):
            for n2 in range(1,22,2):
                if 2*n4+18*n3+3*n2==21:
                    possible_counts.append({'n_minus4':n4,'n_minus3':n3,
                        'n_minus2':n2,'positive_at_minus2':(n2-1)//2,
                        'negative_at_minus2':(n2+1)//2})
    assert {p['n_minus2']for p in possible_counts}=={3,7}
    rows=[]
    for p in formula['parked_positions']:
        m=p['matching'];pol=p['inner_pairing']
        extreme=pol[-1][0]
        evidence={'degree':extreme,'exact_raw_record_count':None,
                  'reason':'The control archive omitted its raw incidence records.'}
        if m==1:
            evidence.update(possible_record_counts=[3,7],possible_positive_counts=[1,3],
                            possible_negative_counts=[2,4],single_weighted_sign=False,
                            single_raw_sign=False,certificate='surviving_line_parity_certificate')
        moments=[{'k':0,'polynomial':pol,'zero':False,
                  'highest_surviving_degree':evidence,'lowest_surviving_degree':evidence},
                 {'k':1,'polynomial':[],'zero':True},
                 {'k':2,'polynomial':[],'zero':True}]
        rows.append({'matching':m,'parked_index':p['parked_index'],'position':p['position'],
            'record_count':control['intersection_counts'][0][m],
            'raw_records_available':False,'saved_winding_range':[0,0],
            'S_q_u':[[a,0,c]for a,c in pol], 'all_moments_zero':False,
            'mu_0_1_2':moments,'all_moments_order_at_least_1_zero':True,
            'lowest_nonzero_moment':moments[0],'inner_at_u_q_minus2':pol,
            'inner_survives_specialization':True,'outer_sign':p['outer_sign'],
            'outer_degree':p['outer_degree'],
            'outer_contribution':[[a+p['outer_degree'],c*p['outer_sign']]for a,c in pol]})
    total=Counter()
    for r in rows:
        for a,c in r['outer_contribution']:total[a]+=c
    assert enc(clean(total))==formula['total_specialization']==[[-4,1]]
    survivors=[r['parked_index']for r in rows if r['matching']==1 and any(a==-4 for a,c in r['outer_contribution'])]
    assert survivors==[8,12,22]
    result={'case':case,'source_formula_file':str(formula_path.relative_to(WORK)),
        'source_summary_file':str(control_path.relative_to(WORK)),
        'method':'Exact singleton-winding inference from existing verified metadata; no new geometry or raw-record reconstruction',
        'limitation':'Raw 4005 incidence records are not archived; exact extremal record counts unavailable. Partial sign counts follow from an exact archived line-count parity certificate.',
        'statistics':{'parked_positions':47,'total_incidence_records':4005,
            'all_moments_zero':0,'mu0_zero':0,'lowest_nonzero_moment_counts':{'0':47},
            'all_higher_moments_zero':47,'surviving_inner_positions':47,
            'P1_certified_mixed_extrema_positions':23,'P1_undetermined_sign_positions':24,
            'P1_net_surviving_degree_positions':[8,12,22],
            'P1_all_net_surviving_degree_positions_mixed':True},
        'surviving_line_parity_certificate':{'definitions':'n_j counts first-point records of A_x=j in matching1; W=0 for every record.',
            'archived_line':-4,'archived_count':21,'equation':'2*n_-4+18*n_-3+3*n_-2=21',
            'parities':'n_-4,n_-3 even; n_-2 odd because mu_0=-q^-2',
            'all_nonnegative_parity_solutions':possible_counts,
            'conclusion':'n_-2 is 3 or 7; coefficient -1 forces both signs in either case.'},
        'parked_positions':rows}
    (HERE/f'tables_{case}.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    (HERE/f'tables_{case}_summary.json').write_text(json.dumps({k:v for k,v in result.items()if k!='parked_positions'},indent=2)+'\n')
    print(case,json.dumps(result['statistics']),flush=True)
    return result

if __name__=='__main__':
    import sys
    for case in sys.argv[1:] or ['witness_reduced','witness_full','nonzero_control']:
        if case=='nonzero_control':nonzero_from_saved_metadata()
        else:run(case)
