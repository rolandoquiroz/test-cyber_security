#!/bin/bash
sudo nmap -sM -vv -p80,443,21,22,23 $1
