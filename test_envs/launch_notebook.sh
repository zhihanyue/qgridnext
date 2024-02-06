#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"
jupyter notebook --ip 0.0.0.0 --port=39050 --notebook-dir=$SCRIPT_DIR --no-browser
