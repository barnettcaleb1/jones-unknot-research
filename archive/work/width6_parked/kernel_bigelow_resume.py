"""One bounded continuation from the saved prefix46, then sparse parked slices."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,json,time,traceback
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_instrument'))
import transport_pl as pl
import transport_simplify as ts
import transport_exact_intersections as ti
import combinatorial_exact_pairing as ep
from formula_check import path

def clean(d):return {k:v for k,v in d.items()if v}
def encpoly(d):return [[k,v]for k,v in sorted(d.items())if v]
def encode_ints(ints):
    return [[[{'a_param':str(p['a_param']),'b_param':str(p['b_param']),
               'point':[str(z)for z in p['point']],'sign':p['sign']}
             for p in row]for row in c]for c in ints]

def run():
    old=json.loads((HERE/'kernel_bigelow_geometry.json').read_text())
    assert old['completed_prefix']==46 and len(old['effective_matrix_word'])==54
    curves=[[[F(v)for v in p]for p in c]for c in old['source_curves']]
    curves=[[tuple(p)for p in c]for c in curves]
    w=old['effective_matrix_word'];begun=time.monotonic();trace=[]
    out={'input_word':old['input_word'],'i':0,'j':6,'effective_matrix_word':w,
         'resumed_from_prefix':46,'completed_prefix':46,'status':'RESUMING',
         'new_history':trace,'guards':{'vertices_per_arc':70000,'remaining_transport_seconds':240,
                  'parked_positions':4,'winding_comparisons':10000},
         'scope':'Canonical transferred frame; moving source1 against short target0, parking source0 on long target1.'}
    dest=HERE/'kernel_bigelow_resume.json'
    def save():
        out['source_curves']=[pl.encode(c)for c in curves]
        out['seconds']=time.monotonic()-begun
        dest.write_text(json.dumps(out,separators=(',',':'))+'\n')
    for k in range(46,len(w)):
        if time.monotonic()-begun>240:
            out['status']='STOPPED_REMAINING_TRANSPORT_TIME';save();return out
        g=w[k]
        try:curves=[pl.braid_curve(c,[-g],limit=300000)for c in curves]
        except RuntimeError as ex:
            out.update(status='STOPPED_INTERMEDIATE_VERTEX_LIMIT',error=str(ex));save();return out
        curves,stats=ts.simplify_joint(curves,max_seconds=1)
        out['completed_prefix']=k+1
        stats.update(prefix=k+1,matrix_generator=g,total_seconds=time.monotonic()-begun)
        trace.append(stats)
        print('RESUME_PREFIX',k+1,54,[len(c)for c in curves],round(stats['total_seconds'],2),flush=True)
        save()
        if max(map(len,curves))>70000 or time.monotonic()-begun>240:
            out['status']='STOPPED_RESUME_TRANSPORT_GUARD';save();return out
    out['status']='TRANSPORT_COMPLETE';save()
    for radius in(F(13,50),F(17,61),F(19,67),F(23,83)):
        target=[ti.figure8(1,2,radius),ti.figure8(3,4,radius)]
        ints=[];checks=[]
        for c in curves:
            row=[]
            for t in target:
                points,check=ti.intersection_records(c,t);row.append(points);checks.append(check)
            ints.append(row)
        if not any(x['potential_collinear_segments']or x['vertex_intersections']for x in checks):break
    else:raise RuntimeError('No transverse target among fixed radii')
    counts=[[len(x)for x in r]for r in ints]
    out.update(status='GEOMETRY_COMPLETE',target_radius=str(radius),target_curves=[pl.encode(c)for c in target],
               intersection_counts=counts,geometry_checks=checks,one_point_intersections=encode_ints(ints),
               matching_products=[counts[0][0]*counts[1][1],counts[0][1]*counts[1][0]])
    save();print('GEOMETRY_COMPLETE',counts,out['matching_products'],round(out['seconds'],2),flush=True)
    moving=ints[1][0];parks=ints[0][1];selected=[]
    for j,y in enumerate(parks):
        seg=int(y['b_param'])
        if 0<=seg<=8:p=3
        elif 10<=seg<=18:p=4
        else:continue
        selected.append((j,y,p))
        if len(selected)==4:break
    if not moving or not selected:
        out.update(status='NO_SELECTED_MATCHING_INTERSECTIONS');save();return out
    sr=ep.CrossingCurve(curves[1],'ray');tr=ep.CrossingCurve(target[0],'ray')
    ref=moving[0]
    def wind(x,center):
        return tr.change(ref['b_param'],x['b_param'],center)+sr.change(x['a_param'],ref['a_param'],center)
    punctures=[pl.point(p)for p in range(1,7)]
    aa=[sum(wind(x,p)for p in punctures)for x in moving]
    signs=[x['sign']*ref['sign']for x in moving]
    plain=Counter()
    for a,sg in zip(aa,signs):plain[a]+=sg
    out['uncolored_inner_pairing']=encpoly(plain)
    rows=[];comparisons=0;example=None
    for j,y,p in selected:
        if comparisons+len(moving)>10000:break
        colored=Counter();adjacent=Counter();wy=[];wp=[];ds=[]
        for i,x in enumerate(moving):
            sy=wind(x,y['point']);sp=wind(x,pl.point(p));d=sy-sp
            wy.append(sy);wp.append(sp);ds.append(d);comparisons+=1
            colored[aa[i]-2*sy]+=signs[i];adjacent[aa[i]-2*sp]+=signs[i]
            if example is None and (d or (wy and sy!=wy[0])):
                loop=path(target[0],ref['b_param'],x['b_param'])+path(curves[1],x['a_param'],ref['a_param'])[1:]
                assert loop[0]==loop[-1]
                example={'moving_source_index':1,'moving_target_index':0,'parked_source_index':0,'parked_target_index':1,
                         'parked_index':j,'first_index':i,'adjacent_lobe_puncture':p,
                         'parked_position':[str(z)for z in y['point']],
                         'wind_parked':sy,'wind_adjacent_puncture':sp,'difference':d,
                         'closed_first_point_path':[[str(v)for v in pt]for pt in loop]}
        row={'parked_index':j,'parked_position':[str(z)for z in y['point']],
             'adjacent_lobe_puncture':p,'moving_incidence_count':len(moving),
             'wind_parked':wy,'wind_adjacent_puncture':wp,
             'parked_winding_range':[min(wy),max(wy)],'adjacent_winding_range':[min(wp),max(wp)],
             'difference_range':[min(ds),max(ds)],'nonzero_differences':sum(bool(d)for d in ds),
             'uncolored_inner_pairing':encpoly(plain),'parked_colored_inner_pairing':encpoly(colored),
             'adjacent_puncture_colored_inner_pairing':encpoly(adjacent)}
        rows.append(row)
        print('PARKED_SLICE',j,p,'comparisons',len(moving),'plain',encpoly(plain),'colored',encpoly(colored),flush=True)
    out.update(status='SPARSE_PARKED_CHECK_COMPLETE',parked_slices=rows,comparisons=comparisons,explicit_path_example=example)
    save();return out

if __name__=='__main__':
    r=run();print('FINAL',r['status'],r['seconds'],flush=True)
