import ast,json,collections
from pathlib import Path
base=Path('work/research22')
rows={r['name']:r for r in json.load(open('work/proof10/homology/polys.json'))}
pairs=json.load(open(base/'ribbon_final_candidates.json'))['candidates']
def polynomial(v):
    s=-1 if v['mirror'] else 1
    c=collections.Counter()
    for _,rank,h,q in ast.literal_eval(rows[v['name']]['khovanov_reduced_rational_vector']): c[s*h,s*q]+=rank
    return c

def divide(d):
    diags=collections.defaultdict(dict)
    for (h,q),v in d.items(): diags[q-2*h][h]=v
    result={}; tails=[]
    for diagonal,seq in sorted(diags.items()):
        prev=0
        for h in range(min(seq),max(seq)+1):
            prev=seq.get(h,0)-prev
            if prev: result[h,diagonal+2*h]=prev
        if prev: tails.append([diagonal,max(seq),prev])
    neg=[[h,q,v] for (h,q),v in sorted(result.items()) if v<0]
    if not tails:
        check=collections.Counter()
        for (h,q),v in result.items():check[h,q]+=v;check[h+1,q+2]+=v
        assert {k:v for k,v in check.items() if v}==d
    return {'divisible':not tails,'nonnegative':not neg,'pass':not tails and not neg,'quotient':[[h,q,v] for (h,q),v in sorted(result.items())] if not tails else None,'tails':tails,'negative_terms':neg}

def match(d,maxa=None):
    # Pair vertices of opposite homological parity, with an allowed Lee bar
    # exactly when its upper endpoint is (h+1,q+2a), a a positive integer.
    vertices=sorted(d); left=[v for v in vertices if v[0]%2==0];right=[v for v in vertices if v[0]%2]
    S=('S',);T=('T',);adj=collections.defaultdict(list);cap={};original={};bars={}
    def add(a,b,c):
        adj[a].append(b);adj[b].append(a);cap[a,b]=c;cap[b,a]=0;original[a,b]=c
    for v in left:add(S,v,d[v])
    for v in right:add(v,T,d[v])
    for v in left:
        for w in right:
            lo,hi=(v,w) if v[0]<w[0] else (w,v)
            diff=hi[1]-lo[1]
            if hi[0]-lo[0]!=1 or diff<=0 or diff%2:continue
            a=diff//2
            if maxa is not None and a>maxa:continue
            add(v,w,min(d[v],d[w]));bars[v,w]=(lo,hi,a)
    flow=0
    while True:
        seen={S:None};Q=collections.deque([S])
        while Q and T not in seen:
            v=Q.popleft()
            for w in adj[v]:
                if w not in seen and cap[v,w]>0:seen[w]=v;Q.append(w)
        if T not in seen:break
        inc=10**9;w=T
        while seen[w] is not None:v=seen[w];inc=min(inc,cap[v,w]);w=v
        w=T
        while seen[w] is not None:v=seen[w];cap[v,w]-=inc;cap[w,v]+=inc;w=v
        flow+=inc
    chosen=[];covered=collections.Counter()
    for edge,(lo,hi,a) in bars.items():
        n=original[edge]-cap[edge]
        if n:chosen.append({'source':list(lo),'target':list(hi),'length':a,'multiplicity':n});covered[lo]+=n;covered[hi]+=n
    total=sum(d.values());passed=2*flow==total
    if passed:assert dict(covered)==d
    cut_capacity=sum(c for (v,w),c in original.items() if v in seen and w not in seen)
    assert cut_capacity==flow
    return {'pass':passed,'total_defect_rank':total,'matched_rank':2*flow,'unmatched_rank':total-2*flow,'bars':chosen,'uncovered':[[h,q,d[h,q]-covered[h,q]] for h,q in vertices if d[h,q]!=covered[h,q]],'min_cut':{'capacity':cut_capacity,'reachable_grade_vertices':[list(v) for v in vertices if v in seen],'source_reachable':S in seen,'sink_reachable':T in seen}}

results=[]
for p in pairs:
    source=polynomial(p['source']);target=polynomial(p['target'])
    d={k:target[k]-source[k] for k in source.keys()|target.keys() if target[k]!=source[k]}
    assert all(v>0 for v in d.values())
    assert d=={(h,q):v for h,q,v in p['defect']}
    one=divide(d);allbars=match(d)
    assert one['pass']==match(d,1)['pass']
    bounds={}
    if allbars['pass']:
        lengths=sorted({b['length'] for b in allbars['bars']})
        for length in range(1,max(lengths)+1):
            trial=match(d,length)
            bounds[length]=trial['pass']
            if trial['pass']:minbound=length;break
    else:minbound=None
    results.append({'source':p['source'],'target':p['target'],'rank_difference':sum(d.values()),'rank_divisible_by_four':sum(d.values())%4==0,'one_band':one,'any_length_bars':allbars,'minimum_maximum_bar_length':minbound})
key=lambda r:(r['source']['name'],r['source']['mirror'],r['target']['name'],r['target']['mirror'])
bykey={key(r):r for r in results}
for r in results:
    a,b,c,d=key(r);rm=bykey[a,not b,c,not d]
    for kind in ('one_band','any_length_bars'): assert r[kind]['pass']==rm[kind]['pass']
    assert r['minimum_maximum_bar_length']==rm['minimum_maximum_bar_length']
stats={'input_pairs':len(results),'mirror_orbits':len(results)//2,'rank_mod4_pass':sum(r['rank_divisible_by_four'] for r in results),'one_band_divisible':sum(r['one_band']['divisible'] for r in results),'one_band_nonnegative_divisible':sum(r['one_band']['pass'] for r in results),'any_length_bars_pass':sum(r['any_length_bars']['pass'] for r in results),'minimum_maximum_bar_length_counts':dict(collections.Counter(str(r['minimum_maximum_bar_length']) for r in results))}
output={'conventions':{'variable_u':'homological degree','variable_q':'quantum degree','mirror':'(h,q) -> (-h,-q)','unknot_reduced_polynomial':'1','bar_factor':'1+u*q^(2a)'},'stats':stats,'candidates':results}
json.dump(output,open(base/'ribbon_relative_bar_filter.json','w'),indent=2)
print(json.dumps(stats,indent=2))
for r in results:
    if not r['source']['mirror']:
        print(r['source']['name'],'->',r['target']['name'],'mirrorTarget',r['target']['mirror'],'rankdiff',r['rank_difference'],'oneband',r['one_band']['pass'],'allbars',r['any_length_bars']['pass'],'minlength',r['minimum_maximum_bar_length'])
