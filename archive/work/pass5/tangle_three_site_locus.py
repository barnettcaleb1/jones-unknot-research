"""All-integer annular-degree-zero classification for a new three-site family."""
from pathlib import Path
from collections import defaultdict
from itertools import product
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pass4'))
import ren_jones_locus as solver
from tangle_ren_twists import add,neg,mul,shift,DELTA

data=json.loads(Path(__file__).with_name('tangle_three_site_blocks.json').read_text())
blocks=data['blocks_resolving_sites_in_order_1_3_2']
def a(key):return {int(e):c for e,c in blocks[key].get('2',{}).items()}
a0,ap,aq,U=a('000'),a('100'),a('010'),a('101')
D=mul(DELTA,DELTA);Dm2=add(D,{0:-2})
assert a('001')==mul(DELTA,U) and a('011')==U
Fs={
    (1,0,0):add(mul(DELTA,ap),neg(U)),
    (0,1,0):add(mul(DELTA,aq),neg(U)),
    (0,0,1):mul(U,Dm2),
    (1,0,1):U,
    (0,1,1):U,
    (0,0,0):add(add(mul(D,a0),neg(mul(DELTA,add(ap,aq)))),neg(mul(U,Dm2))),
}
out=[];start=time.monotonic()
for parity in product([0,1],repeat=3):
    pp=defaultdict(int)
    for powers,f in Fs.items():
        offset=sum(x*y for x,y in zip(parity,powers))
        sign=-1 if offset%2 else 1
        for e,c in f.items():
            assert (e-2)%4==0
            pp[tuple(-2*v for v in powers)+((e-2)//4-offset,)]+=sign*c
    solver.poly={b:c for b,c in pp.items() if c}
    solver.seen=set();solver.leaves=[];solver.stats=defaultdict(int)
    solver.solve()
    row={'parity':parity,'parameterization':'(p,q,r)=parity+2(m,l,n)',
         'monomials':len(solver.poly),'stats':dict(solver.stats),
         'solution_loci_rref':[[[str(x) for x in row] for row in s] for s in solver.leaves]}
    out.append(row);print(row,flush=True)
result={'family':'Ren core times sigma1^p sigma3^q sigma2^r',
        'all_integer_annular_degree_zero_loci':out,
        'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
