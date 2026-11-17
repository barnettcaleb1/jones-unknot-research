import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import axislink
rows=json.load(open('inv_rows2.json'))
for r in rows[:20]:
    print(r['w'], axislink.sato_levine(r['w']))
