#!/bin/bash
sudo nmap -sX --open --packet-trace --reason -p440-450 $1
