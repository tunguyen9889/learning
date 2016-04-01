#!/bin/bash
exec 1>testout
echo -n 'This script run when the answer is Yes.\n'
/usr/bin/ps -ef | grep jenkins
