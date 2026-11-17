"""Independent check from SAVED records/summaries. No geometry is constructed."""
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

def read(path):
    return json.loads((ROOT/path).read_text())

def enc(poly):
    return [[d,c] for d,c in sorted(poly.items()) if c]

def fall(w,k):
    result = 1
    for i in range(k): result *= w-i
    return result

reduced = read('work/width6_instrument/transport_simplified_pairing_14.json')
reduced_formula = read('work/width6_parked/formula_witness_reduced.json')
groups = defaultdict(list)
for m,x,y,a,b,sign in reduced['records']:
    groups[m,y].append((x,a,b,sign))
reduced_results=[]
for pos in reduced_formula['parked_positions']:
    m,y=pos['matching'],pos['parked_index']
    ref=reduced_formula['matching_references'][str(m)]
    records=groups[m,y]
    sign0=next(sign for x,a,b,sign in records if x==0)
    inner=[]
    for x,a,b,sign in records:
        assert (b-ref['b_m'])%2==0
        inner.append((a-ref['a_m']-pos['A_y'],
                      (b-ref['b_m'])//2-pos['w0_geometric'],sign*sign0))
    moments=[]
    for k in range(3):
        poly=Counter()
        for a,w,eta in inner: poly[a]+=eta*fall(w,k)
        moments.append(enc(poly))
    assert moments[0]==pos['inner_pairing']
    assert all(w==0 for a,w,eta in inner)
    extremal=[]
    for degree in sorted({moments[0][0][0],moments[0][-1][0]}):
        signs=Counter(eta for a,w,eta in inner if a==degree)
        extremal.append({'degree':degree,'positive':signs[1],'negative':signs[-1]})
    reduced_results.append({'matching':m,'parked_index':y,'inner_records_A_W_eta':inner,
                            'moments_0_1_2':moments,'extremal_record_signs':extremal})

control=read('work/width6_parked/formula_nonzero_control.json')
summary=read('work/width6_instrument/arc_noncancellation_exact.json')
assert 'records' not in summary
assert all(p['first_loop_winding_range']==[0,0] for p in control['parked_positions'])
assert all(p['w0_geometric']==0 for p in control['parked_positions'])
for p in control['parked_positions']:
    assert p['inner_pairing']==([[-1,1]] if p['matching']==0 else [[-2,-1]])
ay_counts=Counter(p['A_y'] for p in control['parked_positions'] if p['matching']==1)
assert ay_counts=={0:2,-1:18,-2:3}
ref=control['matching_references']['1']
assert ref['a_m']==ref['b_m']==1
line=summary['extremal_configuration_data']['highest_surviving_line']
assert line['degree']==-4 and line['exchange_exponents']=={'1':21}
# Since W=w0=0 and a_m=b_m, degree=a-b=A_x+A_y.
# Let n_j count first-point intersections at A_x=j. Their signed sum is
# mu0=-q^-2, so n_-4 and n_-3 are even and n_-2 is odd.
# Exact archived line count: 2*n_-4+18*n_-3+3*n_-2=21.
possibilities=[]
for n4 in range(0,22,2):
    for n3 in range(0,22,2):
        for n2 in range(1,22,2):
            if 2*n4+18*n3+3*n2==21:
                possibilities.append({'n_minus4':n4,'n_minus3':n3,'n_minus2':n2,
                                      'positive_at_minus2':(n2-1)//2,
                                      'negative_at_minus2':(n2+1)//2})
assert possibilities==[
    {'n_minus4':0,'n_minus3':0,'n_minus2':7,'positive_at_minus2':3,'negative_at_minus2':4},
    {'n_minus4':6,'n_minus3':0,'n_minus2':3,'positive_at_minus2':1,'negative_at_minus2':2}]
result={
    'method':'Saved incidence records and saved aggregate counts only; no geometry replay.',
    'reduced_witness':reduced_results,
    'nonzero_control':{
        'parked_positions':47,'all_W_zero':True,
        'matching0':{'positions':24,'mu0':[[-1,1]],'mu1':[],'mu2':[]},
        'matching1':{'positions':23,'mu0':[[-2,-1]],'mu1':[],'mu2':[]},
        'all_higher_moments_zero':True,
        'raw_records_saved':False,
        'P1':'FALSE in this saved representative: all 23 matching-1 positions have both signs at their only nonzero mu0 degree.',
        'parity_certificate':{
            'Ay_multiplicities':dict(ay_counts),'archived_degree_minus4_record_count':21,
            'equation':'2 n[-4] + 18 n[-3] + 3 n[-2] = 21',
            'parities':'n[-4],n[-3] even; n[-2] odd (since mu0=-q^-2)',
            'all_possible_extremal_counts':possibilities,
            'qualification':'Exact count is 3 or 7, not identifiable from summaries alone; either count has mixed signs.'}}}
(OUT/'independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'reduced_positions':len(reduced_results),'control_P1':result['nonzero_control']['P1'],
                  'possible_counts':possibilities},indent=2))
