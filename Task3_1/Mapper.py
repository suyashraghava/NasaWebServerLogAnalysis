#!/usr/bin/python
import sys
for line in sys.stdin:
    line = line.strip().split('- -')[0]
    print("{0}\t{1}".format(line, 1))