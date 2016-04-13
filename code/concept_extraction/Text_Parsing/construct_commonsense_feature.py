#!/usr/bin/python
import sys
import json
from stem import *

question_file_path = sys.argv[1]
keywords_file_path = sys.argv[2]
objects_file_path = sys.argv[3]
concept_map_file_path = sys.argv[4]
num_concept_to_extract = int(sys.argv[5])
output_file_path = sys.argv[6]

question_concept_features = []

irrelevant_keywords = set(['a', 'an', 'the', 'he', 'she', 'what', 'who', 'I', 'we', 'they'])

question_features = []
with open(question_file_path) as question_file:
    questions = question_file.readlines()
for question in questions:
    question_feature = []
    question = question.rstrip()
    question_words = question.split(' ')
    for question_word in question_words:
        question_feature.append(question_word)
    question_features.append(question_feature)

with open(concept_map_file_path) as concept_map_file:
    concept_map = json.load(concept_map_file)

with open(keywords_file_path) as keywords_file:
    keywords_list = keywords_file.readlines()

with open(objects_file_path) as objects_file:
    objects_list = objects_file.readlines()

assert(len(keywords_list) == len(objects_list))

concept_features = []
for i in range(len(keywords_list)):
    keywords_str = keywords_list[i].rstrip()
    objects_str = objects_list[i].rstrip()
    elements_str = keywords_str + "-" + objects_str
    concept_feature = []
    if len(elements_str) == 1:
        concept_features.append(concept_feature)
        continue
    elements = elements_str.split('-')
    for element in elements:
        if element in irrelevant_keywords or len(element) == 0:
            continue
        concepts = concept_map[element][:num_concept_to_extract]
        for concept in concepts:
            concept_feature.extend(concept.split(' '))
    concept_feature = list(set(concept_feature))
    concept_features.append(concept_feature)

assert(len(question_features) == len(concept_features))

for i in range(len(question_features)):
    print i
    question_concept_feature = []
    for question_word in question_features[i]:
        #question_concept_feature.append(stem(question_word))
        question_concept_feature.append(question_word)
    for concept_word in concept_features[i]:
        #question_concept_feature.append(stem(concept_word))
        question_concept_feature.append(concept_word)
    question_concept_feature_ascii = []
    for word in question_concept_feature:
        question_concept_feature_ascii.append(stem(word.encode('ascii', 'ignore')))
    question_concept_feature = question_concept_feature_ascii
    question_concept_features.append(question_concept_feature)

fout = open(output_file_path, 'w')
for question_concept_feature in question_concept_features:
    question_concept_str = ' '.join(question_concept_feature)
    # print question_concept_str
    fout.write(question_concept_str + '\n')
fout.close()
