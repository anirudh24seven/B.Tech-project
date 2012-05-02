import os, os.path
import re
from nltk.tokenize import RegexpTokenizer
from replacer import RepeatReplacer

rep = RepeatReplacer()

file = os.path.expanduser('output')
tokenizer = RegexpTokenizer("[\w']+")
tweets = []

if not os.path.exists(file):
	print "No such file found"
else:
	o = open("output1", "w")
	for line in open(file):
		a = tokenizer.tokenize(line)
	o.close()

	for line in tweets:
		for word in line:
			rep.replace(word)
			print word

		

