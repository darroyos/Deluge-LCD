#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern.

if pgrep -x "deluged" > /dev/null
then
    echo "Deluge is already running"
else
    echo "Starting deluge daemon"
    deluged
fi

while pgrep -x "deluged" > /dev/null; do
  deluge-console info > output.txt
  python delugelcd.py
done
