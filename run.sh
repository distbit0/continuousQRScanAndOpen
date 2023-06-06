#!/bin/bash
export DISPLAY=:0

script_path="/home/pimania/Dev/qrScan/run.py"

# Run the script for 30 seconds
timeout 30 python3 $script_path
