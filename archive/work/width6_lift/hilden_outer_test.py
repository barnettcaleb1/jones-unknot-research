"""One bounded depth-two test of paired excursions outside embedded B6.

The prediction tested is whether the first nontrivial double-coset trace
already leaves the partial-cap stabilizer orbit. Stop after 20 new
projective coefficient classes or 120 seconds; do not enlarge the search.
"""
from pathlib import Path
import sys,json,itertools,time
import hilden_locus as h
p=h.p
HERE=Path(__file__).resolve().parent
SEED=[4,3,2,1,5,4,3,-2,4,4,4]
def projective(f):
    if not f:return ()
    lo=min(f);sgn=1 if f[lo]>0 else-1
    return tuple((a-lo,sgn*v)for a,v in sorted(f.items()))

def main():
    start=time.monotonic();gens=list(h.H.items())+[(n+'^-1',p.inv(w))for n,w in h.H.items()]
    allwords={};outer=[]
    for (an,a),(bn,b)in itertools.product(gens,repeat=2):
        w=p.reduce(a+b)
        if tuple(w)in allwords:continue
        ext=p.reduce(h.GAMMA+w+p.inv(h.GAMMA))
        allwords[tuple(w)]=1
        if h.in_embedded_B6(ext)is None:outer.append((an+' '+bn,ext))
    counts={'depth_two_H_words':len(allwords),'genuine_excursions':len(outer),'pairs_tested':0,
            'returns':0,'new_projective_coefficients':0,'zeros':0,'D_closure_failures':0}
    base=projective(p.coefficient(SEED,7,7));seen={base};rows=[]
    for (ln,lw),(rn,rw)in itertools.product(outer,repeat=2):
        counts['pairs_tested']+=1
        full=p.reduce(lw+SEED+rw);beta=h.in_embedded_B6(full)
        if beta is None:continue
        counts['returns']+=1;f=p.coefficient(beta,7,7);key=projective(f)
        if key in seen:continue
        seen.add(key);counts['new_projective_coefficients']+=1
        cl=p.closure_checks(beta,7,7)
        if not cl['denominator_closure']['unknot_certified']:counts['D_closure_failures']+=1
        row={'left_H':ln,'right_H':rn,'beta':beta,'coefficient':f,'closures':cl}
        if not f:
            counts['zeros']+=1;row['topology']=h.tc.classify(beta,7,7)
        rows.append(row)
        if len(rows)>=20 or time.monotonic()-start>120:break
    out={'status':'TRUSTED bounded mechanism test','seed':SEED,'counts':counts,
         'seconds':time.monotonic()-start,'results':rows,
         'scope':'Two Hilden letters per side, each side genuinely outside B6 after cap-system conjugation; no exhaustive full-locus claim.'}
    (HERE/'hilden_outer_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(counts,indent=2));print('seconds',out['seconds'])
if __name__=='__main__':main()
