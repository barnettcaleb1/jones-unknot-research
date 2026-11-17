#!/bin/zsh
# usage: waitfor.sh file pattern timeout_s
f=$1; p=$2; t=${3:-300}; i=0
until grep -q "$p" "$f" 2>/dev/null; do sleep 3; i=$((i+3)); if [ $i -ge $t ]; then echo TIMEOUT; exit 1; fi; done
grep "$p" "$f" | tail -2
