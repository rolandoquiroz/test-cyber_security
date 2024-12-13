#!/bin/bash
dig -t MX +short @10.42.240.137 passive.hbtn;
dig -t TXT +short @10.42.240.137 mail.passive.hbtn
