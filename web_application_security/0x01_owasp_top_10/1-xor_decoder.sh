#!/bin/bash

password="$1"
password="${password#'{xor}'}"
decoded_password=$(echo -n "$password" | base64 -d 2>/dev/null)

# Check if base64 decoding succeeded
if [ $? -ne 0 ]; then
    echo "Error: Invalid Base64 input"
    exit 1
fi

# Convert decoded bytes to hex and process each byte
hex=$(echo -n "$decoded_password" | xxd -p | tr -d '\n')
output=""
for ((i=0; i<${#hex}; i+=2)); do
    byte_hex="${hex:i:2}"
    byte_dec=$((16#$byte_hex))
    xor_byte=$((byte_dec ^ 95))
    output+=$(printf "\\x$(printf '%02x' $xor_byte)")
done

echo -en "$output"
