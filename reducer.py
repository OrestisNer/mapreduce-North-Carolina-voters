#!/usr/bin/env python3
"""reducer.py"""

import sys

#orig_stdout = sys.stdout
#f = open("finalDataOutputfileSort.txt", "w")
#sys.stdout = f

current_key=None
current_value=None
i=0
key=None
value=None

#input comes from STDIN
for line in sys.stdin:
    #key, value = line.strip().split('\t')
    #print(key+"-"+value)
    l=line.strip();
    key, value = l.split('\t',1)
    if current_key == key:
        current_value=current_value+" "+value
        i=i+1
    else:
        if current_key and i>0:
            print(current_key+"\t"+current_value)
            i=0

        current_value = value
        current_key = key


#if(i>0):
    #print(current_key+"\t"+current_value)
#sys.stdout = orig_stdout
#f.close()