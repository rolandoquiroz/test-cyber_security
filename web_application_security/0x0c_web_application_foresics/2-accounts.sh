#!/bin/bash
grep "Accepted password" auth.log | awk '{print $9}' | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
