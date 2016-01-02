#!/usr/bin/python
import sys
def parser(val,record):
    for i in record:

        if (val == i[:len(val)]):
            return i[len(val)+2:len(i)-1]

for line in sys.stdin:
    line = line.strip().split()

    if (parser('PostTypeId',line) == '2'):
        print parser('OwnerUserId',line),'\t',parser('ParentId',line)
