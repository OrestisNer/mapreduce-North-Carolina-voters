#!/usr/bin/env python3

"""mapper.py"""
import sys
import re
import io
# myDictionary stores our data in key value form
myDictionary = {}
#threshold = max number of items that myDictionary can have before printing
threshold = 5000
# input comes from STDIN (standard input)
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='windows-1252')

for line in input_stream:
    line = re.findall("\"[^\"]*\"", line)
    # we already know which columns we need
    # first index = 0
    # index 9 = "last_name"
    # index 10 = "first_name"
    # index 11 = "middle_name"

    # index 14 = "res_city_desc"
    # index 68 = "NCID"

    key = line[9] + line[10] + line[11] + line[14]
    value = line[68]
	
    #case of duplicate
    if key in myDictionary:
        myDictionary[key] = myDictionary[key] + " " + value
    #case of unique
	else:
        myDictionary[key] = value
        
	#when dictionary length is greater than threshold then print
    if (int(len(myDictionary)) > threshold):
        for k, v in myDictionary.items():
            print('%s\t%s' % (k, v))
        #cleans up dictionary
        myDictionary.clear()
		
#reading ends but our dictionary might have items so we print!
for k, v in myDictionary.items():
    print('%s\t%s' % (k, v))
