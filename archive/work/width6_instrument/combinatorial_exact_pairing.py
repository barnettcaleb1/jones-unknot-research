"""Exact integer monodromy on rational square/torus intersection records.

Geometry from transport_exact_intersections; exponents from signed crossings,
not floating angle sums. All output pairs refer to actual geometric points.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import json, time, sys
import combinatorial_winding as cw
from transport_exact_intersections import rational_model


def at(curve,t):
    k=min(int(t),len(curve)-2)
    u=t-k
    return (curve[k][0]+u*(curve[k+1][0]-curve[k][0]),
            curve[k][1]+u*(curve[k+1][1]-curve[k][1]))


class CrossingCurve:
    def __init__(self,curve,kind,lean=F(1,101)):
        self.curve=curve
        self.kind=kind
        self.lean=lean
        self.prefix={}
        self.values={}
        self.h=[p[0]-lean*p[1] for p in curve]
        self.primitive=cw.ray_segment_count if kind=='ray' else cw.line_segment_count

    def segment(self,a,b,center):
        # Source arcs terminate at punctures. Prefix constants there are arbitrary;
        # every queried change has interior endpoints, so they cancel exactly.
        if self.kind=='ray' and (a==center or b==center):
            return 0
        return self.primitive(a,b,center,self.lean)

    def value(self,t,center):
        key=(t,center)
        if key in self.values:
            return self.values[key]
        if center not in self.prefix:
            prefix=[0]
            ch=center[0]-self.lean*center[1]
            for i,(a,b) in enumerate(zip(self.curve,self.curve[1:])):
                f,g=self.h[i]-ch,self.h[i+1]-ch
                delta=self.segment(a,b,center) if ((f<=0<g) or (g<=0<f)) else 0
                prefix.append(prefix[-1]+delta)
            self.prefix[center]=prefix
        k=min(int(t),len(self.curve)-2)
        p=at(self.curve,t)
        v=self.prefix[center][k]+self.segment(self.curve[k],p,center)
        self.values[key]=v
        return v

    def change(self,start,end,center):
        return self.value(end,center)-self.value(start,center)


def exact_model(word,source_caps=((1,2),(3,4)),keep_records=True,progress=50000,lean=F(1,101)):
    begun=time.monotonic()
    source,target,ints,checks=rational_model(word,source_caps)
    counts=[[len(row) for row in s] for s in ints]
    total=sum(counts[0][m]*counts[1][1-m] for m in (0,1))
    print('EXACT_GEOMETRY',word,[len(c) for c in source],counts,total,flush=True)
    records=[]
    poly=Counter()
    if not total:
        return {'word':word,'source_caps':source_caps,'configuration_count':0,
                'intersection_counts':counts,'geometry_checks':checks,
                'polynomial':[],'TL_line_specialization':{},'records':[],
                'seconds':round(time.monotonic()-begun,3),
                'winding_method':'No complete matching: the actual configuration intersection set is empty',
                'one_point_intersections':[[[{'source_parameter':str(p['a_param']),
                    'target_parameter':str(p['b_param']),'position':[str(z)for z in p['point']],
                    'sign':p['sign']}for p in row]for row in s]for s in ints]}
    bm=next(m for m in (0,1) if counts[0][m] and counts[1][1-m])
    base=[ints[0][bm][0],ints[1][1-bm][0]]
    bt=[None,None]
    bt[bm]=base[0]['b_param'];bt[1-bm]=base[1]['b_param']
    bs=[p['a_param'] for p in base]
    bsign=base[0]['sign']*base[1]['sign']*(-1 if bm else 1)
    r=(base[0]['point'][0]-base[1]['point'][0],base[0]['point'][1]-base[1]['point'][1])
    assert r[0]-lean*r[1]!=0
    sr=[CrossingCurve(c,'ray',lean)for c in source]
    tr=[CrossingCurve(c,'ray',lean)for c in target]
    sl=[CrossingCurve(c,'line',lean)for c in source]
    tl=[CrossingCurve(c,'line',lean)for c in target]
    punctures=[(F(j),F(0))for j in range(1,7)]
    # Puncture winding splits into independently precomputed one-point terms.
    a_terms={}
    for i in (0,1):
        for m in (0,1):
            for k,p in enumerate(ints[i][m]):
                a_terms[i,m,k]=sum(tr[m].change(bt[m],p['b_param'],c)
                    +sr[i].change(p['a_param'],bs[i],c)for c in punctures)
    ti1base=at(target[1],bt[1])
    b0=base[0]['point']
    index=0
    for m in (0,1):
        for i,x in enumerate(ints[0][m]):
            for j,y in enumerate(ints[1][1-m]):
                t0,t1=(x,y)if m==0 else(y,x)
                a=a_terms[0,m,i]+a_terms[1,1-m,j]
                b=(tl[0].change(bt[0],t0['b_param'],ti1base)
                    +tl[1].change(bt[1],t1['b_param'],t0['point'])
                    +sl[0].change(x['a_param'],bs[0],y['point'])
                    +sl[1].change(y['a_param'],bs[1],b0))
                assert b%2==int(m!=bm),(m,bm,a,b)
                sign=x['sign']*y['sign']*(-1 if m else 1)*bsign
                poly[a,b]+=sign
                if keep_records:records.append([m,i,j,a,b,sign])
                index+=1
                if progress and index%progress==0:
                    print('EXACT_PAIRS',index,total,round(time.monotonic()-begun,2),flush=True)
    spec=Counter()
    for (a,b),coefficient in poly.items():
        spec[a-b]+=coefficient*(-1 if b%2 else 1)
    result={'word':word,'source_caps':source_caps,'configuration_count':total,
            'intersection_counts':counts,'geometry_checks':checks,
            'winding_method':'Exact rational ray crossings for a; signed full-line crossings in RP1 for b',
            'cut_lean':str(lean),'base_matching':bm,'base_point_indices':[0,0],
            'record_columns':['matching','source0_point_index','source1_point_index','a','b','sign'],
            'records':records,
            'polynomial':[[a,b,v]for(a,b),v in sorted(poly.items())if v],
            'TL_line_specialization':{str(k):v for k,v in sorted(spec.items())if v},
            'seconds':round(time.monotonic()-begun,3)}
    # One-point coordinates recorded once; every pair row refers back to them.
    result['one_point_intersections']=[[[{'source_parameter':str(p['a_param']),
         'target_parameter':str(p['b_param']),'position':[str(z)for z in p['point']],
         'sign':p['sign']}for p in row]for row in s]for s in ints]
    return result


if __name__=='__main__':
    cases={'identity':[],'sigma2':[2],'witness14':[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]}
    label=sys.argv[1]if len(sys.argv)>1 else'witness14'
    result=exact_model(cases[label])
    destination=Path(__file__).parent/f'combinatorial_exact_{label}.json'
    destination.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('RESULT',label,result['polynomial'],result['TL_line_specialization'],result['seconds'],str(destination),flush=True)
