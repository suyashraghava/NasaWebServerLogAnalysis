#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    uid = line[1].split()

    print uid[0],'\t','->','\t',uid[1]

