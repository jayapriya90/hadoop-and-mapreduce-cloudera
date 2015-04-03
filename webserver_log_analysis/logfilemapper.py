#!/usr/bin/python
#
# We need to write them out to standard output, separated by a tab

import sys
import re

p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )

for line in sys.stdin:
    m = p.match(line)
    if not m:
        continue
    host, ignore, user, date, request, status, size = m.groups()
    request = request.split(' ')[1]
    request = re.sub('http://www.the-associates.co.uk','',request)
    print "{0}\t 1".format(request) 

