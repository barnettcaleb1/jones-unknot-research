"""Retrospective incidence check on the archived 222 words; no new braids or Jones scan."""
from pathlib import Path
from collections import Counter
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6'))
import probe

def endpoint(v):return ('top_'if v<6 else'bottom_')+str(v%6+1)

def analyze(word,i,j):
    # Same archived braid convention, followed by independent graph-path tracing.
    permutation=list(range(6))
    for letter in word:
        k=abs(letter)-1;permutation[k],permutation[k+1]=permutation[k+1],permutation[k]
    edges=[(top,6+bottom,'braid')for bottom,top in enumerate(permutation)]
    edges +=[(a,b,'top_cap')for a,b in probe.caps(probe.STATES[i])]
    edges +=[(6+a,6+b,'bottom_cup')for a,b in probe.caps(probe.STATES[j])]
    adj={v:[]for v in range(12)}
    for k,(a,b,kind)in enumerate(edges):adj[a].append((b,k));adj[b].append((a,k))
    ends=[v for v in range(12)if len(adj[v])==1]
    assert len(ends)==4
    used=set();paths=[]
    for start in ends:
        if adj[start][0][1]in used:continue
        vertices=[start];labels=[];v=start;previous=None
        while True:
            choices=[(w,k)for w,k in adj[v]if k!=previous]
            if not choices:break
            assert len(choices)==1
            w,k=choices[0];assert k not in used;used.add(k)
            labels.append(edges[k][2]);vertices.append(w);v=w;previous=k
        count=Counter(labels)
        paths.append({'endpoints':[endpoint(vertices[0]),endpoint(vertices[-1])],
                      'top_cap_count':count['top_cap'],'bottom_cup_count':count['bottom_cup'],
                      'braid_segment_count':count['braid'],'vertices':[endpoint(v)for v in vertices],
                      'edge_types':labels})
    closed=0
    for k,(a,b,kind)in enumerate(edges):
        if k in used:continue
        closed+=1;v=a;previous=None
        while True:
            choices=[(w,l)for w,l in adj[v]if l!=previous and l not in used]
            if not choices:break
            w,l=choices[0];used.add(l);v=w;previous=l
    pairs=sorted(sorted([ends.index(next(v for v in ends if endpoint(v)==p['endpoints'][0])),
                         ends.index(next(v for v in ends if endpoint(v)==p['endpoints'][1]))])for p in paths)
    geo=probe.geometry(word,i,j)
    assert geo['closed_components']==closed
    assert sorted(sorted(p)for p in geo['boundary_pairs'])==pairs
    etype=pairs==[[0,1],[2,3]]
    result={'closed_components':closed,'e_type':etype,'paths':paths}
    if etype and not closed:
        short=[p for p in paths if p['top_cap_count']+p['bottom_cup_count']==1]
        assert len(short)==1
        assert sorted((p['top_cap_count'],p['bottom_cup_count'])for p in paths)in[
                [(0,1),(2,1)],[(1,0),(1,2)]]
        p=short[0]
        result['short_arc']={'boundary_side':'top'if p['endpoints'][0].startswith('top')else'bottom',
            'kind':'single_bottom_cup'if p['bottom_cup_count']else'single_top_cap',
            'endpoints':p['endpoints'],
            'single_edge':next([endpoint(a),endpoint(b)]for a,b,kind in edges
                 if kind==('bottom_cup'if p['bottom_cup_count']else'top_cap')
                 and endpoint(a)in p['vertices']and endpoint(b)in p['vertices'])}
    return result

def main():
    saved=json.loads((HERE.parent/'width6/probe_results.json').read_text())
    candidates=json.loads((HERE.parent/'width6/probe_candidates.json').read_text())
    results=[];totals=Counter();zero_counts=Counter()
    for wi,entry in enumerate(saved['word_results']):
        zeros={(i,j)for i,j,c in entry['zeros']}
        for i in range(9):
            for j in range(9):
                r=analyze(entry['word'],i,j);totals['archived_word_cap_pairs']+=1
                if not r['e_type']:continue
                totals['e_type']+=1
                if r['closed_components']:totals['e_type_with_closed_components']+=1;continue
                totals['e_type_two_arc']+=1;totals[r['short_arc']['kind']]+=1
                r.update(word_index=wi,family=entry['family'],word=entry['word'],i=i,j=j,
                         archived_id_coefficient_zero=(i,j)in zeros)
                if(i,j)in zeros:zero_counts[r['short_arc']['kind']]+=1
                results.append(r)
    candidate_rows=[]
    for ci,c in enumerate(candidates):
        r=analyze(c['word'],c['i'],c['j'])
        assert r['closed_components']==c['geometry']['closed_components']
        if r['closed_components']:continue
        assert r['e_type']
        r.update(candidate_index=ci,family=c['family'],word=c['word'],i=c['i'],j=c['j'])
        candidate_rows.append(r)
    lp=json.loads((HERE.parent/'width6_targeted/lp_e_fixed_cap_completions.json').read_text())
    lp_rows=[]
    for c in lp:
        r=analyze(c['effective_word_tau_inverse_beta'],2,7)
        r.update(tau=c['top_cap_transport_tau']);lp_rows.append(r)
    out={'scope':'Retrospective incidence classification of archived 222-word x 81-cap domain; no new words or Jones computations.',
         'counts':dict(totals),'zero_counts':dict(zero_counts),'candidate_zero_count':len(candidate_rows),
         'failures':0,'all_e_type_two_arc_records':results,'archived_zero_records':candidate_rows,
         'long_paton_completions':lp_rows}
    (HERE/'structure_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k]for k in ['counts','zero_counts','candidate_zero_count','failures']}))
    print('LP short arcs',[(r['tau'],r['short_arc'])for r in lp_rows])

if __name__=='__main__':main()
