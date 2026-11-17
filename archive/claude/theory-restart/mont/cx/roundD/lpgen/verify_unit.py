"""HIT protocol step (1)-(2) for units found by exact_run.py: rebuild the explicit half-word, recompute J with lp.J, det/Delta(2)/
Delta(3) of K via engineA units.py conventions."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import exact, lib, vc, lp, alex, units
def tree_of(tag,items,R):
    fam=tag[0]
    if fam=='J1' or fam=='J3': xs=[tag[3],tag[4]]; L,rr=tag[5],tag[6]
    elif fam=='J2': xs=[tag[2]]; L,rr=tag[3],tag[4]
    elif fam=='J4': xs=list(tag[4:7]); L,rr=tag[7],tag[8]
    return ('p',[items[x][1] for x in xs]+[R[L][i][2] for i in rr])
if __name__=='__main__':
    items=exact.load_items(); R={L:lib.rational(L) for L in (4,5,6)}
    for fn in sys.argv[1:]:
        D=pickle.load(open(fn,'rb'))
        for tag,us in D['units']:
            T=tree_of(tag,items,R)
            for kind,x,N,J in us:
                w=units.unit_word((kind,x,N,T))
                Jlp=lp.J(w)
                det=alex.alex_eval(w,-1); d2=alex.alex_eval(w,2); d3=alex.alex_eval(w,3)
                print(fn,tag,kind,x,N,'J(calculus)=',J,'lp.J=',Jlp,'det',det,'Delta(2)',d2,'Delta(3)',d3,'word',w)
