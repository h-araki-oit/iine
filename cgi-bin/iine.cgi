#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import os
import datetime
import sys
import shutil

#
# main function start here
#
print("Content-Type:text/html\n\n")
if os.environ['REQUEST_METHOD'] != "GET" :
	sys.exit()

form = cgi.FieldStorage()
file = None
dt_now = datetime.datetime.now()
file_name = "work/iine.txt"

try:
	vcc=3.0
	file = open(file_name,'a') #Write File
	datastring = form['your_name'].value
	file.write(dt_now.strftime('%Y,%m,%d,%H:%M:%S,'))

#	print(datastring)
	file.write(datastring)
	file.write('\r\n')

except IOerror:
	print("File write error.", file=sys.stderr)
	
finally:
	if file :
		file.close()

#
#main function end here
#

