#!/bin/zsh
# relaunch of the E3c (e3w3) and E3d runs after the import-order fix (07:04)
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3
L=/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/logs
CAP=3300
PY=python3
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
