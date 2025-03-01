#!/bin/bash
semanage login -m -s user_u -r s0-s0:c0.c1023 "$1"
