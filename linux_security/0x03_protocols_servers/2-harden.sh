#!/bin/bash
find / -xdev -type d -perm -0002 ! -path "/proc/*" -print -exec chmod o-w {} \; 2>/dev/null
