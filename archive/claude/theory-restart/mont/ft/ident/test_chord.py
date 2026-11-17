import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import chord
for w in ['s.r2.r1.y0.y2.u1.u1','s.r1.y2.y2.y2.u1','s.l1.y0.l3.x4.x2.y1.u3.x0.x1.u1']:
    print(w, chord.traverse(w))
    toks=w.split('.')[1:]
    fl=[i for i,a in enumerate(toks) if a[0] in 'xy']
    for i in fl: print('  site',i,toks[i],chord.dstr(chord.diagram(w,[i])))
