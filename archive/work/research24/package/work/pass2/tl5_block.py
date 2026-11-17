"""Exact five-dimensional TL5 one-through-strand module, with Laurent entries."""
from collections import defaultdict
from braid_kernel import search, HALF,FULL,KERNEL,ANCHOR,add,shift,burau

def mul(p,q):
    r=defaultdict(int)
    for e,a in p.items():
        for f,b in q.items():r[e+f]+=a*b
    return {e:a for e,a in r.items() if a}

STATES=[]
for pairs in search.matchings(tuple(range(6))):
    state=[-1]*5
    for a,b in pairs:
        if b!=5:state[a]=b;state[b]=a
    STATES.append(tuple(state))
assert len(STATES)==5 and len(set(STATES))==5

def transition(state,i):
    j=i+1
    a,b=state[i],state[j]
    if a==j:return STATES.index(state),True
    out=list(state)
    out[i]=j;out[j]=i
    if a==-1:out[b]=-1
    elif b==-1:out[a]=-1
    else:out[a]=b;out[b]=a
    return STATES.index(tuple(out)),False

TRANS=[[transition(s,i) for s in STATES] for i in range(4)]
def ident():return [[{0:1} if i==j else {} for j in range(5)] for i in range(5)]
def rho(word):
    m=ident()
    for s in word:
        sign=1 if s>0 else -1
        transitions=TRANS[abs(s)-1]
        new=[]
        for row in m:
            target=[]
            for j,(dest,loop) in enumerate(transitions):
                p=search.loopmul(row[dest]) if loop else row[dest]
                target.append(add(shift(row[j],sign),shift(p,-sign)))
            new.append(target)
        m=new
    return m
def trace(m):return add(*(m[i][i] for i in range(5)))
def matmul(m,n):return [[add(*(mul(m[i][k],n[k][j]) for k in range(5))) for j in range(5)] for i in range(5)]
def lincomb(*terms):return [[add(*(mul(p,m[i][j]) for p,m in terms)) for j in range(5)] for i in range(5)]
def iszero(m):return not any(p for row in m for p in row)
def closed_jones_from_blocks(word):
    delta={2:-1,-2:-1};d2=mul(delta,delta);d4=mul(d2,d2)
    wt5=add(d4,shift(d2,0,-4),{0:3})
    wt3=add(d2,{0:-2})
    w=sum(1 if s>0 else -1 for s in word)
    fullburau=burau(word)
    burautrace=add(*(fullburau[i][i] for i in range(5)),{0:-1})
    reduced_trace={-4*e+w:c for e,c in burautrace.items()}
    raw=add(shift(wt5,w),mul(wt3,reduced_trace),trace(rho(word)))
    return shift(raw,-3*w,-1 if w%2 else 1)

def verify_all_basis_traces():
    """Prove the closure trace formula by checking all 42 TL5 basis diagrams."""
    from collections import deque
    base,transitions,loops=search.tables(5)
    words={base:[]};queue=deque([base])
    while queue:
        current=queue.popleft()
        for i,trans in enumerate(transitions):
            dest,lp=trans[current]
            if lp==0 and dest not in words:
                words[dest]=words[current]+[i+1];queue.append(dest)
    assert len(words)==42
    I=ident();delta={2:-1,-2:-1};d2=mul(delta,delta)
    wt5=add(mul(d2,d2),shift(d2,0,-4),{0:3})
    wt3=add(d2,{0:-2})
    e5=[lincomb(({1:1},rho([i])),({2:-1},I)) for i in range(1,5)]
    e4=[]
    for i in range(1,5):
        B=burau([i])
        e4.append([[shift(add({-4*e:c for e,c in B[r][s].items()},
                                 {0:-1} if r==s else {}),2)
                    for s in range(5)] for r in range(5)])
    for basis,word in words.items():
        m4=I;m5=I
        for i in word:
            m4=matmul(m4,e4[i-1]);m5=matmul(m5,e5[i-1])
        # A nonempty e-word is zero on the invariant Burau line.
        char4=trace(m4) if word else {0:4}
        actual={0:1}
        for _ in range(loops[basis]-1):actual=search.loopmul(actual)
        predicted=add(wt5 if not word else {},mul(wt3,char4),trace(m5))
        assert predicted==actual,(basis,word,predicted,actual)
    return len(words)

if __name__=='__main__':
    assert verify_all_basis_traces()==42
    I=ident()
    assert rho([1,-1])==I
    assert rho([1,2,1])==rho([2,1,2])
    assert rho([1,3])==rho([3,1])
    C=rho(ANCHOR);assert trace(C)=={}
    H=rho(HALF)
    assert iszero(lincomb(({0:1},matmul(H,H)),({1:-1,-3:1},H),({-2:-1},I)))
    F=rho(FULL)
    assert iszero(lincomb(({0:1},matmul(F,F)),({0:-1,-8:-1},F),({-8:1},I)))
    assert not iszero(lincomb(({0:1},F),({0:-1},I)))
    assert not iszero(lincomb(({0:1},F),({-8:-1},I)))
    for word in [[],[1],[1,2,3,4],[1,-2,3,-4],KERNEL+ANCHOR,KERNEL+[-1,2,3,-4]]:
        assert closed_jones_from_blocks(word)==search.jones_a(word,5)
    print('Verified TL5 module relations, Coxeter trace zero, H and F quadratic identities, and exact full trace decomposition.')
