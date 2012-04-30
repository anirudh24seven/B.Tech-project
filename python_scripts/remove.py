import os, os.path
import re
file = os.path.expanduser('anirudh24seven.txt')

if not os.path.exists(file):
	print "No such file found"
else:
	o = open("output", "w")
	for line in open(file):
		line = re.sub(r'@([\w\.-])+ ', r'', line)
		line = line.replace("http","")
		o.write(line)
	o.close()

