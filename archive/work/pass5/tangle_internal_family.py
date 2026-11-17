"""Complete highest-channel classification for a two-parameter Ren family.

The completeness proof is algebraic (roots of unity), not the finite checks.
The finite checks independently verify the formula against the full TL6 model.
"""
from pathlib import Path
import sys, json
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'pass4'))
import tangle_ren_twists as t
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'braid_classification/packages'))
from spherogram.links.tangles import BraidTangle, Tangle, join_strands
import regina

def run(i, k):
    return [i if k > 0 else -i] * abs(k)

def word(r, k):
    return run(2,r)+run(1,k)+run(2,r)+run(4,-r)+run(5,-k)+run(4,-r)

def blocks(r,k):
    v=[{} for _ in t.basis];v[t.ident]=t.ONE
    for i in word(r,k):v=t.times_crossing(v,i)
    return [t.close(v),t.close(t.times_e(v,1)),t.close(t.times_e(v,5)),
            t.close(t.times_e(t.times_e(v,1),5))]

def zp(k):
    return {-4*k:-1 if k%2 else 1}

def C(k):
    return t.add(zp(k),zp(-k))

D=t.mul(t.DELTA,t.DELTA)
def numerator(r,k):
    S=t.add(C(r),{0:-2})
    return t.add(t.add(t.mul(D,D),t.mul(t.add(D,{0:-1}),t.mul(S,S))),
                 t.add(t.mul(t.add(t.shift(D,0,4),{0:-2}),S),t.mul(S,C(r+k))))

formula_checks=[]
for r,k in [(-3,-2),(-2,3),(-1,-3),(-1,-1),(-1,0),(-1,3),
            (0,0),(0,3),(1,1),(1,-3),(2,1),(3,5)]:
    bb=blocks(r,k)
    actual=t.mul(t.mul(t.mul(t.DELTA,t.DELTA),t.DELTA),bb[0].get(4,{}))
    assert actual==numerator(r,k),(r,k,actual,numerator(r,k))
    formula_checks.append([r,k])

survivors=[[-1,3],[-1,-1],[1,1],[1,-3]]
all_blocks={str((r,k)):blocks(r,k) for r,k in survivors}
assert all(not b.get(4) for bb in all_blocks.values() for b in bb)
newblocks=all_blocks[str((-1,-1))]
assert [b.get(2,{}) for b in newblocks]==[{6:-1,-6:-1},{8:1},{-8:1},{}]

def annular(r,k,p,q):
    f,g=t.power_coeff(p);h,j=t.power_coeff(q)
    weights=[t.mul(f,h),t.mul(g,h),t.mul(f,j),t.mul(g,j)]
    out={}
    for degree in [0,2,4]:
        v={}
        for weight,b in zip(weights,blocks(r,k)):
            v=t.add(v,t.mul(weight,b.get(degree,{})))
        if v:out[degree]=v
    return out

def diagram_with_axis(r,k,p,q):
    w=word(r,k)+run(1,p)+run(5,q)
    tt=BraidTangle(w,6).copy();e=tt.adjacent.copy()
    join_strands(e[2],e[3]);join_strands(e[8],e[9])
    four=Tangle((4,4),tt.crossings,[e[i] for i in [0,1,4,5,6,7,10,11]])
    # Last strand winds once around the four closure strands; its closure is axis.
    return ((four|BraidTangle([],1))*BraidTangle([4,3,2,1,1,2,3,4],5)).braid_closure()

def regina_link(L):
    return regina.Link.fromPD([[x+1 for x in row] for row in L.PD_code()])

published=json.loads((Path(__file__).resolve().parents[1]/'pass3/tangle_ren_check.json').read_text())
original=regina_link(diagram_with_axis(-1,3,1,1)).jones()
original_A={-2*e:int(str(original[e])) for e in range(original.minExp(),original.maxExp()+1) if original[e]!=0}
assert original_A=={int(e):c for e,c in published['Jones_K_union_axis_in_A'].items()}

topology=[]
for p,q in [(1,-1),(3,-3)]:
    assert annular(-1,-1,p,q)=={0:t.DELTA}
    L=diagram_with_axis(-1,-1,p,q);pd=L.PD_code();R=regina_link(L)
    J=str(R.jones());R.simplify();L.simplify('global')
    spherogram_components=len(L.link_components)+L.unlinked_unknot_components
    assert R.size()==0 and R.countComponents()==2
    assert len(L.crossings)==0 and spherogram_components==2
    topology.append({'p':p,'q':q,'axis_link_PD_zero_based':pd,'axis_link_Jones':J,
                     'Regina_crossings':R.size(),'Regina_components':R.countComponents(),
                     'Spherogram_crossings':len(L.crossings),'Spherogram_components':spherogram_components})

out={'family':'(sigma2^r sigma1^k sigma2^r)(sigma4^-r sigma5^-k sigma4^-r)',
     'highest_channel_formula':'delta^3 a4 = D^2+(D-1)S^2+(4D-2)S+S C_(r+k), D=2-z-z^-1, S=z^r+z^-r-2, C_j=z^j+z^-j, z=-A^-4',
     'all_integer_highest_channel_zero_parameters':survivors,
     'proof':'r=0 gives D^2; |r|>1 evaluated at a nontrivial r-th root of unity gives D^2 nonzero; |r|=1 gives D(C_2-C_(r+k)), hence r+k=+/-2',
     'independent_full_TL6_formula_checks':formula_checks,
     'survivor_four_block_brackets':all_blocks,
     'new_family_degree_two_formula':'delta A^(-p-q) a2 = z^(p-2)+z^(q+2)-z-z^-1',
     'new_family_all_integer_annular_degree_zero_parameters':[[1,-1],[3,-3]],
     'axis_construction_matches_published_Ren_Jones':True,
     'new_degree_zero_cases_are_geometrically_inessential':topology}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ('survivor_four_block_brackets','new_degree_zero_cases_are_geometrically_inessential')},indent=2))
