#!/usr/bin/python
import sys
from datetime import datetime

old = None

sd = None
ld = None
for line in sys.stdin:
    line = line.strip().split()
    host = line[0]
    d = line[1]
    
    d = datetime.strptime(d, "%d/%b/%Y:%H:%M:%S")

    if ( old  and old != host ) :
        if ( sd == None):
            print d
        else:
            print old,'\t', ld -sd
        sd = None
        ld = None

    old = host

    if ( ld == None and sd == None ) :
        ld = d
    if ( d < ld and sd == None ):
        sd = d
    if ( d > ld and sd == None ) :
        sd = ld
        ld = d

    if ( sd != None):
        if ( d > ld ) :
            ld = d
        if ( d < sd) :
            sd = d


if ( old != None ):
    if ( sd == None ):

        print d
    else:
        print old,'\t', ld -sd