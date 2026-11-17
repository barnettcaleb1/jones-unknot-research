#!/bin/sh
# sequential queue of the remaining validation runs (cert lane); each writes its own log/summary in out/
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert
until [ -s out/suiteB_mirrors.log ]; do sleep 5; done
$PY validate_pd.py 11 650 5 out/validate_pd_650_v2.json > out/validate_pd_650_v2.log 2>&1
$PY suites.py out/set_suiteC.json C1u C1u_unknots_26_32 5 out/suiteC1u > out/suiteC1u.log 2>&1
$PY suites.py out/set_suiteC.json C1n C1n_nontrivial_26_32 5 out/suiteC1n > out/suiteC1n.log 2>&1
$PY suites.py out/set_suiteC.json C2u C2u_unknots_60_62 5 out/suiteC2u > out/suiteC2u.log 2>&1
$PY suites.py out/set_suiteC.json C2n C2n_nontrivial_64 5 out/suiteC2n > out/suiteC2n.log 2>&1
$PY stress_tietze.py 5 20 out/stress_tietze.json > out/stress_tietze.log 2>&1
echo QUEUE_DONE > out/queue_done.flag
