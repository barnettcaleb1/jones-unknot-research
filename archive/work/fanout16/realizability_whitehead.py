from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/braid_classification/packages'))
from spherogram import Link
import regina
# Load rank routines without executing the earlier finite test driver.
ns={'__file__':str(Path(__file__).parent/'realizability_floer_test.py')};source=(Path(__file__).parent/'realizability_floer_test.py').read_text().split('\nout=[]')[0];exec(source,ns)
ahat=ns['ahat']
out=[]
for mirror in [False,True]:
    C=Link('3_1');C=C.mirror() if mirror else C
    R=regina.Link.fromPD([[x+1 for x in c]for c in C.PD_code()])
    for positive in [False,True]:
        W=R.whiteheadDouble(positive); W.simplify()
        pd=[[x-1 for x in c] for c in W.pdData()]
        L=Link(pd);D=L.knot_floer_homology(complex=True);g=D['seifert_genus']
        aa={s:ahat(D,s) for s in range(-g-1,g+2)}
        V=W.jones();v={e//2:int(str(V[e]))for e in range(V.minExp(),V.maxExp()+1)if int(str(V[e]))}
        a2=-sum(c*e*(e-1)for e,c in v.items())//6
        row={'base_mirror':mirror,'positive_clasp':positive,'PD':pd,'Jones_t':v,'a2':a2,'genus':g,'tau':D['tau'],'nu':D['nu'],'HFK_rank':D['total_rank'],'Ahat_ranks':aa,'large_positive_surgery_rank_excess':sum(v-1 for v in aa.values()),'CFK_generators':{str(k):list(v)for k,v in D['generators'].items()},'CFK_UV0_differentials':{str(k):v for k,v in D['differentials'].items()}}
        out.append(row);print({k:v for k,v in row.items()if k not in['PD','Jones_t','CFK_generators','CFK_UV0_differentials']},flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
