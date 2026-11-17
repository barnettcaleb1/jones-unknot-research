"""F_2 certificate for a full s4 type-D module and its A-infinity extension.

Operations: KWZ 2602.23442 Definitions 2.6,10.1; Remark 10.3.
The exact s4 module is published in KWZ 2022 Figure 6.
This constructs algebraic objects, not a classical tangle diagram.
"""
from collections import Counter
from pathlib import Path
import json

names = [f'{r}{i}' for r in 'xy' for i in range(6)]
grades = {}
for row in 'xy':
    for i, (q,h) in enumerate(zip([-5,-4,-2,0,2,3],[-3,-2,-1,0,1,2])):
        grades[f'{row}{i}'] = {'q':q+(2 if row=='y' else 0),
                               'h':h+(1 if row=='y' else 0),
                               'id':'b' if i in (0,5) else 'c'}
# A monomial is (kind,power,U-power), with I the matching idempotent.
I = ('I',0,0)
def mul(a,b):
    ka,pa,ua=a; kb,pb,ub=b
    if ka=='I': return kb,pb,ua+ub
    if kb=='I': return ka,pa,ua+ub
    if ka!=kb: return None
    return ka,pa+pb,ua+ub

def clean(entries):
    return sorted(k for k,v in Counter(entries).items() if v%2)

edges=[]
for row in 'xy':
    for i,(kind,power) in enumerate([('S',1),('D',1),('S',2),('D',1),('S',1)]):
        edges.append((f'{row}{i}',f'{row}{i+1}',(kind,power,0)))
edges += [('x0','y0',('D',1,0)),('x5','y5',('D',1,0))]
added=[('x1','y3',('I',0,1)),('x2','y4',('I',0,1))]
extended=edges+added

def paths(es,length):
    nodes=sorted(set(a for a,b,c in es)|set(b for a,b,c in es))
    out={n:[] for n in nodes}
    for a,b,c in es: out[a].append((b,c))
    def go(start,node,labels):
        if len(labels)==length:
            yield start,node,labels
        else:
            for nxt,lab in out[node]:
                yield from go(start,nxt,labels+[lab])
    for n in nodes: yield from go(n,n,[])

def mu(labels):
    ell=len(labels)
    if ell==2: return mul(*labels)
    if ell%2: return None
    # Strict unitality kills higher operations involving the new U*I arrows.
    if any(k=='I' for k,p,u in labels): return None
    if ell==4:
        kinds=''.join(k for k,p,u in labels)
        powers=[p for k,p,u in labels]
        if kinds not in ('SDSD','DSDS'): return None
        if powers[1:]==[1,1,1]:
            return (labels[0][0],powers[0]-1,1) if powers[0]>1 else ('I',0,1)
        if powers[:3]==[1,1,1]:
            return (labels[-1][0],powers[-1]-1,1) if powers[-1]>1 else ('I',0,1)
        return None
    # Every possible length>=6 path in this finite graph has insufficient
    # negative quantum degree to support a nonzero B-output of mu_ell.
    q_input=sum((-p if k=='S' else -2*p)-6*u for k,p,u in labels)
    assert q_input+6*(ell//2-1)>0, (ell,labels,q_input)
    return None

residues={}
for ell in (2,4,6,8):
    terms=[]
    for a,b,labs in paths(extended,ell):
        c=mu(labs)
        if c is not None: terms.append((a,b,c))
    residues[ell]=clean(terms)
assert clean([t for rows in residues.values() for t in rows])==[]
assert residues[2]==residues[4]
for a,b,(kind,power,u) in extended:
    qa=-power if kind=='S' else -2*power if kind=='D' else 0
    assert grades[b]['q']+qa-6*u-grades[a]['q']==0
    assert grades[b]['h']-2*u-grades[a]['h']==1

# Solve for a genuine B-nullhomotopy H of G*id, with deg(H)=(-1,-2).
candidates=[]
for a in names:
    for b in names:
        if grades[b]['h']-grades[a]['h']!=-1: continue
        qalg=-2+grades[a]['q']-grades[b]['q']
        same=grades[a]['id']==grades[b]['id']
        if qalg==0 and same: candidates.append((a,b,I))
        if qalg<0:
            if same and qalg%2==0: candidates.append((a,b,('D',-qalg//2,0)))
            if ((-qalg)%2==0)==same: candidates.append((a,b,('S',-qalg,0)))

def boundary_of_h(H):
    a,b,c=H; terms=[]
    for u,v,d in edges:
        if u==b:
            m=mul(c,d)
            if m: terms.append((a,v,m))
        if v==a:
            m=mul(d,c)
            if m: terms.append((u,b,m))
    return clean(terms)

columns=[boundary_of_h(c) for c in candidates]
target=[(n,n,a) for n in names for a in [('D',1,0),('S',2,0)]]
allterms=sorted(set(target).union(*map(set,columns)))
rows=[]
for term in allterms:
    bits=sum(1<<j for j,col in enumerate(columns) if term in col)
    rows.append([bits,int(term in target)])
pivots={}
for bits,rhs in rows:
    while bits:
        p=bits.bit_length()-1
        if p in pivots:
            bits ^= pivots[p][0]; rhs ^= pivots[p][1]
        else:
            pivots[p]=(bits,rhs); break
    else:
        assert rhs==0, 'No nullhomotopy solution'
solution=0
for p,(bits,rhs) in sorted(pivots.items()):
    value=rhs^((bits&solution).bit_count()%2)
    if value: solution |=1<<p
H=[c for j,c in enumerate(candidates) if (solution>>j)&1]
assert clean([t for h in H for t in boundary_of_h(h)]+target)==[]

# Compute the actual A-infinity differential of H, retaining higher terms.
def paths_with_one_h(length):
    out={n:[] for n in names}
    for a,b,c in extended: out[a].append((b,c,0))
    for a,b,c in H: out[a].append((b,c,1))
    def go(start,node,labels,used):
        if len(labels)==length:
            if used==1: yield start,node,labels
        else:
            for nxt,lab,tag in out[node]:
                if used+tag<=1:
                    yield from go(start,nxt,labels+[lab],used+tag)
    for n in names: yield from go(n,n,[],0)

gh_terms=[]
for ell in (2,4,6,8,10):
    for a,b,labs in paths_with_one_h(ell):
        c=mu(labs)
        if c is not None: gh_terms.append((a,b,c))
G_lift=clean(gh_terms)
G_corrections=[(f'{r}{i}',f'{r}{i+2}',('I',0,1)) for r in 'xy' for i in (1,2)]
assert G_lift==clean(target+G_corrections)

# Directly verify the 24-generator cone of this lifted map. Over F_2 no
# suspension signs remain. Its copies have shifts q^-1 h^-1 and q^1 h^0.
cone=[]
for copy in 'ab':
    cone.extend((copy+a,copy+b,c) for a,b,c in extended)
cone.extend(('a'+a,'b'+b,c) for a,b,c in G_lift)
cone_residues={}
for ell in (2,4,6,8,10):
    terms=[]
    for a,b,labs in paths(cone,ell):
        c=mu(labs)
        if c is not None: terms.append((a,b,c))
    cone_residues[ell]=clean(terms)
assert clean([t for rows in cone_residues.values() for t in rows])==[]

# Check connectivity/basepoint-action conditions on X as well.
central_actions={}
for label in ('D_c','D_b','S2'):
    tgt=[(n,n,('S',2,0) if label=='S2' else ('D',1,0)) for n in names
         if label=='S2' or grades[n]['id']==label[-1]]
    piv={}
    for term in allterms:
        bits=sum(1<<j for j,col in enumerate(columns) if term in col)
        rhs=int(term in tgt)
        while bits:
            p=bits.bit_length()-1
            if p in piv:
                bits^=piv[p][0]; rhs^=piv[p][1]
            else:
                piv[p]=(bits,rhs); break
        else:
            assert rhs==0, ('central action is not nullhomotopic',label)
    sol=0
    for p,(bits,rhs) in sorted(piv.items()):
        if rhs^((bits&sol).bit_count()%2): sol|=1<<p
    homotopy=[c for j,c in enumerate(candidates) if (sol>>j)&1]
    assert clean([t for h in homotopy for t in boundary_of_h(h)]+tgt)==[]
    central_actions[label]=homotopy

out={'status':'all exact checks passed',
     'generators':grades,'base_arrows':edges,'U_correction_arrows':added,
     'MC_residues_by_arity':residues,
     'G_nullhomotopy_arrows':H,
     'lifted_G_arrows':G_lift,'lifted_G_U_corrections':G_corrections,
     'cone_MC_residues_by_arity':cone_residues,
     'central_action_nullhomotopies':central_actions,
     'scope':'algebraic tangle objects only; no classical diagram realization'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
print('G-nullhomotopy arrows:', H)
