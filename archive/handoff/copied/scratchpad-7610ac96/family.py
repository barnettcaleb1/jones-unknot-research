import sys
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/tools')
import flat_search as fs, alex
import sympy as sp
t=sp.symbols('t')
def J_of(word):
    half=alex.parse(word)
    full=alex.symmetrize(half)
    if full is None or alex.diagram(full) is None: return None
    y,x=fs.bracket_vector(half)
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x))
    u={e:c for e,c in u.items() if c}
    assert len(u)==1
    (eu,cu),=u.items()
    return sum(c*cu*t**((e-eu)//4) for e,c in y.items() if c), eu, cu
def blk(letter,n):
    other={'y':'x','x':'y'}[letter[0]]
    return [letter]*n if n>=0 else [other+letter[1:]]*(-n)
res={}
for n in range(-12,25):
    w='.'.join(['s','r1','x2']+blk('y1',n)+['y0','r2','y0','y1','y0','y1','x2','u3','u1'])
    r=J_of(w)
    res[n]=r
    print(n, r[1], r[2], sp.expand(r[0]))
# fit a linear recurrence J_{n+3} = a J_{n+2} + b J_{n+1} + c J_n with a,b,c in Q(t)
A,B,C=sp.symbols('A B C')
eqs=[sp.expand(res[n+3][0]-A*res[n+2][0]-B*res[n+1][0]-C*res[n][0]) for n in range(0,3)]
sol=sp.solve(eqs,[A,B,C],dict=True)
print('order-3 fit:',[{k:sp.factor(v) for k,v in s.items()} for s in sol])
