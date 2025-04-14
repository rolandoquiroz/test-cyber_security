#!/bin/bash
tail -n 1000 auth.log | grep -i "failed" | awk '{print $11}' | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
