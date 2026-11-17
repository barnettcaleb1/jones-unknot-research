import json, ast, collections, sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
polys=json.loads((ROOT/'work/proof10/homology/polys.json').read_text())
metadata=json.loads((ROOT/'work/proof10/homology/metadata.json').read_text())
meta={r['name']:r for r in metadata}
rows={r['name']:r for r in polys}
def kh(row,field,mirror=False):
    d=collections.Counter()
    for mod,rank,i,j in ast.literal_eval(row['khovanov_reduced_'+field+'_vector']):
        assert mod=={'rational':1,'mod2':2}[field]
        d[(-i,-j) if mirror else (i,j)]+=rank
    return d
def euler(d):
    p=collections.Counter()
    for (i,j),r in d.items():p[j]+=(-1 if i%2 else 1)*r
    return tuple(sorted((j,r) for j,r in p.items() if r))
def hfk(row,mirror=False):
    s=row['hfk_polynomial_vector'].strip()
    if not s:return None
    out=collections.Counter()
    for r,a,m in ast.literal_eval('['+','.join('['+v+']' for v in s[1:-1].split(';'))+']'):
        out[(-a,-m) if mirror else (a,m)]+=r
    return out
def alex(h):
    d=collections.Counter()
    for (a,m),r in h.items():d[a]+=(-1 if m%2 else 1)*r
    return {a:r for a,r in d.items() if r}
def divides(a,b):
    # Remove Laurent-unit shifts, then exact polynomial long division over Q.
    aa={i-min(a):Fraction(v) for i,v in a.items()};bb={i-min(b):Fraction(v) for i,v in b.items()}
    da=max(aa)
    while bb and max(bb)>=da:
        k=max(bb)-da;c=bb[max(bb)]/aa[da]
        for i,v in aa.items():
            bb[i+k]=bb.get(i+k,0)-c*v
            if not bb[i+k]:bb.pop(i+k)
    return not bb
def injects(a,b):return all(b.get(g,0)>=r for g,r in a.items())
def key(s,t):return (s['name'],s['mirror'],t['name'],t['mirror'])
def num(v):
    if isinstance(v,(float,int)):return int(v) if float(v).is_integer() else None
    try:
        f=float(v);return int(f) if f.is_integer() else None
    except (ValueError,TypeError):return None
def g4interval(v):
    n=num(v)
    if n is not None:return (n,n)
    if isinstance(v,str) and v.startswith('['):
        x=ast.literal_eval(v);return tuple(x)
    return None
variants=[];groups=collections.defaultdict(list)
for r in polys:
    for mirror in [False,True]:
        h=kh(r,'rational',mirror)
        s={'name':r['name'],'mirror':mirror,'rank':sum(h.values()),'kh':h}
        groups[euler(h)].append(s)
candidates=[]
for p,ss in groups.items():
    for s in ss:
        for t in ss:
            if s['rank']<t['rank'] and injects(s['kh'],t['kh']):candidates.append((s,t))
original=json.loads((ROOT/'work/research22/ribbon_homology_candidates.json').read_text())['candidates']
assert {key(s,t) for s,t in candidates}=={key(c['source'],c['target']) for c in original}
stats=collections.Counter();survivors=[]
for s,t in candidates:
    a,b=rows[s['name']],rows[t['name']]
    ha,hb=hfk(a,s['mirror']),hfk(b,t['mirror'])
    if ha is None or hb is None:raise ValueError('missing HFK')
    if not injects(ha,hb):stats['HFK_obstructed']+=1;continue
    if not divides(alex(ha),alex(hb)):stats['Alexander_obstructed']+=1;continue
    stats['HFK_Alexander_survive']+=1
    if not injects(kh(a,'mod2',s['mirror']),kh(b,'mod2',t['mirror'])):stats['mod2Kh_obstructed']+=1;continue
    ma,mb=meta[s['name'].replace('*','')],meta[t['name'].replace('*','')]
    sa,sb=num(ma['rasmussen_invariant']),num(mb['rasmussen_invariant'])
    if sa is not None and s['mirror']:sa=-sa
    if sb is not None and t['mirror']:sb=-sb
    if sa is not None and sb is not None and sa!=sb:stats['s_obstructed']+=1;continue
    stats['through_s_survive']+=1
    ga,gb=g4interval(ma['smooth_four_genus']),g4interval(mb['smooth_four_genus'])
    if ga and gb and max(ga[0],gb[0])>min(ga[1],gb[1]):stats['g4_obstructed']+=1;continue
    stats['final_survive']+=1
    survivors.append({'source':{k:v for k,v in s.items() if k!='kh'},'target':{k:v for k,v in t.items() if k!='kh'},'s':[sa,sb],'g4_intervals':[ga,gb]})
out={'polynomial_rows':len(polys),'directed_candidates':len(candidates),'stats':dict(stats),'survivors':survivors}
sys.path.insert(0,str(ROOT/'work/proof10/homology/packages'))
import xlrd
sheet=xlrd.open_workbook(str(ROOT/'work/proof10/homology/knotinfo_data_complete.xls')).sheet_by_index(0)
head=sheet.row_values(0)
full={sheet.cell_value(i,0):dict(zip(head,sheet.row_values(i))) for i in range(2,sheet.nrows)}
extra_stats=collections.Counter();extra_survivors=[]
for c in survivors:
    bad=False
    for field in ['signature','ozsvath_szabo_tau_invariant']:
        vals=[]
        for end in ['source','target']:
            r=c[end];v=num(full[r['name'].replace('*','')][field])
            if v is not None and r['mirror']:v=-v
            vals.append(v)
        c[field]=vals
        if None in vals:extra_stats[field+'_unknown']+=1
        elif vals[0]!=vals[1]:extra_stats[field+'_obstructed']+=1;bad=True
    if not bad:extra_survivors.append(c);extra_stats['survive']+=1
out['signature_tau_stats']=dict(extra_stats)
out['survivors_after_signature_tau']=extra_survivors
checked=0
for r in polys:
    if not r['jones_polynomial_vector']:continue
    v=ast.literal_eval(r['jones_polynomial_vector'].replace('{','[').replace('}',']'))
    assert dict(euler(kh(r,'rational')))=={2*(v[0]+i):c for i,c in enumerate(v[2:]) if c}
    checked+=1
out['independent_Jones_vector_checks']=checked
out['unequal_Alexander_final_survivors']=sum(alex(hfk(rows[c['source']['name']],c['source']['mirror']))!=alex(hfk(rows[c['target']['name']],c['target']['mirror'])) for c in extra_survivors)
(ROOT/'work/research22/candidate_filter_independent_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ['survivors','survivors_after_signature_tau']},indent=2))
old=json.loads((ROOT/'work/research22/ribbon_final_candidates.json').read_text())['candidates']
newkeys={key(c['source'],c['target']) for c in survivors}
print('g4 excluded pairs:', [key(c['source'],c['target']) for c in old if key(c['source'],c['target']) not in newkeys])
