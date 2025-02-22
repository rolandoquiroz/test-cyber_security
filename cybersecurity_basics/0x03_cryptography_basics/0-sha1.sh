#!/bin/bash
python3 -c "import hashlib, sys; print(hashlib.sha1(sys.argv[1].encode()).hexdigest())" "$1" > 0_hash.txt
