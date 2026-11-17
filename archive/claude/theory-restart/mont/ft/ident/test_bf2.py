import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import butterfly as bf, diag
rows=json.load(open('inv_rows.json'))
bad=0
for r in rows[:40]:
    w=r['w']; a2=r['K.a2']
    out=[]
    for axis in ('out','in'):
        s=bf.sato_levine(w,axis)
        if not isinstance(s,dict): out.append((axis,s)); bad+=1; continue
        ok=abs(s['step'])==abs(int(float(eval(a2)))) if True else None
        out.append((axis,s['a3'],s['step'],s['lk1'],ok))
    print(w,'a2(K)=',a2,out)
print('bad',bad)
