#!/bin/sh
# cert/run: certify the junctions engineB's MITM never examined (non-geometric bottom dedup), then 5% re-check.
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/code
O=../out/dedup
$PY cert_words.py $O/missed_window_words.json 4 $O/missed_window > $O/missed_window.log 2>&1
$PY cert_words.py $O/missed_words_77.json 4 $O/missed_77 > $O/missed_77.log 2>&1
$PY verify_sample.py 0.05 29 4 $O/verify5_missed.json $O/missed_window.jsonl.gz $O/missed_77.jsonl.gz > $O/verify5_missed.log 2>&1
echo DONE > $O/missed_done.flag
