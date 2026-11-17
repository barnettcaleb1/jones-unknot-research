#!/bin/zsh
# certify the J = 1 word list of each named run with the audited certifier copy (u45/code), NPROC processes
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45
NP=$1; shift
for r in "$@"; do
  python3 code/cert_words.py cert/words_$r.json $NP cert/u4_$r > logs/cert_u4_$r.log 2>&1
  echo "$r $(tail -1 logs/cert_u4_$r.log)"
done
