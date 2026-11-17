"""Exact highest-through-channel checks for Ren's pattern and its 2-cable.

The 6/4-through cell module has dimension 5; its doubled 12/8-through
counterpart has dimension 54. This avoids a 2^40 smoothing expansion.
"""
import pathlib,sys,json,itertools
from collections import defaultdict
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'pass2'))
import braid_kernel as bk
import tl5_block as tl

WORD=[-2,1,1,1,-2,4,-5,-5,-5,4]

def basis(n,pairs):
    """Noncrossing partial matchings with no defect inside a cup."""
    def gen(start,end,r):
        if r==0:
            yield ();return
        if end-start<2*r:return
        # First point is a defect, or is paired with a fully paired interval.
        yield from gen(start+1,end,r)
        for inside in range(r):
            partner=start+2*inside+1
            if partner>=end:break
            for inn in gen_full(tuple(range(start+1,partner))):
                for rest in gen(partner+1,end,r-inside-1):
                    yield ((start,partner),)+inn+rest
    def gen_full(xs):
        if not xs:
            yield ();return
        for j in range(1,len(xs),2):
            for a in gen_full(xs[1:j]):
                for b in gen_full(xs[j+1:]):yield ((xs[0],xs[j]),)+a+b
    out=[]
    for pp in gen(0,n,pairs):
        state=[-1]*n
        for a,b in pp:state[a]=b;state[b]=a
        out.append(tuple(state))
    assert len(out)==len(set(out))
    return out

def transition(state,i):
    j=i+1;a,b=state[i],state[j]
    if a==j:return state,1
    if a==b==-1:return None,0
    out=list(state);out[i]=j;out[j]=i
    if a==-1:out[b]=-1
    elif b==-1:out[a]=-1
    else:out[a]=b;out[b]=a
    return tuple(out),0

def cap_weight(state,caps):
    n=len(state);capends=set(sum(([a,b] for a,b in caps),[]))
    outputs=set(range(n))-capends
    defects={i for i,a in enumerate(state) if a==-1}
    edges=list(caps)+[(i,a) for i,a in enumerate(state) if i<a]
    roots=bk.search.components(edges,n)
    groups=defaultdict(set)
    for i,r in enumerate(roots):groups[r].add(i)
    loops=0
    for group in groups.values():
        out=len(group&outputs);inn=len(group&defects)
        if out==inn==0:loops+=1
        elif out!=1 or inn!=1:return None
    return loops

def highest(word,n,caps):
    states=basis(n,len(caps));ix={s:i for i,s in enumerate(states)}
    initial=[-1]*n
    for a,b in caps:initial[a]=b;initial[b]=a
    vec=[{} for _ in states];vec[ix[tuple(initial)]]={0:1}
    trans=[]
    for i in range(n-1):
        tr=[]
        for s in states:
            dest,loops=transition(s,i)
            tr.append((ix[dest] if dest is not None else None,loops))
        trans.append(tr)
    # Left action: rho(word) v applies the rightmost letter first.
    for s in reversed(word):
        sign=1 if s>0 else -1;out=[defaultdict(int) for _ in states]
        for j,p in enumerate(vec):
            bk.search.addto(out[j],p,sign)
            dest,loops=trans[abs(s)-1][j]
            if dest is None:continue
            q=bk.search.loopmul(p) if loops else p
            bk.search.addto(out[dest],q,-sign)
        vec=[bk.search.clean(p) for p in out]
    result={}
    for state,p in zip(states,vec):
        loops=cap_weight(state,caps)
        if loops is None:continue
        for _ in range(loops):p=bk.search.loopmul(p)
        result=bk.add(result,p)
    return result,len(states)

def cable2(word):
    out=[]
    for s in word:
        i=abs(s);block=[2*i,2*i-1,2*i+1,2*i]
        out+=block if s>0 else bk.inv(block)
    return out

def verify_relations(n,pairs):
    def act(state,word):
        loops=0
        for i in word:
            state,extra=transition(state,i)
            if state is None:return None
            loops+=extra
        return state,loops
    for s in basis(n,pairs):
        for i in range(n-1):
            once=act(s,[i]);twice=act(s,[i,i])
            assert twice==(None if once is None else (once[0],once[1]+1))
            for j in range(n-1):
                if abs(i-j)==1:assert act(s,[i,j,i])==once
                elif abs(i-j)>1:assert act(s,[i,j])==act(s,[j,i])

def run():
    verify_relations(6,1);verify_relations(12,2)
    assert highest([],6,[(2,3)])[0]=={2:-1,-2:-1}
    assert highest([],12,[(4,7),(5,6)])[0]=={4:1,0:2,-4:1}
    original,d1=highest(WORD,6,[(2,3)])
    doubled,d2=highest(cable2(WORD),12,[(4,7),(5,6)])
    assert d1==5 and d2==54 and original=={} and doubled
    # Mirror the six-strand word and check the corresponding Laurent symmetry.
    mirror,_=highest(cable2([-s for s in WORD]),12,[(4,7),(5,6)])
    assert mirror=={-e:c for e,c in doubled.items()}
    factor={-24:-1}
    for p in [{4:1,0:-1}]*4+[{4:1,0:1}]*2+[{4*j:1 for j in range(7)}]:
        factor=tl.mul(factor,p)
    assert doubled==factor
    out=dict(word=WORD,cable_word=cable2(WORD),dimensions=[d1,d2],
             highest_z4=original,highest_z8=doubled,min_A=min(doubled),max_A=max(doubled),
             factorization='-A^-24 (A^4-1)^4 (A^4+1)^2 (1+A^4+A^8+A^12+A^16+A^20+A^24)',
             top_twist_cable_coefficient='A^(4*(p+q)) * highest_z8',
             implication='Every two-top-twist pattern has wrapping number exactly four.')
    (ROOT/'braid_ren_cable.json').write_text(json.dumps(out,indent=2))
    print('Verified original highest channel zero; cable highest channel nonzero.')
    print('z8 coefficient:',dict(sorted(doubled.items(),reverse=True)))
    return out

if __name__=='__main__':run()
