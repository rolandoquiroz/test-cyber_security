#!/bin/bash
awk 'NR == FNR {if (++count[$1] > max) {max = count[$1]; ip = $1}; next}
     $1 == ip {split($0, parts, "\""); print parts[6]}' logs.txt logs.txt |
sort | uniq -c | sort -nr | head -n 1 | awk '{gsub(/ /,""); print $2 $3}'
