"""Rational source/target curves and exact transverse intersection records."""
from fractions import Fraction as F
from pathlib import Path
import json,time,sys
import transport_pl as pl

def figure8(left,right,r=F(13,50)):
    offsets=[(F(0),-r),(r/2,-r),(r,-r/2),(r,r/2),(r/2,r),
             (-r/2,r),(-r,r/2),(-r,-r/2),(-r/2,-r),(F(0),-r)]
    a=[pl.add(pl.point(left),p)for p in offsets]
    b=[pl.add(pl.point(right),p)for p in reversed(offsets)]
    return a+b+[a[0]]

def intersection_records(a,b):
    out=[];collinear=0;vertices=0
    for i,(p,p1)in enumerate(zip(a,a[1:])):
        u=pl.sub(p1,p)
        for j,(q,q1)in enumerate(zip(b,b[1:])):
            # Cheap exact bounding boxes before determinant arithmetic.
            if any(max(p[k],p1[k])<min(q[k],q1[k]) or
                   max(q[k],q1[k])<min(p[k],p1[k]) for k in(0,1)):
                continue
            v=pl.sub(q1,q);w=pl.sub(q,p);det=pl.cross(u,v)
            if not det:
                if pl.cross(w,u)==0:collinear+=1
                continue
            t=pl.cross(w,v)/det;s=pl.cross(w,u)/det
            if 0<=t<1 and 0<=s<1:
                if t==0 or s==0:vertices+=1
                out.append({'a_param':F(i)+t,'b_param':F(j)+s,
                            'point':pl.add(p,pl.scale(u,t)),
                            'sign':1 if det>0 else-1})
    return out,{'potential_collinear_segments':collinear,'vertex_intersections':vertices}

def exact_curves(matrix_word,source_caps=((1,2),(3,4))):
    source=[pl.braid_curve([pl.point(a),pl.point(b)],[-g for g in matrix_word])
            for a,b in source_caps]
    target=[figure8(1,2),figure8(3,4)]
    return source,target

def rational_model(matrix_word,source_caps=((1,2),(3,4))):
    source,target=exact_curves(matrix_word,source_caps)
    allints=[];checks=[]
    for c in source:
        row=[]
        for t in target:
            ints,check=intersection_records(c,t);row.append(ints);checks.append(check)
        allints.append(row)
    assert not any(c['potential_collinear_segments']or c['vertex_intersections']for c in checks),checks
    return source,target,allints,checks

def complex_records(records):
    return [{'a_param':float(r['a_param']),'b_param':float(r['b_param']),
             'z':complex(float(r['point'][0]),float(r['point'][1])),
             'sign':r['sign']}for r in records]

def float_angle_adapter(matrix_word):
    """Exact intersections; the angle primitive remains a separately checked layer."""
    sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'width6_targeted'))
    import geometric_intersections as old
    source,target,ints,checks=rational_model(matrix_word)
    cs=[pl.complex_curve(c)for c in source];ct=[pl.complex_curve(c)for c in target]
    rawcurves=iter(cs);rawtargets=iter(ct);rawints=iter([complex_records(r)for row in ints for r in row])
    previous=old.braid_curve,old.figure8,old.intersections
    try:
        old.braid_curve=lambda *args,**kwargs:next(rawcurves)
        old.figure8=lambda *args,**kwargs:next(rawtargets)
        old.intersections=lambda *args,**kwargs:next(rawints)
        result=old.model([-g for g in matrix_word])
    finally:
        old.braid_curve,old.figure8,old.intersections=previous
    result['matrix_word']=matrix_word
    result['transport']='Exact rational PL homeomorphism with exact cell-edge splitting'
    result['intersection_geometry']='Exact rational segment intersections, transversality checked'
    result['winding']='Float angle primitives; aggregate exact calibration remains mandatory'
    result['rational_geometry_checks']=checks
    return result

if __name__=='__main__':
    word=[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]
    start=time.monotonic()
    result=float_angle_adapter(word)
    print('RESULT',result['polynomial'],result['TL_line_specialization'],round(time.monotonic()-start,2),flush=True)
    (Path(__file__).parent/'transport_exact_intersections_14.json').write_text(json.dumps(result,indent=2)+'\n')
