#!/usr/bin/python
import sys
for line in sys.stdin:
    line = line.strip().split()

    if ( len(line) == 10  ):
    	time = line[3][1:]
    	host = line[0]
    	print host,'\t',time
