#!/bin/bash
printf "%s" "$1$(openssl rand -hex 16)" | openssl sha512 > 3_hash.txt || { echo "Error generating hash"; exit 1; }
