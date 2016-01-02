#!/usr/bin/python
import sys
def parser(val,record):
    for i in record:

        if (val == i[:len(val)]):
            return i[len(val)+2:len(i)-1]

previous = None
total = 0
AllquestionID = []
for line in sys.stdin:
    line = line.strip().split()
    user,questionID = line

    if ( previous and user != previous) :
        print total,'\t',previous, ','.join(AllquestionID )
        total = 0
        AllquestionID = []

    previous = user
    total = total + 1
    AllquestionID.append(questionID)

if (previous != None) :
    print total , '\t',previous,','.join(AllquestionID)


