import re, sys
from fractions import Fraction as Fr
from collections import Counter
from rule import predicted
ANSI=re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
LINE=re.compile(r'(r|s)(\d*)\(([^)]*)\)\s+q\^(-?[\d/]+)\s+δ[_|]\^(-?[\d/]+)\s*$')
def parse_log(path):
    comps=[]
    for l in ANSI.sub('',open(path,encoding='utf8',errors='replace').read()).splitlines():
        m=LINE.search(l)
        if m: comps.append((m.group(1),m.group(2),m.group(3),Fr(m.group(4)),Fr(m.group(5))))
    return comps
def analyse(path,word):
    comps=parse_log(path)
    rat=[c for c in comps if c[0]=='r']; sp=[c for c in comps if c[0]=='s']
    assert len(rat)==1, rat
    k=int(rat[0][2]); qr=rat[0][3]
    j=(qr-Fr(k*(abs(k)+2),abs(k)+1))/24
    assert j.denominator==1
    j=int(j)
    lens=set(c[1] for c in sp); slopes=set(c[2] for c in sp)
    obs=Counter((int(c[3])-24*j,int(c[4])-4*j) for c in sp)
    kp,pred=predicted(word)
    return dict(k=k,j=j,lens=lens,slopes=slopes,n=len(sp),ok=(kp==k and pred==obs),kpred=kp,obs=obs,pred=pred)
if __name__=='__main__':
    path=sys.argv[1]; nums=[int(x) for x in sys.argv[2].split(',')]
    word=[('A' if i%2==0 else 'B',n) for i,n in enumerate(nums)]
    r=analyse(path,word)
    print(path, 'word',nums,'k',r['k'],'(pred %d)'%r['kpred'],'j',r['j'],'#specials',r['n'],'types',r['lens'],r['slopes'],'RULE OK' if r['ok'] else 'RULE FAILS')
    if not r['ok']:
        print(' obs ',sorted(r['obs'].items())); print(' pred',sorted(r['pred'].items()))
