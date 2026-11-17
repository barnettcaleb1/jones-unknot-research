import sys, json, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, chord, flat_search as fs
def N(J,k): return sum(c*e**k for e,c in J.items())
rnd=random.Random(41); stat={}; n=0; ex=[]
while n<400:
    w=fs.gen(rnd,rnd.randint(4,16))
    if not w: continue
    J=lp.J(w)
    if J is None: continue
    n+=1
    oc=chord.order1_counts(w)
    guess=oc['wup']-oc['lm']
    key=(N(J,1)//8 - guess)
    stat[key]=stat.get(key,0)+1
    if len(ex)<5 and key!=0: ex.append((w,N(J,1)//8,oc))
print('N1/8 - (wup - lm) distribution:',stat)
print(ex)
