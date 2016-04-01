#!/bin/bash
echo -n "GitHub Testscript for Jenkins."
/usr/bin/whoami
/usr/sbin/ss -t -a | tee output.txt
/usr/bin/ip a s
