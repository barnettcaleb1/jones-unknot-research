#!/usr/bin/env python3
"""Search half-diagram words for strongly invertible knots with Alexander polynomial 1.
usage: alex_search.py SEED COUNT MAXLEN OUT.txt   (random words in two families; prints candidates)"""
import sys,random,itertools
import alex
def reduced(word):
    out=[]
    for l in word:
        if out and out[-1][1:]==l[1:] and out[-1][0]!=l[0]: out.pop()
        else: out.append(l)
    return out
def trivial_alex(word):
    try:
        d=alex.alex_eval(word,-1)
        if d!=1: return False
        if alex.alex_eval(word,2)!=1: return False
        if alex.alex_eval(word,3)!=1: return False
        if alex.alex_eval(word,5)!=1: return False
        return True
    except Exception:
        return False
def gen(rnd,L):
    r=rnd.random()
    if r<0.45:
        w=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(L)])
        return 's.'+rnd.choice(['l1','r1'])+'.'+'.'.join(w)+'.'+rnd.choice(['u1','u2']) if w else None
    else:
        a=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(rnd.randint(1,max(1,L//2)))])
        b=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2,3,4])) for _ in range(rnd.randint(2,L//2+2))])
        c=reduced([rnd.choice('xy')+str(rnd.choice([0,1,2])) for _ in range(rnd.randint(0,L//2))])
        if not a or not b: return None
        return 's.'+rnd.choice(['l1','r1'])+'.'+'.'.join(a)+'.'+rnd.choice(['l1','r1','l2','r2','l3','r3'])+'.'+'.'.join(b)+'.'+rnd.choice(['u1','u2','u3'])+('.'+'.'.join(c) if c else '')+'.'+rnd.choice(['u1','u2'])
def main():
    seed,count,maxlen,outp=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
    rnd=random.Random(seed); seen=set(); found=0; valid=0
    fo=open(outp,'a')
    for it in range(count):
        L=rnd.randint(4,maxlen)
        w=gen(rnd,L)
        if not w or w in seen: continue
        seen.add(w)
        d=None
        try: d=alex.alex_eval(w,-1)
        except Exception: d=None
        if d is None: continue
        valid+=1
        if d==1 and trivial_alex(w):
            ncross=sum(1 for tok in w[2:].split('.') if tok[0] in 'xy')
            fo.write('%s\t%d\n'%(w,ncross)); fo.flush(); found+=1
    print('tried',len(seen),'valid knots',valid,'alexander-trivial',found)
if __name__=='__main__': main()
