"""One fixed nonzero control: compare its parked puncture with lobe puncture."""
from pathlib import Path
from fractions import Fraction as F
import json
from formula_check import load_case,path
import combinatorial_exact_pairing as ep

saved,source,target,ints=load_case('nonzero_control')
sr=[ep.CrossingCurve(c,'ray')for c in source]
tr=[ep.CrossingCurve(c,'ray')for c in target]
rows=[];example=None;total=0;different=0;connectors=0
for m in(0,1):
    xref=ints[0][m][0]
    def winding(x,center):
        return tr[m].change(xref['b_param'],x['b_param'],center)+sr[0].change(x['a_param'],xref['a_param'],center)
    for j,y in enumerate(ints[1][1-m]):
        segment=int(y['b_param'])
        if 0<=segment<=8:puncture=1+2*(1-m)
        elif 10<=segment<=18:puncture=2+2*(1-m)
        else:
            connectors+=1;rows.append({'matching':m,'parked_index':j,'target_segment':segment,
               'status':'CONNECTOR_NO_CANONICAL_ADJACENT_PUNCTURE'});continue
        deltas=[];wys=[];wps=[]
        for i,x in enumerate(ints[0][m]):
            wy=winding(x,y['point']);wp=winding(x,(F(puncture),F(0)))
            delta=wy-wp;total+=1;different+=bool(delta)
            deltas.append(delta);wys.append(wy);wps.append(wp)
            if delta and example is None:
                loop=path(target[m],xref['b_param'],x['b_param'])+path(source[0],x['a_param'],xref['a_param'])[1:]
                assert loop[0]==loop[-1]
                example={'matching':m,'parked_index':j,'first_intersection_index':i,
                         'adjacent_puncture':puncture,'target_lobe_segment':segment,
                         'parked_position':[str(v)for v in y['point']],
                         'first_position':[str(v)for v in x['point']],
                         'wind_parked':wy,'wind_adjacent_puncture':wp,'winding_difference':delta,
                         'colored_exponent_difference':-2*delta,
                         'closed_first_point_path':[[str(v)for v in p]for p in loop]}
        rows.append({'matching':m,'parked_index':j,'adjacent_puncture':puncture,'target_segment':segment,
             'parked_position':[str(v)for v in y['point']],
             'parked_winding_range':[min(wys),max(wys)],'adjacent_winding_range':[min(wps),max(wps)],
             'difference_range':[min(deltas),max(deltas)],'nonzero_differences':sum(bool(x)for x in deltas)})
out={'case':'nonzero_control','input_word':[2,1,-2,3,2,-3],'cap_indices':[3,7],
     'checked_lobe_incidences':total,'nonzero_differences':different,'connector_parked_positions_omitted':connectors,
     'example':example,'parked_position_summary':rows,
     'scope':'Only this existing nonzero control, not either kernel-braid configuration. No new word or minimization.'}
dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps(out,indent=2)+'\n')
print('RESULT',total,different,'example',None if example is None else{k:v for k,v in example.items()if k!='closed_first_point_path'})
