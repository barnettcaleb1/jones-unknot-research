#!/bin/zsh
D=/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code
until [ -s $D/s3_lines_6_6.json ]; do sleep 5; done
sleep 2
$PY s3b_items.py
$PY generic_pipeline.py $D/s3b_items.json s3b 6
if [ -s $D/s3b_stage1_residue.json ]; then $PY residue_stage3.py $D/s3b_stage1_residue.json $D/s3b_stage3.json 6 10; fi
$PY verify_all.py s3b s3b_stage3.json > $D/verify_s3b.log 2>&1
echo S3B_DONE
