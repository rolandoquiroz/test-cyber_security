#!/bin/bash
attacker_ip=$(grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}' logs.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')
grep -c "$attacker_ip" logs.txt
