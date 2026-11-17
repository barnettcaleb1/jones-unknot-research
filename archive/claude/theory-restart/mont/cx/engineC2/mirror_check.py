import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs
def mirror(w):
    out=[]
    for tok in w.split('.'):
        if tok and tok[0]=='x': out.append('y'+tok[1:])
        elif tok and tok[0]=='y': out.append('x'+tok[1:])
        else: out.append(tok)
    return '.'.join(out)
def inv(J): return {-e:c for e,c in J.items()}
rnd=random.Random(1); ok=bad=0; n=0
while n<300:
    w=fs.gen(rnd,rnd.randint(4,16))
    if not w: continue
    J=lp.J(w)
    if J is None: continue
    n+=1
    Jm=lp.J(mirror(w))
    if Jm==inv(J): ok+=1
    else: bad+=1; print('BAD',w,J,Jm)
print('mirror rule J(mirror w)(t) == J(w)(1/t):',ok,'ok',bad,'bad')
# palindromic examples among two-bridge: figure eight etc.
for w in ['s.l1.y0.x1.u2','s.l1.x0.y1.u2','s.l1.y0.y0.x1.x1.u2','s.l1.y1.x0.u2']:
    print(w, lp.J(w))
