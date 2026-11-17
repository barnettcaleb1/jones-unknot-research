#!/bin/sh
# Reproduce the whole cx-clasp computation (forced double corner C00* of the
# two-slot shell, determinant check, Hoste-Thistlethwaite 3-component scan,
# composites and hand candidates).  Needs the cx-tools venv (snappy,
# spherogram) and cx-tools/bracket.py, twist.py (paths are set in common.py).
#
#   c00star.py    -> c00star.json, c00star.txt      (the twelve C00*(m, eps))
#   table_scan.py -> table_scan.json, table_scan.txt (109 prime 3-component links <= 10 cr)
#   composites.py -> composites.json, composites.txt (connected sums, split links, hand candidates)
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
PY="$HERE/../cx-tools/venv/bin/python"
cd "$HERE"
"$PY" c00star.py    2>&1 | grep -v "Plink\|warnings.warn" > c00star.txt
"$PY" table_scan.py 2>&1 | grep -v "Plink\|warnings.warn" > /dev/null   # writes table_scan.txt itself
"$PY" composites.py 2>&1 | grep -v "Plink\|warnings.warn" > /dev/null   # writes composites.txt itself
echo "done: c00star.txt table_scan.txt composites.txt (+ .json)"
