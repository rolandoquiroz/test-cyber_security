#!/bin/bash
nmap -sC -sV -A -O --traceroute --script "banner,ssl-enum-ciphers,default,smb-enum-domains" "$1" -oN service_enumeration_results.txt
