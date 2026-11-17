"""Large-surgery rank from UV=0 knot Floer complex; no mixed arrows needed."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/braid_classification/packages'))
from spherogram import Link

def rank2(cols):
    basis={}
    for v in cols:
        while v:
            k=v.bit_length()-1
            if k in basis:v^=basis[k]
            else:basis[k]=v;break
    return len(basis)

def ahat(data,s):
    G=data['generators']; D=data['differentials']; n=len(G); cols=[0]*n
    shift={i:max(0,A-s) for i,(A,M) in G.items()}
    for (i,j),c in D.items():
        Ai,Mi=G[i]; Aj,Mj=G[j]
        if Mi-Mj==1:r=0
        else:
            r=Aj-Ai
            assert r>0 and Mi-Mj+2*r==1
        if shift[i]+r==shift[j]:cols[i]^=1<<j
        else:assert shift[i]+r>shift[j]
    for v in cols:
        dv=0
        while v:
            k=v.bit_length()-1;v^=1<<k;dv^=cols[k]
        assert dv==0
    return n-2*rank2(cols)

out=[]
for name in ['3_1','4_1','6_1','K11n42','K11n34']:
    L=Link(name);D=L.knot_floer_homology(complex=True);g=D['seifert_genus']
    aa={s:ahat(D,s) for s in range(-g-1,g+2)}
    assert aa[-g-1]==aa[-g]==aa[g]==aa[g+1]==1
    excess=sum(v-1 for v in aa.values())
    row={'name':name,'PD':L.PD_code(),'genus':g,'tau':D['tau'],'nu':D['nu'],'HFK_rank':D['total_rank'],'Ahat_ranks':aa,'large_positive_surgery_rank_excess':excess,'CFK_generators':{str(k):list(v) for k,v in D['generators'].items()},'CFK_UV0_differentials':{str(k):v for k,v in D['differentials'].items()}}
    out.append(row);print(name,'genus',g,'Ahat',aa,'rank excess',excess)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
