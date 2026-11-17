#!/bin/sh
# cert/run: re-validation of the FIXED certifier (run/code), every builder suite + audit tests.  Outputs in run/out/validation.
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
SETS=/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/out
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/code
O=../out/validation
NP=4
$PY suites.py $SETS/set_unknots_le12.json - A1_J1_le24 $NP $O/suiteA1 > $O/suiteA1.log 2>&1
$PY suites.py $SETS/set_families.json top A2_top_rehits $NP $O/suiteA2top > $O/suiteA2top.log 2>&1
$PY suites.py $SETS/set_families.json bottom A2_bottom_rehits $NP $O/suiteA2bot > $O/suiteA2bot.log 2>&1
$PY suites.py $SETS/set_families.json codex A2_codex $NP $O/suiteA2codex > $O/suiteA2codex.log 2>&1
$PY suites.py $SETS/set_suiteB.json alex_trivial B_alextriv $NP $O/suiteB_alextriv 1.0 60 blind > $O/suiteB_alextriv.log 2>&1
$PY suites.py $SETS/set_suiteB.json random_V_ne_1 B_random $NP $O/suiteB_random 1.0 30 blind > $O/suiteB_random.log 2>&1
$PY suites.py $SETS/set_suiteB.json random_mirrors B_mirrors $NP $O/suiteB_mirrors 1.0 30 blind > $O/suiteB_mirrors.log 2>&1
echo AB_DONE > $O/ab_done.flag
$PY transplant_test.py $O/transplant.json > $O/transplant.log 2>&1
$PY validate_pd.py 11 650 $NP $O/validate_pd_650.json > $O/validate_pd_650.log 2>&1
$PY validate_group.py 21 320 $NP $O/validate_group_320.json > $O/validate_group_320.log 2>&1
$PY resaved_certs.py $NP 4000 $O/resaved_certs.json > $O/resaved_certs.log 2>&1
$PY suites.py $SETS/set_suiteC.json C1u C1u_unknots_26_32 $NP $O/suiteC1u > $O/suiteC1u.log 2>&1
$PY suites.py $SETS/set_suiteC.json C1n C1n_nontrivial_26_32 $NP $O/suiteC1n > $O/suiteC1n.log 2>&1
$PY suites.py $SETS/set_suiteC.json C2u C2u_unknots_60_62 $NP $O/suiteC2u > $O/suiteC2u.log 2>&1
$PY suites.py $SETS/set_suiteC.json C2n C2n_nontrivial_64 $NP $O/suiteC2n > $O/suiteC2n.log 2>&1
$PY affine_reduced_test.py $NP $O/affine_reduced.json > $O/affine_reduced.log 2>&1
$PY stress_tietze.py $NP 20 $O/stress_tietze.json > $O/stress_tietze.log 2>&1
echo DONE > $O/validation_done.flag
