import ast,json,collections
from pathlib import Path
root=Path(__file__).resolve().parents[2]
rows=json.loads((root/'work/proof10/homology/polys.json').read_text())
byname={r['name']:r for r in rows}
def integral(row,mirror=False):
    out=collections.Counter()
    for modulus,rank,h,q in ast.literal_eval(row['khovanov_reduced_integral_vector']):
        if mirror:h,q=(-h,-q) if modulus==0 else (1-h,-q)
        if modulus==0:out[h,q,0]+=rank;continue
        # Elementary divisors, not invariant factors: Z/ab=Z/a+Z/b
        # for coprime a,b. Keep each prime-power cyclic multiplicity.
        d=2;n=modulus
        while d*d<=n:
            power=1
            while n%d==0:power*=d;n//=d
            if power>1:out[h,q,power]+=rank
            d+=1
        if n>1:out[h,q,n]+=rank
    return out
def mod2_from_integral(z):
    out=collections.Counter()
    for (h,q,m),r in z.items():
        if m==0:out[h,q]+=r
        elif m%2==0:out[h,q]+=r;out[h-1,q]+=r
    return out
uct_checks=0
for row in rows:
    original=collections.Counter()
    for _,r,h,q in ast.literal_eval(row['khovanov_reduced_mod2_vector']):original[h,q]+=r
    for mirror in [False,True]:
        expected=collections.Counter({((-h,-q) if mirror else (h,q)):r for (h,q),r in original.items()})
        assert mod2_from_integral(integral(row,mirror))==expected,(row['name'],mirror)
        uct_checks+=1
candidates=json.loads((root/'work/research22/ribbon_final_candidates.json').read_text())['candidates']
survivors=[];rejected=[];torsion_endpoints=set()
for c in candidates:
    ends=[]
    for e in ['source','target']:
        s=c[e];z=integral(byname[s['name']],s['mirror']);ends.append(z)
        if any(m for h,q,m in z):torsion_endpoints.add((s['name'],s['mirror']))
    a,b=ends
    failures=[{'h':h,'q':q,'modulus':m,'source':r,'target':b.get((h,q,m),0)} for (h,q,m),r in a.items() if r>b.get((h,q,m),0)]
    if failures:rejected.append({'candidate':c,'failures':failures})
    else:survivors.append(c)
out={'input_candidates':len(candidates),'UCT_checks_original_and_mirror':uct_checks,'torsion_endpoint_variants':sorted(torsion_endpoints),'rejected_count':len(rejected),'survivor_count':len(survivors),'rejected':rejected,'survivors':survivors}
(root/'work/research22/ribbon_integral_filter_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ['rejected','survivors']},indent=2))
