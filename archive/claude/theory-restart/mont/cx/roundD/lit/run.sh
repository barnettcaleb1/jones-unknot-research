#!/bin/sh
# usage: ./run.sh script.py args   (regina/spherogram from the Codex package dir, sympy from the project venv)
export PYTHONPATH=/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/work/braid_classification/packages:/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/lib/python3.13/site-packages
exec /opt/homebrew/bin/python3.13 "$@"
