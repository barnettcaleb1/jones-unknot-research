"""One guarded geometry attempt for the specified Bigelow configuration."""
from pathlib import Path
from fractions import Fraction as F
import sys,time,json,traceback
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_instrument'))
sys.path.insert(0,str(HERE.parent/'width6'))
import transport_pl as pl
import transport_simplify as ts
import transport_exact_intersections as ti
import combinatorial_exact_pairing as ep
from intersection_instrument import effective_word
from kernel_words import BIGELOW6_REN
from formula_check import path

def encode_ints(ints):
    return [[[{'a_param':str(p['a_param']),'b_param':str(p['b_param']),
               'point':[str(z)for z in p['point']],'sign':p['sign']}
              for p in row]for row in c]for c in ints]

def run():
    start=time.monotonic();w=effective_word(BIGELOW6_REN,0,6)
    curves=[[pl.point(1),pl.point(2)],[pl.point(3),pl.point(4)]];history=[]
    result={'input_word':BIGELOW6_REN,'i':0,'j':6,'effective_matrix_word':w,
            'status':'RUNNING','history':history,
            'guards':{'transport_seconds':180,'vertices_per_arc':15000,'winding_comparisons':10000},
            'scope':'Canonical isometric counterpart: short object is target loop, not literal original source s=k(12).'}
    dest=HERE/'kernel_bigelow_geometry.json'
    for k,g in enumerate(w):
        curves=[pl.braid_curve(c,[-g],limit=200000)for c in curves]
        curves,stats=ts.simplify_joint(curves,max_seconds=1)
        stats.update(prefix=k+1,matrix_generator=g,total_seconds=time.monotonic()-start)
        history.append(stats)
        print('PREFIX',k+1,len(w),[len(c)for c in curves],round(stats['total_seconds'],2),flush=True)
        if max(map(len,curves))>15000 or time.monotonic()-start>180:
            result.update(status='STOPPED_AT_TRANSPORT_GUARD',source_curves=[pl.encode(c)for c in curves],
                          completed_prefix=k+1,total_seconds=time.monotonic()-start)
            dest.write_text(json.dumps(result,separators=(',',':'))+'\n');return result
    result['source_curves']=[pl.encode(c)for c in curves]
    result['status']='TRANSPORT_COMPLETE';dest.write_text(json.dumps(result,separators=(',',':'))+'\n')
    for radius in(F(13,50),F(17,61),F(19,67),F(23,83)):
        target=[ti.figure8(1,2,radius),ti.figure8(3,4,radius)]
        ints=[];checks=[]
        for c in curves:
            row=[]
            for t in target:
                points,check=ti.intersection_records(c,t);row.append(points);checks.append(check)
            ints.append(row)
        if not any(c['potential_collinear_segments']or c['vertex_intersections']for c in checks):break
    else:raise RuntimeError('No transverse target among fixed radii')
    counts=[[len(x)for x in r]for r in ints]
    result.update(target_radius=str(radius),target_curves=[pl.encode(c)for c in target],
                  intersection_counts=counts,geometry_checks=checks,one_point_intersections=encode_ints(ints),
                  matching_products=[counts[0][0]*counts[1][1],counts[0][1]*counts[1][0]],
                  status='EXACT_GEOMETRY_COMPLETE')
    # Persist actual geometry before any winding budget is checked.
    dest.write_text(json.dumps(result,separators=(',',':'))+'\n')
    sr=[ep.CrossingCurve(c,'ray')for c in curves];tr=[ep.CrossingCurve(t,'ray')for t in target]
    # The canonical transfer puts the short object in target loop0. For the
    # relevant cross matching, move source1 against target0 and park source0
    # on target1. This is an isometric counterpart, not literal s=k(12).
    moving_source,parked_source,moving_target,parked_target=1,0,0,1
    selected=[]
    for m in(1,):
        if not ints[moving_source][moving_target]:continue
        lobe=[]
        for j,y in enumerate(ints[parked_source][parked_target]):
            seg=int(y['b_param'])
            if 0<=seg<=8:p=1+2*parked_target
            elif 10<=seg<=18:p=2+2*parked_target
            else:continue
            lobe.append((m,j,y,p))
            if len(lobe)==2:break
        selected.extend(lobe)
    comparisons=0;rows=[];example=None
    for m,j,y,p in selected:
        if comparisons+len(ints[moving_source][moving_target])>10000:break
        ref=ints[moving_source][moving_target][0];deltas=[];parked_windings=[];adjacent_windings=[]
        def wind(x,center):
            return tr[moving_target].change(ref['b_param'],x['b_param'],center)+sr[moving_source].change(x['a_param'],ref['a_param'],center)
        for i,x in enumerate(ints[moving_source][moving_target]):
            wy=wind(x,y['point']);wp=wind(x,pl.point(p));d=wy-wp;deltas.append(d);comparisons+=1
            parked_windings.append(wy);adjacent_windings.append(wp)
            if d and example is None:
                loop=path(target[moving_target],ref['b_param'],x['b_param'])+path(curves[moving_source],x['a_param'],ref['a_param'])[1:]
                assert loop[0]==loop[-1]
                example={'matching':m,'parked_index':j,'first_index':i,'lobe_puncture':p,
                         'parked_position':[str(z)for z in y['point']],
                         'wind_parked':wy,'wind_adjacent_puncture':wp,'difference':d,
                         'reference_closed_path':[list(map(str,z))for z in loop]}
        rows.append({'matching':m,'parked_index':j,'lobe_puncture':p,'first_intersections':len(deltas),
                     'wind_parked':parked_windings,'wind_adjacent_puncture':adjacent_windings,
                     'parked_winding_range':[min(parked_windings),max(parked_windings)],
                     'adjacent_winding_range':[min(adjacent_windings),max(adjacent_windings)],
                     'difference_range':[min(deltas),max(deltas)],'nonzero_differences':sum(bool(x)for x in deltas)})
    result.update(status='BOUNDED_PARKED_COMPARISON_COMPLETE',parked_comparisons=comparisons,
                  parked_summary=rows,first_nonzero_difference=example,total_seconds=time.monotonic()-start,
                  moving_source_index=moving_source,parked_source_index=parked_source,
                  moving_target_index=moving_target,parked_target_index=parked_target)
    dest.write_text(json.dumps(result,separators=(',',':'))+'\n');return result

if __name__=='__main__':
    r=run();print('FINAL',r['status'],r.get('total_seconds'),flush=True)
