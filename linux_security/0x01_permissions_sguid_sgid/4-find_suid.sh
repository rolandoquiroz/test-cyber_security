#!/bin/bash
find "$1" -type f -perm /4000 -exec stat -c "%U %G %A %s %y %n" {} + 2>/dev/null
