#!/usr/bin/env python3

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = re.findall("\"[^\"]*\"",line)
    print('%s\t%s' %(line[9]+line[10]+line[11]+line[14],line[68])) 
