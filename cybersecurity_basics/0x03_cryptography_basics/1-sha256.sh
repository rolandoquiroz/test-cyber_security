#!/bin/bash
echo -n "$1" | sha256sum | cut -d ' ' -f1 > 1_hash.txt
