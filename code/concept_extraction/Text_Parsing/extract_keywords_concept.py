#!/usr/bin/python
import sys
import os
import json
from get_commonsense import *

input_file_path = 'concepts/unique_keywords.txt'
output_file_path = 'concepts/concept_map.json'

concept_map = {}
if os.path.isfile(output_file_path):
	with open(output_file_path) as concept_map_file:
		concept_map = json.load(concept_map_file)

with open(input_file_path) as fin:
	list_words = fin.readlines()

for word in list_words:
	word = word.rstrip()
	print word
	if word in concept_map:
		continue
	list_concepts = get_commonsense(word.replace(' ', '_'), 50)
	concept_map[word] = list_concepts

with open(output_file_path, 'w') as outfile:
	json.dump(concept_map, outfile)