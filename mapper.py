#!/usr/bin/python

# 
# 
#
# We want elements 0 (station Id),elements 2(month) and 3 (temperature)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 1:
        for item in data:
            elements = item.split()
            stnId = elements[0]
            month = elements[2][4:6]
            temperature = elements[3]
	
	
        print ("{0}\t{1}".format(stnId+month, temperature))

