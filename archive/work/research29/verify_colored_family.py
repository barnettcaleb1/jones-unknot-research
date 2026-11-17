#!/usr/bin/env python3
"""Portable exact certificate for a fixed-Jones, unbounded-color-three family.

Default: verify stored polynomial arithmetic and an independent eighth
sample of the fusion recurrence. --diagrams: regenerate actual diagrams
with the existing local Spherogram/Regina packages first.
The all-integer inference is the fusion theorem in colored_global.txt;
sampling alone is not its proof.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import argparse,json,os,sys
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--diagrams',action='store_true')
parser.add_argument('--packages',type=Path,help='Directory containing Regina and Spherogram; alternatively JONES_REPLAY_PACKAGES')
args=parser.parse_args()

def add(a,b):
    c=defaultdict(int,a)
    for e,v in b.items(): c[e]+=v
    return {e:v for e,v in c.items() if v}
def mul(a,b):
    c=defaultdict(int)
    for e,v in a.items():
        for f,w in b.items():c[e+f]+=v*w
    return {e:v for e,v in c.items() if v}
def divide(a,b):
    ans={};rem=dict(a);bmax=max(b);bmin=min(b)
    while rem and max(rem)>=min(a)-bmin+bmax:
        e=max(rem)-bmax;c=F(rem[max(rem)],b[bmax])
        ans[e]=ans.get(e,0)+c
        rem=add(rem,{e+f:-c*v for f,v in b.items()})
    assert not rem,rem
    assert all(v.denominator==1 for v in ans.values())
    return {e:int(v) for e,v in ans.items() if v}
def evaluate(a,x):return sum(F(v)*x**e for e,v in a.items())
def solve(a,b):
    m=[list(map(F,r))+[F(v)] for r,v in zip(a,b)];n=len(m)
    for j in range(n):
        p=next(i for i in range(j,n) if m[i][j]);m[j],m[p]=m[p],m[j]
        d=m[j][j];m[j]=[v/d for v in m[j]]
        for i in range(n):
            if i!=j:
                d=m[i][j];m[i]=[x-d*y for x,y in zip(m[i],m[j])]
    return [r[-1] for r in m]

if args.diagrams:
    packages=args.packages or Path(os.environ.get('JONES_REPLAY_PACKAGES',HERE.parent/'braid_classification/packages'))
    if not packages.exists():packages=HERE/'packages'
    sys.path.insert(0,str(packages))
    import regina,spherogram
    print('Diagram runtime:',sys.version.split()[0], 'Regina',regina.versionString(),
          'Spherogram',getattr(spherogram,'__version__','unknown'))
    from spherogram.links.tangles import Tangle,Strand,RationalTangle,BraidTangle
    def endcap(t,top):
        u=t.reshape((4,0) if top else (0,4)).copy();o=Strand('outer')
        return Tangle((6,0) if top else (0,6),u.crossings+[o],[(o,0)]+u.adjacent+[(o,1)])
    alpha=[1,1,1,-2,1]
    beta=alpha+[-(6-abs(i))*(1 if i>0 else -1) for i in alpha]
    rows=[]
    for m in range(8):
        L=(endcap(RationalTangle(2*m),True)*BraidTangle(beta,6)*endcap(RationalTangle(-2*m),False)).link()
        assert len(L.link_components)==1 and L.writhe()==0
        R=regina.Link.fromPD([[x+1 for x in row] for row in L.PD_code()]);R.simplify()
        C=R.parallel(2,regina.Framing.Seifert);C.simplify();J=C.jones()
        co={e:int(str(J[e])) for e in range(J.minExp(),J.maxExp()+1) if J[e]}
        rows.append(dict(m=m,PD=R.pdData(),writhe=R.writhe(),V=str(R.jones()),cable=co))
    (HERE/'watson_color3_samples.json').write_text(json.dumps(rows,indent=2)+'\n')

rows=json.loads((HERE/'watson_color3_samples.json').read_text())
assert len(rows)==8 and len({r['V'] for r in rows})==1
assert all(r['writhe']==0 for r in rows)
delta={1:-1,-1:-1};dim3={2:1,0:1,-2:1}
polys=[]
for r in rows:
    cable={int(e):v for e,v in r['cable'].items()}
    H=divide(add(mul(delta,cable),{0:-1}),dim3)
    assert mul(H,dim3)==add(mul(delta,cable),{0:-1})
    assert sum(H.values())==1 and sum(e*v for e,v in H.items())==0
    assert all(e%2==0 for e in H)
    polys.append(H)
assert polys[0]!=polys[1]
values=[evaluate(p,F(2)) for p in polys]  # x=2, ordinary t=x²=4.
freq=[-6,-4,-2,0,2,4,6]
coeff=solve([[F(4)**(k*m) for k in freq] for m in range(7)],values[:7])
assert sum(c*F(4)**(k*7) for k,c in zip(freq,coeff))==values[7]
active=[k for k,c in zip(freq,coeff) if c]
assert len(active)>=2
out={'alpha':[1,1,1,-2,1],'parameters':'T=2m, U=-2m',
     'ordinary_Jones_x':rows[0]['V'],
     'normalization':'x=sqrt(t); H3=(delta*V_zero_parallel-1)/(x²+1+x^-2)',
     'H3_m0_x':polys[0],'H3_m1_x':polys[1],
     'H3_at_t4':[str(v) for v in values],
     'fusion_coefficients_at_t4':{str(k):str(c) for k,c in zip(freq,coeff)},
     'active_frequencies_at_t4':active,
     'sample_t_spans':[(max(p)-min(p))//2 for p in polys],
     'eighth_sample_recurrence_check':True}
(HERE/'colored_family_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact whole Jones equality, normalized unequal H3, fusion recurrence eighth sample.')
print('Active frequencies at t=4:',active)
print('H3 t-spans:',out['sample_t_spans'])
