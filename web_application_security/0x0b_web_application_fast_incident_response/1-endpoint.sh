#!/bin/bash
grep -o 'GET \S*' logs.txt | awk '{print $2}' | cut -d '?' -f 1 | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
