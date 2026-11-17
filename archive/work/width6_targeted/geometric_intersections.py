"""PL geometric square/figure-eight-product intersection data.

This is a geometric model, not an expansion of representation matrices.
Numerical positions are checked by refinement; integer winding is rounded only
after recording its error. It does not certify a cap-slide minimum.
"""
import cmath
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUNCTURES = [complex(k, 0) for k in range(1, 7)]


def cross(a, b):
    return (a.conjugate() * b).imag


def figure8(left, right, n=64, radius=.26):
    # The connectors retrace below the real axis. They have no intersections
    # with the undeformed source arcs; multiplicities are retained if crossed.
    lb = complex(left, -radius)
    rb = complex(right, -radius)
    out = [lb]
    for k in range(1, n+1):
        out.append(left + radius * cmath.exp(1j * (-math.pi/2 + 2*math.pi*k/n)))
    out.append(rb)
    for k in range(1, n+1):
        out.append(right + radius * cmath.exp(1j * (-math.pi/2 - 2*math.pi*k/n)))
    out.append(lb)
    return out


def rotate_braid(z, generator):
    center = abs(generator) + .5
    w = z-center
    radius = abs(w)
    if radius >= .9:
        return z
    if radius <= .55:
        weight = 1.0
    else:
        u = (radius-.55)/.35
        weight = 1 - (3*u*u-2*u*u*u)
    angle = (1 if generator > 0 else -1)*math.pi*weight
    return center + w*cmath.exp(1j*angle)


def subdivide(curve, max_step):
    out = [curve[0]]
    for a, b in zip(curve, curve[1:]):
        n = max(1, math.ceil(abs(b-a)/max_step))
        out.extend(a+(b-a)*k/n for k in range(1, n+1))
    return out


def braid_curve(curve, word, step=.006):
    # Word convention here is chronological action on geometry.
    for g in word:
        curve = [rotate_braid(z, g) for z in subdivide(curve, step)]
    return curve


def intersections(a, b):
    out = []
    for i, (p, p1) in enumerate(zip(a, a[1:])):
        u = p1-p
        for j, (q, q1) in enumerate(zip(b, b[1:])):
            v = q1-q
            det = cross(u, v)
            if abs(det) < 1e-14:
                continue
            s = cross(q-p, v)/det
            t = cross(q-p, u)/det
            # Half-open segments avoid double counting polygon vertices.
            if -1e-10 <= s < 1-1e-10 and -1e-10 <= t < 1-1e-10:
                z=p+s*u
                out.append({'a_param':i+s, 'b_param':j+t,
                            'z':z, 'sign':1 if det > 0 else -1})
    return out


def at(curve, t):
    if t >= len(curve)-1:
        return curve[-1]
    k=max(0, int(t))
    return curve[k]+(curve[k+1]-curve[k])*(t-k)


def path(curve, start, end):
    if start > end:
        return list(reversed(path(curve, end, start)))
    ts=[start]+[k for k in range(math.floor(start)+1, math.ceil(end)) if start < k < end]+[end]
    return [at(curve,t) for t in ts]


def pair_path(curves, starts, ends):
    # Move points successively. The two supporting curves are disjoint.
    p0=path(curves[0],starts[0],ends[0])
    p1=path(curves[1],starts[1],ends[1])
    return [(z,p1[0]) for z in p0]+[(p0[-1],z) for z in p1[1:]]


def angle_sum(zs):
    return sum(cmath.phase(b/a) for a,b in zip(zs,zs[1:]))


def exponents(loop):
    a=sum(angle_sum([zs[k]-p for zs in loop]) for p in PUNCTURES for k in (0,1))/(2*math.pi)
    b=angle_sum([zs[0]-zs[1] for zs in loop])/math.pi
    ai,bi=round(a),round(b)
    error=max(abs(a-ai),abs(b-bi))
    assert error < 1e-6, (a,b,error)
    return ai,bi,error


class AngleCurve:
    def __init__(self, curve):
        self.curve=curve
        self.cache={}

    def value(self, t, center):
        if center not in self.cache:
            prefix=[0.0]
            for a,b in zip(self.curve,self.curve[1:]):
                z,w=a-center,b-center
                change=cmath.phase(w/z) if abs(z)>1e-12 and abs(w)>1e-12 else 0.0
                prefix.append(prefix[-1]+change)
            self.cache[center]=prefix
        prefix=self.cache[center]
        k=min(int(t),len(self.curve)-2)
        z=self.curve[k]-center
        w=at(self.curve,t)-center
        if abs(z)<1e-12:
            z=self.curve[k+1]-center
        change=cmath.phase(w/z) if abs(w)>1e-12 else 0.0
        return prefix[k]+change

    def change(self, start, end, center):
        return self.value(end,center)-self.value(start,center)


def model(word, resolution=64, step=.006, source_caps=((1,2),(3,4))):
    source=[braid_curve([complex(a),complex(b)],word,step)for a,b in source_caps]
    target=[figure8(1,2,resolution),figure8(3,4,resolution)]
    allints=[[intersections(c,n) for n in target] for c in source]
    configs=[]
    for matching in (0,1):
        for x in allints[0][matching]:
            for y in allints[1][1-matching]:
                configs.append({'matching':matching,'points':[x,y],
                                'sign':x['sign']*y['sign']*(-1 if matching else 1)})
    print('GEOMETRY',word,'curve_vertices',[len(c)for c in source],
          'intersection_counts',[[len(x)for x in r]for r in allints],
          'configuration_count',len(configs),flush=True)
    if not configs:
        return {'word':word,'source_caps':source_caps,
                'intersection_counts':[[len(x)for x in r]for r in allints],
                'one_point_intersections':[[[{'source_parameter':p['a_param'],
                                            'target_parameter':p['b_param'],
                                            'position':[p['z'].real,p['z'].imag],
                                            'sign':p['sign']}for p in pts]for pts in row]
                                           for row in allints],
                'configurations':[], 'polynomial':[], 'TL_line_specialization':{}}
    base=configs[0]
    base_targets=[None,None]
    for i,p in enumerate(base['points']):
        base_targets[base['matching'] if i==0 else 1-base['matching']]=p['b_param']
    records=[]
    poly={}
    sa=[AngleCurve(c)for c in source]
    ta=[AngleCurve(c)for c in target]
    for index,conf in enumerate(configs):
        end_targets=[None,None]
        for i,p in enumerate(conf['points']):
            end_targets[conf['matching'] if i==0 else 1-conf['matching']]=p['b_param']
        # Same B followed by A^-1 loop as the explicit trajectory version,
        # using cached winding primitives rather than resumming long paths.
        source_start=[p['a_param']for p in conf['points']]
        source_end=[p['a_param']for p in base['points']]
        av=sum(ta[i].change(base_targets[i],end_targets[i],p)
               +sa[i].change(source_start[i],source_end[i],p)
               for p in PUNCTURES for i in (0,1))/(2*math.pi)
        bv=(ta[0].change(base_targets[0],end_targets[0],at(target[1],base_targets[1]))
            +ta[1].change(base_targets[1],end_targets[1],at(target[0],end_targets[0]))
            +sa[0].change(source_start[0],source_end[0],conf['points'][1]['z'])
            +sa[1].change(source_start[1],source_end[1],base['points'][0]['z']))/math.pi
        a,b=round(av),round(bv)
        error=max(abs(av-a),abs(bv-b))
        assert error<1e-6,(av,bv,error)
        sign=conf['sign']*base['sign']
        poly[a,b]=poly.get((a,b),0)+sign
        records.append({'index':index,'matching':conf['matching'], 'a':a,'b':b,'sign':sign,
                        'winding_error':error,
                        'source_parameters':[p['a_param']for p in conf['points']],
                        'target_parameters':[p['b_param']for p in conf['points']],
                        'positions':[[p['z'].real,p['z'].imag]for p in conf['points']]})
    spec={}
    for (a,b),v in poly.items():
        spec[a-b]=spec.get(a-b,0)+v*((-1)**b)
    return {'word':word,'resolution':resolution,'step':step,
            'intersection_counts':[[len(x)for x in r]for r in allints],
            'configurations':records,
            'polynomial':[[a,b,v]for(a,b),v in sorted(poly.items())if v],
            'TL_line_specialization':{str(k):int(v)for k,v in sorted(spec.items())if v}}


if __name__=='__main__':
    results={}
    for label,word in [('identity',[]),('sigma2',[2]),('sigma2_inverse',[-2])]:
        low=model(word,64,.006)
        high=model(word,128,.003)
        assert low['polynomial']==high['polynomial'], label
        results[label]=high
        print(label,'counts',high['intersection_counts'],'configurations',len(high['configurations']),
              'poly',high['polynomial'],'spec',high['TL_line_specialization'])
    (HERE/'geometric_controls.json').write_text(json.dumps(results,indent=2)+'\n')
