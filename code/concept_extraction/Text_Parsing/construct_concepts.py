#!/usr/bin/python
import sys
import json
import os.path
from stem import *

def fast_stem(word, stem_map):
    if word in stem_map:
        return stem_map[word]
    else:
        stem_word = stem(word)
        stem_map[word] = stem_word
        return stem_word

keywords_file_path = sys.argv[1]
objects_file_path = sys.argv[2]
output_file_path = sys.argv[3]
concept_map_file_path = 'concepts/concept_map.json'
num_concept_to_extract = 8

stem_map_file_path = 'concepts/stem_map.json'

concepts = []

irrelevant_keywords = set(['a', 'an', 'the', 'he', 'she', 'what', 'who', 'I', 'we', 'they'])

with open(concept_map_file_path) as concept_map_file:
    concept_map = json.load(concept_map_file)
if os.path.exists(stem_map_file_path):
    with open(stem_map_file_path) as stem_map_file:
        stem_map = json.load(stem_map_file)
else:
    stem_map = {}

with open(keywords_file_path) as keywords_file:
    keywords_list = keywords_file.readlines()

with open(objects_file_path) as objects_file:
    objects_list = objects_file.readlines()

assert(len(keywords_list) == len(objects_list))

concepts_list = []
for i in range(len(keywords_list)):
    concepts = []
    keywords_str = keywords_list[i].rstrip()
    objects_str = objects_list[i].rstrip()
    elements_str = keywords_str + "-" + objects_str
    if len(elements_str) == 1:
        concepts_list.append(concepts)
        continue
    elements = elements_str.split('-')
    concepts.extend(elements)
    for element in elements:
        if element in irrelevant_keywords or len(element) == 0:
            continue
        external_concepts = concept_map[element][:num_concept_to_extract]
        for external_concept in external_concepts:
            concepts.extend(external_concept.split(' '))
    concepts = list(set(concepts))
    concepts_list.append(concepts)

stem_concepts_list = []
for i in range(len(concepts_list)):
    print i
    concepts = concepts_list[i]
    stem_concepts = []
    for word in concepts:
        stem_concepts.append(fast_stem(word.encode('ascii', 'ignore'), stem_map))
    stem_concepts = list(set(stem_concepts))
    stem_concepts_list.append(stem_concepts)

fout = open(output_file_path, 'w')
for stem_concepts in stem_concepts_list:
    stem_concepts_str = ' '.join(stem_concepts)
    # print question_concept_str
    fout.write(stem_concepts_str + '\n')
fout.close()

with open(stem_map_file_path, 'w') as fout_stem_map:
    json.dump(stem_map, fout_stem_map)