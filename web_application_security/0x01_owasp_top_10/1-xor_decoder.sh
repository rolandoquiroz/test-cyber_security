#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 {xor}base64_string"
    exit 1
fi

encoded_input=${1#"{xor}"}

echo "$encoded_input" | base64 -d | perl -pe 's/(.)/chr(ord($1) ^ 0x5F)/ge'
