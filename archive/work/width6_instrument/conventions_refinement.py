from pathlib import Path
import sys,time,json,contextlib,io
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'width6_targeted'))
import geometric_intersections as g
w=[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]
rows=[]
for res,step in [(128,.006),(64,.003),(128,.003)]:
 st=time.monotonic()
 with contextlib.redirect_stdout(io.StringIO()):r=g.model([-z for z in w],res,step)
 z={k:r[k] for k in ['resolution','step','intersection_counts','polynomial','TL_line_specialization']};z['configurations']=len(r['configurations']);z['seconds']=time.monotonic()-st;rows.append(z)
 print(json.dumps(z),flush=True)
 (Path(__file__).parent/'conventions_refinement.json').write_text(json.dumps(rows,indent=2)+'\n')
