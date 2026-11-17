import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import fastS, lp
from lp import add, mul, top, bot
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
ep=({0:1},{0:1}); em=({0:1,2:1},{1:-1})
def pair(G,u,w):
    a,b=u; c,d=fastS.tilde(w[0]),fastS.tilde(w[1])
    return add(mul(G[0][0],mul(a,c)),mul(G[0][1],mul(a,d)),mul(G[1][0],mul(b,c)),mul(G[1][1],mul(b,d)))
for m in sorted(tab):
    if m==0: continue
    G=tab[m]; out=[]
    for nm,u,w in [('++',ep,ep),('+-',ep,em),('-+',em,ep),('--',em,em)]:
        p=pair(G,u,w)
        out.append('%s:[%s,%s] nterms %d'%(nm,bot(p) if p else '-',top(p) if p else '-',len(p)))
    print(m,' | '.join(out))
print('m=2 g++ =',sorted(pair(tab[2],ep,ep).items()))
print('m=2 g-- =',sorted(pair(tab[2],em,em).items()))
print('m=2 g+- =',sorted(pair(tab[2],ep,em).items()))
