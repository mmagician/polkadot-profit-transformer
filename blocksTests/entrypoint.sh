#!/usr/bin/env bash
ssh -4 -o StrictHostKeyChecking=no -NL 9944:127.0.0.1:9944 tunnel@94.130.148.168 &
PID=$!
python -m pytest -v blocksTests/tests/suites/api/polkadot.py
kill $PID


