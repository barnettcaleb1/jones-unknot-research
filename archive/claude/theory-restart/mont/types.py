import sys, itertools, collections
sys.path.insert(0,'.')
from lp import *
inv={'X':'x','x':'X','Y':'y','y':'Y'}
cnt=collections.Counter(); ex={}
for L in range(1,9):
    for w in itertools.product('XxYy',repeat=L):
        w=''.join(w)
        if any(inv[w[i]]==w[i+1] for i in range(L-1)): continue
        v=apply(w); a=a_of(v); b=b_of(v)
        if len(a)==1: continue   # integral / trivial closure
        key=(top(a)-top(b), bot(a)-bot(b), a[top(a)]*b[top(b)], a[bot(a)]*b[bot(b)])
        cnt[key]+=1; ex.setdefault(key,w)
tot=sum(cnt.values())
for k,c in cnt.most_common(): print(k,c,ex[k])
print('total non-integral words',tot)
