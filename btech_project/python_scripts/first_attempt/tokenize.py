import os, os.path
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer("[\w']+")
f = open("anirudh24seven.txt")
o = open("output", "w")

while 1:
	line = f.readline()
	if not line: break
	a = tokenizer.tokenize(line)
	o.write(' \n'.join(a))
o.close()
