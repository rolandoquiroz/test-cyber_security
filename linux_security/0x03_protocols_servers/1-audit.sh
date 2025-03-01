#!/bin/bash
awk 'NF && $1 !~ /^#/' /etc/ssh/sshd_config
