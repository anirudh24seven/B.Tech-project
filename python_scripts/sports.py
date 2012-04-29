import os, os.path
import re
from nltk.tokenize import RegexpTokenizer
from replacer import RepeatReplacer
from nltk.corpus import wordnet

rep = RepeatReplacer()

file = os.path.expanduser('output')
tokenizer = RegexpTokenizer("[\w']+")
tweets = []
specific_tweets = []

if not os.path.exists(file):
	print "No such file found"
else:
	o = open("output1", "a")
	for line in open(file):
		a = tokenizer.tokenize(line)
		if(len(a) >= 2):
			tweets.append(a)
	o.close()

	sports_synset = wordnet.synset('sport.n.01')

	for line in tweets:
		out = 0
		for word in line:
			rep.replace(word)
			if not wordnet.synsets(word):
				out = 1	
				break
			syn = wordnet.synsets(word)[0]
			

			if syn.name != "":
				for element in syn.hypernym_paths():
					for word1 in element:
						if word1 == sports_synset:
							specific_tweets.append(line)
							out = 1
							break
				if out == 1:
					break
			if out == 1:
				break
	for line in specific_tweets:
		print line
