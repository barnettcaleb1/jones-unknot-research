"""Exact identification of the two variable twist sites in Ren's published PD."""
from pathlib import Path
import contextlib,io,runpy,json
from tangle_ren_twists import blocks,add,mul,shift,DELTA,ONE
with contextlib.redirect_stdout(io.StringIO()):
    data=runpy.run_path(str(Path(__file__).resolve().parents[1]/'pass3/tangle_ren_check.py'))
i,j=3,1
delta_powers=[ONE]
for _ in range(max(c for c,e in data['state_features'])):
    delta_powers.append(mul(delta_powers[-1],DELTA))
out=[{0:{},2:{},4:{}}for _ in range(4)]
for state,(c,e)in enumerate(data['state_features']):
    bi=(state>>i)&1;bj=(state>>j)&1;k=bi+2*bj
    out[k][e]=add(out[k][e],shift(delta_powers[c],10-2*(state.bit_count()-bi-bj)))
out=[{e:p for e,p in block.items()if p}for block in out]
assert out==blocks
indices=[int(data['self_crossings'][k].label)for k in(i,j)]
assert indices==[8,5]
result={'left_twist_PD_crossing_zero_based':8,'right_twist_PD_crossing_zero_based':5,
        'left_PD_tuple_source':data['PD'][8],'right_PD_tuple_source':data['PD'][5],
        'all_four_exact_resolved_annular_brackets_match_TL6_model':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
