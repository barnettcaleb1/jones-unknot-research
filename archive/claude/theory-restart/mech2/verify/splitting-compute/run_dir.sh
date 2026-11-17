#!/bin/bash
# usage: run_dir.sh <dir> <seconds>   -- run kht++ -c2 on every .kht in <dir> lacking output, under a time limit, stdin closed
KHT=/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++
cd /Users/calebbarnett/jones-lanes/theory-restart/mech2/verify/splitting-compute
d=$1; lim=${2:-120}
for f in $d/*.kht; do
  b=${f%.kht}
  if ls "$b"/cx* >/dev/null 2>&1; then continue; fi
  s=$(date +%s)
  perl -e 'alarm shift; exec @ARGV' $lim $KHT -c2 "$f" </dev/null > "$b.log" 2>&1
  echo "$f rc=$? time=$(( $(date +%s) - s ))s" >> $d/run.log
done
echo finished >> $d/run.log
