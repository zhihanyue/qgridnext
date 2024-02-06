#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"
voila "$SCRIPT_DIR/test.ipynb" --port 39050 --no-browser --Voila.ip=0.0.0.0 --enable_nbextensions=True
