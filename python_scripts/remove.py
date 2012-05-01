import os, os.path
import re
name = "bhogleharsha"
filename = name + ".txt"
file = os.path.expanduser(filename)

if not os.path.exists(file):
	print "No such file found"
else:
	o = open("output", "w")
	for line in open(file):
		#line = re.sub('(^\@\S+) ', r'person: ', line)
		#line = re.sub('(\@\S+) ', 'person ', line)
		#line = re.sub(' (\@\S+)', ' person', line)
		line = re.sub('@', '', line)
		line = re.sub('(http://\S+)', r'', line)
		o.write(line)
	o.close()

