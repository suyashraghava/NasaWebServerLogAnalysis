#!/usr/bin/python
import sys
def parser(val,record):
    for i in record:

        if (val == i[:len(val)]):
            return i[len(val)+2:len(i)-1]

for line in sys.stdin:

    print line.strip()
