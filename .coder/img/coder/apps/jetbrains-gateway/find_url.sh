#!/bin/sh

# cat /home/coder/jetbrains-dev-server.log | grep "Http link:"

set -e
jetbrains_url=$(cat /home/coder/jetbrains-dev-server.log | grep "Http link:" | awk '{print $3}')

if [ ! -n "$jetbrains_url" ]; then
    exit 1
fi

echo $jetbrains_url