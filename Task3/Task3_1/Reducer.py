#!/usr/bin/python

import sys
previous = ""
words = ""
output = ""
count = 0
MaximumSum = 0

for line in sys.stdin:         
    line = line.strip()        
    words, value = line.split("\t", 1)
    value = int(value)
   
    if previous == words:
        count += value
    else:            
        count = value
        prev_wocountrd = words
    
    if count > MaximumSum:
        MaximumSum = count
        output = previous

if previous == words:  
    if count > MaximumSum:
        MaximumSum = value_total
        output = previous

print output
