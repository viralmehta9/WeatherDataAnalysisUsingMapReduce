#!/usr/bin/python

import sys

tempTotal = 0
count=0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the stationID+month, val is the temperature
#
# Average temperature for a particular stationId will be presented,
# then the key will change and we'll be dealing with the next stationId

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisTemperature = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", tempTotal/count
        oldKey = thisKey;
        tempTotal = 0
	count=0

    oldKey = thisKey
    tempTotal += float(thisTemperature)
    count = count+1
    newTemp = tempTotal
x = count
if oldKey != None:
    print "{0}\t{1}".format(oldKey, newTemp/x)

