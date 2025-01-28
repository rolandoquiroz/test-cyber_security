#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 {xor}base64_string"
    exit 1
fi

encoded=${1#"{xor}"}

python3 -c "
import base64, sys
encoded = \"$encoded\"
decoded = base64.b64decode(encoded).decode('latin1')
result = ''.join(chr(ord(c) ^ 0x5F) for c in decoded)
print(result)
"
