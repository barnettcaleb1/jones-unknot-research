#!/usr/bin/env python3
"""Find explicit braid/Markov reductions, which certify unknot closures.

Jones-one is never used as an unknot criterion. Every certificate uses braid
relations, conjugation, inverse cancellation and Markov destabilization only.
"""
import heapq, itertools, json, pathlib, time
ROOT=pathlib.Path(__file__).resolve().parent

def norm(n,word):
    w=list(word); ops=[]
    while True:
        changed=False
        for i in range(len(w)-1):
            if w[i]==-w[i+1]:
                ops.append(['cancel',i]); del w[i:i+2];changed=True;break
        if changed:continue
        if len(w)>1 and w[0]==-w[-1]:
            ops.append(['rotate',1]); w=w[1:]+w[:1]; continue
        if n>1:
            for g in (n-1,1):
                if sum(abs(s)==g for s in w)==1:
                    i=next(i for i,s in enumerate(w) if abs(s)==g)
                    k=(i+1)%len(w)
                    if k:ops.append(['rotate',k]);w=w[k:]+w[:k]
                    side='high' if g==n-1 else 'low'
                    ops.append(['destabilize',side]);w.pop()
                    if side=='low':w=[s-1 if s>0 else s+1 for s in w]
                    n-=1;changed=True;break
        if changed:continue
        if w:
            k=min(range(len(w)),key=lambda i:tuple(w[i:]+w[:i]))
            if k:ops.append(['rotate',k]);w=w[k:]+w[:k]
        return (n,tuple(w)),ops

def neighbors(state):
    n,w0=state;N=len(w0)
    # Exchange move: X sigma_g Y sigma_g^-1 <-> X sigma_g^-1 Y sigma_g,
    # where X,Y avoid the outermost generator g. This preserves the closure.
    for g in sorted(set((1,n-1))):
        ix=[i for i,s in enumerate(w0) if abs(s)==g]
        if n>=3 and len(ix)==2 and w0[ix[0]]==-w0[ix[1]]:
            v=list(w0)
            for i in ix:v[i]=-v[i]
            st,ops=norm(n,v);yield st,[['exchange',g]]+ops
    # Include moves spanning the cyclic boundary, by first rotating.
    for i in range(N):
        w=list(w0[i:]+w0[:i]); pre=[] if i==0 else [['rotate',i]]
        if N>=2 and abs(abs(w[0])-abs(w[1]))>1:
            v=w.copy();v[0],v[1]=v[1],v[0]
            st,ops=norm(n,v);yield st,pre+[['commute',0]]+ops
        if N>=3 and abs(w[0])==abs(w[2]) and abs(abs(w[0])-abs(w[1]))==1:
            a,b,c=w[:3];v=w.copy()
            if a==c and a*b>0:v[:3]=[b,a,b]
            elif a==-c and a*b>0:v[:3]=[-b,a,b]
            elif a==-c:v[:3]=[b,c,-b]
            else:continue
            st,ops=norm(n,v);yield st,pre+[['braid',0,v[:3]]]+ops

def verify(n,w,ops):
    w=list(w)
    for op in ops:
        kind=op[0]
        if kind=='rotate':k=op[1];assert 0<=k<len(w);w=w[k:]+w[:k]
        elif kind=='cancel':
            i=op[1];assert w[i]==-w[i+1];del w[i:i+2]
        elif kind=='commute':
            i=op[1];assert abs(abs(w[i])-abs(w[i+1]))>1;w[i],w[i+1]=w[i+1],w[i]
        elif kind=='braid':
            i,new=op[1:];a,b,c=w[i:i+3]
            assert abs(a)==abs(c) and abs(abs(a)-abs(b))==1
            if a==c and a*b>0:expected=[b,a,b]
            elif a==-c and a*b>0:expected=[-b,a,b]
            elif a==-c:expected=[b,c,-b]
            else:raise AssertionError('Invalid braid move')
            assert new==expected;w[i:i+3]=new
        elif kind=='destabilize':
            side=op[1];g=n-1 if side=='high' else 1
            assert n>1 and abs(w[-1])==g and sum(abs(s)==g for s in w)==1
            w.pop();n-=1
            if side=='low':w=[s-1 if s>0 else s+1 for s in w]
        elif kind=='exchange':
            g=op[1];assert n>=3 and g in (1,n-1)
            ix=[i for i,s in enumerate(w) if abs(s)==g]
            assert len(ix)==2 and w[ix[0]]==-w[ix[1]]
            for i in ix:w[i]=-w[i]
        else:raise AssertionError(op)
        assert all(1<=abs(s)<n for s in w)
    assert n==1 and w==[]

def certify(word,limit=30000):
    start,ops=norm(4,word)
    parents={start:(None,ops)};serial=itertools.count();queue=[]
    def priority(st):
        n,w=st
        counts=[sum(abs(s)==g for s in w) for g in (1,n-1)]
        return len(w),n,min(counts)
    heapq.heappush(queue,(*priority(start),next(serial),start))
    while queue and len(parents)<=limit:
        *_,state=heapq.heappop(queue)
        if state==(1,()):
            chunks=[]
            while state is not None:
                prev,ops=parents[state];chunks.append(ops);state=prev
            steps=[x for chunk in reversed(chunks) for x in chunk]
            verify(4,word,steps)
            return steps,len(parents)
        for st,ops in neighbors(state):
            if st in parents:continue
            parents[st]=(state,ops)
            heapq.heappush(queue,(*priority(st),next(serial),st))
    return None,len(parents)

if __name__=='__main__':
    t=time.monotonic();rows=json.loads((ROOT/'exact_hits.json').read_text());results=[]
    for i,row in enumerate(rows):
        if not row['jones_one']:continue
        ops,n=certify(row['word'])
        results.append({'word':row['word'],'certified_unknot':ops is not None,'states':n,'certificate':ops})
        if ops is None:print('UNRESOLVED',i,n,row['word'],flush=True)
    (ROOT/'unknot_certificates.json').write_text(json.dumps(results,indent=2))
    print('Certified',sum(r['certified_unknot'] for r in results),'of',len(results),'in',round(time.monotonic()-t,2),'seconds; max states',max(r['states'] for r in results))
