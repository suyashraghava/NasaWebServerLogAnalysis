#!/usr/bin/python

import sys

TempHost = None
num = 0 

for line in sys.stdin:
    host = line.strip().split()

    if TempHost and TempHost != host:
        print num, TempHost
        TempHost = host
        num = 0
        
    TempHost = host
    num += 1

if TempHost != None:
    print num, TempHost
