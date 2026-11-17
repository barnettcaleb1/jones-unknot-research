#!/bin/sh
# final-final queue: all suites and the stress test on the final tietze.py (adaptive length cap)
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert
until [ -f out/queue3_done.flag ]; do sleep 3; done
mkdir -p out/v3
$PY suites.py out/set_unknots_le12.json - A1_J1_le24 6 out/v3/suiteA1 > out/v3/suiteA1.log 2>&1
$PY suites.py out/set_families.json top A2_top_rehits 6 out/v3/suiteA2top > out/v3/suiteA2top.log 2>&1
$PY suites.py out/set_families.json bottom A2_bottom_rehits 6 out/v3/suiteA2bot > out/v3/suiteA2bot.log 2>&1
$PY suites.py out/set_families.json codex A2_codex 6 out/v3/suiteA2codex > out/v3/suiteA2codex.log 2>&1
$PY suites.py out/set_suiteB.json alex_trivial B_alextriv 6 out/v3/suiteB_alextriv 1.0 60 blind > out/v3/suiteB_alextriv.log 2>&1
$PY suites.py out/set_suiteB.json random_V_ne_1 B_random 6 out/v3/suiteB_random 1.0 30 blind > out/v3/suiteB_random.log 2>&1
$PY suites.py out/set_suiteB.json random_mirrors B_mirrors 6 out/v3/suiteB_mirrors 1.0 30 blind > out/v3/suiteB_mirrors.log 2>&1
$PY suites.py out/set_suiteC.json C1u C1u_unknots_26_32 6 out/v3/suiteC1u > out/v3/suiteC1u.log 2>&1
$PY suites.py out/set_suiteC.json C1n C1n_nontrivial_26_32 6 out/v3/suiteC1n > out/v3/suiteC1n.log 2>&1
$PY suites.py out/set_suiteC.json C2u C2u_unknots_60_62 6 out/v3/suiteC2u > out/v3/suiteC2u.log 2>&1
$PY suites.py out/set_suiteC.json C2n C2n_nontrivial_64 6 out/v3/suiteC2n > out/v3/suiteC2n.log 2>&1
$PY stress_tietze.py 6 20 out/v3/stress_tietze.json > out/v3/stress_tietze.log 2>&1
echo DONE > out/v3/done.flag
