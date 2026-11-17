#!/bin/sh
# final queue (cert lane): final-code suites (a), (b: blind Tietze), (c), then the (7,7) re-certification, then families
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert
until [ -f out/queue_done.flag ]; do sleep 5; done
$PY suites.py out/set_unknots_le12.json - A1_J1_le24 5 out/final_suiteA1 > out/final_suiteA1.log 2>&1
$PY suites.py out/set_families.json top A2_top_rehits 5 out/final_suiteA2top > out/final_suiteA2top.log 2>&1
$PY suites.py out/set_families.json bottom A2_bottom_rehits 5 out/final_suiteA2bot > out/final_suiteA2bot.log 2>&1
$PY suites.py out/set_families.json codex A2_codex 5 out/final_suiteA2codex > out/final_suiteA2codex.log 2>&1
$PY suites.py out/set_suiteB.json alex_trivial B_alextriv 5 out/final_suiteB_alextriv 1.0 60 blind > out/final_suiteB_alextriv.log 2>&1
$PY suites.py out/set_suiteB.json random_V_ne_1 B_random 5 out/final_suiteB_random 1.0 30 blind > out/final_suiteB_random.log 2>&1
$PY suites.py out/set_suiteB.json random_mirrors B_mirrors 5 out/final_suiteB_mirrors 1.0 30 blind > out/final_suiteB_mirrors.log 2>&1
$PY suites.py out/set_suiteC.json C1u C1u_unknots_26_32 5 out/final_suiteC1u > out/final_suiteC1u.log 2>&1
$PY suites.py out/set_suiteC.json C1n C1n_nontrivial_26_32 5 out/final_suiteC1n > out/final_suiteC1n.log 2>&1
$PY suites.py out/set_suiteC.json C2u C2u_unknots_60_62 5 out/final_suiteC2u > out/final_suiteC2u.log 2>&1
$PY suites.py out/set_suiteC.json C2n C2n_nontrivial_64 5 out/final_suiteC2n > out/final_suiteC2n.log 2>&1
echo FINAL_SUITES_DONE > out/final_suites_done.flag
python3 mitm_cert.py 7 7 1 5 out/mitm77_cert > out/mitm77_cert.log 2>&1
echo MITM_DONE > out/mitm_done.flag
$PY bulk_cert.py out/set_families_all_d8.json bottom 5 out/bulk_bottom_d8 5 > out/bulk_bottom_d8.log 2>&1
$PY bulk_cert.py out/set_families_all_d8.json top 5 out/bulk_top_d8 5 > out/bulk_top_d8.log 2>&1
echo QUEUE3_DONE > out/queue3_done.flag
