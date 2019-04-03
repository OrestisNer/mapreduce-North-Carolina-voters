#!/usr/bin/env python3
"""reducer.py"""

import sys

current_key=None
current_value=None
i=0
key=None
value=None

#input comes from STDIN
for line in sys.stdin:
    l=line.strip();
    key, value = l.split('\t',1)
    if current_key == key:
        current_value=current_value+" "+value
        i=i+1
    else:
        if i>0 and current_key:
            print(current_key+"\t"+current_value)
            i=0
        elif (' ' in current_value) and current_key:
            print(current_key+"\t"+current_value)
            i=0
        current_value = value
        current_key = key
		
#prints last input in case it's a dublicate
#case i>0
if(i>0):
    print(current_key+"\t"+current_value)
#case the entry was already combined (mapper)
elif(' ' in current_value):
    print(current_key+"\t"+current_value)

