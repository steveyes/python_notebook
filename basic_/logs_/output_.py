#!/usr/bin/env python3
#

import sys

logfile = open('/tmp/mylog.txt', 'a')
message = 'Fatal error: invalid input!'

print(message, file=logfile)

logfile.close()
