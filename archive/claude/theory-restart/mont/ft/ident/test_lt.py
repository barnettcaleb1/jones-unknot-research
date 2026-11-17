import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import ltheta
rows=json.load(open('inv_rows2.json'))
for r in rows[:25]:
    print(r['w'], 'a2(K)',r['K.a2'],'a2in',r['Kin.a2'],'a2out',r['Kout.a2'], ltheta.a3_lk0(r['w']))
