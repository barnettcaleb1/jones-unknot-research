#!/bin/zsh
# u45 U4: rerun engineB's E3/E3b/E3c/E3d with the ORIGINAL seeds and the ORIGINAL evaluation budgets (evals, restarts taken
# from engineB/out/*.json), wall cap 3300 s, storing every J = 1 word.  Args: e3_search N SECS SEED abs|rel MAXE MAXR CAP;
# e3w3 / e3d_alex N SECS SEED MAXE CAP.
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3
L=/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/logs
CAP=3300
PY=python3
$PY e3_search.py 12 480 112 abs 827336 468 $CAP > $L/e3_n12_s112.log 2>&1 &
$PY e3_search.py 16 480 116 abs 547505 316 $CAP > $L/e3_n16_s116.log 2>&1 &
$PY e3_search.py 20 480 120 abs 395334 231 $CAP > $L/e3_n20_s120.log 2>&1 &
$PY e3_search.py 24 480 124 abs 296938 174 $CAP > $L/e3_n24_s124.log 2>&1 &
$PY e3_search.py 30 480 130 abs 204224 122 $CAP > $L/e3_n30_s130.log 2>&1 &
$PY e3_search.py 40 480 140 abs 127109 76 $CAP > $L/e3_n40_s140.log 2>&1 &
$PY e3_search.py 12 15 7 rel 17534 10 $CAP > $L/e3b_n12_s7.log 2>&1 &
$PY e3_search.py 12 420 212 rel 283218 156 $CAP > $L/e3b_n12_s212.log 2>&1 &
$PY e3_search.py 16 420 216 rel 178677 100 $CAP > $L/e3b_n16_s216.log 2>&1 &
$PY e3_search.py 20 420 220 rel 126109 72 $CAP > $L/e3b_n20_s220.log 2>&1 &
$PY e3_search.py 24 420 224 rel 89046 52 $CAP > $L/e3b_n24_s224.log 2>&1 &
$PY e3_search.py 30 420 230 rel 63595 37 $CAP > $L/e3b_n30_s230.log 2>&1 &
$PY e3_search.py 40 420 240 rel 36399 22 $CAP > $L/e3b_n40_s240.log 2>&1 &
$PY e3d_alex.py 20 480 420 101851 $CAP > $L/e3d_n20_s420.log 2>&1 &
$PY e3d_alex.py 30 480 430 33907 $CAP > $L/e3d_n30_s430.log 2>&1 &
$PY e3d_alex.py 40 480 440 15456 $CAP > $L/e3d_n40_s440.log 2>&1 &
$PY e3w3.py 14 480 1 10163 $CAP > $L/e3w3_n14_s1.log 2>&1 &
$PY e3w3.py 14 480 314 222650 $CAP > $L/e3w3_n14_s314.log 2>&1 &
$PY e3w3.py 18 480 318 141675 $CAP > $L/e3w3_n18_s318.log 2>&1 &
$PY e3w3.py 24 480 324 82530 $CAP > $L/e3w3_n24_s324.log 2>&1 &
$PY e3w3.py 30 480 330 54055 $CAP > $L/e3w3_n30_s330.log 2>&1 &
wait
echo ALLDONE
