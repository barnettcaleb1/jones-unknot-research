from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('work/braid_classification/packages').resolve()))
from spherogram import Link
# Musick1208.4233v3 p71, row11n42: minimal bridge projection DT code.
D=[38,58,114,52,44,106,108,46,50,112,60,36,40,56,116,54,42,-122,-74,-76,-120,-84,-66,-130,-128,-68,-82,-118,-78,-72,-124,-12,150,94,144,136,102,156,100,138,142,96,152,62,110,48,-16,-8,-32,-26,-2,-22,-86,-64,-132,-126,-70,-80,140,98,154,104,134,146,92,148,-88,-20,-4,-28,-30,-6,-18,-90,-14,-10,-34,-24]
assert sorted(abs(x) for x in D)==list(range(2,2*len(D)+1,2))
L=Link('DT: '+str([tuple(D)]))
s=[x.is_over_crossing() for x in L.link_components[0]]
print('crossings',len(D),'overpass count',sum(s[i] and not s[i-1] for i in range(len(s))))
print('overstrands',list(map(len,L.overstrands())))
print('gauss',[(x.crossing.label,x.strand_index,x.is_over_crossing()) for x in L.link_components[0]])
L2=L.copy();L2.simplify('global')
print('simplified',len(L2.crossings),L2.DT_code())
data={'source':'https://arxiv.org/abs/1208.4233','DT':D,'PD':L.PD_code(),'overpass_count':sum(s[i] and not s[i-1] for i in range(len(s))),'overstrand_lengths':list(map(len,L.overstrands())),'simplified_PD':L2.PD_code(),'simplified_DT':L2.DT_code()}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2))
