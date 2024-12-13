#!/bin/bash
dig -t NS +short @10.42.240.137 passive.hbtn;
dig -t TXT +short @10.42.240.137 holberton.passive.hbtn
