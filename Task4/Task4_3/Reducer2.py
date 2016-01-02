#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip().split('\t')

    uid = line[0].split()
    print uid[1],'\t','->',uid[0],'\t',uid[2]
