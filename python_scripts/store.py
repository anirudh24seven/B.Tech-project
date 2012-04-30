import os, os.path
import re
from nltk.tokenize import RegexpTokenizer

file = os.path.expanduser('output')
tokenizer = RegexpTokenizer("[\w']+")
tweets = []

if not os.path.exists(file):
	print "No such file found"
else:
	o = open("output1", "w")
	for line in open(file):
		a = tokenizer.tokenize(line)
		if(len(a) >= 2):
			tweets.append(a)
	o.close()
	print tweets

