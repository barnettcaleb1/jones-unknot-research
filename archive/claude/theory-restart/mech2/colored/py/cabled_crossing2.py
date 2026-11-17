#!/usr/bin/env python3
"""All 16 smoothings of the 2-cabled crossing with their matchings of the 8 ends and circle counts."""
import itertools,collections
X=[(-1,1),(1,1),(-1,-1),(1,-1)]
strand=[('w1',((-1,1),'W')),(((-1,1),'E'),((1,1),'W')),(((1,1),'E'),'e1'),
 ('w2',((-1,-1),'W')),(((-1,-1),'E'),((1,-1),'W')),(((1,-1),'E'),'e2'),
 ('n1',((-1,1),'N')),(((-1,1),'S'),((-1,-1),'N')),(((-1,-1),'S'),'s1'),
 ('n2',((1,1),'N')),(((1,1),'S'),((1,-1),'N')),(((1,-1),'S'),'s2')]
ends=['w1','w2','e1','e2','n1','n2','s1','s2']
out=collections.defaultdict(list)
for bits in itertools.product([0,1],repeat=4):
    adj=collections.defaultdict(list)
    for a,b in strand: adj[a].append(b); adj[b].append(a)
    for x,bit in zip(X,bits):
        for p,q in ([('W','N'),('E','S')] if bit==0 else [('W','S'),('N','E')]):
            adj[(x,p)].append((x,q)); adj[(x,q)].append((x,p))
    seen=set(); match=[]
    for e in ends:
        if e in seen: continue
        prev=None; cur=e; seen.add(e)
        while True:
            if cur in ends and prev is not None: break
            nxt=[z for z in adj[cur] if z!=prev]; prev,cur=cur,nxt[0]; seen.add(cur)
        match.append(''.join(sorted((e,cur))))
    loops=0; done=set(seen)
    for n in list(adj):
        if n in done: continue
        loops+=1; st=[n]
        while st:
            z=st.pop()
            if z in done: continue
            done.add(z); st+=adj[z]
    out[tuple(sorted(match))].append((sum(bits),bits,loops))
for m,L in sorted(out.items(),key=lambda kv:min(kv[1])):
    caps=[s for s in 'wens' if any(p[0]==s and p[2]==s for p in m)]
    print('matching',' '.join(m),'  caps at',caps if caps else '-')
    for r,bits,loops in sorted(L): print('      r=%d bits(self1,mix,mix,self2)=%s circles=%d'%(r,bits,loops))
