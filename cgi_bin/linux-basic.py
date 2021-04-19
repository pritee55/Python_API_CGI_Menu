#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess as sp
import cgi

field = cgi.FieldStorage()
task = field.getvalue("task")
field = sp.getoutput("sudo {}".format(task))
print(field)
