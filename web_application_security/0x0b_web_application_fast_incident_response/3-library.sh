#!/bin/bash
awk '{count[$1]++} END {for (ip in count) print count[ip], ip}' logs.txt | sort -nr | head -n1 | awk '{print $2}' | xargs -I{} awk -v ip="{}" '$1 == ip' logs.txt | awk -F'"' '{count[$6]++} END {for (req in count) print count[req], req}' | sort -nr | head -n1 | awk '{print $2}' | tr -d ' '
