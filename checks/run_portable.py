#!/usr/bin/env python3
"""Run only the named fixed certificates, in temporary working directories."""
from pathlib import Path
import subprocess
import sys
import tempfile

root=Path(__file__).resolve().parents[1]
names=['ef_depth.py','maps_exact.py','integral_ladder.py','bare_b_slope_one.py']
for name in names:
    p=root/'archive/work/theory_restart/referee_checks'/name
    with tempfile.TemporaryDirectory(prefix='jones-ledger-check-') as d:
        r=subprocess.run([sys.executable,'-I',str(p)],cwd=d,text=True,capture_output=True,timeout=90)
    print(name+': '+('PASS' if r.returncode==0 else 'FAIL'))
    if r.returncode:
        print(r.stdout); print(r.stderr); raise SystemExit(r.returncode)
print('Four fixed certificates passed. This is not a replay of the full research program.')
