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
sports_count = []
pos_list = []

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
				if not word in sports_word:
					sports_word.append(word)
				specific_tweets.append(line)
				break
			
			for element in syn.hypernym_paths():
				for word1 in element:
					if word1 == sports_synset:
						specific_tweets.append(line)
						if not word in sports_word:
							sports_word.append(word)
						out += 1
						i+=1
						break
				if out > 0:
					break
			if out > 0:
				break
	w = WordNetTagger()	

	for word in sports_word:
		count = 0
		for line in specific_tweets:
			if word in line:
				count+=1
		sports_count.append(count)
	
	s_len = len(sports_word)
	sports_pair = []

	for i in range(0, s_len):
		temp_pair = []
		temp_pair.append(sports_word[i])
		temp_pair.append(sports_count[i])
		sports_pair.append(temp_pair)

	sorted_sports = sorted(sports_pair, key = lambda sports_pair: sports_pair[1], reverse=True)

	for line in specific_tweets:
		 pos_line = w.tag(line)
		 pos_list.append(pos_line)

	for pair in sorted_sports:
		sport = pair[0]
		for s in range(0, len(specific_tweets)):
			if sport in specific_tweets[s]:
				for p in range(0, len(pos_list[s])):
					if pos_list[s][p][1] == 'JJ':
						print specific_tweets[s][p],
						
		print ''

