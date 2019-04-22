#!/usr/bin/env python3
"""reducer.py"""
import sys

"""we do take advantage of the shuffle merge sort phase of the reducer
   that's why we use the current <key,value> and compare it with
   the very next entry, in case that the current key is different
   than the key we do know that we won't encounter the current key again."""

current_key = None
current_value = None
dublicate_counter = 0
key = None
value = None

# input comes from STDIN
for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    # in this case our entries have the same key thus we got a "duplicate"
    if current_key == key:
        current_value = current_value+" "+value
        dublicate_counter += 1
    else:
        # in this case we encountered a diffrent key but our dulpicate counter is greater than 0
        # so we print the previous key-value pair
        if dublicate_counter > 0 and current_key:
            print(current_key+"\t"+current_value)
            dublicate_counter = 0
        # in this last case if we hadnt classify the entry as duplicate we check if the mapper did so
        # in case that the entry has been merged in the mapping phase we print it
        elif current_key and (' ' in current_value):
            print(current_key+"\t"+current_value)
            dublicate_counter = 0
        current_value = value
        current_key = key

# prints last input in case it's a dublicate
# case i>0
if(dublicate_counter > 0):
    print(current_key+"\t"+current_value)
# case the entry was already combined (mapper)
elif(' ' in current_value):
    print(current_key+"\t"+current_value)
