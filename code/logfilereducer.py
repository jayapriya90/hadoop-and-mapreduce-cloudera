#!/usr/bin/python

import sys

pagehitcount = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thispagehitcount = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", pagehitcount
        oldKey = thisKey;
        pagehitcount = 0

    oldKey = thisKey
    pagehitcount += int(thispagehitcount)

if oldKey != None:
    print oldKey, "\t", pagehitcount

