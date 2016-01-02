#!/usr/bin/python
import sys
def parser(val,record):
    for i in record:
        if (val == i[:len(val)]):
            return i[len(val)+2:len(i)]

for line in sys.stdin:
    line = line.strip().split('\t')
    print line[1], line[0]
