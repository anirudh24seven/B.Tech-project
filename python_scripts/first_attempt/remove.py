import os, os.path
import re
path = os.path.expanduser('tweet-texts-anirudh24seven.txt')

if not os.path.exists(path):
	print "No such file found"
else:
	o = open("output", "a")
	data = open(path).read()
	o.write( re.sub(r'^@*', '**', data) )
	o.close()

