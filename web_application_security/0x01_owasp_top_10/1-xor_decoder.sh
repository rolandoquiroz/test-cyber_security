#!/bin/bash

# Check if the required argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 {xor}Base64EncodedString"
    exit 1
fi

# Extract and clean the input
password="$1"

# Remove the '{xor}' prefix if it exists
password="${password#'{xor}'}"

# Decode the Base64 string
decoded_password=$(echo -n "$password" | base64 -d 2>/dev/null)

# Check if decoding was successful
if [ $? -ne 0 ]; then
    echo "Error: Invalid Base64 encoded string."
    exit 1
fi

# Perform XOR decoding
output=""
xor_key=95 # The XOR key used in the encoding process
for ((i = 0; i < ${#decoded_password}; i++)); do
    char="${decoded_password:$i:1}"
    char_ascii=$(printf '%d' "'$char")
    xor_result=$((char_ascii ^ xor_key))
    output+=$(printf "\\$(printf '%03o' $xor_result)")
done

# Print the decoded result
echo "$output"
