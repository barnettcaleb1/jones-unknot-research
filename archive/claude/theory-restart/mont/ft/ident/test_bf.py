import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import butterfly as bf, diag
for w in ['s.r2.r1.y0.y2.u1.u1','s.r1.y2.y2.y2.u1','s.l1.y0.l3.x4.x2.y1.u3.x0.x1.u1']:
    for axis in ('out','in'):
        for btype in ('x','y'):
            out=[]
            for nb in range(0,6):
                b=bf.build(w,axis,nb,btype)
                if b is None: out.append((nb,'none')); continue
                crs,partner,s1,s2=b
                try:
                    ld=bf.link_data(crs,partner,[s1,s2],[False,True])
                except Exception as e:
                    out.append((nb,'err',str(e)[:30])); continue
                if ld is None: out.append((nb,'1comp?')); continue
                out.append((nb,ld[4]))
            print(w,axis,btype,out)
