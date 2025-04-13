#!/bin/bash
grep "sshd" auth.log | tr -s ' ' '\n' | grep -v "^$" | sort | uniq -c | sort -nr
