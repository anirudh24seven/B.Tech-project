import os, os.path
import re
import nltk.data
from nltk.tokenize import WordPunctTokenizer
from replacer import RepeatReplacer
from nltk.corpus import wordnet
from taggers import WordNetTagger
from decimal import *

#usernames need to be handled as nouns for pos tagging. might lead to poor results while interpreting.

def bag_of_words(words):
	return dict([(word, True) for word in words])

rep = RepeatReplacer()

file = os.path.expanduser('output')
tokenizer = WordPunctTokenizer()
tweets = []
specific_tweets = []
sports_word = []
sports_count = []
pos_list = []
adjective_list = []

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
			adj_per_tweet = []
			if sport in specific_tweets[s]:
				for p in range(0, len(pos_list[s])):
					if pos_list[s][p][1] == 'JJ':
						#print specific_tweets[s][p],
						adj_per_tweet.append(specific_tweets[s][p])
			adjective_list.append(adj_per_tweet)			

	senti = []
	for line in open("AFINN-111.txt"):
		a = tokenizer.tokenize(line)
		senti.append(a)
	
	for pair in senti:
		if pair[1] == '-':
			pair[1] = pair[1]+pair[2]
			pair[2]=""


	adj_sports = []

	for pair in sorted_sports:
		sport = pair[0]
		adj_sport = []
		adj_sport.append(sport)
		for s in range(0, len(specific_tweets)):
			if sport in specific_tweets[s]:
				for p in range(0, len(pos_list[s])):
					if pos_list[s][p][1] == 'JJ':
						adj_sport.append(specific_tweets[s][p])
		adj_sports.append(adj_sport)
	
	sport_wt = []
	
	for sport in adj_sports:
		s_wt = []
		s_wt.append(sport[0])
		wt = 0

		for i in range (1, len(sport)):
			adjective = sport[i]
			for pair in senti:
				if adjective == pair[0]:
					weight = int(pair[1])

					for line in specific_tweets:
						s_pos = -2
						a_pos = -2
						n_pos = -2
						t_pos = -2

						if (sport[0] in line) and (adjective in line):
							for j in range(0, len(line)):
								if line[j] == sport[0]:
									s_pos = j
								if line[j] == adjective:
									a_pos = j
								if line [j] == "not":
									n_pos = j
								if line [j] == "than":
									t_pos = j
							if a_pos+1 == t_pos:
								if s_pos > t_pos:
									weight=weight*(-1)
							if n_pos+1 == a_pos:
								if s_pos > a_pos:
									weight=weight*(-1)
							wt=wt+weight
		s_wt.append(wt)
		sport_wt.append(s_wt)

	final_sport_list = []

	for pair1 in sorted_sports:
		sport = []
		for pair2 in sport_wt:
			if pair1[0] == pair2[0]:
				sport.append(pair1[0])
				weight = Decimal(pair2[1])/Decimal(pair1[1])
				sport.append(pair1[1])
				sport.append(pair2[1])
				sport.append(weight)
		final_sport_list.append(sport)


	for sport in final_sport_list:
		if sport[3] >= Decimal(1.5):
			sport[3] = Decimal(1.5)
		if sport[3] <= Decimal(-1.5):
			sport[3] = Decimal(-1.5)
		print sport
