#!/bin/bash
export DISPLAY=:0

script_path="/home/pimania/Dev/qrScan/run.py"

while true
do
    # Check if the script is running
    if pgrep -f "$script_path" >/dev/null
    then
        echo "Script is running"
    else
        echo "Script is not running, starting script..."
        python3 $script_path
    fi
    sleep 1
done
