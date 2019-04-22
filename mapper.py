#!/usr/bin/env python3
"""mapper.py"""
import sys
import re
import io
# outputDict stores our data in key value form
outputDict = {}
# threshold = max number of items that outputDict can have before printing
threshold = 5000
# input comes from STDIN (standard input)
# changing encoding to read non UTF-8 characters
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='windows-1252')

for line in input_stream:
    # regex to find all values into quotes (e.g "word")
    line = re.findall("\"[^\"]*\"", line)
    """
    We already know which columns we need.
    index 9 = "last_name", index 10 = "first_name"
    index 11 = "middle_name", index 14 = "res_city_desc"
    index 68 = "NCID".
    """
    key = line[9] + line[10] + line[11] + line[14]
    value = line[68]

    # case of duplicate
    if key in outputDict:
        outputDict[key] = outputDict[key] + " " + value
    # case of unique
    else:
        outputDict[key] = value

    # when dictionary length is greater than threshold then print
    if (int(len(outputDict)) > threshold):
        for k, v in outputDict.items():
            print('%s\t%s' % (k, v))
        # cleans up dictionary
        outputDict.clear()

# reading ends but our dictionary might have items so we print!
for k, v in outputDict.items():
    print('%s\t%s' % (k, v))
