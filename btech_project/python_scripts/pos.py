import os, os.path
import re
from nltk.tokenize import WordPunctTokenizer
from replacer import RepeatReplacer
from nltk.corpus import wordnet
from taggers import WordNetTagger

#usernames need to be handled as nouns for pos tagging. might lead to poor results while interpreting.
rep = RepeatReplacer()

file = os.path.expanduser('output')
tokenizer = WordPunctTokenizer()
tweets = []
specific_tweets = []
sports_word = []

if not os.path.exists(file):
	print "No such file found"
else:
	for line in open(file):
		a = tokenizer.tokenize(line)
		tweets.append(a)
	
	sports_synset = wordnet.synset('sport.n.01')
	cricket_synset = wordnet.synset('cricket.n.02')
	i = 0	

	for line in tweets:
		out = 0
		for word in line:
			rep.replace(word)
			if not wordnet.synsets(word):
				continue
			syn = wordnet.synsets(word)[0]

			if word == "cricket" :
				i+=1
				specific_tweets.append(line)
				break
			
			for element in syn.hypernym_paths():
				for word1 in element:
					if word1 == sports_synset:
						specific_tweets.append(line)
						#if not word in sports_word:
						#	sports_word.append(word)
						out += 1
						i+=1
						break
				if out > 0:
					break
			if out > 0:
				break
	w = WordNetTagger()	

	for word in sports_word:
		print word

#	for line in specific_tweets:
#		print line
#		print w.tag(line)
     
	print i
