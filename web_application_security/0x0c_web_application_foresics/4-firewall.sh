#!/bin/bash
grep -a "iptables" auth.log | grep "A INPUT" | sort -u | wc -l
