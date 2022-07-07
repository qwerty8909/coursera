#!/bin/bash
line="---------------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPYIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"