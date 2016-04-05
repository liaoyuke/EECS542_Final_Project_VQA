#!/usr/bin/python
import sys
from stem import *

def is_phrase( phrase ):
	return (' ' in phrase)

def stem_phrase( phrase ):
	words = phrase.split(' ')
	stem_words = []
	for word in words:
		stem_word = stem(word)
		stem_words.append(stem_word)

	return ' '.join(stem_words)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

with open(input_file_path) as fin:
	list_str_k = fin.readlines()

list_stem_str = []
for str_k in list_str_k:
	str_k = str_k.rstrip()
	stem_words = []
	words = str_k.split('-')
	for word in words:
		if is_phrase(word):
			stem_words.append(stem_phrase(word))
		else:
			stem_words.append(stem(word))
	list_stem_str.append('-'.join(stem_words))

fout = open(output_file_path, 'w')
for stem_str in list_stem_str:
	fout.write(stem_str + "\n")

fout.close()